# Workflow Provenance

## Canonical workflow pin

This project follows `ryotamatsuki/research-paper-workflow`:

- Stages 0–11 canonical version: **v2.2**
- Stages 0–11 workflow commit: `42574d6c5931275ccff3ef7e8b4acc188077332a`
- Stage-12 re-audit rule set: **v2.3 candidate-universe refinement**
- Stage-12 re-audit workflow commit: `9eb616bd31ea3a9ef3c29e288228ed962c44c9cf`
- canonical hierarchy:
  1. `GOVERNANCE.md`
  2. `THEORY_PAPER_RESEARCH_PIPELINE.md`
  3. stage templates
  4. checklists / examples as subordinate materials

The project does not silently upgrade frozen mathematical stages. The later v2.3 change is a backward-compatible Stage-12 journal-positioning refinement only; it was applied explicitly by reopening and recertifying Stage 12. It does not alter the Stage-8 theory freeze or Stage-11 certification.

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


## Canonical Stage 12 closure — v2.3 recertification

Stage 12 was first closed under v2.2 at checkpoint `884ca99b4dfc7d8ef194775fd37aa30fa84593d5`.

A later reusable-workflow improvement exposed a **candidate-universe completeness defect** in that close: several plausible IO venues, most importantly IJIO, had not been explicitly evaluated before journal ranking.

Stage 12 was therefore reopened under workflow commit:

`9eb616bd31ea3a9ef3c29e288228ed962c44c9cf`.

Canonical recertification records:

- `audit/STAGE_12_CANDIDATE_UNIVERSE_LEDGER.md`
- `audit/STAGE_12_JOURNAL_POSITIONING.md`
- `audit/STAGE_12_RIO_REQUIREMENTS_LEDGER.md`

Recertified outcome:

- candidate-universe completeness audit: **PASS**;
- journal-positioning completeness regression: **REPAIRED**;
- primary: **Review of Industrial Organization**;
- best stretch: **International Journal of Industrial Organization**;
- default ladder: `RIO → JITE → Journal of Economics → JICT → Bulletin of Economic Research → Economics Bulletin`;
- optional one-shot stretch: `IJIO → RIO → JITE → …`.

RIO remained primary only after the enlarged candidate set was compared. The reason is contribution-type fit: RIO explicitly accommodates shorter notes/commentaries, while IJIO is an excellent topical fit but a higher-risk venue for a source-specific correction rather than a new general IO mechanism.

The RIO requirements ledger was rechecked on the same date and remains the Stage-13 operational baseline.

No theory, novelty, welfare, equilibrium, or formal-verification rollback was triggered.

Stage 13 inherits both the candidate-universe ledger and RIO requirements ledger. Stage 14 must refresh current live journal/portal rules before submission QA.


## Canonical Stage 13 closure

Stage 13 integrated the Stage-8-frozen / Stage-11-certified manuscript for the Stage-12-selected primary journal, **Review of Industrial Organization**.

Canonical record:

- `audit/STAGE_13_FULL_PAPER_INTEGRATION.md`

Substantive integration head:

`72c2f233199bea82e67de9b93987a64fe2dae804`

New reproducibility/package artifacts:

- `code/stage13_integration_verify.py`
- `code/stage13_build_rio_bundle.py`
- `paper/sections/07_reproducibility.tex`
- `paper/RIO_SUBMISSION_NOTES.md`

Green evidence:

- Python push run `35473538351`;
- Python PR run `35473541979`;
- canonical plus flat RIO manuscript build `35473538163`.

The generated flat package is derived from the canonical modular source and is not an independent manuscript authority.

Stage 13 introduced no new economic theorem, mechanism, equilibrium concept, welfare result, or formal-verification claim. The Stage-8 theory freeze and Stage-11 certification remain valid.

Current route:

\[
\text{Stage 12 PASS}
\rightarrow
\text{Stage 13 PASS}
\rightarrow
\textbf{Stage 14 NEXT}.
\]


## Independent-audit certification regression and repair — 2026-09-20

After the original Stage-13 close, a clean-room audit of checkpoint
\`5bdf156347da4267167513d96b5ef53456cd3f9a\` found three material issues:

1. C7's feasible positive-slope branch was over-quantified with respect to the sourcing cap;
2. C8's five-case equilibrium statement survived, but the internal proof/certificate did not explicitly establish branch completeness;
3. downstream exit had been overstated as necessary for multiplicity.

This invalidated the historical Stage-11 conclusion that no certification regression had occurred.

The project therefore used the workflow rollback rule rather than patching only the manuscript:

- Stage 4A partially reopened for C7/C8;
- Stage 7.5A reconciled because its scope ledger had already contained the correct feasibility qualifier;
- Stage 8 freeze amended;
- Stage 6 absorption/novelty rechecked;
- Stage 11 reopened and recertified;
- Stage 13 reintegrated and rebuilt.

Controlling repair artifacts:

- \`audit/INDEPENDENT_AUDIT_REPAIR_LEDGER_2026-09-20.md\`;
- \`audit/STAGE_04A_INDEPENDENT_AUDIT_RECERTIFICATION_2026-09-20.md\`;
- \`audit/STAGE_075A_INDEPENDENT_AUDIT_RECONCILIATION_2026-09-20.md\`;
- \`audit/STAGE_08_INDEPENDENT_AUDIT_AMENDMENT_2026-09-20.md\`;
- \`audit/STAGE_06_INDEPENDENT_AUDIT_RECHECK_2026-09-20.md\`;
- \`audit/STAGE_11_RECERTIFICATION_2026-09-20.md\`;
- \`audit/STAGE_13_INDEPENDENT_AUDIT_REINTEGRATION_2026-09-20.md\`.

The Lean source remained byte-identical to the prior formal certificate; the repair narrows the interpretation of C7 formal coverage rather than changing a Lean theorem.

Latest substantive green evidence before documentation-only closure commits:

- \`0bd82c56703655f0a72784b4ef8f964520875cdc\`;
- Python run \`35477505973\` — success;
- canonical + flat manuscript build run \`35477505977\` — success;
- final 22-page canonical PDF rendered and visually inspected page by page — PASS.

Current route:

\[
\text{Stage 13 PASS — repaired and recertified}
\]

Stage 14 is **not started**.


## Canonical Stage 14 conditional closure

Stage 14 refreshed the live public Review of Industrial Organization instructions and performed submission QA over the repaired Stage-13 manuscript.

Technical QA head:

\`446ce7bdf7eff1d2363a315c905c28572c91861a\`.

Evidence:

- Python verification run \`35478726461\` — success;
- manuscript / flat source package / font / page-count run \`35478726453\` — success;
- Stage-14 source-only flat bundle — PASS;
- 22-page visual QA — PASS;
- final-head visual comparison — zero changed pages.

Stage 14 repaired only submission/package defects and did not change frozen economics.

The gate cannot be promoted to full PASS because the public instructions require factual author/title-page and declaration information that has not been authoritatively supplied, and the authenticated RIO portal is not inspectable in the current environment.

Current verdict:

\[
\boxed{\textbf{CONDITIONAL PASS — AUTHOR INPUT + AUTHENTICATED PORTAL PREFLIGHT REQUIRED}}
\]

Current route:

\[
\boxed{\textbf{STAGE 15 BLOCKED / NOT STARTED}}
\]
