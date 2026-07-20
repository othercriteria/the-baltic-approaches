"""Order of battle: battalion atoms, loaded from scenario TOML.

Year-parameterized by design (planning/setting-time.md): units carry
in_service years so re-picking the setting year is a query, not a
rebuild. Combat values are abstract points; calibration is a shelf
task (QJM's OLI values are the period instrument for this — see
reference/shelf.md purchase list).
"""

from dataclasses import dataclass, field

import tomllib


@dataclass
class Battalion:
    name: str
    side: str  # "blue" | "red"
    kind: str  # armor | mech | inf | arty
    cv: float  # combat value at full strength, abstract points
    strength: float = 1.0  # fraction remaining
    in_service: int | None = None  # first year fieldable, if known

    @property
    def effective_cv(self):
        return self.cv * self.strength

    def apply_loss_fraction(self, frac):
        self.strength = max(self.strength * (1.0 - frac), 0.0)


@dataclass
class Force:
    """All battalions of one side assigned to one axis."""

    side: str
    units: list[Battalion] = field(default_factory=list)

    @property
    def cv(self):
        return sum(u.effective_cv for u in self.units)

    @property
    def alive(self):
        return [u for u in self.units if u.strength > 0.05]

    def distribute_losses(self, total_cv_lost):
        """Spread a CV loss across surviving units pro rata."""
        cv = self.cv
        if cv <= 0 or total_cv_lost <= 0:
            return
        frac = min(total_cv_lost / cv, 1.0)
        for u in self.units:
            if u.strength > 0:
                u.apply_loss_fraction(frac)


def load_scenario(path, year=None):
    """Load a scenario TOML; filter units not in service by `year`."""
    with open(path, "rb") as f:
        data = tomllib.load(f)
    if year is None:
        year = data.get("meta", {}).get("year")
    dropped = []
    axes = {}
    for axis in data["axes"]:
        axes[axis["name"]] = {"spec": axis, "blue": Force("blue"), "red": Force("red")}
    for u in data["units"]:
        bn = Battalion(
            name=u["name"],
            side=u["side"],
            kind=u["kind"],
            cv=u["cv"],
            in_service=u.get("in_service"),
        )
        if year and bn.in_service and bn.in_service > year:
            dropped.append(bn.name)
            continue
        axes[u["axis"]][u["side"]].units.append(bn)
    return data, axes, dropped
