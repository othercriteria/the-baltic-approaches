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
    ap.add_argument("--json", type=Path, help="write day logs as JSON")
    args = ap.parse_args()

    data, axes, dropped = load_scenario(args.scenario, year=args.year)
    print(f"# {data['meta']['name']}")
    if dropped:
        print(f"# dropped (not in service): {', '.join(dropped)}")

    camp = Campaign(axes=axes, params=data["params"])
    state = camp.run(args.days)

    hdr = f"{'day':>3} {'axis':<22} {'ratio':>6} {'rloss':>6} {'bloss':>6} {'wdrw':>5} {'adv':>5} {'feba':>6}"
    print(hdr)
    for log in camp.logs:
        print(
            f"{log.day:>3} {log.axis:<22} {log.ratio:>6} "
            f"{log.red_loss_frac:>6} {log.blue_loss_frac:>6} "
            f"{log.withdrawal_km:>5} {log.advance_km:>5} {log.feba_km:>6}"
        )
    print()
    for name, st in state.items():
        status = "FALLEN" if st.fallen else "holding"
        blue = axes[name]["blue"]
        red = axes[name]["red"]
        print(
            f"{name}: FEBA {st.feba_km:.0f}/{st.length_km:.0f} km [{status}] "
            f"| blue CV {blue.cv:.1f} ({len(blue.alive)} bns) "
            f"| red CV {red.cv:.1f} ({len(red.alive)} bns)"
        )
    if args.json:
        args.json.write_text(json.dumps([vars(entry) for entry in camp.logs], indent=1))
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
