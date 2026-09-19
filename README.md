# Shy–Stenbacka Correction

Reproducible correction and adversarial equilibrium audit of Shy & Stenbacka (2005).

## Canonical status

\[
\boxed{\textbf{STAGE 4 — PASS (AMENDED)}}
\]

\[
\boxed{\textbf{STAGE 4A — IN PROGRESS}}
\]

Workflow: \`research-paper-workflow\` v2.2.

## Canonical architecture after Stage-4A refinement attack

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

**No-loss robustness model:** if one explicitly imposes

\[
p_j\ge c_j,
\]

the pure price continuation becomes unique and Proposition 6 fails on an exact cap-aware region.

This price floor is **not** attributed to Shy–Stenbacka and is **not** described as elimination of all weakly dominated strategies. Stage 4A found that although every \(p<c\) is weakly dominated by \(p=c\), the price \(p=c\) itself is weakly dominated by any fixed \(p=c+\varepsilon\).

## Verification artifacts

- \`code/stage01_verify.py\`
- \`code/stage04_verify.py\`
- \`code/stage04_hotelling_refinement_verify.py\`
- \`code/stage04a_independent_verify.py\`

## Canonical reports

- \`audit/STAGE_04_MINIMAL_MODEL_GATE.md\`
- \`audit/STAGE_04_HOTELLING_REAUDIT.md\`
- \`audit/STAGE_04A_MATH_RED_TEAM.md\` once Stage 4A closes

\`main\` remains stable. No theory-freeze claim is made before Stage 4A, Stage 7.5A, and Stage 8.
