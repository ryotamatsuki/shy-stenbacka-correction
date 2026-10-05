# Material AI-Use Provenance Log

Status: **ACTIVE / RETROFIT COMPLETE THROUGH 2026-10-05**

Workflow authority:
- `research-paper-workflow` current main at `7d754032f292205264bd404116b561366836c7fd`
- prospective v2.6 AI provenance / human-accountability refinement
- `checklists/AI_PROVENANCE_AUTHOR_ACCOUNTABILITY_CHECKLIST.md`

## Governing rule

This log records material AI assistance by reference. It is not a transcript archive. Historical model identifiers are not guessed when they are not recoverable from repository evidence.

Verification actors are kept distinct:
- `AUTHOR`: the author personally accepts/reviews the research judgment or final manuscript;
- `AI`: an AI system performs drafting, search support, adversarial analysis, or a check;
- `COMPUTATION`: deterministic Python/SymPy or other executable checks;
- `FORMAL`: Lean/kernel verification of encoded statements;
- `EXTERNAL HUMAN`: none claimed in this repository.

A second AI pass is never classified as external human review.

## Material-use ledger

| Date / period | Tool / model | Purpose | Adopted artifact / decision | Verification actor(s) | Evidence / boundary |
|---|---|---|---|---|---|
| 2026-09-19 to 2026-09-20 | ChatGPT / historical model not reliably recoverable from repository | source reconstruction, mathematical audit, branch/corner discovery, theorem-scope attack | Stage 1–8 audit records, decision log, theorem certificates | AI + COMPUTATION + FORMAL; AUTHOR responsibility recorded separately | `audit/decision_log.md`; Stage 4A/7.5A records; Lean certificate. AI output is not itself proof. |
| 2026-09-19 to 2026-09-20 | ChatGPT / historical model not reliably recoverable | literature-search support and theorem-absorption/novelty attack | source-specific novelty boundary; generic novelty claims killed | AI; bibliographic claims source-checked in project ledgers | `audit/STAGE_06_NOVELTY_REKILL.md`; `audit/STAGE_11_KNOWN_MODEL_ATTACK.md` |
| 2026-09-19 to 2026-09-20 | ChatGPT / historical model not reliably recoverable | manuscript drafting, organization, proof exposition, code assistance | Stage 10/13 manuscript and reproducibility scripts | AI + COMPUTATION; AUTHOR final responsibility | `audit/STAGE_10_PAPER_CONSTRUCTION.md`; `audit/STAGE_13_FULL_PAPER_INTEGRATION.md` |
| 2026-09-20 | ChatGPT / historical model not reliably recoverable | adversarial clean-room re-audit | C7 cap-quantifier repair; C8 proof-completeness repair; multiplicity-mechanism narrowing | AI + COMPUTATION; no external-human claim | `audit/INDEPENDENT_AUDIT_REPAIR_LEDGER_2026-09-20.md`; downstream recertification records |
| 2026-09-24 | ChatGPT / historical model not reliably recoverable | exposition-streamlining retrofit | v2.5 exposition report; no theory change | AI; manuscript build/QA by COMPUTATION | `audit/EXPOSITION_STREAMLINING_V2_5_RETROFIT.md` |
| 2026-10-05 | ChatGPT, GPT-5.6 Sol | v2.6/v2.7 retrofit; reviewer-verifiability clean-room reconstruction; provenance/accountability hardening | this log, author-intellectual-contribution record, reviewer-verifiability map/report, QA script, disclosure clarification | AI + COMPUTATION; AUTHOR final responsibility; FORMAL scope unchanged | `audit/V2_6_V2_7_RETROFIT_2026-10-05.md` and linked artifacts |

## AI-audit independence record

The adversarial audits are **AI-side independent reviews**, not external peer review. Their value comes from using manuscript-facing or primitive-level objects and separate derivation/check paths where recorded. They do not establish AUTHOR verification and do not establish EXTERNAL HUMAN review.

The principal non-AI evidence layers are:
1. analytical derivations visible in the manuscript/appendix and audit records;
2. deterministic executable regression tests;
3. targeted Lean proof certificates for the mapped algebra/order core.

## Formal-verification boundary

Lean checks only the encoded statements and assumptions mapped in:
- `audit/stage075a_formal_statement_fidelity.md`;
- `audit/stage075a_formal_verification_certificate.md`.

Lean is not evidence of authorship, author understanding, novelty, empirical relevance, full equilibrium-domain completeness, or the unformalized model-to-theorem bridge.

## Author-accountability boundary

The project contains a prior author/declaration record stating sole-author approval and responsibility:
- `paper/RIO_AUTHOR_INPUT_REQUIRED.md`.

The central-result reasoning/accountability map is now separately preserved in:
- `audit/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md`.

Stage 15 must still obtain a final AUTHOR sign-off tied to the exact frozen commit, portal-generated PDF, and uploaded package. This requirement cannot be satisfied by AI or by repository CI.

## Disclosure reconciliation

The manuscript disclosure in `paper/sections/07_reproducibility.tex` has been revised so that:
- material ChatGPT uses are named;
- analytical, computational, and formal evidence are distinguished;
- AI/computation/formal checks are not described as external-human review;
- formal coverage is not overstated;
- final author responsibility remains explicit.

Verdict:

**PASS — MATERIAL AI USE IS PROVENANCE-TRACKED WITHOUT COLLAPSING VERIFICATION ACTORS.**
