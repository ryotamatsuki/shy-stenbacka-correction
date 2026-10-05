# Contribution Robustness Certificate

Status: **PASS — RETROFIT FROM EXISTING STAGE-7.5A EVIDENCE**

Date: 2026-10-05

This certificate packages the portability/falsification evidence already present in the project into the current `research-paper-workflow` format. It introduces no new theorem.

## Headline claims

| Claim | Mechanism invariant / object | Portability attack | Result | Classification | Maximum defensible wording |
|---|---|---|---|---|---|
| C4 corrected competition sign in the Shy–Stenbacka symmetric Cournot sourcing formula | unilateral sourcing incentive at symmetry under the source linear/quadratic primitives and cap | nonlinear demand / alternative technology not certified; source formula itself independently checked | exact source-model sign reversal survives | **MODEL-SPECIFIC** | In the published source model, the corrected symmetric pure sourcing action is weakly decreasing across admissible integer market sizes, strictly off the cap. |
| C7 Prop.-5 correction | global active-set continuation and rival-exit threshold can create a positive-slope sourcing BR piece | replace `M(x)=x^2` by `10x^2` while retaining the exit geometry | exit geometry survives but exit-inducing action is not globally optimal | **MODEL-SPECIFIC** | Admissible source parameters exist for which the constrained pure global BR increases on a nondegenerate interval; Prop. 5 is not globally valid as stated. |
| C8 pure-duopoly multiplicity | exact capped source BR crossing geometry | same alternative monitoring-cost attack; all-active cap witness | generic multiplicity does not survive as a cross-model theorem | **MODEL-SPECIFIC** | The source duopoly has the exact certified pure Stage-I correspondence; no generic outsourcing-game multiplicity claim. |
| H1 literal Hotelling continuation | clipped full-coverage price game with source cost differences | incomplete coverage / finite reservation utility not certified | result depends on maintained full-coverage institution | **INSTITUTION-SPECIFIC** | Under the maintained literal full-coverage interpretation, large cost gaps generate multiple pure corner continuations. |
| H3–H6-NL auxiliary no-loss result | explicit price-domain restriction `p_j >= c_j` | remove the auxiliary restriction | literal game reverts to set-valued corner continuation | **INSTITUTION-SPECIFIC** | Under the explicit auxiliary no-loss strategy restriction, the pure continuation is unique and the source symmetric candidate fails on the stated region. |

## Failure boundaries retained

- C7/C8 are not promoted to arbitrary convex monitoring costs.
- No nonlinear-demand general theorem is claimed.
- No mixed-strategy completeness is claimed.
- H1 is not transported to uncovered-demand Hotelling models.
- The no-loss result is not called a refinement of the literal source game.
- Welfare remains selection-dependent where Stage-I multiplicity occurs.

## Stop-rule status

The project does not continue redesigning alternative models to rescue a generic result. The exact source corrections remain valuable as source-specific results; cross-model generality is closed rather than repeatedly expanded.

## Evidence

- `audit/STAGE_075A_GENERALITY_QUANTIFIER_RED_TEAM.md`
- `audit/stage075a_function_class_counterexamples.md`
- `code/stage075a_scope_counterexamples.py`
- `audit/STAGE_06_NOVELTY_REKILL.md`
- `audit/STAGE_11_KNOWN_MODEL_ATTACK.md`

Verdict:

**PASS — THE CERTIFIED CONTRIBUTION STRENGTH IS MODEL/INSTITUTION-SPECIFIC AND THE MANUSCRIPT DOES NOT EXCEED IT.**
