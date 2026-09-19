"""Independent repair verifier for the 2026-09-20 clean-room audit.

This file does not import the production best-response functions. Cournot payoffs
are reconstructed from primitive nonnegative-quantity active sets. Exact
candidate maximization is then performed over stationary points and regime
boundaries of those primitive payoff pieces. Symbolic identities support the
analytic proofs in the manuscript; finite parameter checks are regressions, not
substitutes for those proofs.
"""

from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import sympy as sp


# ---------------------------------------------------------------------------
# Primitive Cournot continuation and direct reduced payoff
# ---------------------------------------------------------------------------

def cournot_active_sets(a: F, b: F, costs: list[F]):
    out = []
    n = len(costs)
    for m in range(1, n + 1):
        for S0 in combinations(range(n), m):
            S = set(S0)
            p = (a + sum(costs[j] for j in S)) / (m + 1)
            q = [F(0) for _ in range(n)]
            ok = True
            for j in range(n):
                if j in S:
                    q[j] = (p - costs[j]) / b
                    if q[j] <= 0:
                        ok = False
                        break
                elif costs[j] < p:
                    ok = False
                    break
            if ok:
                out.append((p, tuple(q), tuple(sorted(S))))
    return out


def normalized_payoff(x: F, y: F, delta: F, rho: F) -> F:
    # Equivalent normalization H=1, C0=0, a=delta.
    sols = cournot_active_sets(delta, rho, [-x, -y])
    assert len(sols) == 1
    p, q, _ = sols[0]
    return (p + x) * q[0] - x * x


def candidate_points(y: F, delta: F, rho: F, phi: F) -> list[F]:
    pts = {F(0), phi}
    # Own-entry boundary, rival-exit boundary, and branch stationary points.
    raw = [
        (y - delta) / 2,
        delta + 2 * y,
        2 * (delta - y) / (9 * rho - 4),
        delta / (4 * rho - 1),
    ]
    for z in raw:
        if 0 <= z <= phi:
            pts.add(z)
    return sorted(pts)


def direct_best_responses(y: F, delta: F, rho: F, phi: F) -> tuple[F, ...]:
    pts = candidate_points(y, delta, rho, phi)
    vals = [(normalized_payoff(x, y, delta, rho), x) for x in pts]
    vmax = max(v for v, _ in vals)
    return tuple(x for v, x in vals if v == vmax)


def is_eq(x: F, y: F, delta: F, rho: F, phi: F) -> bool:
    return x in direct_best_responses(y, delta, rho, phi) and y in direct_best_responses(x, delta, rho, phi)


# ---------------------------------------------------------------------------
# F01: cap feasibility of the positive-slope rival-exit response
# ---------------------------------------------------------------------------

rho = F(3, 5)
delta = F(1)

# Source-feasible primitive witness from the external audit.
H = F(1)
gamma = F(1)
phi_small = F(1, 10)
b = F(3, 5)
C0 = H * phi_small + gamma * phi_small * phi_small / 2
a = F(221, 200)
D = a - C0
assert C0 == F(21, 200)
assert D == 1
assert b > (F(2, 3) * H) ** 2

for y in (F(0), F(1, 20), F(1, 10)):
    assert direct_best_responses(y, delta, rho, phi_small) == (phi_small,)

# rho=3/5: positive-length feasibility switches strictly at phi=delta.
for cap in (F(99, 100), F(1)):
    assert direct_best_responses(F(0), delta, rho, cap) == (cap,)
    y = min(cap, F(1, 400))
    assert direct_best_responses(y, delta, rho, cap) == (cap,)
cap = F(101, 100)
assert direct_best_responses(F(0), delta, rho, cap) == (F(1),)
assert direct_best_responses(F(1, 400), delta, rho, cap) == (F(201, 200),)

# 4/9<rho<1/2 representative: rho=17/36 gives M=9/8, y_M=1/16.
rho_low = F(17, 36)
M_low = F(9, 8)
yM_low = F(1, 16)
assert delta / (4 * rho_low - 1) == M_low
assert delta * (1 - 2 * rho_low) / (4 * rho_low - 1) == yM_low
for cap in (M_low - F(1, 100), M_low):
    assert direct_best_responses(yM_low, delta, rho_low, cap) == (cap,)
    assert direct_best_responses(yM_low + F(1, 400), delta, rho_low, cap) == (cap,)
cap = M_low + F(1, 100)
assert direct_best_responses(yM_low, delta, rho_low, cap) == (M_low,)
assert direct_best_responses(yM_low + F(1, 400), delta, rho_low, cap) == (M_low + F(1, 200),)

# rho=1/2 joins the upper regime: M=delta, y_M=0.
rho_half = F(1, 2)
assert delta / (4 * rho_half - 1) == delta
assert delta * (1 - 2 * rho_half) / (4 * rho_half - 1) == 0
assert direct_best_responses(F(0), delta, rho_half, F(1)) == (F(1),)
assert direct_best_responses(F(1, 400), delta, rho_half, F(1)) == (F(1),)
assert direct_best_responses(F(0), delta, rho_half, F(101, 100)) == (F(1),)
assert direct_best_responses(F(1, 400), delta, rho_half, F(101, 100)) == (F(201, 200),)

# Existing large-cap witness survives.
assert direct_best_responses(F(0), delta, F(3, 5), F(2)) == (F(1),)
assert direct_best_responses(F(1, 20), delta, F(3, 5), F(2)) == (F(11, 10),)


# ---------------------------------------------------------------------------
# F02: symbolic identities behind the complete pure correspondence
# ---------------------------------------------------------------------------

r, d, z, ph = sp.symbols("r d z ph", positive=True)
A = 2 * (d - z) / (9 * r - 4)
s = 2 * d / (9 * r - 2)
yA = d * (2 - 3 * r) / (2 * (3 * r - 1))
yM = d * (1 - 2 * r) / (4 * r - 1)

assert sp.factor(A - z) == (2 * d - (9 * r - 2) * z) / (9 * r - 4)
assert sp.factor(s - yA) == 3 * d * r * (9 * r - 4) / (2 * (3 * r - 1) * (9 * r - 2))
assert sp.factor(d - s) == d * (9 * r - 4) / (9 * r - 2)
assert sp.factor(yA - yM) == d * r / (2 * (3 * r - 1) * (4 * r - 1))

Aph = 2 * (d - ph) / (9 * r - 4)
AAph = sp.factor(2 * (d - Aph) / (9 * r - 4) - ph)
assert AAph == 3 * (3 * r - 2) * (2 * d - (9 * r - 2) * ph) / (9 * r - 4) ** 2

# Representative exact equilibria for all five theorem regimes/boundaries.
assert is_eq(F(8, 19), F(8, 19), F(1), F(3, 4), F(2))
assert is_eq(F(2, 5), F(2, 5), F(1), F(2, 3), F(2, 5))
assert is_eq(F(1, 2), F(1, 2), F(1), F(2, 3), F(1, 2))
for x, y in ((F(1, 4), F(3, 4)), (F(1, 2), F(1, 2)), (F(3, 4), F(1, 4))):
    assert is_eq(x, y, F(1), F(2, 3), F(3, 4))
assert is_eq(F(1, 2), F(1, 2), F(1), F(3, 5), F(1, 2))  # phi<s
assert is_eq(F(10, 17), F(10, 17), F(1), F(3, 5), F(10, 17))  # phi=s
for x, y in ((F(10, 17), F(10, 17)), (F(3, 4), F(5, 14)), (F(5, 14), F(3, 4))):
    assert is_eq(x, y, F(1), F(3, 5), F(3, 4))
for x, y in ((F(10, 17), F(10, 17)), (F(1), F(0)), (F(0), F(1))):
    assert is_eq(x, y, F(1), F(3, 5), F(1))
    assert is_eq(x, y, F(1), F(3, 5), F(2))
# Low-rho R(0)=M boundary.
assert is_eq(F(9, 8), F(0), F(1), F(17, 36), F(9, 8))
assert is_eq(F(0), F(9, 8), F(1), F(17, 36), F(9, 8))


# ---------------------------------------------------------------------------
# F03: multiplicity with all feasible sourcing histories both active
# ---------------------------------------------------------------------------

phi_all = F(3, 4)
gamma_all = F(1)
C0_all = phi_all + gamma_all * phi_all * phi_all / 2
a_all = C0_all + 1
assert C0_all == F(33, 32)
assert a_all == F(65, 32)

# Both normalized quantity numerators are positive over the entire box.
for x in (F(0), phi_all):
    for y in (F(0), phi_all):
        assert 1 + 2 * x - y >= F(1, 4)
        assert 1 + 2 * y - x >= F(1, 4)

all_active_eq = (
    (F(10, 17), F(10, 17)),
    (F(3, 4), F(5, 14)),
    (F(5, 14), F(3, 4)),
)
for x, y in all_active_eq:
    assert is_eq(x, y, F(1), F(3, 5), phi_all)


# ---------------------------------------------------------------------------
# Literal Hotelling: direct payoff candidate checks
# ---------------------------------------------------------------------------

def share(p: F, rprice: F, tau: F) -> F:
    q = F(1, 2) + (rprice - p) / (2 * tau)
    return max(F(0), min(F(1), q))


def price_profit(p: F, rprice: F, c: F, tau: F) -> F:
    return (p - c) * share(p, rprice, tau)


def max_price_candidate_profit(rprice: F, c: F, tau: F) -> F:
    pts = {
        rprice - tau,
        rprice + tau,
        (rprice + tau + c) / 2,
        c,
    }
    return max(price_profit(p, rprice, c, tau) for p in pts)


def is_price_br(p: F, rprice: F, c: F, tau: F) -> bool:
    return price_profit(p, rprice, c, tau) == max_price_candidate_profit(rprice, c, tau)


tau1 = F(1)
# Interior d=1.
cA, cB = F(1), F(2)
pA = (2 * cA + cB + 3 * tau1) / 3
pB = (cA + 2 * cB + 3 * tau1) / 3
assert is_price_br(pA, pB, cA, tau1)
assert is_price_br(pB, pA, cB, tau1)

# Boundary d=3.
cA, cB = F(1), F(4)
assert is_price_br(F(3), F(4), cA, tau1)
assert is_price_br(F(4), F(3), cB, tau1)

# Corner d=4, including endpoints and interior.
cA, cB = F(1), F(5)
for zz in (F(4), F(9, 2), F(5)):
    assert is_price_br(zz - 1, zz, cA, tau1)
    assert is_price_br(zz, zz - 1, cB, tau1)
# Mirror.
for zz in (F(4), F(9, 2), F(5)):
    assert is_price_br(zz, zz - 1, cA + 4, tau1)
    assert is_price_br(zz - 1, zz, cA, tau1)


# ---------------------------------------------------------------------------
# Weak dominance and no-loss theorem
# ---------------------------------------------------------------------------

c = F(1)
eps = F(1, 10)
for rr in [F(k, 10) for k in range(-20, 41)]:
    for pp in (F(-1), F(0), F(9, 10)):
        if pp < c:
            assert price_profit(c, rr, c, F(1, 5)) >= price_profit(pp, rr, c, F(1, 5))
    assert price_profit(c + eps, rr, c, F(1, 5)) >= price_profit(c, rr, c, F(1, 5))
assert price_profit(c + eps, c + eps, c, F(1, 5)) > price_profit(c, c + eps, c, F(1, 5))

# Exact no-loss strict-gain and cap-tie regressions.
Hn = F(1)
tau = F(1, 15)
i0 = F(1, 6)

def v_no_loss(x: F, y: F, tau: F) -> F:
    k = 3 * tau
    if x - y <= -k:
        return -x * x
    if x - y <= k:
        return (3 * tau + x - y) ** 2 / (18 * tau) - x * x
    return (x - y - tau) - x * x

assert v_no_loss(F(1, 2), i0, tau) - v_no_loss(i0, i0, tau) == F(1, 90)
tau_tie = F(5, 72)
xminus_tie = F(5, 12)
assert v_no_loss(xminus_tie, F(1, 6), tau_tie) == v_no_loss(F(1, 6), F(1, 6), tau_tie)


# ---------------------------------------------------------------------------
# Welfare and manuscript-scope regressions
# ---------------------------------------------------------------------------

def welfare_norm(x: F, y: F, delta: F = F(1), rho: F = F(3, 5)) -> F:
    sols = cournot_active_sets(delta, rho, [-x, -y])
    assert len(sols) == 1
    _, q, _ = sols[0]
    Q = q[0] + q[1]
    return delta * Q - rho * Q * Q / 2 + x * q[0] + y * q[1] - x * x - y * y

assert welfare_norm(F(10, 17), F(10, 17)) == F(20, 17)
assert welfare_norm(F(1), F(0)) == F(3, 2)
assert welfare_norm(F(0), F(1)) == F(3, 2)

paper = Path("paper")
text = "\n".join(p.read_text(encoding="utf-8") for p in paper.rglob("*.tex"))
assert "positive-length increasing piece survives" in text
assert "exit is not necessary for multiplicity" in text
assert "source of multiplicity is therefore not own-payoff nonconcavity; it is the change in downstream participation" not in text
assert "At \\(\\phi=\\delta/2\\) it is a singleton" in text or "at \\(\\phi=\\delta/2\\) it is a singleton" in text
assert "\\widetilde W_C" in text

print("Independent-audit repair verification PASS")
print("F01 small-cap counterexample and strict cap thresholds: PASS")
print("F02 five-case / equality regression suite: PASS (analytic completeness proof is in appendix)")
print("F03 all-feasible-histories-active multiplicity regression: PASS")
print("Literal Hotelling BR/equilibrium regressions: PASS")
print("Weak-dominance and no-loss strict/tie regressions: PASS")
print("Welfare and manuscript-scope regressions: PASS")
