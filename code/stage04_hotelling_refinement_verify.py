"""Stage-4 Hotelling re-audit: explicit no-loss price restriction.

Source primitives only.  The auxiliary robustness game imposes p>=c. The source-payoff dominance fact
that p=c weakly dominates each p<c is verified separately; this is not
claimed to be elimination of all weakly dominated strategies.

Requires sympy==1.14.0.
"""

from fractions import Fraction
import sympy as sp

H,n,tau,phi,x,y=sp.symbols("H n tau phi x y", positive=True)

# Source SOC domain: H**2*n < 18*tau.

i0=H*n/6
t=3*tau/H
m=H*n/2

VI=sp.factor(n*(3*tau+H*(x-y))**2/(18*tau)-x**2)
VC=sp.factor(n*(H*(x-y)-tau)-x**2)
VZ=-x**2

u=sp.factor(H*n*(3*tau-H*y)/(18*tau-H**2*n))

# Branch FOCs / stationary points.
assert sp.simplify(sp.diff(VI,x).subs(x,u))==0
assert sp.simplify(sp.diff(VC,x).subs(x,m))==0
assert sp.simplify(sp.diff(VI,x,2)-(H**2*n/(9*tau)-2))==0
assert sp.diff(VC,x,2)==-2

# Payoff continuity at both regime boundaries.
assert sp.simplify(
    VI.subs(x,y-t)-VZ.subs(x,y-t)
)==0
assert sp.simplify(
    VI.subs(x,y+t)-VC.subs(x,y+t)
)==0

# Symmetric interior payoff and low-cost-corner deviation gain.
pi0=sp.factor(n*tau/2-i0**2)
gain=sp.factor(VC.subs(y,i0)-pi0)
expected_gain=-(36*x**2-36*H*n*x+5*H**2*n**2+54*n*tau)/36
assert sp.simplify(gain-expected_gain)==0

max_gain=sp.factor(gain.subs(x,m))
assert sp.simplify(
    max_gain-n*(2*H**2*n-27*tau)/18
)==0

xminus=H*n/2-sp.sqrt(2*n*(2*H**2*n-27*tau))/6
xplus=H*n/2+sp.sqrt(2*n*(2*H**2*n-27*tau))/6
assert sp.simplify(gain.subs(x,xminus))==0
assert sp.simplify(gain.subs(x,xplus))==0

# First low-cost corner point.
L=i0+t
gain_L=sp.factor(gain.subs(x,L))
assert sp.simplify(
    gain_L-tau*(H**2*n-18*tau)/(2*H**2)
)==0

# Normalized proof ingredient: xminus > L when 27/2 < lambda < 18.
lam=sp.symbols("lam", positive=True)
square_gap=sp.factor((2*lam-18)**2-2*lam*(2*lam-27))
assert sp.simplify(square_gap-18*(18-lam))==0

# Exact Stage-1 regression.
H0=Fraction(1)
n0=Fraction(1)
tau0=Fraction(1,15)
phi0=Fraction(1)
i00=Fraction(1,6)
idev=Fraction(1,2)

pi_sym=n0*tau0/Fraction(2)-i00**2
d=H0*(idev-i00)

# Unique undominated-price corner continuation:
# p_high=c_high, p_low=c_high-tau.
pi_dev=n0*(d-tau0)-idev**2
assert pi_sym==Fraction(1,180)
assert pi_dev==Fraction(1,60)
assert pi_dev-pi_sym==Fraction(1,90)

# Exact lower root in the regression.
xminus0=sp.Rational(1,2)-sp.sqrt(10)/30
assert sp.N(xminus0)<1
assert sp.Rational(1,2)>xminus0

# Dominance logic is primitive:
# for p<c, (p-c)*share <= 0 for every share in [0,1],
# whereas p=c gives exactly zero operating profit.

print("PASS: Stage-4 Hotelling no-loss-restriction re-audit")
print("interior stationary response =",u)
print("corner stationary response =",m)
print("max corner deviation gain =",max_gain)
print("failure lower root x_- =",xminus)
print("Stage-1 refined deviation gain =",pi_dev-pi_sym)
