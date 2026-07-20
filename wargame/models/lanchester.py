"""Lanchester attrition laws.

PROVENANCE: canonical (Lanchester 1916; any operations-research
text). The square law models aimed fire (each side's loss rate
proportional to the opposing force size); the linear law models
unaimed/area fire. Both are the baseline the period's own debate
attacked — see planning/wargaming.md.
"""

import math


def square_step(a, d, alpha, beta, dt=1.0):
    """One Euler step of the square law.

    dA/dt = -beta * D ;  dD/dt = -alpha * A

    alpha: effectiveness of A's fire against D (per unit A per day).
    beta: effectiveness of D's fire against A.
    Returns (a', d'), floored at zero.
    """
    a_new = max(a - beta * d * dt, 0.0)
    d_new = max(d - alpha * a * dt, 0.0)
    return a_new, d_new


def square_exact(a0, d0, alpha, beta, t):
    """Closed-form square-law state at time t (both sides positive).

    A(t) = A0 cosh(kt) - sqrt(beta/alpha) D0 sinh(kt), k = sqrt(alpha*beta).
    Valid until one side reaches zero; results floored at zero.
    """
    k = math.sqrt(alpha * beta)
    ch, sh = math.cosh(k * t), math.sinh(k * t)
    a = a0 * ch - math.sqrt(beta / alpha) * d0 * sh
    d = d0 * ch - math.sqrt(alpha / beta) * a0 * sh
    return max(a, 0.0), max(d, 0.0)


def square_invariant(a, d, alpha, beta):
    """alpha*A^2 - beta*D^2, conserved along square-law trajectories.

    Positive: A wins the fight-to-annihilation; negative: D wins.
    """
    return alpha * a * a - beta * d * d


def linear_step(a, d, alpha, beta, dt=1.0):
    """One Euler step of the linear (area-fire) law.

    dA/dt = -beta * A * D ;  dD/dt = -alpha * A * D
    """
    a_new = max(a - beta * a * d * dt, 0.0)
    d_new = max(d - alpha * a * d * dt, 0.0)
    return a_new, d_new
