# Model Canonicalization

Status: **STAGE-1 CANONICAL SOURCE MODEL FROZEN**

The source reconstruction is canonical for Stage 2. It may not be altered to improve novelty.

## Objects and domains

| Object | Source role | Canonical representation | Domain / feasibility |
|---|---|---|---|
| Input index | heterogeneous required inputs | (x) when disambiguation is needed | (xin[0,phi]) |
| Outsourcing choice | measure of outsourced input set | (i_j) | **(0le i_jlephi)** |
| In-house input cost | (H+gamma x) | same | (H>0,gammage0) |
| Subcontractor cost under Assumption 2 | constant advantage, (S=0,alpha=1) | (gamma x) | source normalization |
| Final-good marginal cost | equation (5) | (c_j=C_0-Hi_j) | (C_0=Hphi+gammaphi^2/2) |
| Monitoring cost | equation (6) | (i_j^2) | no (eta) coefficient |
| Cournot demand | equation (7) | (p=a-bQ) | (a,b>0) |
| Cournot output | equation (10), regular branch | (q_j) | nonnegative quantity constraint must be respected |
| Hotelling location | endpoints | A at 0, B at 1 | fixed |
| Hotelling consumer | unit interval | (xin[0,1]), density (n) | full-coverage source model |
| Differentiation parameter | source glyph | canonical (	au) | (	au>0) |
| Prices | Stage-II Hotelling actions | (p_A,p_B) | interior/corner demand regimes |
| Profit | firm objective | (Pi_j) | operating profit minus (i_j^2) |

Define

[
C_0=Hphi+rac{gammaphi^2}{2},
qquad
D=a-C_0.
]

The paper's first Cournot restriction implies (D>0).

## Timing

### Cournot specification

1. Firms choose outsourced input sets; under Assumption 2 only their measures (i_j) matter.
2. Given the induced marginal costs, firms choose Cournot quantities.
3. The claimed solution concept is subgame-perfect equilibrium, with the paper focusing on symmetric equilibria.

### Hotelling specification

1. Firms choose outsourcing (i_A,i_B).
2. Given induced marginal costs, firms choose prices in the Hotelling market.
3. The claimed equilibrium is obtained by backward induction.

## Cournot regular branch

For arbitrary costs, if every firm is active,

[
q_j=
rac{a-Nc_j+sum_{k
e j}c_k}{b(N+1)}.
]

After substituting (c_j=C_0-Hi_j),

[
q_j=
rac{D+NH i_j-HS_{-j}}{b(N+1)},
qquad
S_{-j}=sum_{k
e j}i_k.
]

The induced regular-branch Stage-I payoff is

[
Pi_j^{mathrm{active}}
=
rac{[D+NH i_j-HS_{-j}]^2}{b(N+1)^2}-i_j^2.
]

Under

[
b(N+1)^2>N^2H^2,
]

this branch is strictly concave in (i_j), with stationary response

[
u_j(S_{-j})
=
rac{NH(D-HS_{-j})}{b(N+1)^2-N^2H^2}.
]

This is **not** the globally certified best response unless the relevant Stage-II continuation remains on the all-active branch and the outsourcing bound is enforced.

At a symmetric interior point,

[
i_{C,mathrm{int}}
=
rac{HND}{b(N+1)^2-NH^2}.
]

## Hotelling regular branch

Canonical differentiation notation: (	au>0).

Interior indifferent consumer:

[
hat x=rac12+rac{p_B-p_A}{2	au}.
]

Interior price equilibrium:

[
p_A=rac{2c_A+c_B+3	au}{3},
qquad
p_B=rac{c_A+2c_B+3	au}{3}.
]

At those prices,

[
hat x=rac12+rac{H(i_A-i_B)}{6	au}.
]

Hence the branch requires

[
|H(i_A-i_B)|le3	au.
]

Conditional Stage-I payoff:

[
Pi_A^{mathrm{int}}
=
rac{n[3	au+H(i_A-i_B)]^2}{18	au}-i_A^2.
]

Stationary response:

[
u_H(i_B)
=
rac{Hn(3	au-H i_B)}{18	au-H^2n}.
]

Local SOC:

[
	au>rac{H^2n}{18}.
]

Symmetric interior candidate:

[
i_{H,mathrm{int}}=rac{Hn}{6}.
]

## Domain hazards frozen at Stage 1

1. **Outsourcing bound:** (i_jin[0,phi]) is part of the primitive strategy space.
2. **Cournot nonnegativity:** equation (10) is an all-active formula, not a globally valid continuation under the published restrictions.
3. **Hotelling market shares:** equations (19)–(21) are an interior-share continuation, not a globally valid continuation.
4. **Monitoring-cost normalization:** no (eta) may be inserted into the source model.
5. **Symmetry is not a deviation restriction:** focusing on symmetric candidate equilibria does not eliminate asymmetric unilateral deviations required for Nash/SPNE verification.

## Gate consequence

This file freezes the **source representation**, not the complete corrected equilibrium correspondence.

The latter remains unresolved until all active-set/boundary continuations and unilateral deviations have been classified.
