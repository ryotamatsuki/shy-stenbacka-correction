# Workflow Provenance

## Canonical workflow pin

This project follows the canonical `ryotamatsuki/research-paper-workflow`.

For Stage 1 the workflow state is frozen to:

- version: **v2.2**
- branch: `main`
- commit: `42574d6c5931275ccff3ef7e8b4acc188077332a`
- commit message: `Publish research-paper-workflow v2.2`
- canonical hierarchy:
  1. `GOVERNANCE.md`
  2. `THEORY_PAPER_RESEARCH_PIPELINE.md`
  3. `templates/STAGE_01_AUDIT.md`
  4. checklists / examples as subordinate materials

## Routing consequence

The project's earlier local Stage-0–8 skeleton was bootstrap infrastructure, not a replacement for the canonical workflow.

Canonical routing is therefore:

[
	ext{Stage 1 Source & Mathematical Audit}
ightarrow
	ext{Stage 2 Literature Frontier / Novelty Kill Gate}.
]

Creating the repository early does **not** constitute canonical Stage 9 PASS. Stage 9 (Repository / Reproducibility Setup) must still be closed later against its own v2.2 gate after the theory has survived the preceding stages.

## Stage-1 status

**PASS — GO TO NOVELTY GATE**

Canonical Stage-1 artifact:

- `audit/STAGE_01_SOURCE_MATHEMATICAL_AUDIT.md`

Canonical Stage-1 verification code:

- `code/stage01_verify.py`
