# Stage 7.5A — Generality / Quantifier Red-Team Gate

Status: **GO — GENERALITY / QUANTIFIER CERTIFICATION PASS**

Certification date: 2026-09-19  
Workflow: \`research-paper-workflow\` v2.2  
Frozen value-decision input: Stage-7.5 checkpoint \`098be1c01b13e8174aa847b2912b2bd85b7ede28\`

Formal Verification Gate:

\[
\boxed{\textbf{FORMAL VERIFICATION PASS}}
\]

Formal certificate:
\`audit/stage075a_formal_verification_certificate.md\`

## 1. Executive verdict

Stage 7.5A finds **no remaining theorem-level quantifier blocker** after narrowing the manuscript scope to exactly what the prior gates prove.

The red-team makes several wording restrictions permanent:

1. general-\(N\) Cournot does **not** have a certified unique Stage-I equilibrium; it has a certified unique **symmetric pure Stage-I action**;
2. the source-duopoly equilibrium theorem is a complete **pure Stage-I** correspondence, not a mixed-equilibrium characterization;
3. the Cournot competition comparative static is an economic statement over **admissible integer market sizes satisfying the source restrictions**; the derivative in \(N\) is a continuous-extension calculation;
4. Hotelling uniqueness statements are **pure-price** statements;
5. the \(p\ge c\) Hotelling theorem is conditional on an explicit auxiliary no-loss strategy restriction, not a source primitive or standard equilibrium refinement;
6. welfare is selection-dependent in the Cournot multiplicity regions;
7. exact thresholds remain baseline functional-form results, not general theorems over arbitrary demand/cost/monitoring functions.

A targeted Lean 4 formal certificate independently kernel-checks the proof-critical algebra/order core. The final build is green with no proof placeholders, no project-specific axioms, and no \`sorryAx\`.

Final verdict:

\[
\boxed{\textbf{GO TO STAGE 8 — CANONICAL THEORY FREEZE}}
\]

---

## 2. Formal quantifier audit

Canonical quantifier ledger:

\`audit/stage075a_claim_scope_ledger.md\`.

### 2.1 General-\(N\) Cournot continuation

Certified statement:

> For every feasible source outsourcing history \(i\in[0,\phi]^N\), the downstream Cournot game has a unique **pure quantity vector** satisfying the nonnegative-quantity Nash conditions.

Not certified:

> every downstream equilibrium, including mixed equilibria, is unique.

The paper does not need the stronger statement.

### 2.2 General-\(N\) Stage-I action

Certified statement:

\[
i_C^*
=
\min\left\{
\phi,\,
\frac{HND}{b(N+1)^2-H^2N}
\right\}
\]

is the unique **symmetric pure Stage-I action** under the source restrictions.

Not certified:

- uniqueness of all general-\(N\) Stage-I equilibria;
- absence of asymmetric general-\(N\) equilibria;
- mixed-strategy uniqueness.

### 2.3 Competition comparative static

The continuous extension satisfies

\[
\frac{\partial\bar i_C}{\partial N}
=
-\frac{HDb(N^2-1)}
{[b(N+1)^2-H^2N]^2}<0
\]

for \(N>1\) wherever defined.

Economically, however, \(N\) is integer and the source SOC depends on \(N\).

Final manuscript scope:

> Among integer market sizes for which the source restrictions required by the equilibrium theorem hold, the corrected symmetric outsourcing action is weakly decreasing in the number of firms; it is strictly decreasing when the compared actions are off the cap.

The derivative may be displayed as the continuous-extension calculation, but it must not silently expand the admissible economic domain.

### 2.4 Source-duopoly equilibrium correspondence

Certified scope:

\[
\delta>0,\qquad
\rho>\frac49,\qquad
\phi>0,
\]

with pure Stage-I sourcing.

The exact three cases survive:

- \(\rho>2/3\);
- \(\rho=2/3\);
- \(4/9<\rho<2/3\).

The equality cases \(\phi=s\) and \(\phi=\delta/2\) are assigned explicitly and not left to continuity rhetoric.

The theorem must be titled or worded as:

> complete pure Stage-I equilibrium correspondence of the source duopoly.

No stronger equilibrium-set quantifier is licensed.

---

## 3. Equality / knife-edge audit

### Cournot source SOC

The lower bound

\[
\rho>\frac49
\]

is strict. The equality \(\rho=4/9\) is outside the source SOC and is not incorporated into the certified theorem.

### Internal BR threshold \(\rho=1/2\)

This is a branch-structure threshold for the monopoly stationary point. It is included in the exact BR partition, but it does not create a separate final equilibrium-classification family.

### Strategic threshold \(\rho=2/3\)

The equality is not assigned to either neighboring strict regime.

At

\[
\rho=\frac23
\]

the exact BR becomes

\[
B_\phi(y)
=
\min\{\phi,\max\{0,\delta-y\}\},
\]

and, when

\[
\phi\ge\delta/2,
\]

the equilibrium set is a continuum.

### Cap equality \(\phi=s\)

For

\[
4/9<\rho<2/3,
\]

the equality belongs to the capped-unique case:

\[
\phi\le s.
\]

The exactly-three-equilibria case requires

\[
\phi>s.
\]

### Hotelling price corner equality

\[
|d|=3\tau
\]

is a unique pure boundary price equilibrium, not part of the strict interior regime.

### Hotelling sourcing cap threshold

At

\[
\phi=x_-,
\]

the nonlocal no-loss deviation ties the symmetric candidate rather than strictly improving on it.

Thus failure requires

\[
\phi>x_-.
\]

No strict/weak inequality ambiguity remains in the retained claims.

---

## 4. Equilibrium-set / selection audit

### Cournot Stage II

The pure quantity continuation is unique for every feasible outsourcing history.

### General-\(N\) Cournot Stage I

Only symmetric pure-action uniqueness is claimed.

### Source-duopoly Cournot Stage I

The pure equilibrium set is completely characterized.

The word “complete” may be used only with the explicit pure Stage-I scope.

### Literal Hotelling Stage II

The pure-price continuation is:

- unique for \(|d|\le3\tau\);
- a continuum for \(|d|>3\tau\).

Therefore the literal Stage-I reduced payoff is selection-dependent off path.

### No-loss Hotelling game

Under the explicit auxiliary restriction

\[
p_j\ge c_j,
\]

the pure price continuation is unique.

No mixed-price uniqueness theorem is claimed.

### Welfare

The source-duopoly Cournot multiplicity is welfare-material. Therefore no welfare conclusion may be stated as selection-free unless it is an accounting identity or an explicitly all-equilibria statement.

---

## 5. Selection / refinement provenance

The Hotelling solution concepts are now permanently separated.

### Literal source game

Uses only the source price game as reconstructed from the published model.

Result:

\[
|c_B-c_A|>3\tau
\Rightarrow
\text{multiple pure corner price continuations}.
\]

### Weak-dominance facts

The source payoff implies:

\[
p<c
\preceq
p=c,
\]

but also, for every fixed \(\varepsilon>0\),

\[
p=c
\preceq
p=c+\varepsilon.
\]

Hence the high-cost marginal-cost corner action is not justified as an “undominated-price equilibrium.”

### Auxiliary no-loss game

The strategy restriction

\[
p_j\ge c_j
\]

is an explicitly imposed robustness model.

It is not:

- a published Shy–Stenbacka assumption;
- elimination of all weakly dominated strategies;
- trembling-hand perfection;
- proper equilibrium;
- admissibility;
- an institutionally observed regulation.

No prohibited refinement language remains in the canonical claim set.

---

## 6. Function-class adversarial audit

Stage 7.5A deliberately attacks any attempt to generalize C7/C8 beyond the source functional form.

Exact counterexample:

\`audit/stage075a_function_class_counterexamples.md\`

and

\`code/stage075a_scope_counterexamples.py\`.

Keep

\[
\delta=1,\qquad
\rho=3/5,\qquad
y=0,
\]

so the rival-exit boundary remains

\[
U(0)=1.
\]

Replace only the source monitoring cost by another strictly convex function:

\[
M(x)=10x^2.
\]

Then

\[
\Pi_A(0;0)=\frac5{27},
\]

while the exit-boundary action yields

\[
\Pi_A(1;0)=\frac53-10=-\frac{25}{3}.
\]

Thus an endogenous exit boundary can remain geometrically present while the exit-inducing action is far from globally optimal.

Consequences:

- the active-set interpretation has wider economic plausibility;
- the exact positive-slope **global BR** theorem is not generic over arbitrary convex monitoring costs;
- the exact equilibrium multiplicity theorem is not generic over arbitrary convex monitoring costs.

The headline C7/C8 claims therefore remain **baseline source-functional-form theorems**.

Likewise, nonlinear demand and incomplete Hotelling coverage introduce objects not covered by the frozen proofs. No robustness result is inferred by continuity or analogy.

---

## 7. Assumption classification after red-team

### Source-model baseline assumptions

- linear inverse demand;
- nonnegative Cournot quantities;
- linear outsourcing-induced marginal-cost reduction;
- quadratic monitoring cost;
- sourcing box \(i\in[0,\phi]\);
- source SOC;
- source full-coverage linear Hotelling environment for H1.

### Auxiliary restriction

- \(p\ge c\) only for H3-NL–H6-NL.

### Normalizations

- \(S=0,\alpha=1\);
- \(\delta=D/H\);
- \(\rho=b/H^2\).

### Not assumed

- equilibrium selection favoring symmetric equilibria;
- mixed-equilibrium uniqueness;
- generic convex-monitoring robustness;
- generic nonlinear-demand robustness;
- a policy instrument;
- a no-loss regulation in the source economy.

---

## 8. Baseline / robustness / general-theorem classification

### Baseline source theorems

- C1–C8;
- H1.

### Conditional auxiliary-model theorems

- H3-NL–H6-NL.

### Supporting algebra / scope controls

- H2/H2b;
- welfare identities;
- fixed benchmark formulas.

### Restricted-class mechanism support

The rival-exit boundary can move in the same direction under wider decreasing-cost functions, but this is interpretation only.

### Intended broad general theorems

\[
\boxed{\textbf{NONE}}
\]

The paper is a source-specific correction and re-characterization.

---

## 9. Welfare quantifier audit

### Exact identities

The Cournot and Hotelling welfare accounting identities hold for all source-feasible profiles in their stated environments.

### Restricted Cournot benchmark

The common-sourcing welfare optimum C-R is a:

\[
\boxed{\textbf{restricted-instrument equilibrium-welfare optimum}}
\]

and never a first best.

### Full Cournot planner

FB-C is the first best **within the source reduced technology** because it chooses all firm quantities and sourcing levels.

### Hotelling planner

FB-H is the first best **within the source full-coverage / fixed-location technology**.

### Multiple Cournot equilibria

At the exact regression,

\[
W(10/17,10/17)=20/17
<
3/2
=
W(1,0)=W(0,1).
\]

At the \(\rho=2/3\) continuum welfare also varies with equilibrium selection.

Therefore the paper may not claim a selection-free welfare ranking of the corrected Stage-I game.

### Literal Hotelling corner prices

For a fixed corner sourcing history, total welfare is invariant across the pure-price continuum because allocation is unchanged and prices cancel.

This does not imply two-stage welfare invariance because Stage-I incentives depend on the selected continuation.

---

## 10. Benchmark-definition audit

The following labels are frozen.

| Object | Frozen label |
|---|---|
| FB-C | first best within source reduced technology |
| C-R | restricted-instrument equilibrium-welfare optimum |
| FB-H | first best within source full-coverage technology |
| Hotelling fixed-cost allocation | fixed-sourcing allocation optimum |
| Hotelling 50–50 sourcing comparison | fixed-allocation sourcing benchmark |

No restricted benchmark may be described as first best.

---

## 11. Formal Verification Gate

Decision:

\[
\boxed{\textbf{FORMALIZATION APPLICABLE}}
\]

Final state:

\[
\boxed{\textbf{FORMAL VERIFICATION PASS}}
\]

Certificate:

\`audit/stage075a_formal_verification_certificate.md\`.

Statement-fidelity map:

\`audit/stage075a_formal_statement_fidelity.md\`.

Formal source:

\`ShyStenbackaFormal/Stage075A.lean\`.

Pinned environment:

- Lean 4.19.0;
- mathlib commit
  \`c44e0c8ee63ca166450922a373c7409c5d26b00b\`.

Final green CI:

- run \`35439005968\`;
- job \`105886467491\`;
- formal-source commit
  \`8c575f99daecacd85077ee2db3568dbd362c2004\`.

The build completed successfully.

The final proof-escape audit found:

- no \`sorry\`;
- no \`admit\`;
- no project-specific \`axiom\`.

The \`#print axioms\` audit for the certified theorems reports only:

\[
\{\texttt{propext},\texttt{Classical.choice},\texttt{Quot.sound}\}.
\]

No certified theorem contains \`sorryAx\`.

The formal layer is explicitly **targeted**, not a mechanization of the complete economic game.

---

## 12. Paper-claim / formal-theorem statement fidelity

The highest-consequence mapping is:

### Proposition-3 correction

Paper claim:

> the corrected symmetric interior action falls with the number of firms over admissible market-size comparisons.

Formal core:

- \`C4_cross_identity\`;
- \`C4_step_negative\`.

The Lean theorem assumes the relevant adjacent denominators are positive, matching the final economic scope that both compared market sizes must satisfy the source equilibrium restrictions.

### Proposition-5 correction

Paper claim:

> the source duopoly pure global BR can contain a positive-slope rival-exit branch.

Formal core:

- exact active/exit branch join;
- exact monopoly/exit branch join;
- slope \(2>0\).

Exhaustiveness/global optimality remains certified analytically at Stage 4A.

### Hotelling no-loss result

Paper claim:

> under explicit \(p\ge c\), the source symmetric candidate can be defeated by a nonlocal corner deviation.

Formal core:

- exact vertex-gain identity;
- positivity implication;
- exact \(1/90\) regression.

The full iff cap threshold remains certified analytically, not claimed as fully Lean-mechanized.

This division of labor is acceptable because the formal gate targets the mechanically fragile proof core rather than replacing the economic-domain proof.

---

## 13. Required wording downgrades

Stage 7.5A permanently requires the following.

Use:

- “unique pure downstream quantity continuation”;
- “unique symmetric pure Stage-I action”;
- “complete pure Stage-I equilibrium correspondence of the source duopoly”;
- “unique pure-price equilibrium”;
- “among admissible integer market sizes satisfying the source restrictions”;
- “under the explicit no-loss price restriction \(p\ge c\)”;
- “selection-dependent welfare.”

Do not use:

- “unique SPNE” for general \(N\);
- “complete equilibrium correspondence” without “pure Stage-I”;
- “outsourcing always falls with competition”;
- “globally strategic complements”;
- “undominated-price refinement”;
- “refinement-selected Hotelling equilibrium”;
- “Proposition 6 is globally false” without the no-loss conditional qualifier;
- “first best” for C-R or fixed-allocation Hotelling benchmarks;
- “formally verified full model.”

---

## 14. Rollback assessment

No mathematical rollback is required.

Stage 7.5A made one material **scope narrowing**:

> the economic \(N\)-comparative static is explicitly restricted to admissible integer market sizes satisfying the source theorem's assumptions at the compared values.

This is consistent with the existing Stage-4A mathematics and the new Lean certificate. It does not alter the model, formula, or sign.

All other red-team outcomes are wording/provenance restrictions already anticipated in Stages 4A–7.

Earliest-stage rollback:

\[
\boxed{\textbf{NONE}}
\]

---

## 15. Evidence ledger

| Object | Evidence | Status |
|---|---|---|
| headline pure-strategy mathematics | Stage-4A theorem certificates / clean-room derivation | **PASS** |
| novelty scope | Stage-6 theorem-absorption map | **PASS** |
| welfare / selection | Stage-7 exact benchmarks / regression | **PASS WITH SELECTION QUALIFIERS** |
| claim quantifiers | \`stage075a_claim_scope_ledger.md\` | **PASS** |
| function-class generality | exact convex-monitoring counterexample | **BASELINE-ONLY CONFIRMED** |
| formal applicability | Stage-4A target map + Stage-7.5A review | **APPLICABLE** |
| formal build | Lean 4.19.0 green CI | **PASS** |
| proof placeholders / project axioms | CI grep + \`#print axioms\` | **PASS** |
| paper ↔ formal statement mapping | statement-fidelity map / certificate | **PASS** |

No material field remains \`NOT TESTED\`.

---

## 16. Canonical Stage-8 input package

Stage 8 receives the following frozen theory package.

### Primary Cournot correction

1. unique pure Stage-II quantity continuation;
2. global own-payoff concavity under source SOC;
3. corrected capped unique symmetric pure Stage-I action;
4. Proposition-3 sign reversal / admissible-integer-\(N\) monotonicity;
5. complete pure source-duopoly global BR;
6. Proposition-5 global strategic-substitutes failure;
7. complete pure source-duopoly Stage-I equilibrium correspondence.

### Secondary Hotelling correction

8. literal pure-price corner multiplicity;
9. dominance/provenance clarification;
10. conditional pure-price no-loss robustness theorem and exact symmetric-candidate failure region.

### Supporting interpretation

11. welfare identities and benchmark register;
12. selection-dependent welfare warning;
13. baseline-only generality classification;
14. institutional evidence only at broad phenomenon level.

### Formal certificate

15. targeted Lean proof-core certificate and green CI evidence.

No new theory extension is authorized at Stage 8.

---

## 17. Final verdict

\[
\boxed{
\textbf{GO — GENERALITY / QUANTIFIER CERTIFICATION PASS}
}
\]

Route:

\[
\boxed{
\textbf{STAGE 8 — CANONICAL THEORY FREEZE}
}
\]

Stage 8 must freeze the theory at the claim scopes recorded here. It may not widen any theorem, solution concept, robustness claim, or welfare statement.
