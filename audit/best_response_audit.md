# Constrained Best-Response Audit

Status: **COURNOT DUOPOLY COMPLETE — STAGE 4A NEXT**

## General-\(N\) Cournot

For every rivals' sourcing profile, the source SOC implies global strict concavity of own reduced payoff over \(i_j\in[0,\phi]\). Hence each Cournot Stage-I best response is single-valued.

At a symmetric profile the unique symmetric action is

\[
i_C^*
=
\min\left\{
\phi,\,
\frac{HND}{b(N+1)^2-H^2N}
\right\}.
\]

## Source duopoly

Normalize

\[
\delta=D/H,\qquad
\rho=b/H^2>4/9.
\]

Let \(y\) be rival outsourcing.

Define

\[
A(y)=\frac{2(\delta-y)}{9\rho-4},
\qquad
U(y)=\delta+2y,
\qquad
M=\frac{\delta}{4\rho-1}.
\]

For \(y\ge\delta\), \(R(y)=0\).

For \(0\le y<\delta\):

- if \(\rho\ge2/3\), \(R(y)=A(y)\);
- if \(1/2\le\rho<2/3\), with
  \[
  y_A=\frac{\delta(2-3\rho)}{2(3\rho-1)},
  \]
  \[
  R(y)=
  \begin{cases}
  U(y),&0\le y\le y_A,\\
  A(y),&y_A\le y<\delta;
  \end{cases}
  \]
- if \(4/9<\rho<1/2\), additionally define
  \[
  y_M=\frac{\delta(1-2\rho)}{4\rho-1},
  \]
  and
  \[
  R(y)=
  \begin{cases}
  M,&0\le y\le y_M,\\
  U(y),&y_M\le y\le y_A,\\
  A(y),&y_A\le y<\delta.
  \end{cases}
  \]

The actual source-domain BR is

\[
\boxed{B_\phi(y)=\min\{\phi,R(y)\}.}
\]

## Full-outsourcing boundary

The cap is explicitly part of the BR. If the unconstrained maximizer exceeds \(\phi\), full outsourcing is the unique best response.

## Strategic effect

On the all-active branch,

\[
A'(y)<0.
\]

On the rival-exit kink,

\[
U'(y)=2>0.
\]

Thus Proposition 5 is not globally valid.

## Verification status

- lower boundary: checked;
- full-outsourcing boundary: checked;
- own inactivity: checked;
- both-active regime: checked;
- rival exit / own monopoly: checked;
- branch joins: checked;
- exact rational counterexamples: retained;
- unresolved Cournot BR region: **0**.
