# Stage 14 — Live RIO submission re-audit (2026-10-24)

**Paper:** *Global Equilibrium Corrections to Shy and Stenbacka (2005)*  
**Journal:** Review of Industrial Organization (RIO), Springer Nature  
**Stage-13 input:** commit `043670540dc7c84668e2e7e5900ea39ba41c7916`, draft PR #5  
**Stage-14 working branch:** `stage14-rio-submission-recheck-20261024`, stacked draft PR #6  
**Audit actors:** AI-side manuscript/source inspection; deterministic CI/PDF tooling; **not** external human peer review  
**Theory boundary:** Stage-8 frozen propositions, source assumptions, proof files, Lean statements, bibliography and the Figure 1 plotted numbers unchanged.

## 1. Evidence hierarchy / live official sources (accessed 2026-10-24)

- Level 3, journal-specific: https://link.springer.com/journal/11151/submission-guidelines
- Level 3, journal-specific costs/publishing: https://link.springer.com/journal/11151/how-to-publish-with-us
- Level 4, publisher: https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation
- Level 4, publisher: https://www.springernature.com/gp/policies/editorial-policies/using-ai-in-research

These pages were reopened for this revision; the 2026-09-20 ledger is historical evidence, not substituted for current rules. Authenticated journal portal instructions (evidence Level 2) are not available, and may override assumptions based on public pages.

## 2. Current journal requirements ledger

| Topic | Operative rule / verification against current candidate | Evidence level | Status |
| --- | --- | --- | --- |
| Journal and portal destination | RIO page routes to Springer Nature submission; portal login and exact form not opened | L3 | PASS for public destination; portal pending |
| Article category / correction vs research label | Must use actual selectable category; no public rule establishes exact portal label | L2 needed | UNVERIFIED — PORTAL ONLY |
| Anonymity and author identification | Public page asks for identified title page; review model and upload designation not unambiguously specified | L3; L2 needed | UNVERIFIED — PORTAL ONLY |
| Corresponding author, email, ORCID, affiliation | Populated in `paper/RIO_TITLE_PAGE.tex` from prior author-approved record; canonical `\author{}` preserved for reversible anonymity choice | L3; local evidence | PASS locally; portal mapping pending |
| Abstract | 150–250 words | L3; CI Stage-14 checker | PASS subject to final-head CI |
| Keywords and JEL | 4–6 keywords; appropriate JEL codes | L3; manuscript | PASS subject to final-head CI |
| Manuscript format | Mathematical paper may be submitted as LaTeX; editable source mandatory even at initial submission | L3; flat source builder | PASS subject to final-head CI |
| LaTeX folder structure | No subdirectories; submission source automatically compiled for approval | L3; isolated flat build | PASS locally subject to CI; portal compilation pending |
| Citations / DOI | Author-year, reference list of cited/accepted-published works, alphabetical; full DOI links if available | L3; BibTeX and project source ledger | PASS to project regression scope; no new citations introduced |
| Figure 1 and Table 1 | Number/caption/text references, black solid/dashed vector, legibility, embedded fonts, regenerated values | L3; generator + PDF | PASS at Stage-13 input; final-head CI/PDF to recheck |
| Figure caption | Fig. 1 convention and AI-assisted plotting-code disclosure where applicable | L3 + L4 | Stage-14 manuscript caption clarified; rebuild pending |
| AI use | Disclose material research-stage and manuscript-preparation assistance; record methods, provenance, human accountability, and verifiable figure inputs; AI not author | L3 + L4 | Stage-14 statement clarified; personal exact-package AUTHOR sign-off pending Stage 15 |
| Funding / conflicts / contribution | Manuscript statements and submission-interface contributions/conflicts must agree | L3 | PASS locally; portal fields pending |
| Data / code availability | Required data availability statement for original research; code and selected Lean scope accurately distinguished | L3 | PASS locally; exact links checked in PDF |
| Ethics/consent | No human/animal research asserted by this theoretical manuscript | L3 | NOT APPLICABLE as evidenced; portal attestations pending |
| Reviewer suggestions / cover letter | Suggested reviewers welcome and must be independent; exact portal count/mandatory letter not established publicly | L3; L2 needed | UNVERIFIED — PORTAL ONLY |
| Publishing route | Subscription model available without APC; optional OA APC on acceptance | L3 | PASS; publication choice later |
| Submission fees | No applicable submission-fee rule established by opened public pages | L2 needed | UNVERIFIED — PORTAL ONLY |
| Portal-generated PDF | Uploaded source must be compiled and author-approved | L3; L2 needed | UNVERIFIED — AUTHENTICATED PREFLIGHT |
| Originality / prior submission | No simultaneous submission; recorded author attestation is historical | L3; author record | AUTHOR must reconfirm for actual Stage-15 submission |

**Unverified items are not recoded as PASS.** The prior 2026-09-20 fee snapshot remains correct for the public publishing-options page on this access date (optional OA £2390/$3290/€2690 plus tax, price set upon acceptance).

## 3. Actual Stage-13 input package reviewed

- GitHub Actions, exact Stage-13 head `043670540dc7...`: Python verification run `40087265053` **SUCCESS**; manuscript workflow run `40087265052` **SUCCESS**.
- The workflow artifact `stage14-review-pdfs` (artifact ID `12557881403`, digest `sha256:46d4a49543ade457b3231954ddb7874a13c4d8a65c73084498b217a6a8eb99aa`) was downloaded and extracted independently.
- Canonical `manuscript.pdf` and isolated flat-build `rio_submission_build/manuscript.pdf`: **24 pages each**; extracted text identical; all PDF fonts embedded.
- Every page 1–24 was rendered for visual scanning: Figure 1 and Table 1 are present on page 8; proof appendix begins on page 14; Statements and Declarations span pages 21–22; references continue to page 24. No visually evident clipped text, equation spill, overlapping figure/table text, broken glyph or missing page was identified. PDF text blocks were also checked for text outside the horizontal print margins (none).
- No PDF placeholder `TODO`, `FIXME`, `[?]`, or literal `undefined` detected in extracted text.
- A newly added Stage-13 payoff-domain display fits within the page after the three-line reformulation. The 23 to 24 page change reflects additional mathematical exposition and reference pagination, not a broken build.
- The initial 24-page review predates the Stage-14 **disclosure-only** manuscript edits. **The exact Stage-14 head requires fresh CI and PDF visual QA before the non-portal close-out verdict.**

## 4. Stage-14 bounded repairs

1. Figure 1 caption, `paper/sections/03_best_responses.tex`: point readers to the Statements and Declarations disclosure of AI-assisted plotting-code development. **No figure data, plotted equations or curve styles changed.**
2. `paper/sections/07_reproducibility.tex`: separate material research-stage exploratory proof/exposition assistance from text drafting and clarify that Figure 1 comes from deterministic, exact-rational inputs, not prompt-to-image generation. Maintain the existing no-external-human claim and the narrow Lean-certificate boundary.
3. `audit/AI_PROVENANCE_MATERIAL_USE_LOG.md`: log this AI-side Stage-13/14 work and preserve actor taxonomy and pending exact-package author sign-off.

The source model, theorems, proof statements, bibliography, referee-facing numeric results, and figure/tabular data are unchanged.

## 5. AI disclosure reconciliation

| Material assistance | Evidence and verifying actor | Journal-facing location | Stage-14 finding |
| --- | --- | --- | --- |
| Manuscript structure, drafting, language and literature/source support | Prior provenance log; AI with author accountability | `Use of generative AI` in Statements and Declarations | Disclosed |
| Exploratory proof reconstruction and adversarial proof-exposition checks | Stage-13 re-audit, analytic proof source; AI + independently executed deterministic tools; selected FORMAL claims only | Same AI paragraph, proof and code availability limits | Explicitly distinguished |
| Python/TikZ graph-generation code assistance | Figure 1 exact-rational generator; Stage-10 regression; AI code support + COMPUTATION; author sign-off pending | Figure 1 caption plus main AI declaration | Explicitly distinguished |
| Final author review/approval of exact uploaded PDF and author responsibility | Historical author record; fresh exact-package approval not yet evidenced | RIO portal declarations and Stage 15 sign-off | **PENDING AUTHOR at Stage 15** |

Do not claim that all proofs were formally certified; only selected Lean mappings were. This audit is not author or external-human validation.

## 6. Stage-14 decision and next gate

**Provisional result until exact Stage-14-head rebuild:** compliant source/package design and 24-page Stage-13 input review. Re-run manuscript build, Python CI, extraction, exact 24/25-page PDF visual and figure-caption review after the Stage-14 edits. Only then consider **CLOSED / CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED**.

The full Stage-14 PASS is barred by (i) authenticated RIO article category, anonymity model, title-page/upload designations, declarations/reviewer/fee/cover-letter fields; (ii) portal-generated PDF review and approval; and (iii) exact-commit and package AUTHOR sign-off. The stacked draft PR must **not** be merged automatically or taken as a final submission.
