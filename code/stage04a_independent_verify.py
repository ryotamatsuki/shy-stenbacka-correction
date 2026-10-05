"""Stage 4A independent clean-room verification.

This file is intentionally independent of code/stage04_verify.py and
code/stage04_hotelling_refinement_verify.py.  It reconstructs continuation
objects directly from primitive payoffs/active-set conditions.

Requires sympy==1.14.0.
"""

from fractions import Fraction
from itertools import combinations
import sympy as sp

# ---------------------------------------------------------------------------
# I. Cournot continuation: brute-force active-set enumeration
# ---------------------------------------------------------------------------

def cournot_all_valid_active_sets(a, b, costs):
    """Enumerate every strict-positive-output active set satisfying KKT."""
    n = len(costs)
    out = []
    for m in range(1, n + 1):
        for S0 in combinations(range(n), m):
            S = set(S0)
            p = (a + sum(costs[j] for j in S)) / (m + 1)
            q = [Fraction(0) for _ in range(n)]
            ok = True
            for j in range(n):
                if j in S:
                    q[j] = (p - costs[j]) / b
                    if q[j] <= 0:
                        ok = False
                        break
                else:
                    if costs[j] < p:
                        ok = False
                        break
            if ok:
                out.append((p, tuple(q), tuple(sorted(S))))
    return out


def cournot_payoff_direct(x, y, delta, rho):
    """Normalized source-duopoly payoff reconstructed from primitive quantities.

    Normalize H=1, C0=0, hence a=delta and costs are -x,-y.
    """
    sols = cournot_all_valid_active_sets(
        delta, rho, [-x, -y]
    )
    assert len(sols) == 1
    p, q, _ = sols[0]
    return (p + x) * q[0] - x*x


# Exact stress histories, including ties and zero-output boundaries.
tests = [
    (Fraction(1), Fraction(1,2), [Fraction(0), Fraction(-1)]),
    (Fraction(1), Fraction(3,5), [Fraction(-1), Fraction(0)]),
    (Fraction(2), Fraction(2,3), [Fraction(0), Fraction(0)]),
    (Fraction(3), Fraction(5,4), [Fraction(1), Fraction(1), Fraction(2)]),
    (Fraction(4), Fraction(7,5), [Fraction(0), Fraction(1), Fraction(1), Fraction(2)]),
]
for a0,b0,c0 in tests:
    sols = cournot_all_valid_active_sets(a0,b0,c0)
    assert len(sols) == 1

# Stage-4 exact duopoly regression: rho=3/5, delta=1, phi=2.
rho0 = Fraction(3,5)
delta0 = Fraction(1)
phi0 = Fraction(2)
s0 = Fraction(10,17)

equilibria = [
    (s0,s0),
    (Fraction(1),Fraction(0)),
    (Fraction(0),Fraction(1)),
]

# Independent finite-deviation attack on a fine exact rational grid.
for x0,y0 in equilibria:
    incumbent = cournot_payoff_direct(x0,y0,delta0,rho0)
    for k in range(2001):
        z = phi0*Fraction(k,2000)
        assert cournot_payoff_direct(z,y0,delta0,rho0) <= incumbent


# ---------------------------------------------------------------------------
# II. Cournot symbolic claims reconstructed independently
# ---------------------------------------------------------------------------

N,H,D,b = sp.symbols("N H D b", positive=True)
iC = H*N*D/(b*(N+1)**2-H**2*N)
di = sp.factor(sp.diff(iC,N))
assert sp.simplify(
    di + H*D*b*(N**2-1)/(b*(N+1)**2-H**2*N)**2
) == 0

k,z = sp.symbols("k z", positive=True)
curv = 2*H**2*k**2/(b*(k+1)**2)-2
# The Stage-4 source SOC at k=N implies branch curvature <0 because
# k/(k+1) is increasing.  This assertion records the derivative-jump sign.
jump_drop = sp.simplify(
    2*z*H/b*(k/(k+1)-(k-1)/k)
)
assert sp.simplify(jump_drop-2*z*H/(b*k*(k+1))) == 0


# ---------------------------------------------------------------------------
# III. Hotelling primitives and literal price equilibrium
# ---------------------------------------------------------------------------

def share_A(pA,pB,tau):
    x = Fraction(1,2)+(pB-pA)/(2*tau)
    return max(Fraction(0),min(Fraction(1),x))


def operating_profit(pA,pB,cA,tau,n=Fraction(1)):
    return n*(pA-cA)*share_A(pA,pB,tau)


# H-DOM1: every below-cost price is weakly dominated by marginal-cost pricing.
# Exact adversarial price grid.
c = Fraction(1)
tau0 = Fraction(1,5)
for p in [Fraction(k,10) for k in range(-10,10)]:
    if p < c:
        for r in [Fraction(k,10) for k in range(-20,41)]:
            assert operating_profit(c,r,c,tau0) >= operating_profit(p,r,c,tau0)

# Stage-4A refinement attack:
# p=c is itself weakly dominated by every fixed p=c+eps, eps>0.
eps = Fraction(1,10)
for r in [Fraction(k,10) for k in range(-20,41)]:
    assert operating_profit(c+eps,r,c,tau0) >= operating_profit(c,r,c,tau0)
# Strict for a rival price giving positive demand.
assert operating_profit(c+eps,c+eps,c,tau0) > operating_profit(c,c+eps,c,tau0)

# Therefore p>=c may be used as an explicit no-loss strategy restriction,
# but the selected p=c corner equilibrium must NOT be called an equilibrium
# obtained by eliminating all weakly dominated strategies.


# Literal corner continuum regression, d>3*tau.
cL = Fraction(0)
cH = Fraction(1,3)
t = Fraction(1,15)
assert cH-cL > 3*t

# Three distinct literal corner equilibria.
for pH in [
    cL+3*t,
    (cL+3*t+cH)/2,
    cH,
]:
    pL = pH-t
    # Low-cost firm captures whole market.
    assert share_A(pL,pH,t) == 1
    # Direct local/global BR membership follows from exact branch conditions:
    assert pH >= cL+3*t
    assert pH <= cH

# Under explicit no-loss restriction pH>=cH, only upper endpoint survives.
assert max(cL+3*t,cH) == cH


# ---------------------------------------------------------------------------
# IV. Hotelling no-loss restricted Stage-I theorem
# ---------------------------------------------------------------------------

Hs,ns,tau,x,y = sp.symbols("Hs ns tau x y", positive=True)
i0 = Hs*ns/6
threshold = 3*tau/Hs

VI = ns*(3*tau+Hs*(x-y))**2/(18*tau)-x**2
VF = ns*(Hs*(x-y)-tau)-x**2
VZ = -x**2

assert sp.simplify(VI.subs(x,y-threshold)-VZ.subs(x,y-threshold)) == 0
assert sp.simplify(VI.subs(x,y+threshold)-VF.subs(x,y+threshold)) == 0

u = Hs*ns*(3*tau-Hs*y)/(18*tau-Hs**2*ns)
assert sp.simplify(sp.diff(VI,x).subs(x,u)) == 0

m = Hs*ns/2
assert sp.simplify(sp.diff(VF,x).subs(x,m)) == 0

pi0 = ns*tau/2-i0**2
gain = sp.factor(VF.subs(y,i0)-pi0)
max_gain = sp.factor(gain.subs(x,m))
assert sp.simplify(max_gain-ns*(2*Hs**2*ns-27*tau)/18) == 0

xminus = Hs*ns/2-sp.sqrt(2*ns*(2*Hs**2*ns-27*tau))/6
assert sp.simplify(gain.subs(x,xminus)) == 0

lam = sp.symbols("lam", positive=True)
assert sp.simplify(
    (2*lam-18)**2-2*lam*(2*lam-27)-18*(18-lam)
) == 0

# Exact source-admissible regression.
H0=n0=Fraction(1)
tt=Fraction(1,15)
ii=Fraction(1,6)
dev=Fraction(1,2)
pi_sym = n0*tt/Fraction(2)-ii**2
pi_dev = n0*(H0*(dev-ii)-tt)-dev**2
assert pi_sym == Fraction(1,180)
assert pi_dev == Fraction(1,60)
assert pi_dev-pi_sym == Fraction(1,90)

print("PASS: Stage 4A independent clean-room reconstruction")
print("Critical Stage-4A refinement finding: p=c is weakly dominated by p=c+eps.")
print("Cournot di/dN =",di)
print("Hotelling no-loss max deviation gain =",max_gain)
print("Hotelling exact regression gain =",pi_dev-pi_sym)
