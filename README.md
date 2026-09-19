# Shy–Stenbacka Correction

Reproducible adversarial equilibrium audit and correction project for Shy & Stenbacka (2005).

## Project status

**Canonical Stage 1 — Source & Mathematical Audit: PASS**

[
oxed{	extbf{GO TO NOVELTY GATE}}
]

Canonical workflow: `research-paper-workflow` **v2.2**, pinned at commit `42574d6c5931275ccff3ef7e8b4acc188077332a`.

Stage-1 audit:

- `audit/STAGE_01_SOURCE_MATHEMATICAL_AUDIT.md`

Exact verification:

- `code/stage01_verify.py`

Next canonical stage:

- **Stage 2 — Literature Frontier / Novelty Kill Gate**

## Stage-1 certified source-model findings

The audit currently certifies four material issues using the published model's own normalization:

1. equation (14)'s Cournot comparative-static sign is reversed;
2. the hard outsourcing bound (0le i_jlephi) is not enforced in the reported Cournot and Hotelling solutions;
3. the Cournot all-active quantity continuation can fail after feasible asymmetric Stage-I histories;
4. the Hotelling interior-market-share price continuation can fail after feasible Stage-I histories, and an exact profitable corner deviation overturns the reported symmetric candidate for a nonempty region satisfying the paper's local SOC.

These are Stage-1 mathematical findings, **not** yet a novelty certification.

## Source-model discipline

The published monitoring cost is

[
M(i_j)=i_j^2.
]

This repository does **not** import a generalized (eta i_j^2) monitoring cost into the canonical source model.

## Repository policy

- `main` is the stable project history.
- Mathematical audit work is developed on dedicated branches.
- No headline correction claim is treated as final until the relevant global-equilibrium and novelty gates have passed.
- Published expressions and corrected expressions are kept distinct.
- Solver/branch failure is never interpreted as an unprofitable deviation.
- Numerical or symbolic checks supplement, but do not replace, analytical proof.
- Copyrighted source PDFs are not committed unless redistribution is clearly permitted.

## Structure

```text
audit/        canonical audits and theorem-impact tracking
derivations/  clean mathematical derivations
paper/        manuscript material (not yet a frozen paper)
code/         symbolic/numerical verification
sources/      source manifest and provenance notes
docs/         workflow provenance and decisions
```

## Current branch

`audit/full-equilibrium-correspondence`

The branch name predates adoption of the canonical v2.2 routing. Work on it is currently at Stage 1 PASS; a complete corrected equilibrium correspondence remains a downstream task.

## Reproducibility principle

Every eventual correction claim must be recoverable from:

1. the published source model;
2. explicit feasible sets and product-market continuation domains;
3. valid continuation equilibria after every material unilateral deviation;
4. exact parameter-region classification;
5. independent symbolic/numerical checks where useful;
6. later adversarial and formal-verification gates required by v2.2.
