# Author Intellectual-Contribution Record

Status: **RETROFIT RECORD COMPLETE — FINAL EXACT-PACKAGE SIGN-OFF REMAINS STAGE 15**

Date: 2026-10-05

Workflow authority:
- prospective v2.6 refinement in `research-paper-workflow` main;
- `checklists/AI_PROVENANCE_AUTHOR_ACCOUNTABILITY_CHECKLIST.md`.

## Purpose and evidence boundary

This record preserves the substantive research judgments carried by the sole-author project. It does **not** claim that the author independently re-proved every equation without AI assistance, and it does not convert AI/computational/formal checks into AUTHOR verification.

The record is reconstructed from the frozen manuscript, the dated project decision log, the claim-scope ledger, the theory freeze, and the previously approved sole-author declaration record. Its role is to make the intellectual choices explicit enough to distinguish them from machine-side verification.

Primary evidence:
- `audit/decision_log.md`;
- `audit/STAGE_075A_GENERALITY_QUANTIFIER_RED_TEAM.md`;
- `audit/stage075a_claim_scope_ledger.md`;
- `audit/STAGE_08_CANONICAL_THEORY_FREEZE.md` plus 2026-09-20 amendments;
- `paper/RIO_AUTHOR_INPUT_REQUIRED.md`;
- final manuscript and appendix.

## Central research judgments

### 1. Why the question matters

The project does not treat Shy–Stenbacka (2005) as an arbitrary old model. The source paper makes economically substantive claims about how product-market competition affects outsourcing and about strategic substitutability of sourcing choices. The project therefore asks whether those conclusions survive the source model's own strategy bounds and globally valid downstream continuations.

Maximum defensible contribution: a **source-specific correction and global re-characterization**, not a new general outsourcing theory.

### 2. Why the source restrictions are maintained

The canonical model preserves:
- the source sourcing box `0 <= i_j <= phi`;
- nonnegative Cournot quantities;
- linear marginal-cost reduction from outsourcing;
- quadratic monitoring cost;
- the source SOC;
- the maintained full-coverage Hotelling interpretation.

The auxiliary `p_j >= c_j` price restriction is kept separate because it is not a source primitive and is not justified as an equilibrium refinement.

### 3. Proposition-3 correction

Research judgment:
- the reported competition comparative static must be evaluated from the correctly differentiated symmetric sourcing expression;
- the cap must be retained;
- economically, comparisons are across admissible integer market sizes, not an unrestricted continuous-`N` theorem.

Proof logic:
- derive the unilateral sourcing FOC at symmetry;
- use global own-payoff concavity for sufficiency;
- project onto the source cap;
- differentiate only the continuous extension for the sign;
- translate the sign back to admissible integer comparisons.

Maximum wording:
> the corrected symmetric pure sourcing action is weakly decreasing across admissible integer market sizes and strictly decreasing when both compared actions are interior.

### 4. Proposition-5 / global-best-response correction

Research judgment:
- an all-active downstream formula cannot be transported through histories where a rival's Cournot quantity hits zero;
- downstream active-set changes must be solved globally before making a strategic-substitutes claim.

Proof logic:
- solve the nonnegative-quantity Cournot continuation;
- establish global own-payoff concavity across entry/exit thresholds;
- derive the active, rival-exit, and monopoly sourcing branches;
- apply the sourcing cap only after finding the unconstrained global maximizer;
- retain the exact cap condition under which the positive-slope rival-exit segment survives.

Maximum wording:
> admissible source parameters exist for which the constrained pure global sourcing best response increases on a nondegenerate interval, so Proposition 5 is false as an unqualified global strategic-substitutes statement.

Prohibited wording:
- outsourcing is globally a strategic complement;
- the positive-slope segment survives for every cap.

### 5. Source-duopoly equilibrium correspondence

Research judgment:
- the contribution is the exact **pure Stage-I** correspondence in the source duopoly;
- no mixed-strategy completeness claim is needed or authorized.

Proof logic:
- use the exact capped global best response;
- split at `rho > 2/3`, `rho = 2/3`, and `4/9 < rho < 2/3`;
- use contraction in the high-`rho` regime;
- treat the knife-edge continuum explicitly;
- use crossing/branch-exclusion arguments to prove the unique asymmetric ordered pair in the low-`rho` regime.

Important limitation:
- multiplicity is model-specific and does not require downstream exit; the all-active cap example prevents an overstated mechanism story.

### 6. Hotelling correction and no-loss robustness

Research judgment:
- the literal source-compatible full-coverage price game must be distinguished from the auxiliary no-loss game.

Literal result:
- sufficiently asymmetric costs generate a continuum of pure corner price continuations, so the published interior backward induction is not globally single-valued.

Auxiliary result:
- under explicit `p_j >= c_j`, the pure price continuation is unique and the published symmetric sourcing candidate fails on the certified cap-aware region.

Prohibited wording:
- undominated-price refinement;
- trembling-hand/proper-equilibrium selection;
- unconditional global falsification of Proposition 6 in the literal game.

### 7. Generality and welfare boundaries

The exact best-response and multiplicity results remain source-functional-form results. The `M(x)=10x^2` counterexample is retained because it shows that the geometric exit threshold does not imply a generic positive-slope global best response.

Welfare in Cournot multiplicity regions is selection-dependent. Restricted planner objects are not called first best.

### 8. Formal-verification judgment

Targeted formalization is used because several claims contain fragile sign, threshold, branch-join, and exact-gain algebra. The project does not attempt to formalize the entire economic game.

FORMAL evidence supports only the mapped encoded core. Global equilibrium construction, complete source-duopoly correspondence, interpretation, novelty, and journal fit remain outside the Lean guarantee.

## AI-assisted suggestions: acceptance / rejection discipline

The project record contains multiple examples where an initially attractive AI-assisted narrative was rejected or narrowed after adversarial checking:
- the initial Hotelling unconditional rejection was superseded by selection dependence;
- the proposed “undominated-price refinement” was rejected;
- generic negative-competition novelty was killed by prior art;
- C7's cap quantifier was narrowed;
- downstream exit was rejected as a necessary explanation for multiplicity.

These reversals are retained as evidence that the project did not preserve AI-generated claims merely because they were convenient.

## Verification-actor map

| Object | AUTHOR responsibility/judgment | AI | COMPUTATION | FORMAL |
|---|---|---|---|---|
| research question / contribution scope | yes | assistance | no | no |
| source-model assumptions and auxiliary-model separation | yes | assistance/audit | checks | selected algebra only |
| Proposition-3 corrected sign | accepts scoped claim | adversarial support | exact/regression checks | selected sign core |
| Proposition-5 correction | accepts scoped claim | adversarial support | branch/regression checks | branch-join/slope core |
| pure-duopoly correspondence | accepts pure-strategy scope | adversarial support | regression checks | not complete |
| Hotelling literal/no-loss split | accepts separation and limits | adversarial support | exact checks | selected gain core |
| novelty / journal positioning | accepts source-specific positioning | search/analysis support | no | no |
| final manuscript responsibility | yes | drafting/edit support | QA | mapped proof core only |

No EXTERNAL HUMAN verification is claimed.

## Final accountability state

The intellectual record is sufficient for the retrofit because the project now states:
- what the central judgments are;
- why the assumptions/restrictions were retained;
- the proof/equilibrium logic at the level needed to detect material mistakes;
- the important failure boundaries and non-claims;
- what AI/computation/formal verification did and did not establish.

Stage 15 still requires a personal AUTHOR sign-off tied to the exact final commit, portal-generated PDF, and submission package. That later sign-off is not pre-certified here.

Verdict:

**PASS — AUTHOR INTELLECTUAL-CONTRIBUTION RECORD PRESENT; FINAL STAGE-15 EXACT-PACKAGE SIGN-OFF REMAINS REQUIRED.**
