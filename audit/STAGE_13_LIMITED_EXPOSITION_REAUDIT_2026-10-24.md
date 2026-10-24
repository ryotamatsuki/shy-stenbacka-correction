# Stage 13 limited re-audit — exposition and proof bridges

Date: 2026-10-24  
Paper: *Global Equilibrium Corrections to Shy and Stenbacka (2005)*  
Scope: **limited Stage 13** on the manuscript-facing presentation; not a substantive Stage 4, 7.5A, or 8 reopening.  
Workflow: `ryotamatsuki/research-paper-workflow`, `EXPOSITION_STREAMLINING_CHECKLIST.md` and `REVIEWER_VERIFIABILITY_CHECKLIST.md` (prospective v2.7+; workflow v2.9 as currently applicable).  
Review actor: **AI-side independent proof-exposition read**, not human peer review.

## 1. Non-negotiable boundary

The following remain unchanged:

- published-model primitives, source bounds, price strategy domains, source SOC, and all theorems/lemmas;
- the corrected equation-(14)/Proposition-3 sign and the integer-market-size qualification;
- Proposition 5's **existential and sourcing-cap-qualified** counterexample;
- the **pure** Stage-I duopoly correspondence, including the knife edge and both-active multiplicity;
- the literal Hotelling price-continuation multiplicity and **separate** auxiliary `p_j >= c_j` restriction;
- welfare/selection limitations, novelty boundary, and formal-verification scope.

The Lean certificate `ShyStenbackaFormal/Stage075A.lean` has identical Git blob SHA (`a634b04eb2ec13a632f10928974f8eab96d1d05c`) on `main` and this branch. **No claim of a fresh Lean execution is made.**

## 2. Section-role and compression audit

Profile: **CORRECTION / COMMENT / REASSESSMENT**.

| Integrated section / item | Role | Stage-13 decision |
| --- | --- | --- |
| Abstract and Introduction | CORE | Retain immediate source result, exact correction, and scope. Clarify that Cournot is the principal correction and Hotelling a separate diagnosis. Do not remove source-equation identification or cap qualification. |
| Model / strategy spaces | CORE | Preserve the published sourcing bounds and literal versus auxiliary price domains. Shorten one overfull introductory sentence without altering assumptions. |
| Cournot continuation and symmetric comparison | CORE | Preserve potential, global concavity, unilateral FOC, integer-`N` distinction, and source-equation link. Shorten the equation-(14) explanation. |
| Duopoly response and equilibrium correspondence | CORE | Retain all cases and boundaries. State each payoff branch's explicit domain and add a proof roadmap. |
| Hotelling / auxiliary no-loss analysis | CORE | Retain literal-game versus restricted-game distinction. Add a two-line inequality bridge for the no-loss threshold proof. |
| Welfare and limitation section | CORE (scope) | No deletion: equilibrium-selection caveat is material. |
| Related literature | HELPFUL | Retain calibrated source-specific positioning; do not broaden novelty. No substantive edit. |
| Conclusion / reproducibility | HELPFUL/CORE (respectively) | No new theorem claims or formal-certification inflation. |
| Appendix | APPENDIX (proof-critical) | Preserve exhaustive branches and add reviewer-facing intermediate equations. |
| Figure 1 and Table 1 | CORE | Retain both; source-model global-response geometry and complete pure-regime classification cannot be replaced by a generic visual. |

**Introduction compression / section purity:** The contribution appears before the section guide, and the model and main results precede literature and secondary context. The narrow correction warrants keeping the relevant source proposition, formula, and qualifications visible rather than deleting them solely to save lines. No model, proof, literature or reproducibility material was moved into an inappropriate section.

**Reader arrival / exhibits:** The last independently compiled PR package was **23 pages** in both canonical and flat forms; the Introduction starts on page 1, model follows immediately, global Cournot section is reached near page 4, equilibrium classification near page 7–8, and technical proof details are in the Appendix. Only **one main-text figure and one table** are used, passing the five-exhibit scarcity test. An exact post-final-edit pagination/visual review belongs to Stage 14.

## 3. Reviewer reconstruction, by headline claim

| Claim | Reader-visible proof chain | Verdict |
| --- | --- | --- |
| Global Cournot continuation | nonnegative quantities → exact strictly concave, coercive potential → KKT conditions → active-set price/output | PASS |
| Global own-sourcing concavity | active-set curvature → own-entry derivative continuity → only downward marginal-benefit jumps on rival exit → global strict concavity | PASS |
| Corrected symmetric outsourcing | symmetric Cournot output → unilateral sourcing FOC → root and source SOC → capped action → explicit derivative sign → integer-`N` scope | PASS |
| Global source-duopoly best response | both-active quantity equations → payoff branches **and their exact `x` domains** → stationary `A(y), M` and rival-exit boundary `U(y)` → joins and global concavity → cap-survival test | PASS after bridge addition |
| Pure Stage-I correspondence | mutual response system → contraction above `2/3` → clipped affine knife edge → crossing property below `2/3` → exhaustive ordered asymmetric split at `x_H=delta` | PASS after roadmap |
| Literal Hotelling corner family | clipped share → literal pure-price best response → complete mutual response interval → set-valued off-path payoff | PASS, unchanged |
| No-loss Hotelling cap threshold | separate restricted-game continuation → full-market gain quadratic → vertex and two roots → explicit strictly positive squared comparison on `27/2 < lambda < 18` → feasible-cap condition | PASS after bridge addition |

The Hotelling comparison uses
```text
(2 - 18/lambda)^2 - 2(2*lambda - 27)/lambda
 = 18*(18 - lambda)/lambda^2 > 0
```
and only squares after verifying that both compared sides are positive on the stated interval. The identity and the response join identities `A(y_A)=U(y_A)`, `M=U(y_M)` were checked independently with SymPy.

**Residual proof-critical bridge gaps:** None identified within the limited changes. This is a readability/reviewer-verifiability finding, not an independent recertification of all economic theorems.

## 4. Scope and regression safeguards

The edited manuscript still distinguishes: global versus local response, all-active versus exited rival, cap binding versus interior choice, symmetric action versus all general-`N` equilibria, pure versus mixed strategies, literal versus auxiliary Hotelling games, and equality versus strict failure. No symbols, theorem statements, assumptions, figures, tables, bibliography entries, Lean source, or regression scripts were changed.

## 5. Verification evidence and boundaries

On initial PR revision `82b1bac19d1d3ee10c440833fbedf5c6c8d6d354`:

- **Python verification:** GitHub Actions run `40086593856`, success. Source-model, Stage 4/4A/7/7.5A/10/11, independent-repair, Stage 13, and non-portal Stage 14 checks passed.
- **Manuscript smoke build:** run `40086593849`, success. Canonical and flat RIO PDFs compiled; both report **23 pages**, with embedded fonts. The non-portal submission-package check passed.
- The source code has since received additional **exposition-only** edits to specify exact payoff domains, add a proof roadmap, and alleviate source-model prose overfull boxes. The prior green checks are **not** represented as post-edit validation; review the latest PR-head CI before merge.
- A full PDF page-by-page visual proofread, fresh Lean execution, publisher portal login, author metadata completion, and final Stage-14 submission certification are **not** part of this limited Stage 13 exercise.

## 6. Decision

**PASS — LIMITED STAGE-13 EXPOSITION AND REVIEWER-VERIFIABILITY RE-AUDIT (SOURCE REVIEW).**

The former proof-exposition gaps have specific manuscript repairs. No rollback to the frozen mathematical stages is indicated. This PASS does not override the separate CI-on-final-HEAD, visual-PDF, and authenticated Stage-14/15 submission gates. Leave the PR in **Draft** until its final-head automated build is green and the remaining submission checks are completed.
