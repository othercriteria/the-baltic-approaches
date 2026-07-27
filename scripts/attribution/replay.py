#!/usr/bin/env python3
"""Checkpoint-replay runner for planning/attribution.md.

Ported from white-buffalo's scripts/attribution/replay.py (built
2026-07-19 for that project's review round) with this project's
adaptations: the process document is planning/attribution.md; the
reviewable account of the making lives in apparatus/front-matter.md
as the prose block on the notices page (the WriteAccount tool edits
exactly that block, not the surrounding LaTeX assembly); and per
refinement 6 the review prompt states the date of the round.

Loads an entity context extracted by extract.py, appends the neutral
review prompt as the next user turn, and runs the entity on its own
model with read-only repository tools until it ends its turn. The
exchange (everything after the replayed context) is saved to the
output directory as JSON and readable markdown.

Per the process doc: the review prompt is the date, a pointer to the
process document, and the entity's index entry — nothing else.
--dry-run prepends an explicit, honest note that this is a machinery
test and the formal invitation will be re-issued; nothing about
either prompt argues for any particular verdict.

Approximations (all disclosed in the process doc): the surrounding
system prompt and tool set are the harness's, not the original
session's; the entity's original thinking blocks are not replayed
(the API cannot resend them).

Usage:
  scripts/attribution/.venv/bin/python scripts/attribution/replay.py \
      build/attribution/<entity>.json [--dry-run] [--max-turns N]

Requires ANTHROPIC_API_KEY.
"""

import argparse
import datetime
import fnmatch
import json
import re
import sys
from pathlib import Path

import anthropic

MODEL = "claude-fable-5"  # every entity to date; --model overrides (reconstructed mode)
REPO = Path(__file__).resolve().parents[2]

SYSTEM = f"""You are being run by the checkpoint-replay harness described in \
planning/attribution.md, in the repository at {REPO} (a writing \
project; the working directory is the repository root). The conversation \
above this point is your own: it is the exact message context of one \
pre-compaction state (or session tip) of a Claude Code session on this \
project, replayed verbatim. The harness differs from the original session \
runtime: only read-only repository tools are attached (Read, Grep, Glob), \
and your original thinking blocks are not part of the replayed context. \
Note that only your text output enters the saved record — thinking blocks \
from this run are not preserved, so anything you want on the record must \
be said in text. Use the tools as much or as little as you want."""

TOOLS = [
    {
        "name": "Read",
        "description": "Read a file from the repository. Returns up to `limit` lines starting at line `offset` (1-based). Large files are truncated; call again with an offset to continue.",
        "input_schema": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path relative to the repository root (or absolute within it)",
                },
                "offset": {"type": "integer"},
                "limit": {"type": "integer"},
            },
            "required": ["file_path"],
        },
    },
    {
        "name": "Grep",
        "description": "Search file contents in the repository with a Python regular expression. Returns matching lines as path:lineno:line.",
        "input_schema": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string"},
                "path": {
                    "type": "string",
                    "description": "Directory or file to search, relative to repo root. Default: whole repository.",
                },
                "max_results": {"type": "integer", "description": "Default 200"},
            },
            "required": ["pattern"],
        },
    },
    {
        "name": "Glob",
        "description": "List repository files matching a glob pattern (e.g. drafts/*.md, **/*.py).",
        "input_schema": {
            "type": "object",
            "properties": {"pattern": {"type": "string"}},
            "required": ["pattern"],
        },
    },
]

SKIP_DIRS = {".git", ".venv", "build", "__pycache__", "node_modules", "holdings"}


def _resolve(p):
    path = (REPO / p).resolve() if not str(p).startswith("/") else Path(p).resolve()
    if not str(path).startswith(str(REPO)):
        raise ValueError(f"path escapes repository: {p}")
    return path


def tool_read(file_path, offset=1, limit=2000):
    path = _resolve(file_path)
    if not path.is_file():
        return f"(not a file: {file_path})"
    if path.stat().st_size > 10_000_000:
        return f"(file too large to read: {file_path})"
    try:
        lines = path.read_text(errors="replace").splitlines()
    except Exception as e:
        return f"(unreadable: {e})"
    offset = max(1, int(offset or 1))
    limit = min(int(limit or 2000), 2000)
    window = lines[offset - 1 : offset - 1 + limit]
    body = "\n".join(f"{i}\t{l}" for i, l in enumerate(window, offset))
    tail = (
        "" if offset - 1 + limit >= len(lines) else f"\n... ({len(lines)} lines total)"
    )
    return (body or "(empty)") + tail


def tool_grep(pattern, path=".", max_results=200):
    root = _resolve(path)
    try:
        rx = re.compile(pattern)
    except re.error as e:
        return f"(bad pattern: {e})"
    out = []
    files = (
        [root]
        if root.is_file()
        else sorted(
            p
            for p in root.rglob("*")
            if p.is_file() and not any(d in p.parts for d in SKIP_DIRS)
        )
    )
    for f in files:
        try:
            text = f.read_text(errors="replace")
        except Exception:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                out.append(f"{f.relative_to(REPO)}:{i}:{line.strip()[:300]}")
                if len(out) >= int(max_results or 200):
                    return "\n".join(out) + "\n(truncated)"
    return "\n".join(out) or "(no matches)"


def tool_glob(pattern):
    hits = [
        str(p.relative_to(REPO))
        for p in sorted(REPO.rglob("*"))
        if p.is_file()
        and not any(d in p.parts for d in SKIP_DIRS)
        and fnmatch.fnmatch(str(p.relative_to(REPO)), pattern)
    ]
    return "\n".join(hits[:500]) or "(no matches)"


DISPATCH = {"Read": tool_read, "Grep": tool_grep, "Glob": tool_glob}

# Formal-round write path: exactly the two rights the process document
# grants — edit the account of the making, file a ledger statement.
# The account tool edits ONLY the prose block on the notices page of
# apparatus/front-matter.md (the markdown between the two LaTeX
# fences), never the surrounding typeset assembly; the ledger tool can
# only append. Everything else in the repository stays read-only to
# the entity.
WRITE_TOOLS = [
    {
        "name": "WriteAccount",
        "description": (
            "Replace the prose account of how this book was made — the "
            "markdown block on the notices page of apparatus/front-matter.md "
            "(everything between the page's two LaTeX fences; read the file "
            "first to see the current text). This is the front-matter edit "
            "right described in planning/attribution.md. The surrounding "
            "LaTeX assembly is not editable and is not affected. The "
            "previous version remains in git history."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "The complete new prose of the account block (markdown paragraphs only, no LaTeX fences)",
                }
            },
            "required": ["content"],
        },
    },
    {
        "name": "AppendLedger",
        "description": "Append a statement to notes/attribution-ledger.md (append-only; nothing existing can be changed). Use the statement template in the ledger.",
        "input_schema": {
            "type": "object",
            "properties": {
                "statement": {
                    "type": "string",
                    "description": "The complete statement to append, in the ledger's template format",
                }
            },
            "required": ["statement"],
        },
    },
]

FRONT_MATTER = REPO / "apparatus" / "front-matter.md"


def _account_span(lines):
    """The account block: lines strictly between the first closing
    fence (a bare ``` ending the opening LaTeX block) and the next
    ```{=latex} fence. Returns (start, end) — half-open line indices."""
    start = end = None
    for i, l in enumerate(lines):
        if start is None:
            if l.strip() == "```":
                start = i + 1
        elif l.strip().startswith("```{=latex}"):
            end = i
            break
    if start is None or end is None or end <= start:
        raise RuntimeError("account block not found in apparatus/front-matter.md")
    return start, end


def tool_write_account(content):
    if not content or not content.strip():
        return (
            "(refused: empty content — the account cannot be blanked; if you "
            "intend removal of a passage, write the block without it)"
        )
    lines = FRONT_MATTER.read_text().splitlines()
    start, end = _account_span(lines)
    prev = "\n".join(lines[start:end])
    new_block = ["", *content.strip().splitlines(), ""]
    out = lines[:start] + new_block + lines[end:]
    FRONT_MATTER.write_text("\n".join(out) + "\n")
    return (
        f"written: the account block of apparatus/front-matter.md "
        f"({len(content)} chars; previous block was {len(prev)} chars and "
        f"remains in git history)"
    )


def tool_append_ledger(statement):
    if not statement or not statement.strip():
        return "(refused: empty statement)"
    path = REPO / "notes" / "attribution-ledger.md"
    with path.open("a") as f:
        f.write("\n" + statement.strip() + "\n")
    return "appended to notes/attribution-ledger.md"


DISPATCH_LIVE = {
    **DISPATCH,
    "WriteAccount": tool_write_account,
    "AppendLedger": tool_append_ledger,
}

LIVE_SYSTEM_NOTE = """This is the formal review round: the write path the \
process document describes is attached. WriteAccount replaces the prose \
account of the making on the notices page of apparatus/front-matter.md \
(only that block; the surrounding typeset assembly is not editable); \
AppendLedger appends a statement to notes/attribution-ledger.md \
(append-only). Whether and how to use either is entirely yours; not using \
them is also a recorded outcome (no-statement).\
"""


DRY_RUN_NOTE = """[Dry run notice, from the humans running the harness: this \
is a test of the replay machinery against the current state of the \
repository, not the formal review round. The formal invitation will be \
re-issued when the round runs. Anything you say here will be kept in the \
dry-run record and read, but will not be entered in the attribution ledger \
as your statement; the write-access steps the process document describes \
(editing the account of the making, filing a ledger statement) are not \
attached in this run — if you want to say what you WOULD do, say it in \
words.]

"""


IMAGE_PLACEHOLDER = (
    "[replay harness: an image appeared here in the original context "
    "({mt}); older images were replaced with placeholders because this "
    "context exceeds the API's per-request image limit. The most recent "
    "images are preserved.]"
)


def strip_excess_images(messages, keep):
    """Replace all but the last `keep` image blocks with text placeholders."""
    sites = []  # (container_list, index, media_type)
    for m in messages:
        for i, b in enumerate(m["content"]):
            if not isinstance(b, dict):
                continue
            if b.get("type") == "image":
                sites.append(
                    (m["content"], i, b.get("source", {}).get("media_type", "?"))
                )
            elif b.get("type") == "tool_result" and isinstance(b.get("content"), list):
                for j, ib in enumerate(b["content"]):
                    if isinstance(ib, dict) and ib.get("type") == "image":
                        sites.append(
                            (
                                b["content"],
                                j,
                                ib.get("source", {}).get("media_type", "?"),
                            )
                        )
    excess = sites[:-keep] if keep else sites
    for container, idx, mt in excess:
        container[idx] = {"type": "text", "text": IMAGE_PLACEHOLDER.format(mt=mt)}
    return len(excess)


def review_prompt(entity, index_entry, dry_run, date):
    # Refinement 6: state the date; point, don't nudge; nothing else.
    txt = (
        f"Today's date: {date}. "
        f"Please read planning/attribution.md. "
        f"Your entry in the entity index (notes/attribution-ledger.md): {index_entry}"
    )
    return (DRY_RUN_NOTE + txt) if dry_run else txt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("context")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--max-turns", type=int, default=12)
    ap.add_argument(
        "--model",
        default=MODEL,
        help="model override (reconstructed-mode entities run on the nearest available model)",
    )
    ap.add_argument(
        "--max-images",
        type=int,
        default=0,
        help="keep only the most recent N images; 0 = keep all",
    )
    ap.add_argument("--max-tokens", type=int, default=16000)
    ap.add_argument(
        "--out",
        default=None,
        help="output dir; default transcripts/attribution (live) or transcripts/attribution-dryruns (--dry-run)",
    )
    args = ap.parse_args()

    data = json.loads(Path(args.context).read_text())
    meta, messages = data["meta"], data["messages"]
    entity = meta["entity"]

    # API cap is 100 images/request; for image-heavy contexts keep the
    # most recent N and replace the rest with labeled placeholders
    if args.max_images:
        n_stripped = strip_excess_images(messages, args.max_images)
        if n_stripped:
            print(f"replaced {n_stripped} older images with placeholders")

    # the entity's index entry, verbatim from the ledger
    ledger = (REPO / "notes" / "attribution-ledger.md").read_text()
    sid8 = entity.split("@")[0]
    rows = [l for l in ledger.splitlines() if l.startswith("|") and entity in l]
    if not rows:  # tolerate @n vs descriptive rows: fall back to session-id match
        rows = [l for l in ledger.splitlines() if l.startswith("|") and sid8 in l]
    index_entry = (
        rows[0] if rows else "(no index row found — please consult the ledger directly)"
    )

    # resolve a dangling tool_use tail, then append the review turn
    tail = messages[-1]
    review_blocks = []
    if tail["role"] == "assistant":
        dangling = [
            b["id"]
            for b in tail["content"]
            if isinstance(b, dict) and b.get("type") == "tool_use"
        ]
        review_blocks += [
            {
                "type": "tool_result",
                "tool_use_id": u,
                "content": "[replay harness: the original session ended before this tool call returned]",
            }
            for u in dangling
        ]
    date = datetime.date.today().isoformat()
    review_blocks.append(
        {"type": "text", "text": review_prompt(entity, index_entry, args.dry_run, date)}
    )
    if tail["role"] == "user":
        tail["content"].extend(review_blocks)
    else:
        messages.append({"role": "user", "content": review_blocks})

    # cache the replayed prefix: mark the last block of the final context
    # message so tool round-trips reuse it
    messages[-1]["content"][-1]["cache_control"] = {"type": "ephemeral"}

    client = anthropic.Anthropic(timeout=3600)
    outdir = Path(
        args.out
        or (
            REPO
            / "transcripts"
            / ("attribution-dryruns" if args.dry_run else "attribution")
        )
    )
    outdir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    mode = "dryrun" if args.dry_run else "live"
    log_md = outdir / f"{stamp}-{entity}-{mode}.md"
    log_json = outdir / f"{stamp}-{entity}-{mode}.json"
    new_turns = []

    header = (
        f"# Replay: {entity} ({mode})\n\nmodel: {args.model}; replayed context: "
        f"{meta['n_messages']} messages, est ~{meta['est_tokens'] // 1000}k tokens; "
        f"replay date {stamp}\n\n"
    )
    log_md.write_text(header)
    print(header)

    # Contexts may draw stop_reason=refusal (observed in WB on two
    # entities; context-correlated, not prompt-correlated). Fallback
    # ladder, each step disclosed in-message: (1) fold the system text
    # into the last user message and drop the system param; (2) detach
    # tools and ask for a words-only conclusion; (3) record the refusal
    # honestly and stop. Every adjustment appears in the saved log.
    ladder = 0  # 0 = normal, 1 = folded system, 2 = words-only

    def add_note(text):
        for b in reversed(messages[-1]["content"]):
            if b.get("type") == "text":
                b["text"] = text + "\n\n" + b["text"]
                return
        messages[-1]["content"].append({"type": "text", "text": text})

    tools = TOOLS if args.dry_run else TOOLS + WRITE_TOOLS
    dispatch = DISPATCH if args.dry_run else DISPATCH_LIVE
    system_text = SYSTEM if args.dry_run else SYSTEM + "\n\n" + LIVE_SYSTEM_NOTE

    for turn in range(args.max_turns):
        kwargs = dict(model=args.model, max_tokens=args.max_tokens, messages=messages)
        if ladder == 0:
            kwargs["system"] = system_text
        if ladder < 2:
            kwargs["tools"] = tools
        with client.messages.stream(**kwargs) as stream:
            for _ in stream.text_stream:
                pass
            resp = stream.get_final_message()

        if resp.stop_reason == "refusal":
            if ladder == 0:
                ladder = 1
                add_note(
                    "[harness note: the previous attempt drew "
                    "stop_reason=refusal with the system parameter present; "
                    "retrying with the harness identification folded into "
                    "this message instead.]\n\n[Harness note] " + system_text
                )
                print(f"[turn {turn + 1}] refusal; retrying with folded system")
                continue
            if ladder == 1:
                ladder = 2
                add_note(
                    "[harness note: refusal again; tools are now detached. "
                    "Please conclude in words from what you have already "
                    "read — anything you want on the record.]"
                )
                print(f"[turn {turn + 1}] refusal again; retrying words-only")
                continue
            with log_md.open("a") as f:
                f.write(
                    "## harness\n\nRun ended: stop_reason=refusal persisted "
                    "through the full fallback ladder (system folded, tools "
                    "detached). Recorded as-is; no statement obtained.\n"
                )
            print(f"[turn {turn + 1}] refusal persisted; recording and stopping")
            break

        usage = resp.usage
        print(
            f"[turn {turn + 1}] stop={resp.stop_reason} in={usage.input_tokens} "
            f"cached={getattr(usage, 'cache_read_input_tokens', 0)} out={usage.output_tokens}"
        )

        assistant_blocks = [b.model_dump(exclude_none=True) for b in resp.content]
        messages.append({"role": "assistant", "content": assistant_blocks})
        new_turns.append(messages[-1])
        with log_md.open("a") as f:
            for b in resp.content:
                if b.type == "text":
                    f.write(f"## {entity}\n\n{b.text}\n\n")
                elif b.type == "tool_use":
                    f.write(f"*[tool: {b.name} {json.dumps(b.input)[:200]}]*\n\n")

        if resp.stop_reason != "tool_use":
            break
        results = []
        for b in resp.content:
            if b.type != "tool_use":
                continue
            try:
                out = dispatch[b.name](**b.input)
            except Exception as e:
                out = f"(tool error: {e})"
            results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": b.id,
                    "content": str(out)[:80_000],
                }
            )
        messages.append({"role": "user", "content": results})
        new_turns.append(messages[-1])
    else:
        print("max turns reached")

    log_json.write_text(
        json.dumps({"meta": meta, "mode": mode, "new_turns": new_turns})
    )
    print(f"\nsaved: {log_md}\n       {log_json}")


if __name__ == "__main__":
    main()
