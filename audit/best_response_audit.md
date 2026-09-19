# Constrained Best-Response Audit

Status: **STAGE-4 COMPLETE — STAGE 4A NEXT**

## Cournot

The general-\(N\) symmetric action and complete source-duopoly global BR are recorded in \`audit/STAGE_04_MINIMAL_MODEL_GATE.md\`.

For duopoly,

\[
B_\phi(y)=\min\{\phi,R(y)\},
\]

where \(R(y)\) is the exact inactive / all-active / rival-exit / monopoly piecewise response derived at Stage 4. For \(4/9<b/H^2<2/3\), a feasible segment has slope \(+2\).

## Hotelling — literal source game

The interior BR derived by the source is branch-local. When \(|H(i_A-i_B)|>3\tau\), the literal price subgame can be multiple, so there is no single global reduced Stage-I payoff without continuation selection.

## Hotelling — undominated-price refinement

Every \(p<c\) is weakly dominated by \(p=c\). After deleting such prices, the Stage-I payoff is

\[
V_y(x)=
\begin{cases}
-x^2, & x-y\le-3\tau/H,\\[4pt]
\dfrac{n[3\tau+H(x-y)]^2}{18\tau}-x^2,
& |x-y|\le3\tau/H,\\[8pt]
n[H(x-y)-\tau]-x^2,
& x-y\ge3\tau/H.
\end{cases}
\]

Let

\[
I_y=
[\max\{0,y-3\tau/H\},\min\{\phi,y+3\tau/H\}],
\]

\[
u(y)=
\frac{Hn(3\tau-Hy)}
{18\tau-H^2n},
\]

and let \(x_I(y)\) be the projection of \(u(y)\) onto \(I_y\).

If \(y+3\tau/H\le\phi\), define

\[
C_y=[y+3\tau/H,\phi],
\qquad
x_C(y)=
\operatorname{proj}_{C_y}(Hn/2).
\]

Then

\[
BR_A(y)
=
\arg\max_{x\in K_y}V_y(x),
\]

with

\[
K_y=
\{0,x_I(y)\}
\cup
\{x_C(y):y+3\tau/H\le\phi\}.
\]

This finite-candidate representation is complete because every branch is strictly concave under the source SOC. Ties are retained.

## Symmetric refined equilibrium

If

\[
\phi\le Hn/6,
\]

the corrected symmetric action is \(\phi\).

If

\[
\phi>Hn/6,
\]

the source candidate \(Hn/6\) survives iff the exact condition in \`audit/STAGE_04_HOTELLING_REAUDIT.md\` holds. It fails exactly when

\[
27\tau/2<H^2n<18\tau
\]

and

\[
\phi>
\frac{Hn}{2}
-
\frac{\sqrt{2n(2H^2n-27\tau)}}{6}.
\]

Unresolved BR regions: **0** for the retained characterization.
