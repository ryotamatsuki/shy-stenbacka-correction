# Canonical Submission Candidate

Date: 2026-10-05

## Decision

The sole canonical production and submission-candidate branch for the Shy–Stenbacka (2005) correction project is:

`main`

PR #1, **Stages 0–14: RIO submission QA conditional pass**, was promoted from `audit/full-equilibrium-correspondence` to `main` on 2026-10-05 after the latest head was confirmed to be mergeable, 361 commits ahead of the old main and 0 commits behind it, with the latest Python verification and manuscript smoke-build workflows both passing.

Promotion merge commit:

`fe89ab695fc4715683650f64ae05409f044a2f96`

The current `main` HEAD, including subsequent governance/documentation-only commits, is the authoritative submission candidate. The promotion SHA above is a provenance checkpoint, not a permanently frozen submission SHA.

## Current gate

- Stages 0–13: passed/recertified as recorded in the canonical audit files.
- Stage 14: **CLOSED — CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED**.
- Stage 15: **READY FOR AUTHENTICATED PORTAL PREFLIGHT / NOT STARTED**.
- Target journal: **Review of Industrial Organization**.
- No final submission action has been taken.

The remaining blocker is administrative rather than mathematical: authenticated portal-only checks such as article type, review/anonymity model, file designations, portal declarations, and approval of the portal-generated PDF.

## Source-of-truth policy

1. `main` is the only canonical branch.
2. A development branch is never a submission candidate merely because it contains later commits.
3. Future scientific or submission-package changes must branch from current `main`, pass the applicable verification gates, and be merged back to `main` before becoming canonical.
4. `audit/STAGE_14_SUBMISSION_QA.md` controls the Stage-14 verdict.
5. `audit/STAGE_14_JOURNAL_REQUIREMENTS_LEDGER.md` controls the known RIO requirements and portal-only uncertainties.
6. `paper/RIO_AUTHOR_INPUT_REQUIRED.md` records the resolved author/declaration facts despite its historical filename.
7. The historical development branches are provenance refs only; they must not be submitted or cited internally as a competing canonical state.

## Canonical submission materials

The submission-facing manuscript and package artifacts on `main` are governed by the Stage-14 QA records. The manuscript remains deliberately compatible with unresolved portal anonymity requirements until authenticated preflight determines the correct identification/file-designation treatment.


## Current-workflow retrofit checkpoint — 2026-10-05

The prospective v2.6 AI-accountability and v2.7 reviewer-verifiability retrofit was merged to canonical `main` through PR #4.

Retrofit merge checkpoint:

`b9728300b388f039e3b01a8f34c707b53499e5a2`

Canonical evidence added:
- `audit/AI_PROVENANCE_MATERIAL_USE_LOG.md`;
- `audit/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md`;
- `audit/CONTRIBUTION_ROBUSTNESS_CERTIFICATE.md`;
- `audit/REVIEWER_VERIFIABILITY_MAP.md`;
- `audit/REVIEWER_VERIFIABILITY_REPORT.md`;
- `audit/V2_6_V2_7_RETROFIT_2026-10-05.md`.

At that merge checkpoint, all three canonical CI workflows passed on `main`:
- Python verification — PASS;
- Manuscript smoke build / RIO package QA — PASS;
- Lean formal verification — PASS.

The retrofit changes evidence, exposition, QA, and CI governance only. It does not change the Stage-8 scientific theory freeze.

Current submission state remains:
- Stage 14: **CLOSED — CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED**;
- Stage 15: **READY FOR AUTHENTICATED PORTAL PREFLIGHT / NOT STARTED**;
- final Stage-15 AUTHOR sign-off must be tied to the exact frozen commit/PDF/package.
