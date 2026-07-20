"""Epstein-style adaptive withdrawal.

PROVENANCE: UNVERIFIED. Joshua Epstein, The Calculus of Conventional
War (1985), models the defender as trading ground to hold daily
attrition below a tolerable threshold — his answer to Lanchester's
passive defender. The exact published equations must be verified
against the book (reference/shelf.md purchase list) before any
result from this module feeds canon. What is implemented here is the
documented *shape*: withdrawal rate rises from zero when the
defender's daily loss fraction exceeds its tolerance, saturating at
a maximum withdrawal rate.
"""


def withdrawal_rate_kmd(loss_frac, tolerance, w_max_kmd):
    """Defender's chosen withdrawal rate in km/day.

    loss_frac: today's defender losses / defender strength at dawn.
    tolerance: daily loss fraction the defender will stand and absorb.
    w_max_kmd: maximum feasible withdrawal (march capacity, C2).

    Zero at or below tolerance; linear above it; saturates at w_max
    when the loss rate reaches twice the tolerance. The linear ramp
    and the 2x saturation point are OUR placeholders, not Epstein's.
    """
    if loss_frac <= tolerance:
        return 0.0
    if tolerance <= 0:
        return w_max_kmd
    excess = (loss_frac - tolerance) / tolerance
    return min(w_max_kmd, w_max_kmd * excess)


def contact_attrition_scale(withdrawal_kmd, w_max_kmd, floor=0.35):
    """How much a withdrawal dilutes the day's engagement.

    A defender giving ground fights a delaying action: both sides'
    attrition scales down toward `floor` as withdrawal approaches
    max rate. Placeholder curve (linear), same UNVERIFIED status.
    """
    if w_max_kmd <= 0:
        return 1.0
    frac = min(withdrawal_kmd / w_max_kmd, 1.0)
    return 1.0 - (1.0 - floor) * frac
