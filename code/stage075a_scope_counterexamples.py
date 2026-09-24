"""Stage 7.5A scope counterexamples.

Exact rational regressions showing why the source's global BR/equilibrium
claims must remain baseline-functional-form results.
"""

from fractions import Fraction

# Normalized duopoly: H=1, delta=1, rho=3/5, rival outsourcing y=0.
# The source rival-exit boundary is U(0)=1.
delta = Fraction(1)
rho = Fraction(3,5)
y = Fraction(0)
x_exit = delta + 2*y
assert x_exit == 1

def cournot_profit(x, y, kappa):
    # a=delta, C0=0, costs cA=-x, cB=-y.
    a = delta
    cA, cB = -x, -y

    # both-active candidate
    qA = (a - 2*cA + cB)/(3*rho)
    qB = (a - 2*cB + cA)/(3*rho)

    if qA > 0 and qB > 0:
        opA = rho*qA*qA
    elif qB <= 0:
        qA = (a-cA)/(2*rho)
        opA = rho*qA*qA
    else:
        opA = Fraction(0)
    return opA-kappa*x*x

# Replace source monitoring x^2 by the still-convex M(x)=10 x^2.
kappa = Fraction(10)
pi_no_invest = cournot_profit(Fraction(0), y, kappa)
pi_exit = cournot_profit(x_exit, y, kappa)

assert pi_no_invest == Fraction(5,27)
assert pi_exit == Fraction(5,3)-10
assert pi_no_invest > pi_exit

# Therefore the rival-exit boundary can still exist geometrically while
# aggressive exit-inducing investment is not a global best response.
print("PASS: Stage-7.5A scope counterexample")
print("M(x)=10x^2: payoff at x=0 =", pi_no_invest)
print("M(x)=10x^2: payoff at exit boundary x=1 =", pi_exit)
