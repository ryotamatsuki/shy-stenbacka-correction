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
\text{Stage 10 PASS}
\rightarrow
\text{Stage 11 PASS}
\rightarrow
\text{Stage 12 PASS}
\rightarrow
\textbf{Stage 13 NEXT}.
\]

Any post-freeze theory change must route back to the earliest affected canonical gate rather than being patched only in manuscript prose or code.


## Canonical Stage 10 closure

Stage 10 converted the frozen theory into the working manuscript only after Stage 9 was reproducible.

Canonical records:

- `audit/STAGE_10_PAPER_CONSTRUCTION.md`
- `audit/STAGE_10_FIGURE_TABLE_ARCHITECTURE.md`

Substantive Stage-10 verification head:

`80f4523222e3f473786f3800ca8be0928de78fe2`

Green evidence:

- Python verification run `35444042815`;
- manuscript smoke-build run `35444042793`.

The figure generator is `code/stage10_generate_figure.py`; the generated TikZ file is a build artifact. Stage 10 changed exposition and reproducibility infrastructure only within the Stage-8 frozen theory boundary.


## Canonical Stage 11 closure

Stage 11 independently attacked the completed manuscript and repeated the known-model/theorem-absorption check.

Canonical records:

- `audit/STAGE_11_ROBUSTNESS_REFEREE_ATTACK.md`
- `audit/STAGE_11_KNOWN_MODEL_ATTACK.md`

Independent verifier:

- `code/stage11_hostile_referee_verify.py`

Final Stage-11 verification head:

`89d04eb048257db3f930cd34f96209d34d1e3bc7`

Green evidence:

- Python push run `35451023487`;
- Python PR run `35451026809`;
- manuscript build run `35450876387` after the only prose scope repair.

The certified Lean source/toolchain blobs remain byte-identical to the Stage-7.5A formal certificate. No certification regression or rollback was triggered.


## Canonical Stage 12 closure

Stage 12 used current official journal guidance and recent publications to position the frozen manuscript without changing theory.

Primary target:

`Review of Industrial Organization`

Canonical records:

- `audit/STAGE_12_JOURNAL_POSITIONING.md`
- `audit/STAGE_12_RIO_REQUIREMENTS_LEDGER.md`

Default submission ladder:

`RIO → JICT → Bulletin of Economic Research → Economics Bulletin`

Canadian Journal of Economics is retained only as an optional stretch.

Stage 13 inherits the RIO requirements ledger; Stage 14 must refresh all live journal/portal rules before submission QA.
