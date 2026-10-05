# Stage 8 — Independent-Audit Theory-Freeze Amendment

Date: **2026-09-20**  
Original theory-freeze checkpoint: `2fbcf47ff18ea3650d307d90cbdeab78ddb63256`

## Amendment status

[
oxed{	extbf{THEORY FREEZE AMENDED AND RECERTIFIED}}
]

The original freeze remains historical provenance. This amendment changes theorem **scope wording and proof evidence**, not the core five-case C8 equilibrium set.

## C7 amended freeze

For (4/9<ho<2/3), the uncapped response (R) contains the (+2) rival-exit branch. The source-domain response (B_phi=min{phi,R}) has a positive-length increasing segment only when

[
phi>delta
quad	ext{for}quad
rac12leho<rac23,
]

or

[
phi>rac{delta}{4ho-1}
quad	ext{for}quad
rac49<ho<rac12.
]

At equality the piece degenerates. Small caps may eliminate the increasing segment entirely.

The frozen correction is existential: the source parameter space contains admissible cases with a positive-slope constrained best response, which is enough to reject Proposition 5 as an unqualified global strategic-substitutes claim.

## C8 amended proof status

The five equilibrium regimes are unchanged. The certification basis is now the explicit analytic completeness proof in the manuscript Appendix and the Stage-4A amendment, not an undocumented “branch intersection gives exactly three” step.

At (ho=2/3,phi=delta/2), the equilibrium set is a singleton. It is a nondegenerate continuum only for (phi>delta/2).

## Multiplicity mechanism

Downstream exit is **not** frozen as a necessary cause of multiplicity.

The permanent all-active witness is

[
(ho,delta,phi)=left(rac35,1,rac34ight),
]

with pure equilibria

[
left(rac{10}{17},rac{10}{17}ight),
quad
left(rac34,rac5{14}ight),
quad
left(rac5{14},rac34ight).
]

Both downstream firms are active for every feasible sourcing history. Exit remains the mechanism that creates the positive-slope C7 branch.

## Hotelling domain freeze

The source supplies the full-coverage consumer comparison and interior price formulas but does not separately impose (p_jge c_j) or give the global corner continuation.

The frozen literal audit therefore uses:

- maintained full coverage;
- clipped source consumer shares at the endpoints;
- pure prices on (mathbb R) (or (mathbb R_+), which gives the same certified pure equilibrium set because source costs and equilibrium prices are positive);
- no outside-option/uncovered-demand extension.

The (p_jge c_j) game remains a separate auxiliary restriction.

## No-loss root domain

[
x_-=
rac{Hn}{2}
-
rac{sqrt{2n(2H^2n-27	au)}}6
]

is a real threshold only when (H^2nge27	au/2).

Under the maintained strict source condition (H^2n<18	au):

- (H^2nle27	au/2): no strictly profitable nonlocal deviation from the stated symmetric candidate;
- (27	au/2<H^2n<18	au): strict failure iff (phi>x_-);
- (phi=x_-): tie;
- (H^2n=27	au/2): zero vertex gain, no strict failure.

## Welfare freeze clarification

Define the reduced welfare function

[
widetilde W_C(i)=W_C(q^*(i),i)
]

using the unique Cournot continuation. Welfare variation on the (ho=2/3) equilibrium set is asserted only when the set is nondegenerate, (phi>delta/2).

Restricted-instrument and fixed-allocation benchmarks remain distinct from first best.

## Formal coverage

Formal coverage remains **PROOF-CRITICAL CORE**. No Lean source or encoded hypothesis changed. In particular, the C7 formal theorem proving a positive slope does not prove feasibility of a positive-length constrained branch.

## Recertified freeze verdict

All current manuscript claims must conform to this amendment and the updated main freeze file.

[
oxed{	extbf{STAGE 8 — PASS / THEORY FROZEN AS AMENDED}}
]
