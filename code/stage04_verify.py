"""Stage 4 construction-level verification for the Shy–Stenbacka correction.

Canonical source model only.

Requires:
    sympy==1.14.0

This script verifies:
1. general-N constrained symmetric Cournot equilibrium identities;
2. global Cournot continuation by active sets;
3. duopoly global best-response regime boundaries;
4. duopoly equilibrium-regression examples;
5. Hotelling price-subgame multiplicity outside the interior-share region;
6. correction of the Stage-1 Hotelling deviation claim to a selection-dependent result.

The script is a verification artifact, not a substitute for the analytical proof.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence

import sympy as sp


# ---------------------------------------------------------------------------
# Symbolic general-N Cournot checks
# ---------------------------------------------------------------------------

N, H, D, b, phi, a, gamma = sp.symbols(
    "N H D b phi a gamma", positive=True
)

B = b * (N + 1) ** 2 - H**2 * N
i_int = sp.factor(H * N * D / B)

di_dN = sp.factor(sp.diff(i_int, N))
expected_di_dN = -H * D * b * (N**2 - 1) / B**2
assert sp.simplify(di_dN - expected_di_dN) == 0

D_source = a - H * phi - gamma * phi**2 / 2
i_source = sp.factor(H * N * D_source / B)
f_source = sp.factor(i_source / phi)

assert sp.simplify(sp.diff(i_source, a) - H * N / B) == 0
assert sp.simplify(
    sp.diff(i_source, gamma) + H * N * phi**2 / (2 * B)
) == 0
assert sp.simplify(
    sp.diff(i_source, phi) + H * N * (H + gamma * phi) / B
) == 0
assert sp.simplify(
    sp.diff(f_source, phi)
    + H * N * (2 * a + gamma * phi**2) / (2 * phi**2 * B)
) == 0

cap_gap = sp.factor(sp.together(i_source - phi))
cap_gap_num = sp.factor(cap_gap.as_numer_denom()[0])
expected_cap_num = (
    2 * H * N * a
    - H * N * gamma * phi**2
    - 2 * b * (N + 1) ** 2 * phi
)
assert sp.simplify(cap_gap_num - expected_cap_num) == 0


# ---------------------------------------------------------------------------
# Unique Stage-II Cournot equilibrium from primitives
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CournotOutcome:
    price: Fraction
    quantities: tuple[Fraction, ...]
    active: tuple[int, ...]


def cournot_equilibrium(
    a_: Fraction, b_: Fraction, costs: Sequence[Fraction]
) -> CournotOutcome:
    """Unique linear-Cournot equilibrium with q_j >= 0.

    Costs are sorted only internally; returned quantities preserve original order.
    A firm with c_j == p receives zero output.
    """
    order = sorted(range(len(costs)), key=lambda j: costs[j])
    active: list[int] = []
    p = a_

    for j in order:
        candidate = active + [j]
        p_candidate = (a_ + sum(costs[k] for k in candidate)) / (
            len(candidate) + 1
        )
        if costs[j] < p_candidate:
            active = candidate
            p = p_candidate
        else:
            break

    q = []
    aset = set(active)
    for j, c in enumerate(costs):
        if j in aset:
            q.append((p - c) / b_)
        else:
            q.append(Fraction(0))

    # KKT / best-response conditions.
    for j, c in enumerate(costs):
        if j in aset:
            assert q[j] > 0
            assert p > c
        else:
            assert q[j] == 0
            assert c >= p

    return CournotOutcome(p, tuple(q), tuple(active))


def cournot_stage1_payoff(
    own_i: Fraction,
    rivals_i: Sequence[Fraction],
    *,
    a_: Fraction,
    b_: Fraction,
    C0_: Fraction,
    H_: Fraction,
) -> Fraction:
    xs = [own_i, *rivals_i]
    costs = [C0_ - H_ * x for x in xs]
    out = cournot_equilibrium(a_, b_, costs)
    q0 = out.quantities[0]
    operating = (out.price - costs[0]) * q0
    return operating - own_i**2


# ---------------------------------------------------------------------------
# Stage-1 Cournot counterexamples retained as regressions
# ---------------------------------------------------------------------------

# A. The old all-active formula can fail off path.
aA = Fraction(5, 4)
bA = Fraction(1, 2)
C0A = Fraction(21, 20)
HA = Fraction(1)
phiA = Fraction(1)

outA = cournot_equilibrium(
    aA,
    bA,
    [C0A, C0A - HA * phiA],
)
assert outA.quantities == (Fraction(0), Fraction(6, 5))
assert outA.price == Fraction(13, 20)

# The regular all-active formula would assign q_high = -8/15.
D_A = aA - C0A
q_high_regular = (D_A - HA * phiA) / (3 * bA)
assert q_high_regular == Fraction(-8, 15)

# B. The published symmetric stationary point can exceed phi.
aB = Fraction(51, 20)
bB = Fraction(1, 2)
C0B = Fraction(21, 20)
HB = Fraction(1)
phiB = Fraction(1)
D_B = aB - C0B
i_published_B = 2 * HB * D_B / (9 * bB - 2 * HB**2)
assert i_published_B == Fraction(6, 5)
i_corrected_B = min(phiB, i_published_B)
assert i_corrected_B == 1

# Verify directly on a dense rational grid that i=phi is the best response
# to symmetric rival outsourcing phi for this regression case.
pay_B = cournot_stage1_payoff(
    phiB, [phiB], a_=aB, b_=bB, C0_=C0B, H_=HB
)
for k in range(1001):
    x = phiB * Fraction(k, 1000)
    assert (
        cournot_stage1_payoff(
            x, [phiB], a_=aB, b_=bB, C0_=C0B, H_=HB
        )
        <= pay_B
    )


# ---------------------------------------------------------------------------
# Duopoly normalized global best response
# ---------------------------------------------------------------------------

rho, delta, y = sp.symbols("rho delta y", positive=True)

A = sp.factor(2 * (delta - y) / (9 * rho - 4))
U = delta + 2 * y
M = sp.factor(delta / (4 * rho - 1))

y_A = sp.factor(delta * (2 - 3 * rho) / (2 * (3 * rho - 1)))
y_M = sp.factor(delta * (1 - 2 * rho) / (4 * rho - 1))

assert sp.simplify((A - U).subs(y, y_A)) == 0
assert sp.simplify((M - U).subs(y, y_M)) == 0

s_duo = sp.factor(2 * delta / (9 * rho - 2))
assert sp.simplify(A.subs(y, s_duo) - s_duo) == 0
assert sp.simplify(sp.diff(A, y) + 2 / (9 * rho - 4)) == 0
assert sp.simplify(sp.diff(U, y) - 2) == 0


def R_uncon(y_: Fraction, d_: Fraction, r_: Fraction) -> Fraction:
    """Unconstrained global Cournot-outsourcing BR for the source duopoly.

    Valid for r_ = b/H^2 > 4/9.
    """
    assert r_ > Fraction(4, 9)
    if y_ >= d_:
        return Fraction(0)

    A_ = 2 * (d_ - y_) / (9 * r_ - 4)
    U_ = d_ + 2 * y_
    M_ = d_ / (4 * r_ - 1)

    if A_ <= U_:
        return A_
    if M_ >= U_:
        return M_
    return U_


def B_constrained(
    y_: Fraction, d_: Fraction, r_: Fraction, phi_: Fraction
) -> Fraction:
    return min(phi_, R_uncon(y_, d_, r_))


# Regression: source-admissible region with a globally increasing BR segment.
rC = Fraction(3, 5)  # 0.6 in (4/9, 2/3)
dC = Fraction(1)
phiC = Fraction(2)

assert R_uncon(Fraction(0), dC, rC) == 1
assert R_uncon(Fraction(1, 20), dC, rC) == Fraction(11, 10)

sC = Fraction(10, 17)
assert B_constrained(sC, dC, rC, phiC) == sC
assert B_constrained(Fraction(0), dC, rC, phiC) == 1
assert B_constrained(Fraction(1), dC, rC, phiC) == 0

# Thus three exact Stage-I equilibria exist in this source-admissible example.
eqC = [
    (sC, sC),
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
]
for x_, y_ in eqC:
    assert B_constrained(y_, dC, rC, phiC) == x_
    assert B_constrained(x_, dC, rC, phiC) == y_


# ---------------------------------------------------------------------------
# Hotelling full-demand price game
# ---------------------------------------------------------------------------

def hotelling_price_br_contains(
    own_price: Fraction,
    other_price: Fraction,
    own_cost: Fraction,
    tau_: Fraction,
) -> bool:
    """Analytical best-response membership under clipped full-coverage demand."""
    z = other_price - own_cost

    if z < -tau_:
        return own_price >= other_price + tau_
    if z == -tau_:
        return own_price >= other_price + tau_
    if z < 3 * tau_:
        return own_price == (other_price + own_cost + tau_) / 2
    # z >= 3 tau: unique full-capture boundary price
    return own_price == other_price - tau_


def hotelling_price_equilibrium(
    pA: Fraction,
    pB: Fraction,
    cA: Fraction,
    cB: Fraction,
    tau_: Fraction,
) -> bool:
    return (
        hotelling_price_br_contains(pA, pB, cA, tau_)
        and hotelling_price_br_contains(pB, pA, cB, tau_)
    )


# Multiplicity regression: cost gap d_c > 3 tau.
tauH = Fraction(1, 15)
cL = Fraction(0)
cH = Fraction(1, 3)

assert cH - cL > 3 * tauH

# Lower and upper endpoints of the equilibrium continuum.
pH_low = cL + 3 * tauH
pL_low = pH_low - tauH
pH_high = cH
pL_high = pH_high - tauH

assert hotelling_price_equilibrium(pL_low, pH_low, cL, cH, tauH)
assert hotelling_price_equilibrium(pL_high, pH_high, cL, cH, tauH)

# Stage-1 witness from the earlier audit: same outsourcing deviation,
# opposite profitability depending on the valid price-continuation selection.
nH = Fraction(1)
i0H = Fraction(1, 6)
idevH = Fraction(1, 2)

pi_sym_H = nH * tauH / 2 - i0H**2
pi_dev_low = nH * (pL_low - cL) - idevH**2
pi_dev_high = nH * (pL_high - cL) - idevH**2

assert pi_sym_H == Fraction(1, 180)
assert pi_dev_low == Fraction(-7, 60)
assert pi_dev_high == Fraction(1, 60)
assert pi_dev_low < pi_sym_H < pi_dev_high


# Symbolic selection-dependence thresholds.
Hs, ns, tau = sp.symbols("Hs ns tau", positive=True)
i0 = Hs * ns / 6
ib = i0 + 3 * tau / Hs

pi_sym = ns * tau / 2 - i0**2
pi_min_boundary = 2 * ns * tau - ib**2
min_gain = sp.factor(pi_min_boundary - pi_sym)
expected_min_gain = tau * (Hs**2 * ns - 18 * tau) / (2 * Hs**2)
assert sp.simplify(min_gain - expected_min_gain) == 0

istar = Hs * ns / 2
pi_max_corner = ns * (Hs * (istar - i0) - tau) - istar**2
max_gain = sp.factor(pi_max_corner - pi_sym)
expected_max_gain = ns * (2 * Hs**2 * ns - 27 * tau) / 18
assert sp.simplify(max_gain - expected_max_gain) == 0


print("PASS: Stage 4 exact construction checks")
print("General-N Cournot di/dN =", di_dN)
print("General-N interior derivatives =", {
    "di/da": sp.factor(sp.diff(i_source, a)),
    "di/dgamma": sp.factor(sp.diff(i_source, gamma)),
    "di/dphi": sp.factor(sp.diff(i_source, phi)),
    "d(i/phi)/dphi": sp.factor(sp.diff(f_source, phi)),
})
print("Duopoly A(y) =", A)
print("Duopoly U(y) =", U)
print("Duopoly M =", M)
print("Duopoly symmetric interior s =", s_duo)
print("Hotelling minimum-selection corner gain =", min_gain)
print("Hotelling maximum-selection corner gain =", max_gain)
print("Regression equilibria at rho=3/5, delta=1:", eqC)
