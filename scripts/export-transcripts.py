#!/usr/bin/env python3
"""Export Claude Code session transcripts to readable markdown.

Ported from white-buffalo (scripts/export-transcripts.py), where the
credential redaction exists because of a real in-session key leak
(its ledger, entity 13). Run regularly — the archive being
contemporaneous is refinement 1 of planning/attribution.md.

Usage:
  python3 scripts/export-transcripts.py [session-id-prefix ...]
  python3 scripts/export-transcripts.py --source-dir DIR [prefix ...]
  python3 scripts/export-transcripts.py --skip PREFIX

--source-dir exports from a different Claude project directory —
needed for sessions that shaped this project but ran elsewhere (the
founding session 656ec2ba ran in -home-dlk-workspace).
--skip excludes a session (prefix ok) — used by `make archive` so the
live session never ships a partial transcript.
"""

import json
import os
import re
import sys
from pathlib import Path

# Strip ANSI escape codes
ANSI_ESCAPE = re.compile(r"\x1b\[[0-9;]*m|\[38;2;[0-9;]+m|\[39m")

# Redact credential-shaped strings (API keys, bearer tokens) so a
# shell-expansion accident in a session can't ship in the published
# transcripts. Applied to all exported text.
SECRETS = re.compile(
    r"sk-ant-[A-Za-z0-9_-]{10,}"
    r"|\bBearer\s+[A-Za-z0-9._~+/-]{20,}"
    r"|-----BEGIN [A-Z ]*PRIVATE KEY-----"
)


def get_project_sessions_dir():
    """Get the Claude sessions directory for this project."""
    cwd = os.getcwd().replace("/", "-")
    return Path.home() / ".claude" / "projects" / cwd


def extract_text_content(message):
    """Extract readable text from a message object."""
    content = message.get("message", {}).get("content", [])
    if isinstance(content, str):
        return content

    texts = []
    for block in content:
        if isinstance(block, str):
            texts.append(block)
        elif isinstance(block, dict):
            if block.get("type") == "text":
                texts.append(block.get("text", ""))
            elif block.get("type") == "tool_use":
                texts.append(f"[Tool: {block.get('name', 'unknown')}]")
            elif block.get("type") == "tool_result":
                texts.append("[Tool Result]")
    return "\n".join(texts)


def parse_session(filepath):
    """Parse a session JSONL file into messages."""
    messages = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                msg_type = obj.get("type")
                if obj.get("subtype") == "compact_boundary":
                    messages.append(
                        {
                            "role": "compact_boundary",
                            "content": f"Compaction boundary at {obj.get('timestamp')} "
                            f"(trigger: {obj.get('compactMetadata', {}).get('trigger', 'unknown')}). "
                            "Everything above is a distinct entity under "
                            "planning/attribution.md; everything below "
                            "continues from a summary of it.",
                            "timestamp": obj.get("timestamp"),
                        }
                    )
                if msg_type in ("user", "assistant"):
                    text = extract_text_content(obj)
                    if text.strip():
                        messages.append(
                            {
                                "role": msg_type,
                                "content": text,
                                "timestamp": obj.get("timestamp"),
                            }
                        )
            except json.JSONDecodeError:
                continue
    return messages


def format_session_markdown(messages, session_id):
    """Format messages as markdown."""
    lines = [f"# Session: {session_id}\n"]

    boundary_n = 0
    for msg in messages:
        role = msg["role"].upper()
        content = msg["content"]
        content = ANSI_ESCAPE.sub("", content)
        content = SECRETS.sub("[REDACTED-CREDENTIAL]", content)
        if msg["role"] == "compact_boundary":
            boundary_n += 1
            role = f"COMPACTION BOUNDARY {boundary_n}"
        lines.append(f"## {role}\n")
        lines.append(content)
        lines.append("\n---\n")

    return "\n".join(lines)


def get_session_date(filepath):
    """Get the earliest timestamp from a session file."""
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                snapshot = obj.get("snapshot", {})
                ts = snapshot.get("timestamp") or obj.get("timestamp")
                if ts and isinstance(ts, str):
                    return ts[:10]
            except (json.JSONDecodeError, ValueError, TypeError):
                continue
    return "unknown"


def main():
    args = sys.argv[1:]
    sessions_dir = get_project_sessions_dir()
    if "--source-dir" in args:
        i = args.index("--source-dir")
        sessions_dir = Path(args[i + 1]).expanduser()
        args = args[:i] + args[i + 2 :]

    skip = []
    while "--skip" in args:
        i = args.index("--skip")
        skip.append(args[i + 1])
        args = args[:i] + args[i + 2 :]

    if not sessions_dir.exists():
        print(f"No sessions found at {sessions_dir}", file=sys.stderr)
        sys.exit(1)

    output_dir = Path("transcripts")
    output_dir.mkdir(parents=True, exist_ok=True)

    session_files = sorted(sessions_dir.glob("*.jsonl"))
    main_sessions = [f for f in session_files if not f.name.startswith("agent-")]

    print(
        f"Found {len(main_sessions)} main sessions, "
        f"{len(session_files) - len(main_sessions)} agent sessions"
    )

    # Optional: restrict to session ids (prefixes ok) given as CLI args,
    # e.g. to avoid exporting a partial transcript of the live session.
    if args:
        main_sessions = [
            f for f in main_sessions if any(f.stem.startswith(w) for w in args)
        ]
    if skip:
        main_sessions = [
            f for f in main_sessions if not any(f.stem.startswith(w) for w in skip)
        ]

    for session_file in main_sessions:
        session_id = session_file.stem
        print(f"Processing {session_id}...")

        messages = parse_session(session_file)
        if not messages:
            print("  (no messages)")
            continue

        session_date = get_session_date(session_file)
        markdown = format_session_markdown(messages, session_id)
        output_file = output_dir / f"{session_date}-{session_id[:8]}.md"
        output_file.write_text(markdown)
        print(f"  -> {output_file} ({len(messages)} messages)")

    print(f"\nTranscripts exported to {output_dir}/")


if __name__ == "__main__":
    main()
