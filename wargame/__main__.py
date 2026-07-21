"""Run a campaign scenario: python -m wargame <scenario.toml> [--days N]."""

import argparse
import json
from pathlib import Path

from .campaign import Campaign
from .oob import load_scenario


def main():
    ap = argparse.ArgumentParser(prog="wargame")
    ap.add_argument("scenario", type=Path)
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--year", type=int, default=None)
    ap.add_argument(
        "--deep",
        type=float,
        default=None,
        help="override deep_fraction (0=all close support, 1=all interdiction)",
    )
    ap.add_argument(
        "--no-hold",
        action="store_true",
        help="ignore hold lines (free Epstein withdrawal to theater rear)",
    )
    ap.add_argument("--seed", type=int, default=None, help="weather seed")
    ap.add_argument(
        "--deep-target",
        choices=("echelon", "throughput"),
        default=None,
        help="what deep fires attack: arrival schedules or supply flow",
    )
    ap.add_argument("--json", type=Path, help="write day logs as JSON")
    ap.add_argument("--ledger", type=Path, help="write markdown OOB ledger")
    args = ap.parse_args()

    data, axes, dropped = load_scenario(args.scenario, year=args.year)
    if args.deep is not None:
        # Direct mode: sets the split. Advocacy mode (v7): sets the
        # corps REQUEST — the theater still decides.
        data["params"]["deep_fraction"] = args.deep
        data["params"]["corps_request_deep"] = args.deep
    if args.no_hold:
        for ax in axes.values():
            ax["spec"]["hold_km"] = ax["spec"]["length_km"]
    if args.deep_target:
        data["params"]["deep_target"] = args.deep_target
    seed = args.seed if args.seed is not None else data["meta"].get("seed", 1986)

    print(f"# {data['meta']['name']}")
    print(
        f"# deep_fraction={data['params'].get('deep_fraction', 0.0)}"
        f" hold={'off' if args.no_hold else 'on'} seed={seed}"
    )
    if dropped:
        print(f"# dropped (not in service): {', '.join(dropped)}")

    camp = Campaign(
        axes=axes,
        params=data["params"],
        seed=seed,
        corps_reserve=data.get("corps_reserve_units", []),
    )
    state = camp.run(args.days)

    print(
        f"{'day':>3} {'axis':<22} {'ratio':>6} {'proj':>6} {'bloss':>6} "
        f"{'wdrw':>5} {'st':>2} {'adv':>5} {'feba':>6} {'arr':>3} "
        f"{'resCV':>6} {'wx':>4}"
    )
    for e in camp.logs:
        flag = "C" if e.ca else ("S" if e.standing else ".")
        print(
            f"{e.day:>3} {e.axis:<22} {e.ratio:>6} {e.proj_blue_frac:>6} "
            f"{e.blue_loss_frac:>6} {e.withdrawal_km:>5} "
            f"{flag:>2} {e.advance_km:>5} "
            f"{e.feba_km:>6} {e.arrivals:>3} {e.red_reserve_cv:>6} {e.wx:>4.2f}"
        )
    print()
    for name, st in state.items():
        status = "FALLEN" if st.fallen else "holding"
        blue = axes[name]["blue"]
        red = axes[name]["red"]
        print(
            f"{name}: FEBA {st.feba_km:.0f}/{st.length_km:.0f} km [{status}] "
            f"| blue CV {blue.cv:.1f} ({len(blue.alive)} bns) "
            f"| red CV {red.cv:.1f} ({len(red.alive)} bns) "
            f"| red delay {st.red_delay_days:.1f} d "
            f"| blue delay {st.blue_delay_days:.1f} d"
        )
    if getattr(camp, "aircraft", None) is not None:
        p0 = data["params"].get("blue_aircraft", 0.0)
        print(f"airframes: {camp.aircraft:.0f}/{p0:.0f} remaining")
    if args.json:
        args.json.write_text(json.dumps([vars(e) for e in camp.logs], indent=1))
        print(f"\nwrote {args.json}")
    if args.ledger:
        from .ledger import render

        args.ledger.write_text(
            render(data["meta"], data["params"], axes, state, camp.logs, args.days)
        )
        print(f"wrote {args.ledger}")


if __name__ == "__main__":
    main()
