# Equilibrium Correspondence Ledger

Status: **STAGE-4 COURNTOT CORRESPONDENCE COMPLETE FOR CLAIMED SCOPE — STAGE 4A PENDING**

## 1. General-(N) symmetric Cournot SPNE

Let

[
D=a-Hphi-rac{gammaphi^2}{2}>0,
qquad
ar i_C=
rac{HND}{b(N+1)^2-H^2N}.
]

Under

[
b>left(rac{HN}{N+1}ight)^2,
]

the unique **symmetric** constrained Stage-I equilibrium is

[
oxed{i_1=cdots=i_N=i_C^*=min{phi,ar i_C}}.
]

Every downstream Cournot subgame is uniquely solved by the active-set KKT continuation.

Classification: **NASH / SPNE within the symmetric Stage-I class, globally deviation-checked.**

No claim is made here that the general-(N) game has no asymmetric SPNE.

## 2. Source duopoly — complete pure Stage-I correspondence

Normalize

[
delta=D/H>0,qquad ho=b/H^2>4/9,
]

and let

[
s=rac{2delta}{9ho-2}.
]

### A. (ho>2/3)

Unique pure equilibrium:

[
oxed{(min{phi,s},min{phi,s})}.
]

### B. (ho=2/3)

If

[
phi<delta/2,
]

the unique equilibrium is

[
(phi,phi).
]

If

[
phigedelta/2,
]

there is a continuum

[
oxed{
mathcal E=
left{
(x,delta-x):
xin[max{0,delta-phi},min{phi,delta}]
ight}.
}
]

### C. (4/9<ho<2/3)

If

[
phile s,
]

the unique equilibrium is

[
(phi,phi).
]

If

[
phi>s,
]

there are exactly three pure equilibria:

[
(s,s),
qquad
(x_H,x_L),
qquad
(x_L,x_H),
]

where

[
h=R(0),qquad
x_H=min{phi,h},qquad
x_L=R(x_H),
]

and (R) is the cap-free global BR stated in the Stage-4 report.

This region supplies the global failure of Proposition 5.

## 3. Exact asymmetric witness

For

[
ho=rac35,qquad
delta=1,qquad
phi=2,
]

the source conditions hold and the pure equilibria are exactly

[
left(rac{10}{17},rac{10}{17}ight),
qquad
(1,0),
qquad
(0,1).
]

The global BR also satisfies

[
R(0)=1,qquad
R(1/20)=11/10,
]

so an increase in rival outsourcing can increase own optimal outsourcing.

## 4. Hotelling continuation ledger

Hotelling is not the Stage-4A canonical paper architecture.

For diagnostic completeness:

| Cost gap | Price-subgame outcome |
|---|---|
| (|c_B-c_A|<3	au) | unique interior equilibrium |
| (|c_B-c_A|=3	au) | unique zero-share boundary equilibrium |
| (|c_B-c_A|>3	au) | continuum of pure corner equilibria |

Because the low-cost firm's continuation payoff differs across the continuum, there is no single source-defined reduced Stage-I payoff outside the interior region.

## 5. Classification vocabulary

- **SPNE** — continuation complete and unilateral deviations checked for the stated scope.
- **MULTIPLE** — multiple equilibria characterized.
- **SELECTION-DEPENDENT** — downstream multiplicity changes continuation payoffs.
- **NOT CLAIMED** — deliberately outside theorem scope; not an unresolved hidden claim.

## 6. Stage-4 gate consequence

Cournot Candidate C: **PASS to Stage 4A**.

Unified Candidate E: **not retained as the canonical minimal architecture** because Hotelling continuation selection is an additional equilibrium-refinement problem not specified by the source.
