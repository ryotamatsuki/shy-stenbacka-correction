# Workflow and Stage Gates

The project uses stage gates so that manuscript language cannot outrun the mathematics.

## Stage 0 — Repository initialization

**PASS** when the reproducible project skeleton exists.

## Stage 1 — Source freeze

Pass criteria:

- final published version identified;
- bibliographic identity fixed;
- relevant equations/propositions transcribed with page-level provenance.

## Stage 2 — Mathematical canonicalization

Pass criteria:

- timing, objectives, feasible sets, and parameter restrictions are explicit;
- published notation is mapped to canonical notation without changing assumptions.

## Stage 3 — Constrained best-response correspondence

Pass criteria:

- all interior and boundary cases derived;
- \(i=\phi\) handled explicitly;
- ties represented as correspondences;
- asymmetric unilateral deviations checked.

## Stage 4 — Complete equilibrium correspondence

Pass criteria:

- every admissible parameter region classified;
- all candidate equilibria tested;
- Hotelling consistency checked;
- no result relies only on symmetric FOCs.

## Stage 5 — Proposition-level impact

Pass criteria:

- Proposition 3, Corollary 4, and Proposition 5 classified;
- exact surviving, qualified, and invalid regions stated;
- replacement propositions formulated.

## Stage 6 — Independent replication

Pass criteria:

- algebra independently rechecked;
- symbolic/numerical verification agrees with analytical claims;
- counterexamples are reproducible.

## Stage 7 — Correction manuscript

Pass criteria:

- claims are no stronger than Stage 5–6 results;
- original result, defect, corrected result, and economic implication are separated cleanly;
- references and attribution are complete.

## Stage 8 — Submission audit

Pass criteria:

- notation consistency;
- proof completeness;
- citation verification;
- reproducibility package check;
- anonymous/submission version as required.

## Branch policy

- `main`: stable history.
- `audit/full-equilibrium-correspondence`: current mathematical audit.
- Future manuscript branches should start only after the relevant mathematical stage has passed.
