# Shy–Stenbacka Correction

Reproducible correction and adversarial equilibrium audit of Shy & Stenbacka (2005).

## Canonical status

\[
\boxed{\textbf{STAGE 4 — PASS (AMENDED)}}
\]

\[
\boxed{\textbf{STAGE 4A — PASS}}
\]

\[
\boxed{\textbf{STAGE 6 — PASS}}
\]

\[
\boxed{\textbf{STAGE 7 — PASS}}
\]

\[
\boxed{\textbf{NEXT: STAGE 7.5 — FULL-THEORY FREEZE DECISION}}
\]

Workflow: \`research-paper-workflow\` v2.2.

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

**Literal source game:** sufficiently asymmetric costs generate multiple pure corner price continuations, so the published interior backward induction is incomplete off path.

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
