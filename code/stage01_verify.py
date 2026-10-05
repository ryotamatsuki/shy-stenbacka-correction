"""Stage 1 exact symbolic checks for Shy & Stenbacka (2005).

This file audits the published source model only. In particular, the
published monitoring cost is i_j**2; there is no free beta coefficient.

Requires: sympy
"""

import sympy as sp

# ---------- Cournot symbolic identities ----------
N, H, D, b, phi, gamma, a = sp.symbols(
    "N H D b phi gamma a", positive=True
)

B = b * (N + 1) ** 2 - H**2 * N
i_c = H * N * D / B

di_dN = sp.factor(sp.diff(i_c, N))
expected_di_dN = -H * D * b * (N**2 - 1) / B**2
assert sp.simplify(di_dN - expected_di_dN) == 0

D_source = a - H * phi - gamma * phi**2 / 2
i_source = sp.simplify(H * N * D_source / B)
f_source = sp.simplify(i_source / phi)

derivatives = {
    "di_da": sp.factor(sp.diff(i_source, a)),
    "di_dgamma": sp.factor(sp.diff(i_source, gamma)),
    "di_dphi": sp.factor(sp.diff(i_source, phi)),
    "df_da": sp.factor(sp.diff(f_source, a)),
    "df_dgamma": sp.factor(sp.diff(f_source, gamma)),
    "df_dphi": sp.factor(sp.diff(f_source, phi)),
}

# ---------- Cournot cap witness ----------
# Satisfies paper restrictions AND a sufficient condition keeping all firms
# active for every feasible outsourcing pair, yet equation (13) exceeds phi.
cap = {
    phi: sp.Rational(1),
    H: sp.Rational(1),
    gamma: sp.Rational(1, 10),
    N: sp.Rational(2),
    b: sp.Rational(1, 2),
    a: sp.Rational(51, 20),
}
C0_cap = (H * phi + gamma * phi**2 / 2).subs(cap)
D_cap = sp.simplify(a.subs(cap) - C0_cap)
concavity_gap_cap = sp.simplify(
    (b * (N + 1) ** 2 - H**2 * N**2).subs(cap)
)
all_active_gap_cap = sp.simplify(
    D_cap - (H * (N - 1) * phi).subs(cap)
)
i_cap = sp.simplify(i_source.subs(cap))

assert D_cap > 0
assert concavity_gap_cap > 0
assert all_active_gap_cap > 0
assert i_cap > cap[phi]

# ---------- Cournot active-set witness ----------
# Paper restrictions hold, but the regular all-active formula assigns a
# negative quantity to the high-cost firm after a feasible Stage-I history.
active = {
    phi: sp.Rational(1),
    H: sp.Rational(1),
    gamma: sp.Rational(1, 10),
    N: sp.Rational(2),
    b: sp.Rational(1, 2),
    a: sp.Rational(5, 4),
}
C0_active = (H * phi + gamma * phi**2 / 2).subs(active)
D_active = sp.simplify(a.subs(active) - C0_active)
concavity_gap_active = sp.simplify(
    (b * (N + 1) ** 2 - H**2 * N**2).subs(active)
)

# Feasible history: own outsourcing 0, rival outsourcing phi.
q_regular_high = sp.simplify(
    (D_active - H.subs(active) * phi.subs(active))
    / (b.subs(active) * (N.subs(active) + 1))
)

c_high = C0_active
c_low = sp.simplify(C0_active - H.subs(active) * phi.subs(active))
q_low_monopoly = sp.simplify(
    (a.subs(active) - c_low) / (2 * b.subs(active))
)
p_low_monopoly = sp.simplify(
    a.subs(active) - b.subs(active) * q_low_monopoly
)

assert D_active > 0
assert concavity_gap_active > 0
assert q_regular_high < 0
assert p_low_monopoly < c_high

# ---------- Hotelling cap witness ----------
Hs, ns, tau, ph = sp.symbols("Hh n tau ph", positive=True)
i_h = Hs * ns / 6

hot_cap = {
    Hs: sp.Rational(1),
    ns: sp.Rational(1),
    tau: sp.Rational(1),
    ph: sp.Rational(1, 10),
}
i_h_cap = sp.simplify(i_h.subs(hot_cap))
hot_soc_gap_cap = sp.simplify(
    (tau - Hs**2 * ns / 18).subs(hot_cap)
)
assert hot_soc_gap_cap > 0
assert i_h_cap > hot_cap[ph]

# ---------- Hotelling global corner-deviation witness ----------
hot = {
    Hs: sp.Rational(1),
    ns: sp.Rational(1),
    tau: sp.Rational(1, 15),
    ph: sp.Rational(1),
}

i0 = sp.simplify(i_h.subs(hot))
idev = sp.simplify((Hs * ns / 2).subs(hot))
cost_advantage = sp.simplify((Hs * (Hs * ns / 2 - Hs * ns / 6)).subs(hot))
interior_threshold = sp.simplify((3 * tau).subs(hot))

pi_sym = sp.simplify((ns * tau / 2 - (Hs * ns / 6) ** 2).subs(hot))
pi_dev = sp.simplify(
    (
        ns * (Hs * (Hs * ns / 2 - Hs * ns / 6) - tau)
        - (Hs * ns / 2) ** 2
    ).subs(hot)
)
gain = sp.simplify(pi_dev - pi_sym)
hot_soc_gap = sp.simplify((tau - Hs**2 * ns / 18).subs(hot))

general_gain = sp.factor(
    ns * (Hs * (Hs * ns / 2 - Hs * ns / 6) - tau)
    - (Hs * ns / 2) ** 2
    - (ns * tau / 2 - (Hs * ns / 6) ** 2)
)
expected_gain = ns * (2 * Hs**2 * ns - 27 * tau) / 18

assert sp.simplify(general_gain - expected_gain) == 0
assert hot_soc_gap > 0
assert idev <= hot[ph]
assert cost_advantage > interior_threshold
assert gain > 0

print("PASS: source-model Stage 1 symbolic checks")
print("Cournot di/dN =", di_dN)
print("Interior comparative statics =", derivatives)
print(
    "Cournot cap witness =",
    {
        "C0": C0_cap,
        "D": D_cap,
        "concavity_gap": concavity_gap_cap,
        "all_active_gap": all_active_gap_cap,
        "paper_i": i_cap,
        "phi": cap[phi],
    },
)
print(
    "Cournot active-set witness =",
    {
        "C0": C0_active,
        "D": D_active,
        "regular_q_high": q_regular_high,
        "monopoly_q_low": q_low_monopoly,
        "monopoly_price_low": p_low_monopoly,
        "high_cost_mc": c_high,
    },
)
print(
    "Hotelling cap witness =",
    {"paper_i": i_h_cap, "phi": hot_cap[ph], "soc_gap": hot_soc_gap_cap},
)
print(
    "Hotelling corner witness =",
    {
        "i0": i0,
        "idev": idev,
        "cost_advantage": cost_advantage,
        "3tau": interior_threshold,
        "pi_sym": pi_sym,
        "pi_dev": pi_dev,
        "gain": gain,
        "soc_gap": hot_soc_gap,
    },
)
print("Hotelling general deviation gain =", general_gain)
