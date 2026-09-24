# Stage 13 — Independent-Audit Repair Reintegration

Date: **2026-09-20**  
Original Stage-13 checkpoint: `5bdf156347da4267167513d96b5ef53456cd3f9a`  
Primary journal: **Review of Industrial Organization**

## 1. Reopening

Stage 13 was reopened after the independent clean-room audit identified three material defects in the integrated manuscript/audit chain:

1. C7 cap quantifier;
2. C8 proof completeness;
3. multiplicity mechanism interpretation.

The original Stage-13 PASS is preserved as historical provenance and is superseded by this repair/reintegration record.

## 2. Mathematical reintegration

The manuscript now incorporates the amended certified theory:

- Proposition 2 distinguishes the uncapped response (R) from the source-domain response (B_phi), states the exact strict cap thresholds for a nondegenerate (+2) segment, and retains the large-cap counterexample to the source's global strategic-substitutes claim;
- Proposition 3's five-case equilibrium set is unchanged, but the Appendix contains a complete analytic exclusion proof;
- (ho=2/3,phi=delta/2) is labeled a singleton, not a continuum;
- the all-active multiplicity example separates C8 multiplicity from the C7 exit mechanism;
- Cournot continuation existence/global concavity proofs include the missing global arguments;
- literal Hotelling is explicitly a maintained full-coverage clipped-demand continuation, with price-domain and no-uncovered-demand boundaries stated;
- the no-loss theorem uses (x_-) only on its real domain and proves the iff/tie cases;
- reduced welfare notation and knife-edge welfare scope are explicit;
- the conclusion separates the sign correction from the active-set/corner corrections.

## 3. Literature / prose / bibliography reintegration

The manuscript now:

- specifies the relevant König marginal-cost-saving/reversed specification;
- distinguishes the Amir/AGK/AHJ/Buehler mechanisms from the exact source result without claiming exit is necessary for multiplicity;
- uses Gill--Thanassoulis only as contextual evidence for a no-below-cost restriction in a different pricing model;
- uses Vogel only as general heterogeneous-cost spatial-competition context;
- retains Dai (2026) as a distinct make-or-buy/supplier-investment mechanism;
- uses corrected König accents in the bibliography;
- uses an author-year bibliography style consistent with the Stage-13 RIO integration record.

The detailed source ledger is `audit/LITERATURE_CLAIM_RECHECK_2026-09-20.md`.

## 4. Verification architecture

The repair adds/uses:

- `code/independent_audit_repair_verify.py`;
- `code/stage11_hostile_referee_verify.py`;
- `code/stage13_integration_verify.py`;
- the existing formal build, without changing the certified Lean source;
- canonical manuscript build;
- generated flat RIO bundle build.

The independent repair verifier reconstructs primitive Cournot continuations rather than importing the production best-response function.

## 5. Formal statement alignment

No formal source is changed.  C7's Lean proof remains a certificate of algebraic joins and slope positivity only; it does not certify cap feasibility.  C8 remains analytically certified.  The manuscript continues to state that the complete economic model/global equilibrium construction is not formally mechanized.

## 6. Final verification and visual inspection

The repaired manuscript passed the final integrated checks.

Latest substantive verification head before closure-record-only commits:

\`0bd82c56703655f0a72784b4ef8f964520875cdc\`.

Green evidence:

- Python verification PR run \`35477505973\` — **success**;
- canonical manuscript + flat RIO bundle build PR run \`35477505977\` — **success**;
- hyperlink-clean PDF build push run \`35477441567\` — **success**.

The generated canonical PDF was downloaded from the CI artifact, rendered to PNG at 140 dpi, and visually inspected page by page. The final manuscript is **22 pages**. No clipped text, overlaps, broken glyphs, missing figure/table content, or visible hyperlink boxes were found. The flat RIO PDF is built from the same canonical content through the Stage-13 bundle generator.

The visual pass also triggered one local presentation repair: \`hyperref\` was changed to \`hidelinks\` so colored link boxes do not appear in the submission PDF.

## 7. Finding disposition

- F01 C7 cap quantifier — **RESOLVED**.
- F02 C8 completeness proof — **RESOLVED**.
- F03 exit/multiplicity mechanism — **RESOLVED**.
- F04--F10 proof/boundary/notation/interpretation findings — **RESOLVED**.
- F11 bibliography/style-record inconsistency — **RESOLVED**.
- literature verification finding — **RESOLVED WITH EXPLICIT EVIDENCE LIMITATION**; no inaccessible source was silently promoted to fresh full-text verification.
- formal-verification scope — **RECONCILED; no Lean theorem or source change required**.

## 8. Final Stage-13 verdict

\[
\boxed{\textbf{REPAIRED AND RECERTIFIED}}
\]

\[
\boxed{\textbf{STAGE 13 — PASS / INTEGRATED MANUSCRIPT RECERTIFIED}}
\]

The original Stage-13 checkpoint remains historical provenance; this repair record is the controlling closure.

Stage 14 was **not started**. The next canonical stage is Stage 14 only when separately authorized.
