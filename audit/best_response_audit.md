# Constrained Best-Response Audit

Status: **COURNOT COMPLETE AT STAGE 4 — STAGE 4A PENDING**

## 1. General-(N) Cournot continuation

Every feasible outsourcing profile (iin[0,phi]^N) induces a cost vector

[
c_j=C_0-Hi_j.
]

The downstream linear Cournot game with (q_jge0) has a unique active-set equilibrium. It is solved by sorting costs and applying the KKT conditions. No feasible history is discarded.

## 2. Own-payoff global concavity

On a branch with (m) active firms including firm (j),

[
rac{d^2Pi_j}{di_j^2}
=
2rac{H^2m^2}{b(m+1)^2}-2<0
]

under the source restriction

[
b>left(rac{HN}{N+1}ight)^2.
]

At own entry the derivative is continuous. When a rival exits, the derivative jumps downward. Hence own reduced payoff is globally strictly concave over ([0,phi]).

Consequences:

- every constrained own best response is single-valued;
- finite deviations, active-set changes, and (i=phi) are covered;
- the published local SOC can be upgraded to a global own-optimality result only after the missing continuations are supplied.

## 3. Full-outsourcing boundary

The full-outsourcing boundary is feasible by the primitive input set.

For the symmetric general-(N) game,

[
ar i_C=
rac{HND}{b(N+1)^2-H^2N}.
]

Therefore

[
oxed{i_C^*=min{phi,ar i_C}}.
]

- If (ar i_C<phi): interior symmetric BR.
- If (ar i_C=phi): boundary stationary point.
- If (ar i_C>phi): (i=phi) is the unique constrained symmetric BR.

The Stage-1 cap witness is retained as a regression test.

## 4. Asymmetric deviations

All unilateral deviations from the symmetric candidate are covered because the exact downstream active set is re-solved after the deviation.

For symmetric rivals (y), own continuation passes through:

1. own-inactive regime;
2. all-(N)-active regime;
3. own-monopoly regime.

The reduced payoff remains globally strictly concave across both switches.

Thus no asymmetric unilateral deviation defeats (i_C^*).

## 5. Source duopoly global BR

Normalize

[
delta=D/H,qquad ho=b/H^2>4/9.
]

The cap-free BR (R(y)) is the exact piecewise function recorded in
`audit/STAGE_04_MINIMAL_MODEL_GATE.md`.

The constrained BR is

[
oxed{B_phi(y)=min{phi,R(y)}}.
]

Material branch slopes are:

- monopoly stationary branch: (0);
- rival-exit kink branch: (+2);
- both-active branch: (-2/(9ho-4));
- own-inactive branch: (0).

Therefore Proposition 5 is not globally a strategic-substitutes result over the entire source parameter domain.

## 6. Hotelling diagnostic

The source Hotelling reduced payoff is not globally single-valued once feasible outsourcing can create

[
|c_B-c_A|>3	au.
]

The price continuation is then a continuum. The earlier Stage-1 corner-deviation witness is selection-dependent.

No new equilibrium-selection refinement is imposed.

## 7. Audit completion

- [x] Complete source strategy set used.
- [x] (i=phi) treated explicitly.
- [x] Interior stationary points checked.
- [x] Active-set/corner continuations re-solved.
- [x] Finite asymmetric unilateral deviations covered for the symmetric Cournot theorem.
- [x] Duopoly global BR derived piecewise.
- [x] Alternative duopoly equilibria searched and classified.
- [x] Stage-1 counterexamples retained as regression tests.
- [x] Hotelling continuation multiplicity recorded rather than hidden.

Canonical verification artifact:

`code/stage04_verify.py`
