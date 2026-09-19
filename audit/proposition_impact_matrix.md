# Proposition Impact Matrix

Status: **STAGE-1 IMPACT CLASSIFICATION COMPLETE; REPLACEMENT THEOREMS OPEN**

This file separates Stage-1 diagnosis from later full-equilibrium reconstruction.

| Published result | Stage-1 classification | Certified impact | Exact replacement status |
|---|---|---|---|
| Proposition 3 | **INCORRECT** | Equation (14)'s sign is reversed. On the source interior branch, more Cournot firms reduce outsourcing per firm for (N>1). Equation (13) also lacks the hard cap (ile\phi). | OPEN — must incorporate all boundaries/active sets. |
| Corollary 4 | **AMBIGUOUS / OVERSTATED GLOBALLY** | Interior derivative directions survive, including for the fraction (i/\phi); when the outsourcing cap binds, strict effects can become weak/flat. | OPEN — piecewise constrained statement required. |
| Proposition 5 | **CORRECT LOCALLY / OVERSTATED GLOBALLY** | Equation (15) gives a negative slope on the regular all-active interior branch. The source restrictions do not establish a globally valid constrained BR because outsourcing boundaries and Cournot active-set changes are omitted. | OPEN — complete global BR correspondence required. |
| Proposition 6 | **INCORRECT AS UNQUALIFIED GLOBAL EQUILIBRIUM CLAIM** | Equation (25) can violate (ile\phi); more strongly, a feasible deviation into a Hotelling corner market-share regime is strictly profitable on a nonempty parameter region satisfying the paper's local SOC. | OPEN — complete piecewise price/outsourcing equilibrium required. |

## Stage-1 exact facts

For the Cournot interior candidate

[
i_C(N)=\frac{HND}{b(N+1)^2-H^2N},
]

the exact derivative is

[
\frac{\partial i_C}{\partial N}
=
-\frac{HDb(N^2-1)}
{[b(N+1)^2-H^2N]^2}<0
\quad(N>1).
]

For the Hotelling corner-deviation construction, comparing (i_0=Hn/6) with the corner optimum (i_A=Hn/2) yields

[
\Delta\Pi=
\frac{n(2H^2n-27\tau)}{18}.
]

Hence a profitable deviation exists for

[
\frac{27}{2}\tau<H^2n<18\tau,
]

subject to the outsourcing deviation being feasible. The upper inequality is precisely compatible with the paper's local SOC.

## What Stage 1 does not certify

Stage 1 does **not** yet certify:

- the complete Cournot constrained best-response correspondence;
- the full set of asymmetric equilibria;
- the complete Hotelling corner/interior price correspondence;
- exact necessary-and-sufficient survival regions for every published proposition;
- novelty of any correction.

Those remain downstream tasks under the canonical v2.2 workflow.

## Rules

1. Do not label a proposition false merely because a proof step is incomplete; the classifications above rely on explicit algebra/counterexamples.
2. Preserve the distinction between local-branch validity and global equilibrium validity.
3. Every future replacement theorem must state exact domains and weak/strict inequalities.
4. Product-market continuation failure must fail closed; it may not be treated as an unprofitable deviation.
