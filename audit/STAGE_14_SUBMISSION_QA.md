# Stage 14 — Submission QA

Date: **2026-09-20**  
Target: **Review of Industrial Organization**  
Entry state: Stage 13 repaired and recertified  
Stage 14 status: **CONDITIONAL PASS — AUTHOR INPUT + AUTHENTICATED PORTAL PREFLIGHT REQUIRED**

## 1. Live requirements refresh

Current official RIO instructions were re-opened on 2026-09-20 rather than relying on the Stage-12 snapshot.

Controlling public evidence:

- https://link.springer.com/journal/11151/submission-guidelines
- https://link.springer.com/journal/11151/how-to-publish-with-us
- https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation

Current requirements are itemized in:

`audit/STAGE_14_JOURNAL_REQUIREMENTS_LEDGER.md`.

## 2. Stage-14 local compliance repairs

Bounded package/format changes only:

- known Data / Code / AI statements moved under the required `Statements and Declarations` heading;
- figure caption label configured as `Fig. 1` without a punctuation separator;
- terminal caption punctuation removed;
- author-specific facts isolated in `paper/RIO_AUTHOR_INPUT_REQUIRED.md` rather than guessed;
- Stage-14 automated source/package/font QA added.

No theory, proof, result, literature interpretation, or journal-positioning claim changed.

## 3. Automated QA

New verifier:

`code/stage14_submission_qa.py`.

It checks:

- 150–250 word abstract;
- 4–6 keywords;
- valid JEL-code format;
- author-year bibliography style;
- Statements and Declarations / Data / Code / AI sections;
- figure caption and black solid/dashed accessibility controls;
- all citation keys and no uncited bibliography entries;
- DOI-bearing BibTeX records include full `https://doi.org/...` URLs;
- no manuscript placeholders;
- explicit author-input blocker remains visible;
- exact flat bundle contains no subdirectories or stale `sections/` / `generated/` paths;
- flat bundle includes all manuscript sections, bibliography, figure source, and compiled PDF.

The manuscript CI additionally checks final PDF font embedding with `pdffonts` and records PDF page counts.

## 4. Artwork QA

Figure 1 is black-and-white vector TikZ/PGF source generated from exact rational inputs.

- distinct series use solid vs dashed line style, not color;
- the caption describes the object and marked equilibria;
- the generator is retained at `code/stage10_generate_figure.py`;
- the figure remains in the manuscript body;
- vector/font embedding is checked on the compiled PDF in CI.

No raster-resolution requirement applies to the retained vector source.

## 5. Formal verification

No Lean theorem, source file, toolchain, or dependency changed during the independent-audit repair or Stage 14.

The formal blobs remain those reconciled at Stage 7.5A. The current manuscript still describes Lean as selected proof-critical formalization only. A whole-model formal-verification claim is prohibited.

The most recent clean formal build remains the frozen formal-verification run `35439005968`; because the formal source is byte-identical, Stage 14 does not manufacture a new formal certificate by changing the formal files merely to trigger CI.

## 6. Author/declaration blocker

The public RIO instructions require author names, affiliations, corresponding-author email, and disclosure facts. The repository has no authoritative current values for these facts.

Therefore Stage 14 will not insert guessed:

- author identity/order;
- affiliation;
- email/ORCID;
- funding;
- competing interests;
- author contributions;
- acknowledgments;
- prior-publication/simultaneous-submission attestation.

These inputs are listed in `paper/RIO_AUTHOR_INPUT_REQUIRED.md`.

## 7. Authenticated portal blocker

The public journal page links to the Springer Nature submission portal, but the authenticated submission workflow cannot be inspected in the current environment.

The following remain portal-only:

- exact article type/category label;
- review/anonymity model;
- separate-title-page designation if any;
- exact source/figure/supplement file designations;
- required number of reviewer suggestions;
- mandatory cover-letter field if any;
- portal-only fee/attestation fields;
- generated submission PDF.

## 8. Defects found and repaired during Stage 14

Stage 14 found several real submission-package defects rather than merely checking boxes:

1. three uncited bibliography entries remained in \`references.bib\`; they were removed because RIO states that the reference list should contain only cited works;
2. the flat source directory was initially also used as the LaTeX build directory, contaminating the upload candidate with generated \`.aux/.log/.bbl/PDF\` files; the source-only upload directory and isolated build directory are now separate;
3. DOI notes contained a doubled LaTeX escape that rendered visibly as \`urlhttps://doi.org/...\`; all DOI links now render correctly and the Stage-14 verifier permanently rejects the doubled escape;
4. the first font-embedding CI check parsed the wrong \`pdffonts\` column; inspection showed that fonts were actually embedded, and the check was repaired to use the stable column position relative to the end of each row;
5. the public RIO figure-caption convention and \`Statements and Declarations\` heading were implemented;
6. citation-dense prose producing a large overfull warning was reflowed without changing its substantive literature claims.

These are packaging/presentation repairs only. No mathematical statement, proof, novelty claim, or journal-positioning decision was changed.

## 9. Final non-portal verification evidence

Final technical head:

\`446ce7bdf7eff1d2363a315c905c28572c91861a\`.

Green runs:

- Python verification PR run \`35478726461\` — **PASS**;
- Python verification push run \`35478726286\` — **PASS**;
- manuscript / flat-package / Stage-14 QA run \`35478726453\` — **PASS**.

The manuscript workflow records:

- canonical manuscript build — PASS;
- flat RIO source build in an isolated output directory — PASS;
- \`Stage-14 non-portal submission QA PASS\`;
- source-only flat bundle with 13 expected files, no subdirectories and no build artifacts;
- all fonts embedded in both canonical and flat-package PDFs;
- canonical PDF pages: **22**;
- flat-package PDF pages: **22**.

The final-head artifact is \`stage14-review-pdfs\` from run \`35478726453\`.

## 10. PDF visual QA

The DOI-fixed final manuscript was rendered page by page and all **22 pages** were visually inspected.

Result:

- no clipped text;
- no overlapping text or equations;
- no broken glyphs or black squares;
- Figure 1 present and legible;
- Table 1 present and legible;
- no visible hyperlink boxes;
- Statements and Declarations appear immediately before the references;
- DOI links display as \`https://doi.org/...\`, not \`urlhttps://...\`;
- no visually material margin overflow despite residual non-fatal TeX box warnings.

The final-head PDF from \`446ce7b...\` was render-compared against the visually inspected DOI-fixed PDF. The comparison reports **22/22 pages identical, changed_pages = 0**.

## 11. Material blockers that prevent full Stage-14 PASS

### Author/title-page/declaration input

The current source intentionally retains \`\\author{}\`. RIO's current public instructions require the author name(s), affiliation(s), city/state/country, corresponding-author active email, and ORCID if available. Funding, competing interests, contribution information, acknowledgments where applicable, author approval, and prior-publication/simultaneous-submission facts also require authoritative human input.

These facts are enumerated in:

\`paper/RIO_AUTHOR_INPUT_REQUIRED.md\`.

They are not inferred from repository metadata, account information, or memory.

### Authenticated portal preflight

The following remain unavailable from the public instructions alone:

- exact selectable article-type label;
- review/anonymity model;
- separate title-page/file designation;
- exact upload labels/archive behavior;
- reviewer-suggestion count/fields;
- whether a cover-letter file is mandatory for this submission;
- any portal-only submission fee/attestation;
- portal-generated PDF and its final source compilation.

If the portal uses double-anonymous review, the author block and the public repository URL in the Code availability statement may require journal-specific anonymization treatment. That cannot be decided safely until the review model is known.

## 12. Stage-14 verdict

All repository-resolvable and public-rule-resolvable Stage-14 checks are green. Full \`SUBMISSION QA PASS\` is nevertheless prohibited because material author facts and authenticated portal fields remain unresolved.

\[
\boxed{\textbf{CONDITIONAL PASS — AUTHOR INPUT + AUTHENTICATED PORTAL PREFLIGHT REQUIRED}}
\]

This is a non-substantive submission-administration block. No rollback to the mathematical stages is triggered.

## 13. Stage-15 routing

\[
\boxed{\textbf{STAGE 15 — BLOCKED / NOT STARTED}}
\]

Stage 15 may begin only after:

1. authoritative author/title-page and declaration facts are supplied;
2. those facts are integrated without contradicting the review model;
3. the authenticated RIO portal is preflighted;
4. the portal-generated PDF is inspected;
5. the Stage-14 ledger is promoted from conditional to full PASS.

No submission action has been taken.
