import math

from wargame.models import lanchester


def test_square_invariant_conserved_exact():
    a0, d0, alpha, beta = 100.0, 60.0, 0.02, 0.03
    i0 = lanchester.square_invariant(a0, d0, alpha, beta)
    for t in (0.5, 1.0, 2.0, 5.0):
        a, d = lanchester.square_exact(a0, d0, alpha, beta, t)
        if a > 0 and d > 0:
            i_t = lanchester.square_invariant(a, d, alpha, beta)
            assert math.isclose(i_t, i0, rel_tol=1e-9)


def test_euler_converges_to_exact():
    a0, d0, alpha, beta = 100.0, 60.0, 0.02, 0.03
    t_end = 2.0
    exact = lanchester.square_exact(a0, d0, alpha, beta, t_end)
    for n, tol in ((20, 0.5), (2000, 0.01)):
        a, d = a0, d0
        dt = t_end / n
        for _ in range(n):
            a, d = lanchester.square_step(a, d, alpha, beta, dt)
        assert abs(a - exact[0]) < tol
        assert abs(d - exact[1]) < tol


def test_square_law_concentration():
    """3:1 numbers at equal effectiveness: attacker wins big (the
    square law's classic, contested, claim)."""
    a, d = 300.0, 100.0
    alpha = beta = 0.01
    for _ in range(1000):
        a, d = lanchester.square_step(a, d, alpha, beta, 0.1)
        if d <= 0:
            break
    assert d == 0.0
    # Square law predicts survivor ~ sqrt(9-1)/3 of A: ~94%.
    assert a > 0.9 * 300.0


def test_linear_law_no_concentration_bonus():
    """Linear law, equal effectiveness: absolute losses are EQUAL
    (both = alpha*A*D*dt) regardless of concentration — the square
    law's concentration advantage is absent. The 3:1 side still
    bleeds the same number of points as the 1."""
    a, d = 300.0, 100.0
    a2, d2 = lanchester.linear_step(a, d, 0.001, 0.001, 1.0)
    assert math.isclose(a - a2, d - d2, rel_tol=1e-9)
