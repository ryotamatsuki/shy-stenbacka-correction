# Stage 10 — Section-by-Section Paper Construction

Status:

[
\boxed{\textbf{CANONICAL STAGE 10 — PASS}}
]

Date: 2026-09-19  
Workflow: `research-paper-workflow` v2.2  
Pinned workflow commit: `42574d6c5931275ccff3ef7e8b4acc188077332a`  
Stage-9 input checkpoint: `9069fe2530658e434c12cc185a9c8e158775c6fa`  
Theory authority: Stage-8 freeze `2fbcf47ff18ea3650d307d90cbdeab78ddb63256`

## 1. Objective and construction order

Stage 10 converts the frozen theoretical object into a complete working manuscript without changing theory.

Construction followed the required dependency order:

1. published model and exact domains;
2. global Cournot continuation and best responses;
3. pure equilibrium characterization;
4. Hotelling source correction and auxiliary robustness;
5. welfare / robustness / institutional scope;
6. relation to literature;
7. Figure/Table Architecture Gate;
8. Introduction;
9. interpretation/discussion integrated into the scope section;
10. Conclusion;
11. technical proof appendix.

Introduction wording was finalized only after the theorem/exposition architecture was fixed.

## 2. Manuscript structure

Canonical manuscript entry:

- `paper/manuscript.tex`

Constructed sections:

- `paper/sections/01_introduction.tex`
- `paper/sections/02_model.tex`
- `paper/sections/03_best_responses.tex`
- `paper/sections/04_equilibrium.tex`
- `paper/sections/05_implications.tex`
- `paper/sections/05a_welfare_scope.tex`
- `paper/sections/05b_related_literature.tex`
- `paper/sections/06_conclusion.tex`
- `paper/sections/appendix.tex`

The Stage-9 skeletal wording and construction placeholders have been removed.

## 3. Model section

The manuscript now states explicitly:

- (0\le i_j\le\phi);
- (c_j=C_0-Hi_j);
- (C_0=H\phi+\gamma\phi^2/2);
- (M(i_j)=i_j^2);
- (D=a-C_0>0);
- nonnegative Cournot quantities;
- the source SOC;
- literal Hotelling price domain versus the separate auxiliary no-loss price domain.

No monitoring-cost coefficient, price floor, refinement, or generalized primitive is silently added to the source model.

## 4. Cournot continuation and corrected comparative statics

The paper states and proves:

- global Stage-II pure quantity continuation via the KKT/potential representation;
- global strict concavity of own reduced Stage-I payoff under the source SOC;
- the corrected symmetric constrained action
  [
  i_C^*
  =
  \min\left\{
  \phi,
  \frac{HND}{b(N+1)^2-H^2N}
  \right\};
  ]
- the corrected competition derivative
  [
  \frac{\partial\bar i_C}{\partial N}
  =
  -
  \frac{HDb(N^2-1)}
  {[b(N+1)^2-H^2N]^2}<0;
  ]
- the economic comparative-static statement only across admissible integer market sizes;
- cap-sensitive (phi) wording.

The manuscript does not promote the symmetric-action result to unique general-(N) SPNE.

## 5. Source-duopoly global best response

The exact normalized response architecture is included:

[
A(y)=\frac{2(\delta-y)}{9\rho-4},
qquad
U(y)=\delta+2y,
qquad
M=\frac{\delta}{4\rho-1},
]

with exact branch thresholds and the source cap applied after the unconstrained global maximizer.

The manuscript states only the certified implication:

> Proposition 5 is false as a global strategic-substitutes claim.

It explicitly rejects the converse overstatement that outsourcing is globally a strategic complement.

## 6. Complete pure source-duopoly correspondence

The complete frozen C8 correspondence is stated as a proposition and summarized in a compact table:

- (ho>2/3);
- (ho=2/3) below the cap threshold;
- (ho=2/3) continuum;
- (4/9<\rho<2/3) with (phi\le s);
- (4/9<\rho<2/3) with (phi>s).

The exact regression

[
(\rho,\delta,\phi)=(3/5,1,2)
]

is retained with the exact equilibrium triple

[
(10/17,10/17),quad(1,0),quad(0,1).
]

No mixed-strategy completeness wording appears.

## 7. Hotelling block

The source-faithful literal pure-price proposition states:

- unique interior continuation for (|d|<3\tau);
- unique boundary continuation for equality;
- continuum of corner pure-price equilibria for (|d|>3\tau).

The manuscript explains why the zero-demand firm's indifference is strategically material for upstream payoffs.

The dominance paragraph records both facts:

- (p<c) is weakly dominated by (p=c);
- (p=c) is itself weakly dominated by (p=c+\varepsilon).

Therefore the manuscript does not use “undominated-price refinement” or any trembling-hand/proper/admissibility language.

The auxiliary no-loss result is explicitly conditional on

[
p_j\ge c_j,
]

and states the exact pure-strategy failure region

[
\frac{27}{2}\tau<H^2n<18\tau,
qquad
\phi>x_-,
]

with the boundary tie at (phi=x_-) and exact (1/90) regression.

## 8. Welfare and benchmark discipline

The manuscript includes exact Cournot and Hotelling welfare identities only as diagnostics.

It preserves the frozen benchmark semantics:

- unrestricted source-technology planner problems are the only objects described as first best;
- the Cournot common-sourcing object is restricted-instrument;
- Hotelling fixed-sourcing and fixed-allocation objects retain those exact labels.

The exact welfare-selection regression is reported:

[
W(10/17,10/17)=20/17
<
3/2=W(1,0)=W(0,1).
]

Hence the manuscript makes no selection-free Cournot welfare claim.

## 9. Robustness and generality

The Stage-7.5A (M(x)=10x^2) counterexample is used to explain why the positive-slope global response and multiplicity results remain source-functional-form theorems.

The manuscript makes no generic nonlinear-demand or arbitrary-convex-monitoring theorem.

Institutional evidence is used only to motivate the broad outsourcing/monitoring trade-off, not to claim empirical validation of the exact source technology.

## 10. Literature positioning

The related-literature section follows the Stage-6 theorem-absorption result.

It explicitly distinguishes the source correction from prior work on:

- negative competition effects on outsourcing;
- asymmetric R&D/investment and exit;
- symmetry breaking;
- multiple/piecewise investment responses;
- heterogeneous-cost spatial pricing and no-loss restrictions.

The manuscript describes itself as a source-specific correction/global re-characterization, not a new general outsourcing theory.

## 11. Figure / Table Architecture Gate

Canonical record:

- `audit/STAGE_10_FIGURE_TABLE_ARCHITECTURE.md`

Retained quantitative architecture:

- Figure 1: exact global duopoly best-response witness;
- Table 1: exact pure-equilibrium regime classification.

Figure generator:

- `code/stage10_generate_figure.py`

The generator uses exact rational arithmetic, asserts the certified thresholds/equilibria, and writes the TikZ build input.

No decorative or evidence-weak visual is included.

## 12. Technical proofs

The appendix supplies manuscript-level proof details for:

- global Cournot continuation;
- global own-payoff concavity;
- corrected symmetric Cournot action/comparative static;
- source-duopoly response construction;
- complete pure correspondence;
- literal Hotelling pure-price continuation;
- auxiliary no-loss threshold theorem.

The appendix does not widen the Stage-4A or Stage-7.5A certificates.

## 13. Build and regression evidence

The current substantive manuscript/code head before closure documentation is:

`80f4523222e3f473786f3800ca8be0928de78fe2`.

At that head:

- Python verification run `35444042815`: **success**;
- manuscript smoke-build run `35444042793`: **success**.

The manuscript build regenerates Figure 1 from the exact Python generator before running `latexmk`.

The Python verification suite also executes the Stage-10 figure generator and its exact assertions.

Repository search found no remaining Stage-9 skeletal marker, TODO, or Stage-10 placeholder in the manuscript source.

The Stage-7.5A Lean source/toolchain was not modified at Stage 10, so the frozen formal certificate remains current.

## 14. Scope audit against Stage 8

The completed manuscript does not claim:

- unique general-(N) SPNE;
- absence of asymmetric general-(N) equilibria;
- mixed-strategy completeness;
- global strategic complementarity;
- generic convex-monitoring or nonlinear-demand theorems;
- literal-game Hotelling refinement selection;
- trembling-hand/perfect/proper/admissible equilibrium;
- selection-free Cournot welfare;
- restricted benchmarks as first best;
- full formal verification of the complete economic model.

No Stage-8 rollback trigger was activated.

## 15. Exit criterion

Every manuscript section compiles as an integrated document, matches the frozen theory/theorem certificates, and has an explicit exposition role.

Every headline result has a primary exposition vehicle.

Every retained quantitative visual/table is either exactly generated from certified values or directly states a certified theorem classification.

No material Stage-10 blocker remains.

## 16. Verdict and route

[
\boxed{\textbf{CANONICAL STAGE 10 — PASS}}
]

[
\boxed{\textbf{MANUSCRIPT CONSTRUCTION COMPLETE}}
]

Next route:

[
\boxed{\textbf{STAGE 11 — ROBUSTNESS / REFEREE ATTACK GATE}}
]

Stage 11 must attack the completed manuscript as a hostile referee, including the known-model-in-disguise/theorem-absorption attack and the paper-claim/formal-theorem scope map.  Any mathematical or scope failure must roll back to the earliest affected stage rather than being patched only in prose.
