# Stage 7.5A Function-Class Counterexample Audit

## Purpose

Test whether the baseline Cournot active-set result can be promoted to a general theorem over convex monitoring technologies.

## Counterexample

Keep the normalized linear-Cournot cost-reduction structure

\[
\delta=1,\qquad \rho=3/5,\qquad y=0,
\]

but replace the source monitoring cost \(M(x)=x^2\) by the still strictly convex function

\[
M(x)=10x^2.
\]

The rival-exit boundary remains

\[
U(0)=1.
\]

Thus the geometric fact that sufficiently aggressive own cost reduction can push the rival to zero output is unchanged.

However, exact primitive-payoff calculation gives

\[
\Pi_A(0;0)=\frac5{27},
\]

whereas at the exit boundary

\[
\Pi_A(1;0)=\frac53-10=-\frac{25}{3}.
\]

Hence the exit-inducing action is strictly worse than no investment.

## Scope consequence

The following implication is false without additional curvature restrictions:

> decreasing marginal cost + convex monitoring + endogenous rival exit
> \(\Rightarrow\) the global best response contains the source's increasing rival-exit segment.

Accordingly:

- the direction of the exit boundary may have restricted-class support;
- C7 and C8 remain **baseline source-functional-form theorems**;
- no generic theorem over arbitrary convex monitoring technologies is licensed.

Exact regression: `code/stage075a_scope_counterexamples.py`.

This is a generality kill test, not an extension of the paper model.
