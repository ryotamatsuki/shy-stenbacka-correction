# Stage 14 — Final PDF Visual QA

Date: **2026-09-20**  
Target: **Review of Industrial Organization**  
Final manuscript-content head: `e08ea10c9ed50ba2b3be862806a41fbebf96128f`  
Stage-14 closure head reverified in CI: `d0ad03dd1c8c7da53405e6e27e3ea01c9c5fa731`

## Method

The CI-generated canonical PDF containing the final Introduction and bibliography was
downloaded from the successful Stage-14 workflow artifact for manuscript-content
head `e08ea10c9ed50ba2b3be862806a41fbebf96128f`, rendered at review resolution,
and inspected page by page.

The later Stage-14 closure commits changed only the Stage-13 verifier and
workflow/audit documentation. They did not change `paper/manuscript.tex`,
`paper/sections/`, `paper/references.bib`, the figure generator, or the flat
bundle generator. The closure head `d0ad03dd1c8c7da53405e6e27e3ea01c9c5fa731`
was nevertheless rebuilt independently in CI; both the canonical and flat RIO
PDFs contain **23 pages**.

## Result

Pages inspected: **23 / 23**.

Checks:

- first-page title, abstract, keywords, and JEL block: PASS;
- revised Introduction and new literature citations: PASS;
- text clipping: PASS;
- equation clipping: PASS;
- overlapping objects: PASS;
- broken/missing glyphs: PASS;
- hyperlink boxes: PASS / none visibly intrusive;
- Figure 1 presence and legibility: PASS;
- Table 1 presence and legibility: PASS;
- declaration placement: PASS;
- reference-page DOI display: PASS;
- reference continuation and alphabetical presentation: PASS;
- page numbering/order: PASS.

The Introduction/literature repositioning increased the manuscript from the
previous 22-page build to **23 pages**. The added page does not create any
visual or submission-package defect.

The closure-head manuscript workflow also reports:

- canonical manuscript build: PASS;
- flat RIO source build: PASS;
- Stage-14 non-portal submission QA: PASS;
- all fonts embedded in both PDFs;
- canonical PDF pages: 23;
- flat-package PDF pages: 23.

Residual non-fatal TeX box warnings, if emitted during intermediate passes, do
not produce visible clipping or readability impairment in the final PDF.

## Verdict

\[
\boxed{\textbf{PDF VISUAL QA — PASS}}
\]

This QA covers the final manuscript content. Authenticated portal-generated PDF
inspection remains a Stage-15 portal-preflight task under the canonical workflow.
