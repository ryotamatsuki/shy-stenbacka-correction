# Shy–Stenbacka Correction

Reproducible adversarial equilibrium audit and correction project for Shy & Stenbacka (2005).

## Project status

**Canonical Stage 2 — Literature Frontier / Novelty Kill Gate: PASS**

[
oxed{	extbf{GO TO MECHANISM SEARCH}}
]

Canonical workflow: `research-paper-workflow` **v2.2**, pinned at commit `42574d6c5931275ccff3ef7e8b4acc188077332a`.

Completed canonical audits:

- `audit/STAGE_01_SOURCE_MATHEMATICAL_AUDIT.md`
- `audit/STAGE_02_LITERATURE_NOVELTY_GATE.md`

Literature evidence ledger:

- `audit/stage02_literature_ledger.md`

Exact Stage-1 verification:

- `code/stage01_verify.py`

Next canonical stage:

- **Stage 3 — Candidate Mechanism Search**

## Surviving contribution after Stage 2

The project must be positioned as a **source-specific correction and global equilibrium re-characterization in a known model**.

It must **not** claim novelty for the generic proposition that stronger competition can reduce outsourcing. König (2010) already obtains that direction in a closely related Cournot partial-outsourcing specification.

What survives the novelty kill gate is narrower:

1. the published Shy–Stenbacka equation (14) has the wrong sign when differentiated from its own equation (13);
2. the primitive outsourcing bound (0le i_jlephi) is omitted from the reported Cournot and Hotelling equilibrium formulas;
3. the Cournot all-active continuation can fail after feasible asymmetric Stage-I histories;
4. the Hotelling interior-market-share continuation can fail after feasible deviations, with an exact profitable corner deviation already certified at Stage 1;
5. a complete constrained SPNE correspondence of the exact source game remains a potentially novel target, not yet a proved theorem.

## Strongest prior-art threat

**Jan König (2010), “Outsourcing motives, competitiveness and taxation.”**

König explicitly adapts the Shy–Stenbacka framework and derives a negative competition effect in a close variant. But he treats Shy–Stenbacka's positive result as a genuine opposite result and attributes the difference to cost structure; he does not correct their equation (14) or the global-equilibrium defects.

Therefore the eventual paper must cite and distinguish König prominently.

## Source-model discipline

The published monitoring cost is

[
M(i_j)=i_j^2.
]

This repository does **not** import a generalized (eta i_j^2) monitoring cost into the canonical source model.

## Repository policy

- `main` is the stable project history.
- Mathematical audit work is developed on dedicated branches.
- No headline correction claim is treated as final until global-equilibrium, adversarial, novelty re-kill, and formal-verification gates have passed.
- Published expressions and corrected expressions are kept distinct.
- Solver/branch failure is never interpreted as an unprofitable deviation.
- Search failure is never treated as proof of novelty.
- Copyrighted source PDFs are not committed unless redistribution is clearly permitted.

## Structure

```text
audit/        canonical audits, literature ledger, theorem-impact tracking
derivations/  clean mathematical derivations
paper/        manuscript material (not yet a frozen paper)
code/         symbolic/numerical verification
sources/      source manifest and provenance notes
docs/         workflow provenance and decisions
```

## Current branch

`audit/full-equilibrium-correspondence`

The branch name predates canonical v2.2 routing. Current canonical state is Stage 2 PASS.

## Reproducibility principle

Every eventual correction claim must be recoverable from:

1. the published source model;
2. explicit feasible sets and product-market continuation domains;
3. valid continuation equilibria after every material unilateral deviation;
4. exact parameter-region classification;
5. model-level prior-art comparison;
6. independent symbolic/numerical checks where useful;
7. later adversarial and formal-verification gates required by v2.2.
