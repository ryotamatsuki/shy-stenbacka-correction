# Shy–Stenbacka Correction

Reproducible correction and adversarial equilibrium audit of Shy & Stenbacka (2005).

## Canonical status

\[
\boxed{\textbf{STAGE 4 — PASS (AMENDED)}}
\]

\[
\boxed{\textbf{STAGE 4A — PASS (AMENDED / RECERTIFIED)}}
\]

\[
\boxed{\textbf{STAGE 6 — PASS (RECHECKED)}}
\]

\[
\boxed{\textbf{STAGE 7 — PASS}}
\]

\[
\boxed{\textbf{STAGE 7.5 — PASS}}
\]

\[
\boxed{\textbf{STAGE 7.5A — PASS (RECONCILED)}}
\]

\[
\boxed{\textbf{STAGE 8 — PASS / THEORY FROZEN AS AMENDED}}
\]

\[
\boxed{\textbf{STAGE 9 — PASS / REPRODUCIBILITY SETUP COMPLETE}}
\]

\[
\boxed{\textbf{STAGE 10 — PASS / MANUSCRIPT CONSTRUCTION COMPLETE}}
\]

\[
\boxed{\textbf{STAGE 11 — PASS / RECERTIFIED ROBUSTNESS GATE CLOSED}}
\]

\[
\boxed{\textbf{STAGE 12 — PASS / PRIMARY JOURNAL SELECTED}}
\]

\[
\boxed{\textbf{STAGE 13 — PASS / REPAIRED AND RECERTIFIED}}
\]

\[
\boxed{\textbf{STAGE 14 — CONDITIONAL PASS / AUTHOR INPUT + PORTAL PREFLIGHT REQUIRED}}
\]

\[
\boxed{\textbf{STAGE 15 — BLOCKED / NOT STARTED}}
\]

Workflow provenance: Stages 0–11 remain governed by \`research-paper-workflow\` v2.2 at \`42574d6c5931275ccff3ef7e8b4acc188077332a\`. Stage 12 was re-audited and Stage 13 integrated under the backward-compatible v2.3 workflow state at \`9eb616bd31ea3a9ef3c29e288228ed962c44c9cf\`.

## Canonical architecture

\[
\boxed{\textbf{HYBRID}}
\]

### Main source-faithful Cournot block

- complete nonnegative-quantity continuation;
- global own-payoff concavity under the source SOC;
- corrected capped symmetric action;
- equation-(14)/Proposition-3 sign reversal;
- Proposition-5 global failure;
- complete pure source-duopoly Stage-I equilibrium classification.

### Secondary Hotelling block

**Maintained literal full-coverage interpretation:** sufficiently asymmetric costs generate multiple pure corner price continuations, so the published interior backward induction is incomplete off path under the clipped full-coverage continuation.

**No-loss robustness model:** under the explicit auxiliary strategy restriction

\[
p_j\ge c_j,
\]

the pure price continuation is unique and Proposition 6 fails on an exact cap-aware parameter region.

This restriction is not attributed to Shy–Stenbacka and is not described as elimination of all weakly dominated strategies. Stage 4A proved that although every \(p<c\) is weakly dominated by \(p=c\), the action \(p=c\) itself is weakly dominated by any fixed \(p=c+\varepsilon\).

## Stage 4A result

Independent clean-room reconstruction passed after one required rollback/amendment.

Canonical artifacts:

- \`audit/STAGE_04A_MATH_RED_TEAM.md\`
- \`audit/stage04a_theorem_certificates.md\`
- \`audit/stage04a_cleanroom_derivation.md\`
- \`audit/stage04a_formalization_target_map.md\`
- \`code/stage04a_independent_verify.py\`

Formal verification is **applicable** and must be closed before theory freeze under the Stage-7.5A gate.

\`main\` remains stable.


## Stage 6 novelty re-kill

Stage 6 kills all broad claims that the paper discovers a new generic investment/outsourcing mechanism.

Known prior literature already establishes:

- negative competition effects on outsourcing/investment in related models;
- endogenous asymmetry and rival exit after cost-reducing investment;
- multiple/asymmetric equilibria in two-stage Cournot investment games;
- piecewise/discontinuous best responses;
- asymmetric-cost spatial price competition and no-loss price restrictions.

The surviving contribution is explicitly **source-specific**:

1. equation (14) / Proposition 3 reverses sign in the published Shy–Stenbacka model itself;
2. the globally valid source-duopoly outsourcing BR contradicts the paper's global Proposition-5 strategic-substitutes claim;
3. the complete pure source-duopoly equilibrium correspondence contains symmetric/asymmetric coexistence and a knife-edge continuum;
4. the literal Hotelling source continuation is incomplete off path;
5. under explicit \(p\ge c\), Proposition 6 fails on the certified cap-aware region.

Canonical Stage-6 artifacts:

- \`audit/STAGE_06_NOVELTY_REKILL.md\`
- \`audit/stage06_theorem_absorption_map.md\`
- \`audit/stage06_search_log.md\`

Generic “first to show competition reduces outsourcing,” “first asymmetric investment equilibrium,” and “new symmetry-breaking mechanism” language is prohibited.


## Stage 7 welfare / generality result

Stage 7 does **not** promote welfare to a new headline contribution.

Key controls:

- exact Cournot and Hotelling welfare identities derived;
- unrestricted first-best problems explicitly defined;
- restricted sourcing benchmarks are not called first best;
- Cournot multiple equilibria have different welfare, so no selection-free global welfare claim is permitted;
- literal Hotelling corner price multiplicity is welfare-invariant at a fixed sourcing history because prices are transfers and the allocation is unchanged;
- the no-loss Hotelling result remains conditional on explicit \(p\ge c\);
- exact functional-form results remain baseline-only unless separately proved more generally;
- broad institutional trade-off is supported, but quadratic/output-independent monitoring cost is not empirically established.

Canonical Stage-7 artifacts:

- \`audit/STAGE_07_WELFARE_GENERALITY.md\`
- \`audit/stage07_welfare_benchmarks.md\`
- \`audit/stage07_generality_institutional.md\`
- \`code/stage07_welfare_verify.py\`


## Stage 7.5 full-theory freeze decision

Stage 7.5 concludes that the project merits full-paper investment **as a compact correction paper / theory note**.

The mechanism can be stated without notation:

> outsourcing lowers marginal cost; sufficiently large sourcing differences can change the downstream active set; once a rival is driven to zero output, the relevant continuation regime changes, so an interior best-response calculation need not describe the global strategic game.

The paper is not positioned as a new general outsourcing theory. Its defensible value is the combination of:

- a published comparative-static sign reversal;
- a global Proposition-5 correction;
- a complete pure source-duopoly equilibrium re-characterization;
- a secondary literal Hotelling continuation correction;
- a conditional no-loss Hotelling robustness theorem.

Stage 7.5 therefore gives:

\[
\boxed{\textbf{GO TO STAGE 7.5A}}
\]

Canonical artifact:

- \`audit/STAGE_075_FREEZE_DECISION.md\`

Stage 7.5A may narrow claim scope but may not add extensions or silently alter the model.


## Stage 7.5A generality / quantifier certification

Stage 7.5A closes with:

\[
\boxed{\textbf{GO — GENERALITY / QUANTIFIER CERTIFICATION PASS}}
\]

Permanent scope controls include:

- general-\(N\): unique **symmetric pure Stage-I action**, not unique SPNE;
- source duopoly: complete **pure Stage-I** equilibrium correspondence;
- Proposition-3 competition comparative static: economic wording only across admissible integer market sizes satisfying the source restrictions;
- Hotelling uniqueness: **pure-price** scope;
- \(p\ge c\): explicit auxiliary no-loss restriction only;
- welfare in Cournot multiplicity regions: selection-dependent;
- exact thresholds: baseline functional-form results.

The Formal Verification Gate is also closed:

\[
\boxed{\textbf{FORMAL VERIFICATION PASS}}
\]

Lean 4.19.0 / pinned mathlib build passed with no \`sorry\`, \`admit\`, project-specific \`axiom\`, or \`sorryAx\` in certified theorems.

Canonical Stage-7.5A artifacts:

- \`audit/STAGE_075A_GENERALITY_QUANTIFIER_RED_TEAM.md\`
- \`audit/stage075a_claim_scope_ledger.md\`
- \`audit/stage075a_function_class_counterexamples.md\`
- \`audit/stage075a_formal_statement_fidelity.md\`
- \`audit/stage075a_formal_verification_certificate.md\`
- \`ShyStenbackaFormal/Stage075A.lean\`

Stage 8 may freeze only these scopes; it may not widen any theorem or solution concept.


## Stage 8 canonical theory freeze

Stage 8 closes with:

\[
\boxed{\textbf{CANONICAL STAGE 8 — PASS}}
\]

\[
\boxed{\textbf{THEORY FROZEN}}
\]

The canonical theory boundary is now recorded in:

- `audit/STAGE_08_CANONICAL_THEORY_FREEZE.md`

The freeze binds manuscript construction to the Stage-7.5A scopes. In particular:

- general-`N` Cournot: unique **symmetric pure Stage-I action**, not unique SPNE;
- source duopoly: complete **pure Stage-I** equilibrium correspondence;
- Proposition-3 comparative static: admissible integer market sizes satisfying source restrictions;
- Hotelling: literal **pure-price** continuation plus a separate conditional no-loss game;
- `p_j\ge c_j`: auxiliary strategy restriction only;
- Cournot welfare under multiplicity: selection-dependent;
- exact C7/C8 thresholds: baseline source-functional-form results;
- formal verification: targeted **proof-critical core**, not the complete economic model.

Any theory, equilibrium-concept, quantifier, benchmark, or formal-statement change after this point requires explicit rollback under the Stage-8 change-control rules.

Stage 9 may reorganize and harden reproducibility infrastructure, but it may not alter the frozen theory.


## Stage 9 repository / reproducibility setup

Stage 9 closes with:

\[
\boxed{\textbf{CANONICAL STAGE 9 — PASS}}
\]

The existing repository has now been converted into the canonical production/reproducibility layout required by workflow v2.2.

Canonical Stage-9 artifacts:

- `audit/STAGE_09_REPOSITORY_REPRODUCIBILITY.md`
- `audit/stage09_artifact_manifest.md`
- `REPRODUCIBILITY.md`
- `Makefile`
- `theorem_certificates/README.md`
- `formal/README.md`
- `audit/counterexample_regression_register.md`

Reproducibility gates are green:

- Python verification: run `35442666402` — **success**;
- Lean formal verification: run `35439005968` — **success**;
- manuscript smoke build: run `35442682700` — **success**.

The manuscript has been modularized into `paper/sections/` without adding substantive theory. Stage 10 may now construct the paper section by section, but remains bound by the Stage-8 theory freeze.


## Stage 10 paper construction

Stage 10 closes with:

\[
\boxed{\textbf{CANONICAL STAGE 10 — PASS}}
\]

The frozen theory is now implemented as an integrated manuscript with model, global Cournot continuation, corrected comparative statics, source-duopoly equilibrium correspondence, literal and no-loss Hotelling blocks, welfare/scope discussion, related literature, conclusion, and proof appendix.

Canonical Stage-10 artifacts:

- `audit/STAGE_10_PAPER_CONSTRUCTION.md`
- `audit/STAGE_10_FIGURE_TABLE_ARCHITECTURE.md`
- `paper/manuscript.tex`
- `code/stage10_generate_figure.py`

Stage-10 substantive head `80f4523222e3f473786f3800ca8be0928de78fe2` passed:

- Python verification run `35444042815`;
- manuscript build run `35444042793`.

Figure 1 is generated from exact rational regression values before the LaTeX build. Table 1 reports the certified pure source-duopoly equilibrium regimes. No Stage-8 rollback trigger was activated.


## Stage 11 robustness / referee attack

Stage 11 closes with:

\[
\boxed{\textbf{CANONICAL STAGE 11 — PASS}}
\]

Canonical Stage-11 artifacts:

- `audit/STAGE_11_ROBUSTNESS_REFEREE_ATTACK.md`
- `audit/STAGE_11_KNOWN_MODEL_ATTACK.md`
- `code/stage11_hostile_referee_verify.py`

The hostile-referee layer independently attacked primitive-level Cournot deviations, active-set boundaries, the (ho=2/3) knife edge, the (phi=s) cap boundary, literal Hotelling corner selection, the auxiliary no-loss threshold, welfare selection, function-class scope, known-model absorption, citation completeness, and formal-verification scope.

One **MINOR** prose-only scope inflation in Related Literature was found and repaired. No FATAL or MAJOR defect and no certification regression was found.

Stage-11 verification head `89d04eb048257db3f930cd34f96209d34d1e3bc7` passed Python verification runs `35451023487` and `35451026809`. The manuscript containing the scope repair passed build run `35450876387`. The frozen Lean blobs remain unchanged.


## Stage 12 journal positioning — v2.3 completeness re-audit

Stage 12 was reopened because the original v2.2 comparison had a **candidate-set omission**: IJIO and several other obvious/repeated IO venues had not been explicitly evaluated before the ranking was closed.

The v2.3 re-audit closes with:

\[
\boxed{\textbf{PRIMARY JOURNAL SELECTED — GO TO INTEGRATION}}
\]

Candidate-universe gate:

\[
\boxed{\textbf{CANDIDATE-UNIVERSE COMPLETENESS AUDIT — PASS}}
\]

The earlier omission is recorded as:

\[
\boxed{\textbf{JOURNAL-POSITIONING COMPLETENESS REGRESSION — REPAIRED}}
\]

Primary target:

\[
\boxed{\textbf{Review of Industrial Organization}}
\]

Best stretch:

\[
\boxed{\textbf{International Journal of Industrial Organization}}
\]

Canonical Stage-12 artifacts:

- `audit/STAGE_12_CANDIDATE_UNIVERSE_LEDGER.md`
- `audit/STAGE_12_JOURNAL_POSITIONING.md`
- `audit/STAGE_12_RIO_REQUIREMENTS_LEDGER.md`

Default fit-first submission ladder:

1. Review of Industrial Organization — **Primary**
2. Journal of Institutional and Theoretical Economics — **Realistic fallback 1**
3. Journal of Economics — **Realistic fallback 2**
4. Journal of Industry, Competition and Trade — **Realistic fallback 3**
5. Bulletin of Economic Research — **Alternative fallback**
6. Economics Bulletin — **Safety net**

Optional one-shot stretch:

`IJIO → RIO → JITE → …`

The Journal of Industrial Economics, Journal of Economics & Management Strategy, and Canadian Journal of Economics were explicitly evaluated as higher-risk stretches but are not preferred to IJIO as the single pre-RIO attempt. RAND Journal of Economics, Journal of Economic Theory, Economic Theory, JEBO, Southern Economic Journal, and JEDC were explicitly excluded with reasons in the candidate-universe ledger.

RIO remains primary **after** the expanded comparison because its explicit accommodation of shorter notes/commentaries matches the certified source-specific correction/re-characterization better than the stronger new-mechanism orientation of the stretch outlets.

No theory, novelty, welfare, equilibrium, or formal-verification claim was changed. Stage 13 may only integrate and package the frozen manuscript for RIO.



## Stage 13 full-paper integration for RIO

Stage 13 closes with:

\[
\boxed{\textbf{INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA}}
\]

Canonical report:

- `audit/STAGE_13_FULL_PAPER_INTEGRATION.md`

Stage-13 integration added:

- RIO-compliant abstract indexing metadata: 5 keywords and JEL codes `L13; L23; L24`;
- current RIO make-or-buy literature positioning via Dai (2026);
- data/code availability and substantive generative-AI disclosure;
- a self-contained scope caption for the pure-equilibrium table;
- `code/stage13_integration_verify.py`;
- `code/stage13_build_rio_bundle.py`;
- `make rio-bundle`, which generates and compiles a no-subfolder flat LaTeX submission bundle;
- `paper/RIO_SUBMISSION_NOTES.md`, preserving authenticated-portal and author-specific unknowns for Stage 14.

Substantive Stage-13 integration head:

`72c2f233199bea82e67de9b93987a64fe2dae804`

Green evidence:

- Python push run `35473538351` — **success**;
- Python PR run `35473541979` — **success**;
- canonical + flat RIO manuscript build run `35473538163` — **success**.

Both canonical and flat package builds converge to a 16-page PDF. No Stage-8/11 theory, novelty, welfare, equilibrium, or formal-verification scope was changed.

Stage 14 must refresh live RIO requirements, resolve portal/author inputs, audit final source/artwork/declarations, and inspect the submission PDF page by page.


## 2026-09-20 independent-audit repair / re-certification

A later independent clean-room audit found a real certification regression in the Stage-4A/8/11/13 chain:

- C7 over-quantified the feasibility of the positive-slope constrained best-response segment;
- C8's five-case equilibrium statement survived, but its completeness proof was under-documented;
- downstream exit was overstated as necessary for multiplicity.

The defects were independently rechecked, repaired, and permanently regression-tested.

Current controlling records:

- \`audit/INDEPENDENT_AUDIT_REPAIR_LEDGER_2026-09-20.md\`;
- \`audit/STAGE_04A_INDEPENDENT_AUDIT_RECERTIFICATION_2026-09-20.md\`;
- \`audit/STAGE_075A_INDEPENDENT_AUDIT_RECONCILIATION_2026-09-20.md\`;
- \`audit/STAGE_08_INDEPENDENT_AUDIT_AMENDMENT_2026-09-20.md\`;
- \`audit/STAGE_06_INDEPENDENT_AUDIT_RECHECK_2026-09-20.md\`;
- \`audit/STAGE_11_RECERTIFICATION_2026-09-20.md\`;
- \`audit/STAGE_13_INDEPENDENT_AUDIT_REINTEGRATION_2026-09-20.md\`;
- \`code/independent_audit_repair_verify.py\`.

Key repaired theory scope:

- the uncapped response has the \(+2\) exit branch for \(4/9<\rho<2/3\), but a positive-length **capped** segment survives only for sufficiently large \(\phi\);
- the complete five-case pure Stage-I source-duopoly equilibrium correspondence is unchanged and now has an explicit analytic exclusion proof;
- downstream exit creates the positive-slope branch but is **not necessary** for multiplicity; the all-active witness \((\rho,\delta,\phi)=(3/5,1,3/4)\) has the symmetric equilibrium plus an asymmetric pair;
- the literal Hotelling result is explicitly tied to the maintained clipped full-coverage continuation, not to an uncovered-demand extension;
- \(x_-\), welfare knife-edge language, and proof-globality conditions are now domain-complete.

Latest integrated green evidence before closure-record-only commits:

- Python verification run \`35477505973\` — success;
- canonical + flat RIO build run \`35477505977\` — success;
- final hyperlink-clean PDF build \`35477441567\` — success;
- final 22-page PDF rendered and visually inspected page by page — PASS.

Stage 14 has now completed all repository-resolvable and public-rule-resolvable QA. It is conditionally closed pending authoritative author/title-page/declaration input and authenticated RIO portal preflight.


## Stage 14 submission QA

Stage 14 closes conditionally:

\[
\boxed{\textbf{CONDITIONAL PASS — AUTHOR INPUT + AUTHENTICATED PORTAL PREFLIGHT REQUIRED}}
\]

Canonical Stage-14 artifacts:

- \`audit/STAGE_14_SUBMISSION_QA.md\`
- \`audit/STAGE_14_JOURNAL_REQUIREMENTS_LEDGER.md\`
- \`audit/STAGE_14_PACKAGE_INVENTORY.md\`
- \`audit/STAGE_14_PDF_VISUAL_QA.md\`
- \`paper/RIO_AUTHOR_INPUT_REQUIRED.md\`
- \`code/stage14_submission_qa.py\`

Stage 14 found and repaired real submission defects: uncited bibliography entries, contamination of the flat upload source with build artifacts, malformed DOI URL rendering, a faulty font-embedding check, and journal-specific declaration/caption formatting.

Final technical head:

\`446ce7bdf7eff1d2363a315c905c28572c91861a\`

Green evidence:

- Python verification \`35478726461\` — PASS;
- canonical + flat-source isolated build / package QA \`35478726453\` — PASS;
- all fonts embedded;
- canonical and flat build PDFs: 22 pages;
- all 22 pages visually inspected — PASS;
- final-head render comparison — 0 changed pages.

Full Stage-14 PASS is blocked only by factual author/declaration inputs and authenticated portal-only requirements. Stage 15 is not started.
