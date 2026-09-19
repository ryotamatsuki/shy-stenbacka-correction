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
\boxed{\textbf{NEXT: STAGE 6 — NOVELTY RE-KILL}}
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
