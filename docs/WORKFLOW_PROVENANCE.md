# Workflow Provenance

## Canonical workflow pin

This project follows `ryotamatsuki/research-paper-workflow`:

- version: **v2.2**
- canonical workflow commit: `42574d6c5931275ccff3ef7e8b4acc188077332a`
- canonical hierarchy:
  1. `GOVERNANCE.md`
  2. `THEORY_PAPER_RESEARCH_PIPELINE.md`
  3. stage templates
  4. checklists / examples as subordinate materials

The project does not silently upgrade to a later workflow version during a frozen stage.

## Historical routing rule

The repository was created before canonical Stage 9. Early repository existence was bootstrap infrastructure only and did **not** constitute Stage-9 completion.

The project subsequently traversed the canonical v2.2 route through Stage 8, including the mandatory Stage 4A and Stage 7.5A gates and the embedded Formal Verification Gate.

## Canonical theory freeze

Stage 8 checkpoint:

`2fbcf47ff18ea3650d307d90cbdeab78ddb63256`

Canonical freeze record:

- `audit/STAGE_08_CANONICAL_THEORY_FREEZE.md`

The Stage-8 freeze controls all downstream manuscript and reproducibility work.

## Canonical Stage 9 closure

Stage 9 was closed only after the post-freeze production repository was made reproducible.

Canonical report:

- `audit/STAGE_09_REPOSITORY_REPRODUCIBILITY.md`

Evidence manifest:

- `audit/stage09_artifact_manifest.md`

Reproduction guide:

- `REPRODUCIBILITY.md`

Green evidence:

- Python verification run `35442666402`;
- Lean formal run `35439005968`;
- manuscript smoke-build run `35442682700`.

Current routing:

\[
\text{Stage 8 PASS / THEORY FROZEN}
\rightarrow
\text{Stage 9 PASS}
\rightarrow
\textbf{Stage 10 NEXT}.
\]

Any post-freeze theory change must route back to the earliest affected canonical gate rather than being patched only in manuscript prose or code.
