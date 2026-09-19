# Canonical Workflow Routing

This repository follows `ryotamatsuki/research-paper-workflow` **v2.2**.

Pinned workflow commit:

`42574d6c5931275ccff3ef7e8b4acc188077332a`

See `docs/WORKFLOW_PROVENANCE.md`.

## Canonical stage sequence

1. Stage 0 — Idea / Motivation Intake
2. Stage 1 — Source & Mathematical Audit
3. **Stage 2 — Literature Frontier / Novelty Kill Gate**
4. **Stage 3 — Candidate Mechanism Search**
5. Stage 4 — Minimal Model Gate
6. Stage 4A — Independent Mathematical Adversarial Certification Gate
7. Stage 5 — Mechanism Hardening
8. Stage 6 — Novelty Re-Kill
9. Stage 7 — Welfare / Generality / Institutional Validation
10. Stage 7.5 — Full-Theory Freeze Decision
11. Stage 7.5A — Generality / Quantifier Red-Team Gate
12. Stage 8 — Canonical Theory Freeze
13. Stage 9 — Repository / Reproducibility Setup
14. Stage 10 — Section-by-Section Paper Construction
15. Stage 11 — Robustness / Referee Attack Gate
16. Stage 12 — Journal Positioning
17. Stage 13 — Full-Paper Integration
18. Stage 14 — Submission QA
19. Stage 15 — Submission Freeze

## Current canonical state

[
oxed{
	ext{Stage 1 PASS}
ightarrow
	ext{Stage 2 PASS}
ightarrow
	extbf{Stage 3 NEXT}
}
]

Stage-1 verdict: **GO TO NOVELTY GATE**.  
Stage-2 verdict: **GO TO MECHANISM SEARCH**.

## Stage-2 contribution constraint

The following claims are killed as novelty claims:

- partial outsourcing as a concept;
- strategic outsourcing;
- strategic-substitute outsourcing decisions;
- the generic statement that competition affects outsourcing;
- the generic statement that more Cournot competitors can reduce outsourcing.

The surviving route is source-specific correction/global re-characterization.

Stage 3 may compare correction architectures, but **may not introduce new primitives or mechanisms merely to create novelty**. The source model remains frozen.

## Important ordering note

This GitHub repository was bootstrapped before canonical Stage 9 for provenance. That does **not** mean Stage 9 has passed. Formal Stage-9 certification remains downstream of theory freeze.

## Fail-closed equilibrium rule

Any later Nash/SPNE claim must provide valid product-market continuations after every economically material Stage-I deviation.

The following may not be treated as evidence that a deviation is unprofitable:

- a negative “equilibrium” quantity produced by an interior formula;
- a market share outside ([0,1]);
- an invalid active set;
- solver failure, NaN, exception, or nonconvergence;
- an FOC/SOC certificate that applies only to one regular branch.

## Branch policy

- `main`: stable project history.
- `audit/full-equilibrium-correspondence`: current audit branch.
- Stage-specific mathematical/manuscript work may be split further as the canonical workflow requires.
