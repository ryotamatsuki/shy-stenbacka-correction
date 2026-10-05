"""Independent Stage-11 hostile-referee regression checks.

This file deliberately reconstructs high-stakes examples from primitives instead
of importing the Stage-4/Stage-7 verification code.
"""

from fractions import Fraction as F
from pathlib import Path

# ---------------------------------------------------------------------------
# 1. Cournot direct-payoff reconstruction at the exact three-equilibrium witness
# ---------------------------------------------------------------------------

D = F(1)
H = F(1)
B = F(3, 5)  # rho = b / H^2 = 3/5
PHI = F(2)
GAMMA = F(1, 2)
C0 = H * PHI + GAMMA * PHI * PHI / 2
A = C0 + D
assert C0 == F(3)
assert A == F(4)


def downstream_quantities(x: F, y: F) -> tuple[F, F]:
    """Unique nonnegative Cournot continuation from source-feasible primitives."""
    a = A
    c_a = C0 - H * x
    c_b = C0 - H * y

    q_a = (a - 2 * c_a + c_b) / (3 * B)
    q_b = (a - 2 * c_b + c_a) / (3 * B)

    if q_a >= 0 and q_b >= 0:
        return q_a, q_b
    if q_b < 0:
        return (a - c_a) / (2 * B), F(0)
    if q_a < 0:
        return F(0), (a - c_b) / (2 * B)
    raise AssertionError("unreachable active-set case")


def payoff_a(x: F, y: F) -> F:
    q_a, q_b = downstream_quantities(x, y)
    p = A - B * (q_a + q_b)
    c_a = C0 - H * x
    return (p - c_a) * q_a - x * x


def welfare(x: F, y: F) -> F:
    q_a, q_b = downstream_quantities(x, y)
    q = q_a + q_b
    return D * q - B * q * q / 2 + x * q_a + y * q_b - x * x - y * y


# Against y=0, the rival-exit kink x=1 is globally optimal:
# left derivative is positive, right derivative is negative.
x0 = F(1)
left_d0 = 4 * (D + 2 * x0) / (9 * B) - 2 * x0
right_d0 = (D + x0) / (2 * B) - 2 * x0
assert left_d0 > 0 > right_d0
assert payoff_a(F(1), F(0)) == F(2, 3)

# A stronger rival y=1/20 shifts the optimal exit-inducing action to 11/10.
y1 = F(1, 20)
x1 = F(11, 10)
left_d1 = 4 * (D + 2 * x1 - y1) / (9 * B) - 2 * x1
right_d1 = (D + x1) / (2 * B) - 2 * x1
assert left_d1 > 0 > right_d1
assert payoff_a(x1, y1) == F(251, 400)
assert payoff_a(x1, y1) > payoff_a(F(1), y1)

# Exact symmetric equilibrium and welfare-selection regression.
s = F(10, 17)
assert payoff_a(s, s) == F(35, 289)
assert welfare(s, s) == F(20, 17)
assert welfare(F(1), F(0)) == F(3, 2)
assert welfare(F(0), F(1)) == F(3, 2)

# Knife-edge / boundary attacks on the pure correspondence.
def r_response(y: F, rho: F, delta: F = F(1)) -> F:
    if y >= delta:
        return F(0)
    if rho >= F(2, 3):
        return 2 * (delta - y) / (9 * rho - 4)
    y_a = delta * (2 - 3 * rho) / (2 * (3 * rho - 1))
    if rho >= F(1, 2):
        return delta + 2 * y if y <= y_a else 2 * (delta - y) / (9 * rho - 4)
    y_m = delta * (1 - 2 * rho) / (4 * rho - 1)
    if y <= y_m:
        return delta / (4 * rho - 1)
    if y <= y_a:
        return delta + 2 * y
    return 2 * (delta - y) / (9 * rho - 4)


# rho=2/3 continuum: x+y=delta when the cap permits.
rho_edge = F(2, 3)
assert r_response(F(7, 10), rho_edge) == F(3, 10)
assert r_response(F(3, 10), rho_edge) == F(7, 10)

# phi=s equality belongs to the unique capped-symmetric regime.
rho_three = F(3, 5)
s_three = F(10, 17)
assert min(s_three, r_response(s_three, rho_three)) == s_three

# Internal BR partition is continuous at rho=1/2.
rho_half = F(1, 2)
y_a_half = F(1, 2)
assert r_response(F(0), rho_half) == F(1)
assert r_response(y_a_half, rho_half) == F(2)

# Stronger convex monitoring destroys the source global-BR conclusion.
# At y=0, rho=3/5, delta=1: x=0 gives 5/27, while x=1 gives
# monopoly operating profit 5/3 minus monitoring cost 10.
assert payoff_a(F(0), F(0)) == F(5, 27)
assert F(5, 3) - 10 == F(-25, 3)
assert F(-25, 3) < F(5, 27)

# ---------------------------------------------------------------------------
# 2. Literal Hotelling corner-continuation reconstruction
# ---------------------------------------------------------------------------

TAU = F(1)
C_A = F(0)
C_B = F(4)  # d=4 > 3*tau


def low_cost_boundary_is_best(z: F) -> bool:
    """For rival price z, compare the full-market boundary with interior vertex."""
    p_boundary = z - TAU
    p_vertex = (z + TAU + C_A) / 2
    return p_boundary >= p_vertex and z >= C_A + 3 * TAU


for z in (F(3), F(7, 2), F(4)):
    assert C_A + 3 * TAU <= z <= C_B
    assert low_cost_boundary_is_best(z)
    p_a = z - TAU
    # High-cost firm gets zero demand at z. Any positive-demand deviation must
    # price below z <= c_B and therefore cannot earn positive operating profit.
    assert z <= C_B
    low_profit = (p_a - C_A)  # full market, unit density
    assert low_profit == z - TAU

# The low-cost continuation profit varies across the valid pure corner family.
assert F(3) - TAU != F(4) - TAU

# ---------------------------------------------------------------------------
# 3. Auxiliary no-loss Hotelling exact deviation
# ---------------------------------------------------------------------------

HN = F(1)
tau = F(1, 15)
y = F(1, 6)


def v_no_loss(x: F) -> F:
    k = 3 * tau
    if x - y <= -k:
        return -x * x
    if x - y <= k:
        return (3 * tau + (x - y)) ** 2 / (18 * tau) - x * x
    return (x - y - tau) - x * x


assert v_no_loss(F(1, 6)) == F(1, 180)
assert v_no_loss(F(1, 2)) == F(1, 60)
assert v_no_loss(F(1, 2)) - v_no_loss(F(1, 6)) == F(1, 90)

# Exact H5 boundary tie with a rational square root:
# H=n=1, tau=5/72 gives x_-=5/12.
tau_tie = F(5, 72)
x_minus = F(5, 12)
delta_tie = -(
    36 * x_minus * x_minus
    - 36 * x_minus
    + 5
    + 54 * tau_tie
) / 36
assert delta_tie == 0
assert F(27, 2) * tau_tie < 1 < 18 * tau_tie

# ---------------------------------------------------------------------------
# 4. Manuscript scope / citation lint for Stage-11 claim inflation
# ---------------------------------------------------------------------------

paper = Path("paper")
text = "\n".join(p.read_text(encoding="utf-8") for p in paper.rglob("*.tex"))

for forbidden in (
    "unique general-N SPNE",
    "undominated-price refinement",
    "formal verification of the complete Shy",
    "Proposition 6 is false in every literal-source SPNE",
    "complete pure-strategy re-characterization of a specific published model",
):
    assert forbidden not in text, forbidden

required = (
    "complete pure Stage-I re-characterization of its Cournot source-duopoly case",
    "does not imply that outsourcing is globally a strategic complement",
    "not a new general theory of outsourcing",
    "complete mixed-strategy correspondence",
    "not formally mechanized",
    "positive-length increasing piece survives",
    "exit is not necessary for multiplicity",
)
for phrase in required:
    assert phrase in text, phrase

assert "source of multiplicity is therefore not own-payoff nonconcavity; it is the change in downstream participation" not in text
assert "For \\(4/9<\\rho<2/3\\), the pure global sourcing best response contains a feasible rival-exit segment" not in text

# Every manuscript citation key must exist in the bibliography.
import re
bib = (paper / "references.bib").read_text(encoding="utf-8")
bib_keys = set(re.findall(r"@[A-Za-z]+\\{([^,]+),", bib))
cite_keys = set()
for match in re.findall(r"\\cite\\{([^}]+)\\}", text):
    cite_keys.update(k.strip() for k in match.split(","))
missing = cite_keys - bib_keys
assert not missing, sorted(missing)

print("Stage-11 hostile-referee regression PASS")
print("Cournot finite-deviation / active-set attack: PASS")
print("Literal Hotelling corner-selection attack: PASS")
print("No-loss exact 1/90 deviation: PASS")
print("Welfare-selection regression: PASS")
print("Knife-edge / cap / function-class attacks: PASS")
print("Manuscript scope and citation lint: PASS")
