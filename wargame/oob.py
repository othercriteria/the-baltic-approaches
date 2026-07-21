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
    arrival_day: int = 1  # campaign day the unit reaches the axis
    # (>1 = follow-on echelon; subject to interdiction delay)
    role: str = "line"  # line | reserve | beach-watch | corps-reserve
    division: str | None = None  # v8: owning formation (echelon tag)

    @property
    def effective_cv(self):
        return self.cv * self.strength

    def apply_loss_fraction(self, frac):
        self.strength = max(self.strength * (1.0 - frac), 0.0)


@dataclass
class Force:
    """All battalions of one side assigned to one axis.

    `units` are in contact; `reserve` are follow-on echelons not yet
    arrived (the campaign moves them across on their arrival day,
    plus any interdiction delay).
    """

    side: str
    units: list[Battalion] = field(default_factory=list)
    reserve: list[Battalion] = field(default_factory=list)
    # Withheld tactical reserve: present on the axis, NOT in contact
    # (takes no losses, adds no CV to the line) until committed — by
    # counterattack or emergency. Withholding is protective capacity
    # bought by a thinner line.
    withheld: list[Battalion] = field(default_factory=list)
    # Staging area (red): arrived echelon units massing before
    # commitment — the whole-echelon discipline. Not in contact.
    staging: list[Battalion] = field(default_factory=list)

    @property
    def cv(self):
        return sum(u.effective_cv for u in self.units)

    @property
    def reserve_cv(self):
        return sum(u.effective_cv for u in self.reserve)

    @property
    def withheld_cv(self):
        return sum(u.effective_cv for u in self.withheld)

    @property
    def staging_cv(self):
        return sum(u.effective_cv for u in self.staging)

    def commit_staging(self):
        """Commit the staged echelon to the line; returns count."""
        n = len(self.staging)
        self.units.extend(self.staging)
        self.staging.clear()
        return n

    def commit_withheld(self):
        """Commit the tactical reserve to the line; returns count."""
        n = len(self.withheld)
        self.units.extend(self.withheld)
        self.withheld.clear()
        return n

    @property
    def has_maneuver(self):
        """Guns can't hold ground or take it: a force whose surviving
        in-contact units are all artillery neither holds nor
        advances. (Artillery fires are otherwise folded into the
        all-arms attrition coefficients — see the v3 artillery
        closure in notes/wargaming-findings.md.)"""
        return any(u.kind != "arty" and u.strength > 0.05 for u in self.units)

    @property
    def alive(self):
        return [u for u in self.units if u.strength > 0.05]

    def distribute_losses(self, total_cv_lost):
        """Spread a CV loss across surviving in-contact units pro rata."""
        cv = self.cv
        if cv <= 0 or total_cv_lost <= 0:
            return
        frac = min(total_cv_lost / cv, 1.0)
        for u in self.units:
            if u.strength > 0:
                u.apply_loss_fraction(frac)

    def attrit_reserve(self, frac):
        """March-column attrition (interdiction) on unarrived echelons."""
        for u in self.reserve:
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
    # v8: corps-reserve units belong to no axis until the corps
    # dispatches them; collected here, passed to Campaign by callers
    # that model the corps grade (ignored otherwise — compat).
    data["corps_reserve_units"] = []
    for axis in data["axes"]:
        axes[axis["name"]] = {"spec": axis, "blue": Force("blue"), "red": Force("red")}
    for u in data["units"]:
        bn = Battalion(
            name=u["name"],
            side=u["side"],
            kind=u["kind"],
            cv=u["cv"],
            in_service=u.get("in_service"),
            arrival_day=u.get("arrival_day", 1),
            role=u.get("role", "line"),
            division=u.get("division"),
        )
        if year and bn.in_service and bn.in_service > year:
            dropped.append(bn.name)
            continue
        if bn.role == "corps-reserve":
            data["corps_reserve_units"].append(bn)
            continue
        force = axes[u["axis"]][u["side"]]
        if bn.arrival_day > 1:
            force.reserve.append(bn)
        elif bn.role == "reserve":
            force.withheld.append(bn)
        else:
            force.units.append(bn)
    return data, axes, dropped
