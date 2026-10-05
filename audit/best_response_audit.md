# Constrained Best-Response Audit

Status: **STAGE-4 AMENDED; STAGE 4A RECERTIFICATION REQUIRED**

## Cournot

The general-\(N\) symmetric action and complete source-duopoly global BR remain as in \`audit/STAGE_04_MINIMAL_MODEL_GATE.md\`.

## Hotelling — literal source game

The source interior BR is branch-local. For \(|H(i_A-i_B)|>3\tau\), the literal pure price continuation is multiple, so no single reduced Stage-I payoff exists without selection.

## Hotelling — explicit no-loss price restriction

Impose

\[
p_j\ge c_j
\]

as an auxiliary robustness restriction.

Then A's reduced payoff against \(y=i_B\) is

\[
V_y^{NL}(x)=
\begin{cases}
-x^2,&x-y\le-3\tau/H,\\[4pt]
\dfrac{n[3\tau+H(x-y)]^2}{18\tau}-x^2,
&|x-y|\le3\tau/H,\\[8pt]
n[H(x-y)-\tau]-x^2,
&x-y\ge3\tau/H.
\end{cases}
\]

Under the source SOC every branch is strictly concave.

Let

\[
I_y=[\max\{0,y-3\tau/H\},\min\{\phi,y+3\tau/H\}],
\]

\[
u(y)=\frac{Hn(3\tau-Hy)}{18\tau-H^2n},
\]

and \(x_I(y)=\operatorname{proj}_{I_y}u(y)\).

If \(y+3\tau/H\le\phi\), let

\[
x_C(y)=
\operatorname{proj}_{[y+3\tau/H,\phi]}\left(\frac{Hn}{2}\right).
\]

Then the exact pure best-response correspondence is

\[
BR_A^{NL}(y)
=
\arg\max_{x\in K_y}V_y^{NL}(x),
\]

where

\[
K_y=
\{0,x_I(y)\}
\cup
\{x_C(y):y+3\tau/H\le\phi\}.
\]

Ties are retained.

## Refinement warning

The no-loss restriction is not called an undominated-strategy refinement. The selected corner action \(p_{\rm high}=c_{\rm high}\) is itself weakly dominated by strictly above-cost prices in the unrestricted game.
