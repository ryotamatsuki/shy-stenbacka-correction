# Stage 12 — Initial Journal Requirements Ledger
## Primary target: Review of Industrial Organization

Status: **INITIAL LEDGER — STAGE 12 / RECHECKED IN v2.3 RE-AUDIT**  
Access date: **2026-09-20**  
Re-audit workflow commit: `9eb616bd31ea3a9ef3c29e288228ed962c44c9cf`  
Journal: **Review of Industrial Organization (RIO)**  
Publisher: Springer Nature  
Journal URL: https://link.springer.com/journal/11151  
Aims/scope: https://link.springer.com/journal/11151/aims-and-scope  
Submission guidelines: https://link.springer.com/journal/11151/submission-guidelines  
Publishing options: https://link.springer.com/journal/11151/how-to-publish-with-us

This ledger is the initial Stage-12 requirements baseline. It was rechecked on 2026-09-20 during the v2.3 candidate-universe re-audit after RIO remained the selected primary journal. No public requirement discovered in that re-audit changed the Stage-13 packaging contract. Stage 14 must still re-open the live official pages and the authenticated submission portal before SUBMISSION QA PASS.

## 1. Article category / scope

| Requirement | Stage-12 status | Evidence / action |
|---|---|---|
| Field fit | **VERIFIED** | RIO covers all aspects of industrial organization; competition, monopoly, efficiency, innovation, and internal organization are core topics. |
| Theory accepted | **VERIFIED** | Aims/scope explicitly states that RIO seeks papers that advance significant theories of industrial organization and policy. |
| Shorter notes/commentaries | **VERIFIED** | Aims/scope explicitly welcomes shorter notes and commentaries. |
| Exact portal article-type label | **UNVERIFIED / PORTAL-ONLY** | Recent papers are labelled `OriginalPaper`; the portal's selectable category for this manuscript must be checked at Stage 14. |
| Current manuscript length | **FIT EVIDENCE, NOT A RULE** | Current compiled manuscript is 15 pages. August 2026 RIO issue contains theory papers of 12–21 pages; no public maximum page limit was located. |

## 2. Review / anonymity

| Requirement | Stage-12 status | Evidence / action |
|---|---|---|
| Single vs double anonymized review | **UNVERIFIED** | Journal-specific public instructions reviewed at Stage 12 do not unambiguously specify the review model. Do not infer from publisher-wide defaults. Check authenticated portal / current editorial policy at Stage 14. |
| Reviewer suggestions | **VERIFIED** | Authors may suggest reviewers and exclusions; suggested reviewers should be independent. Institutional email is required where possible, or another identity-verification link/ID. |
| Number of reviewer suggestions required | **UNVERIFIED / PORTAL-ONLY** | Check portal. |
| Cover letter required | **UNVERIFIED / PORTAL-ONLY** | Check portal. |

## 3. Title page / author metadata

| Requirement | Stage-12 status | Evidence / action |
|---|---|---|
| Concise/informative title | **VERIFIED** | Required by official guidelines. |
| Author names | **VERIFIED REQUIREMENT / AUTHOR INPUT REQUIRED** | Current repository manuscript has an empty author field. |
| Affiliations, city/state/country | **VERIFIED REQUIREMENT / AUTHOR INPUT REQUIRED** | Required on title page. |
| Corresponding author active email | **VERIFIED REQUIREMENT / AUTHOR INPUT REQUIRED** | Required. |
| ORCID | **OPTIONAL IF AVAILABLE** | Official guidelines request ORCID if available. |
| Acknowledgments | **VERIFIED** | Separate section on title page; funding organizations written in full. |

## 4. Initial submission files / LaTeX

| Requirement | Stage-12 status | Evidence / action |
|---|---|---|
| Editable source files at every submission/revision | **VERIFIED** | Complete editable source set required; incomplete source set may prevent review. |
| LaTeX allowed | **VERIFIED** | Mathematical manuscripts may be submitted in LaTeX. |
| Springer Nature LaTeX template | **RECOMMENDED, NOT MANDATORY ON PUBLIC PAGE** | Stage 13 should create a journal-specific submission source without changing canonical theory. |
| LaTeX subfolders | **PROHIBITED** | Official guidelines: do not use subfolders for figures or bibliography files. |
| Current repo compatibility | **REQUIRES PRESENTATION BUILD STEP** | Canonical source uses `paper/sections/` and `paper/generated/`. Stage 13 should create a flat RIO submission bundle while leaving canonical research source intact. |
| Portal-generated PDF | **VERIFIED** | Uploaded source files are automatically compiled into a single PDF for author approval. |

## 5. Abstract / indexing / formatting

| Requirement | Stage-12 status | Evidence / action |
|---|---|---|
| Abstract | **VERIFIED** | 150–250 words; no undefined abbreviations or unspecified references. |
| Keywords | **VERIFIED** | 4–6 keywords. |
| JEL codes | **VERIFIED** | Appropriate JEL codes required. |
| Section headings | **VERIFIED** | Decimal heading system, no more than three levels. |
| Page/word limit | **NO PUBLIC LIMIT LOCATED / RECHECK** | No explicit maximum found in current public RIO instructions; Stage 14 must re-check. |
| Highlights | **NO PUBLIC REQUIREMENT LOCATED / RECHECK** | Portal may differ. |
| Graphical abstract | **NO PUBLIC REQUIREMENT LOCATED / RECHECK** | Portal may differ. |

## 6. References

| Requirement | Stage-12 status | Evidence / action |
|---|---|---|
| In-text style | **VERIFIED** | Author-year citation style. |
| Reference list | **VERIFIED** | Only cited published/accepted works; alphabetized. |
| DOI | **VERIFIED** | Full DOI links encouraged where available. |
| Recent RIO make-or-buy paper | **STAGE-13 LITERATURE ACTION** | Add and position Chifeng Dai (2026), “A New Strategic Element to the Make-or-Buy Decision,” without changing novelty claims. It is directly relevant to RIO's sourcing audience but uses a distinct mechanism. |

## 7. Figures / tables

| Requirement | Stage-12 status | Evidence / action |
|---|---|---|
| Electronic figures | **VERIFIED** | Required. |
| Vector graphics | **VERIFIED** | EPS preferred for vector graphics; fonts embedded. |
| Line-art resolution if bitmap | **VERIFIED** | 1200 dpi minimum. |
| Figure captions | **VERIFIED** | Descriptive captions in manuscript text. |
| Accessibility | **VERIFIED** | Descriptive captions; patterns in addition to color; adequate lettering contrast. |
| Current Stage-10 figure | **PRESENTATION CONVERSION REQUIRED** | Current figure is generated TikZ. Stage 13 should decide whether to retain inline TikZ or generate an EPS-compatible vector artifact for the flat submission package, then Stage 14 re-check portal compilation. |

## 8. Data / code / supplementary material

| Requirement | Stage-12 status | Evidence / action |
|---|---|---|
| Data Availability Statement | **VERIFIED — REQUIRED** | All original research must include one. |
| Research-data repository | **STRONGLY ENCOURAGED** | Official guidelines encourage public repository deposit. |
| This theory paper | **STAGE-13 ACTION** | Use a truthful statement that no empirical datasets were generated/analysed and identify the public verification-code repository, subject to Stage-14 wording re-check. |
| Supplementary files | **VERIFIED — ALLOWED** | Standard formats accepted; text/presentations as PDF, spreadsheets as CSV/XLSX; online resources should be cited appropriately. |
| Code availability statement | **SUPPORTED / PRESENTATION ACTION** | Include repository provenance consistently with the existing reproducibility package. |

## 9. Declarations

| Requirement | Stage-12 status | Evidence / action |
|---|---|---|
| Competing interests | **VERIFIED — REQUIRED** | Financial and non-financial interests must be disclosed. |
| Funding | **VERIFIED — DISCLOSE STATUS** | Funding information belongs in declarations and submission system. Exact author funding status: **AUTHOR INPUT REQUIRED**. |
| Author contributions | **VERIFIED — SUBMISSION INTERFACE REQUIRES INFORMATION** | Exact contribution statement: **AUTHOR INPUT REQUIRED**. |
| Ethics / consent | **LIKELY NOT APPLICABLE, DO NOT ASSUME** | Theory paper has no human/animal data in current manuscript; portal fields still must be checked. |
| Acknowledgments | **VERIFIED** | Put on title page. |
| Generative AI / LLM use | **VERIFIED POLICY; DISCLOSURE REQUIRED FOR THIS PROJECT** | RIO guidelines state that LLM use beyond AI-assisted copyediting should be documented in Methods or another suitable section. This project used substantive LLM assistance, so Stage 13 must prepare a disclosure with human accountability. Exact wording must be checked again at Stage 14. |
| LLM authorship | **PROHIBITED** | LLMs do not meet authorship criteria. |

## 10. Preprints / prior publication

| Requirement | Stage-12 status | Evidence / action |
|---|---|---|
| Manuscript not published / not simultaneously under review | **VERIFIED** | Explicit official submission condition. |
| Preprint policy | **PROVISIONAL — PUBLISHER-WIDE** | Springer Nature generally permits preprints, but the exact journal/portal rule must be re-checked at Stage 14 before posting or relying on it. |

## 11. Fees / access

| Requirement | Stage-12 status | Evidence / action |
|---|---|---|
| Publishing model | **VERIFIED** | Hybrid. |
| Subscription route APC | **VERIFIED: NO APC** | Official page states no APC under subscription publishing. |
| Optional OA APC | **VERIFIED SNAPSHOT** | £2390 / US$3290 / €2690, plus applicable taxes; price determined at acceptance and must be re-checked then. |
| Submission fee | **NO PUBLIC FEE LOCATED / RECHECK PORTAL** | Do not infer zero until portal is inspected. |

## 12. Unverified / author-input items carried to Stage 13–14

1. Exact submission article-type/category label.
2. Review anonymity model.
3. Required number of suggested reviewers and exclusion fields.
4. Whether a cover letter is a mandatory portal field.
5. Any portal-only file naming or source-archive rules beyond the public no-subfolder rule.
6. Any portal-specific abstract/keyword/JEL field limits beyond public instructions.
7. Current author names, affiliations, corresponding-author email, ORCID.
8. Funding status, competing-interest status, author-contribution wording.
9. Exact generative-AI disclosure wording/placement for the actual submission.
10. Exact current preprint rule as applied by RIO.
11. Any submission fee or portal charge not shown on the public pages.
12. Current artwork handling of generated TikZ vs EPS within portal compilation.

## 13. Stage-12 ledger verdict

The public rules reveal no submission-format blocker that requires a theory change. The only material source-layout incompatibility is the no-subfolder LaTeX rule, which is solvable by a flat Stage-13 submission bundle.

[
\boxed{\textbf{RIO REQUIREMENTS BASELINE ESTABLISHED}}
]
