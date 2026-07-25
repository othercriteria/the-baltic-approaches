"""CLI for the theater transport atlas. See atlas/README.md."""

from __future__ import annotations

import argparse
import sys

from .graph import Atlas
from .render import add_subparser as add_render_subparser
from .render import cmd_render


def fmt_edge(e, profile, frm=None):
    tags = []
    if e.crossing:
        tags.append(e.crossing.upper())
    if e.verify:
        tags.append("VERIFY")
    tag = f"  [{', '.join(tags)}]" if tags else ""
    label = e.route or e.cls
    via = f" via {e.via}" if e.via else ""
    a, b = (frm, e.b if e.a == frm else e.a) if frm else (e.a, e.b)
    return (
        f"  {a} -> {b}  {label:<10} {e.km:5.0f} km  "
        f"{e.time_hours(profile):4.1f} h  "
        f"cap {e.capacity():>6.0f} t/d ({e.cap_source}){via}{tag}"
    )


def cmd_path(atlas, args):
    without = set(args.without.split(",")) if args.without else set()
    modes = set(args.modes.split(",")) if args.modes else None
    res = atlas.shortest_path(
        args.src,
        args.dst,
        profile=args.profile,
        metric=args.metric,
        without=without,
        modes=modes,
    )
    if res is None:
        print(f"NO ROUTE {args.src} -> {args.dst} (without={sorted(without)})")
        return 1
    cost, path = res
    unit = "km" if args.metric == "km" else "h"
    print(
        f"{args.src} -> {args.dst}  ({args.profile}, {args.metric}): "
        f"{cost:.1f} {unit}, {len(path)} legs"
    )
    node = args.src
    for e in path:
        print(fmt_edge(e, args.profile, frm=node))
        node = e.b if e.a == node else e.a
    choke = min(path, key=lambda e: e.capacity())
    print(f"chokepoint: {choke.id} ({choke.capacity():.0f} t/d, {choke.cap_source})")
    flagged = [e.id for e in path if e.verify]
    if flagged:
        print(f"verify-flagged legs: {', '.join(flagged)}")
    return 0


def cmd_flow(atlas, args):
    without = set(args.without.split(",")) if args.without else set()
    modes = set(args.modes.split(",")) if args.modes else None
    sources = atlas.resolve(args.src)
    sinks = atlas.resolve(args.dst)
    flow, cut = atlas.max_flow(sources, sinks, without=without, modes=modes)
    print(f"max flow {args.src} -> {args.dst}: {flow:.0f} t/d")
    print(f"min cut ({len(cut)} edges):")
    for e in sorted(cut, key=lambda e: -e.capacity()):
        print(fmt_edge(e, "convoy"))
    guessy = [
        e
        for e in cut
        if e.cap_source != "SOURCED" and not e.cap_source.startswith("SOURCED:")
    ]
    if guessy:
        print(
            f"NOTE: {len(guessy)}/{len(cut)} cut capacities are "
            f"GUESS/DEFAULT tier — the flow number inherits that grade."
        )
    return 0


def cmd_edges(atlas, args):
    for e in atlas.edges:
        if args.crossing and e.crossing != args.crossing:
            continue
        if args.mode and e.mode != args.mode:
            continue
        print(fmt_edge(e, "convoy"))
    return 0


def cmd_critical(atlas, args):
    ranked, base = atlas.critical()
    print("named flows (baseline t/d):")
    for fid, b in base.items():
        print(f"  {fid}: {b:.0f}")
    print(f"\n{'edge':<28}{'flow loss t/d':>14}  cap_source  verify")
    for loss, e in ranked[: args.top]:
        v = "V" if e.verify else ""
        print(f"{e.id:<28}{loss:>14.0f}  {e.cap_source:<10}  {v}")
    unsourced = [
        e for _, e in ranked[: args.top] if not e.cap_source.startswith("SOURCED")
    ]
    print(
        f"\nresearch priority: {len(unsourced)}/{min(args.top, len(ranked))} "
        f"top edges not yet SOURCED"
    )
    return 0


def cmd_check(atlas, args):
    issues, stats = atlas.check()
    for k, v in stats.items():
        print(f"{k}: {v}")
    if issues:
        print(f"\n{len(issues)} ISSUES:")
        for i in issues:
            print(f"  - {i}")
        return 1
    print("\nno issues")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="atlas")
    sub = p.add_subparsers(dest="cmd", required=True)

    pp = sub.add_parser("path", help="shortest route")
    pp.add_argument("src")
    pp.add_argument("dst")
    pp.add_argument("--profile", default="convoy", choices=["convoy", "civil"])
    pp.add_argument("--metric", default="hours", choices=["hours", "km"])
    pp.add_argument("--without", default="", help="comma-separated edge ids to drop")
    pp.add_argument(
        "--modes", default="", help="restrict to modes, e.g. road or rail,ferry"
    )

    pf = sub.add_parser("flow", help="max flow + min cut")
    pf.add_argument("src", help="node id or region:XX")
    pf.add_argument("dst", help="node id or region:XX")
    pf.add_argument("--without", default="")
    pf.add_argument("--modes", default="")

    pe = sub.add_parser("edges", help="list edges by tag")
    pe.add_argument("--crossing", default="")
    pe.add_argument("--mode", default="")

    pc = sub.add_parser("critical", help="rank edges by knockout loss over story flows")
    pc.add_argument("--top", type=int, default=20)

    sub.add_parser("check", help="dataset lint + guess-rate report")

    add_render_subparser(sub)

    args = p.parse_args(argv)
    if args.cmd == "render":
        return cmd_render(args)
    atlas = Atlas.load()
    return {
        "path": cmd_path,
        "flow": cmd_flow,
        "edges": cmd_edges,
        "check": cmd_check,
        "critical": cmd_critical,
    }[args.cmd](atlas, args)


if __name__ == "__main__":
    sys.exit(main())
