# Stage 14 — Submission QA

Date: **2026-09-20**  
Target: **Review of Industrial Organization**  
Entry state: Stage 13 repaired and recertified  
Stage 14 status: **IN PROGRESS — NON-PORTAL QA IMPLEMENTED**

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

## 8. Provisional verdict

Full Stage-14 PASS is prohibited while material author facts and authenticated portal fields remain unresolved.

The intended closure state, if all automated non-portal checks are green, is:

[
oxed{	extbf{CONDITIONAL PASS — AUTHOR METADATA / DECLARATIONS AND AUTHENTICATED PORTAL PREFLIGHT REQUIRED}}
]

Stage 15 must not freeze or submit until these remaining non-substantive inputs are supplied and the authenticated portal-generated PDF is inspected.
