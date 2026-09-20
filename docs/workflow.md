# Canonical Workflow Routing

Stages 0–11 follow \`ryotamatsuki/research-paper-workflow\` v2.2.

Original pinned workflow commit:

\`42574d6c5931275ccff3ef7e8b4acc188077332a\`

Stage 12 was subsequently re-audited under the backward-compatible v2.3 candidate-universe refinement:

\`9eb616bd31ea3a9ef3c29e288228ed962c44c9cf\`

This Stage-12 refinement does not alter the Stage-8 theory freeze or Stage-11 certification.

## Current state

\[
\boxed{
\text{Stage 1 PASS}
\rightarrow
\text{Stage 2 PASS}
\rightarrow
\text{Stage 3 PASS}
\rightarrow
\text{Stage 4 PASS (AMENDED)}
\rightarrow
\text{Stage 4A PASS (AMENDED/RECERTIFIED)}
\rightarrow
\text{Stage 6 PASS (RECHECKED)}
\rightarrow
\text{Stage 7 PASS}
\rightarrow
\text{Stage 7.5 PASS}
\rightarrow
\text{Stage 7.5A PASS (RECONCILED)}
\rightarrow
\text{Stage 8 PASS (AMENDED)}
\rightarrow
\text{Stage 9 PASS}
\rightarrow
\text{Stage 10 PASS}
\rightarrow
\text{Stage 11 PASS (RECERTIFIED)}
\rightarrow
\text{Stage 12 PASS}
\rightarrow
\text{Stage 13 PASS (REPAIRED/RECERTIFIED)}
\rightarrow
\textbf{Stage 14 NOT STARTED}
}
\]

Stage 5 was not triggered.

## Stage-7.5A verdict

\[
\boxed{\textbf{GO — GENERALITY / QUANTIFIER CERTIFICATION PASS}}
\]

Formal gate:

\[
\boxed{\textbf{FORMAL VERIFICATION PASS}}
\]

## Frozen claim scopes entering Stage 8

### General-\(N\) Cournot

- unique pure downstream quantity continuation for every feasible sourcing history;
- globally strictly concave own reduced sourcing payoff under source SOC;
- unique **symmetric pure Stage-I action**;
- competition comparative static stated over admissible integer market sizes satisfying the source restrictions.

No general-\(N\) all-equilibrium uniqueness claim is authorized.

### Source duopoly

- complete **pure Stage-I** global best response and equilibrium correspondence;
- Proposition 5 false as a global strategic-substitutes claim;
- positive-slope rival-exit branch does not imply global strategic complements.

### Hotelling

- literal **pure-price** continuation: unique or exactly characterized multiple;
- auxiliary \(p\ge c\) game: conditional no-loss robustness only;
- no trembling-hand / proper / admissibility / mixed-equilibrium claim.

### Welfare

- exact accounting identities;
- planner/benchmark labels frozen;
- Cournot equilibrium welfare is selection-dependent where Stage-I multiplicity exists.

### Generality

Exact results remain baseline/source-functional-form theorems.

A Stage-7.5A convex-monitoring counterexample blocks any generic promotion of C7/C8.

## Formal verification boundary

Lean 4.19.0 + pinned mathlib commit
\`c44e0c8ee63ca166450922a373c7409c5d26b00b\`.

Final green formal run:
\`35439005968\`.

The formal layer certifies selected proof-critical algebra/order statements, not the complete economic game.

## Stage-8 verdict

\[
\boxed{\textbf{CANONICAL STAGE 8 — PASS}}
\]

\[
\boxed{\textbf{THEORY FROZEN}}
\]

Canonical freeze artifact:

\`audit/STAGE_08_CANONICAL_THEORY_FREEZE.md\`

Stage 8 freezes:

- canonical source model and strategy domains;
- theorem statements at the Stage-7.5A certified quantifiers;
- pure-strategy / pure-price solution-concept boundaries;
- welfare benchmark labels and selection dependence;
- source-specific novelty boundary;
- baseline-only generality boundary;
- formal-verification scope, toolchain, dependency, CI, and axiom/placeholder provenance;
- explicit claims not made;
- rollback rules for every post-freeze theory change.

No theorem widening or new extension is authorized after the freeze without rollback to the earliest affected gate.

## Stage-9 verdict

\[
\boxed{\textbf{CANONICAL STAGE 9 — PASS}}
\]

Production/reproducibility setup is complete.

Canonical report:

\`audit/STAGE_09_REPOSITORY_REPRODUCIBILITY.md\`

Canonical evidence manifest:

\`audit/stage09_artifact_manifest.md\`

Green reproducibility evidence:

- Python verification run \`35442666402\`;
- Lean formal run \`35439005968\`;
- manuscript smoke-build run \`35442682700\`.

Stage 9 established a modular manuscript layout, pinned Python/Lean dependencies, repository-level Make targets, CI for Python/formal/manuscript layers, theorem/formal indexes, and a permanent counterexample/regression register without changing the Stage-8 frozen theory.

## Stage-10 verdict

\[
\boxed{\textbf{CANONICAL STAGE 10 — PASS}}
\]

Canonical construction report:

\`audit/STAGE_10_PAPER_CONSTRUCTION.md\`

Figure/Table Architecture Gate:

\`audit/STAGE_10_FIGURE_TABLE_ARCHITECTURE.md\`

The integrated manuscript now contains the model, global Cournot continuation and best responses, complete pure source-duopoly correspondence, literal and auxiliary Hotelling blocks, welfare/robustness/scope discussion, literature positioning, introduction, conclusion, and proof appendix.

Green Stage-10 evidence at substantive head \`80f4523222e3f473786f3800ca8be0928de78fe2\`:

- Python verification run \`35444042815\`;
- manuscript build run \`35444042793\`.

No theory, quantifier, equilibrium-concept, benchmark, novelty, or formal-scope change relative to Stage 8 was introduced.

## Stage-11 verdict

\[
\boxed{\textbf{CANONICAL STAGE 11 — PASS}}
\]

Canonical hostile-referee report:

\`audit/STAGE_11_ROBUSTNESS_REFEREE_ATTACK.md\`

Known-model-in-disguise record:

\`audit/STAGE_11_KNOWN_MODEL_ATTACK.md\`

Independent verifier:

\`code/stage11_hostile_referee_verify.py\`

The historical Stage-11 close missed a real certification regression. A later independent clean-room audit found the C7 cap-quantifier defect, an incomplete C8 completeness proof record, and an overstatement of the multiplicity mechanism. Those findings were routed back to Stage 4A/8 as required, repaired, and Stage 11 was re-run. The controlling record is `audit/STAGE_11_RECERTIFICATION_2026-09-20.md`; no unresolved FATAL or MAJOR finding remains.

Green Stage-11 evidence:

- Python verification head \`89d04eb048257db3f930cd34f96209d34d1e3bc7\`;
- push run \`35451023487\` — success;
- PR run \`35451026809\` — success;
- manuscript build run \`35450876387\` — success after the scope repair.

## Stage-12 verdict — recertified under v2.3

The original Stage-12 shortlist was incomplete. The v2.3 candidate-universe audit identified the omission, enlarged the candidate set, and reran positioning without altering theory.

\[
\boxed{\textbf{CANDIDATE-UNIVERSE COMPLETENESS AUDIT — PASS}}
\]

\[
\boxed{\textbf{JOURNAL-POSITIONING COMPLETENESS REGRESSION — REPAIRED}}
\]

Final Stage-12 verdict:

\[
\boxed{\textbf{PRIMARY JOURNAL SELECTED — GO TO INTEGRATION}}
\]

Primary target:

\[
\boxed{\textbf{Review of Industrial Organization}}
\]

Best stretch:

\[
\boxed{\textbf{International Journal of Industrial Organization}}
\]

Canonical records:

- `audit/STAGE_12_CANDIDATE_UNIVERSE_LEDGER.md`
- `audit/STAGE_12_JOURNAL_POSITIONING.md`
- `audit/STAGE_12_RIO_REQUIREMENTS_LEDGER.md`

Default fit-first ladder:

`RIO → JITE → Journal of Economics → JICT → Bulletin of Economic Research → Economics Bulletin`.

Optional one-shot stretch:

`IJIO → RIO → JITE → …`.

JIE, JEMS and CJE were explicitly evaluated as higher-risk stretches. Other obvious/closest-literature venues are explicitly excluded in the candidate-universe ledger rather than silently omitted.

No frozen theorem, novelty statement, benchmark, equilibrium concept, welfare claim, or formal-verification scope was modified.


## Stage-13 verdict

\[
\boxed{\textbf{INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA}}
\]

Canonical report:

`audit/STAGE_13_FULL_PAPER_INTEGRATION.md`

Substantive integration head:

`72c2f233199bea82e67de9b93987a64fe2dae804`

Implemented for RIO:

- abstract / keywords / JEL integration;
- Dai (2026) current make-or-buy positioning without novelty inflation;
- reproducibility, data, code, and generative-AI disclosure;
- retained Stage-10 figure/table architecture with strengthened table scope caption;
- flat no-subfolder LaTeX package generator;
- canonical and flat package CI builds;
- dedicated integration lint for citations, references, cross-references, indexing metadata, scope controls, and placeholders.

Green evidence:

- Python verification: `35473538351` and `35473541979`;
- canonical + flat RIO manuscript build: `35473538163`.

No theory or certification rollback was triggered.

## Stage-14 contract

Stage 14 must refresh current RIO journal/portal requirements, resolve all material author- and portal-specific unknowns or fail closed, rebuild the full submission package, verify artwork/source/declarations, resolve all citations and cross-references, confirm formal-verification claim fidelity, and inspect the final PDF page by page.

Stage 14 may repair formatting/package defects but may not enlarge the frozen theory or contribution.


## Independent-audit repair route — 2026-09-20

The Stage-13 manuscript at checkpoint \`5bdf156347da4267167513d96b5ef53456cd3f9a\` was independently audited and did **not** remain valid as-is.

Reopening route actually executed:

\[
\text{Stage 4A partial reopen}
\rightarrow
\text{Stage 7.5A reconciliation}
\rightarrow
\text{Stage 8 amended freeze}
\rightarrow
\text{Stage 6 absorption recheck}
\rightarrow
\text{Stage 11 recertification}
\rightarrow
\text{Stage 13 reintegration}.
\]

The Stage-7.5A claim-scope ledger itself was not the source of the C7 error; it already used a feasibility qualifier.  The regression arose when that qualifier was not preserved consistently in Stage-4A/8/manuscript wording.

Final technical evidence before closure-only documentation:

- branch head \`0bd82c56703655f0a72784b4ef8f964520875cdc\`;
- Python verification \`35477505973\`: **success**;
- canonical + flat RIO build \`35477505977\`: **success**;
- final 22-page PDF visual inspection: **PASS**.

Current state:

\[
\boxed{\textbf{STAGE 13 — REPAIRED AND RECERTIFIED}}
\]

Stage 14 remains **not started**.
