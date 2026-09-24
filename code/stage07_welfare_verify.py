"""Stage 7 welfare / benchmark verification.

Exact symbolic checks only.  This file does not add a new model.
Requires sympy==1.14.0.
"""

from fractions import Fraction
import sympy as sp

# ---------------------------------------------------------------------------
# I. Cournot welfare identity
# ---------------------------------------------------------------------------

N,H,D,b,s = sp.symbols("N H D b s", positive=True)

z = D + H*s
Q = N*z/(b*(N+1))

CS = b*Q**2/2
PS = N*z**2/(b*(N+1)**2) - N*s**2
W_eq = sp.simplify(CS + PS)

W_eq_expected = (
    N*(N+2)*z**2/(2*b*(N+1)**2)
    - N*s**2
)
assert sp.simplify(W_eq-W_eq_expected) == 0

# Restricted-instrument benchmark:
# choose one common sourcing level s, then leave Cournot output decentralized.
s_R = H*(N+2)*D/(2*b*(N+1)**2-H**2*(N+2))
assert sp.simplify(sp.diff(W_eq_expected,s).subs(s,s_R)) == 0

s_P = H*N*D/(b*(N+1)**2-H**2*N)
gap = sp.factor(s_P-s_R)

gap_expected = (
    D*H*b*(N-2)*(N+1)**2
    /
    (
        (b*(N+1)**2-H**2*N)
        *
        (2*b*(N+1)**2-H**2*(N+2))
    )
)
assert sp.simplify(gap-gap_expected) == 0
assert sp.simplify(gap.subs(N,2)) == 0

# ---------------------------------------------------------------------------
# II. Cournot multiplicity makes welfare selection-dependent
# ---------------------------------------------------------------------------

def active_duopoly(delta, rho, x, y):
    """Exact primitive continuation for H=1, C0=0, a=delta."""
    # both-active candidates
    qx = (delta + 2*x - y)/(3*rho)
    qy = (delta + 2*y - x)/(3*rho)
    if qx > 0 and qy > 0:
        return qx,qy
    if qx <= 0:
        return Fraction(0), (delta+y)/(2*rho)
    return (delta+x)/(2*rho), Fraction(0)

def welfare_duopoly(delta,rho,x,y):
    qx,qy = active_duopoly(delta,rho,x,y)
    Q = qx+qy
    return (
        delta*Q-rho*Q*Q/Fraction(2)
        + x*qx+y*qy
        - x*x-y*y
    )

rho0=Fraction(3,5)
delta0=Fraction(1)
sym=Fraction(10,17)

assert welfare_duopoly(delta0,rho0,sym,sym) == Fraction(20,17)
assert welfare_duopoly(delta0,rho0,Fraction(1),Fraction(0)) == Fraction(3,2)
assert welfare_duopoly(delta0,rho0,Fraction(0),Fraction(1)) == Fraction(3,2)

# At rho=2/3 and x+y=delta, welfare varies across the continuum.
xx,dd=sp.symbols("xx dd", nonnegative=True)
yy=dd-xx
rho_edge=sp.Rational(2,3)
qA=sp.simplify((dd+2*xx-yy)/(3*rho_edge))
qB=sp.simplify((dd+2*yy-xx)/(3*rho_edge))
Qedge=sp.simplify(qA+qB)
Wedge=sp.factor(
    dd*Qedge-rho_edge*Qedge**2/2
    +xx*qA+yy*qB-xx**2-yy**2
)
assert sp.simplify(
    Wedge-(sp.Rational(5,4)*dd**2-dd*xx+xx**2)
) == 0

# ---------------------------------------------------------------------------
# III. Hotelling exact CS and welfare accounting
# ---------------------------------------------------------------------------

n,omega,tau,x = sp.symbols("n omega tau x", positive=True)
pA,pB,cA,cB,iA,iB = sp.symbols(
    "pA pB cA cB iA iB", real=True
)

CS_H = n*(
    omega
    - pA*x
    - pB*(1-x)
    - tau*(x**2+(1-x)**2)/2
)

PS_H = (
    n*(pA-cA)*x
    + n*(pB-cB)*(1-x)
    - iA**2-iB**2
)

W_H = sp.simplify(CS_H+PS_H)
W_H_expected = n*(
    omega
    - cA*x
    - cB*(1-x)
    - tau*(x**2+(1-x)**2)/2
)-iA**2-iB**2

assert sp.simplify(W_H-W_H_expected) == 0

# Prices cancel from total welfare: within a fixed sourcing history,
# the literal corner price continuum is welfare-invariant because allocation is fixed.
assert sp.diff(W_H,pA) == 0
assert sp.diff(W_H,pB) == 0

# Efficient share at fixed costs versus interior price-equilibrium share.
d = sp.symbols("d", real=True)
dWdx = sp.factor(sp.diff(W_H_expected,x).subs(cB,cA+d))
assert sp.simplify(dWdx-n*(d+tau-2*tau*x)) == 0

x_W = sp.Rational(1,2)+d/(2*tau)
x_NE = sp.Rational(1,2)+d/(6*tau)
assert sp.simplify(dWdx.subs(x,x_W)) == 0
assert sp.simplify(x_W-x_NE-d/(3*tau)) == 0

# Fixed symmetric 50-50 allocation: social sourcing benchmark.
C0 = sp.symbols("C0", real=True)
W_half = sp.simplify(
    W_H_expected.subs({
        x:sp.Rational(1,2),
        cA:C0-H*iA,
        cB:C0-H*iB
    })
)
iW = H*n/4
assert sp.simplify(sp.diff(W_half,iA).subs(iA,iW)) == 0
assert sp.simplify(sp.diff(W_half,iB).subs(iB,iW)) == 0

iP = H*n/6
assert sp.simplify(iW-iP-H*n/12) == 0

print("PASS: Stage-7 exact welfare and benchmark checks")
print("Cournot private minus restricted-welfare sourcing =",gap)
print("rho=2/3 welfare along continuum =",Wedge)
print("Hotelling efficient minus NE share (interior) =",sp.simplify(x_W-x_NE))
