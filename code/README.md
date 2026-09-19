# Verification Code

Code supplements analytical proof and does not replace it.

## Stage 1

\`\`\`bash
python code/stage01_verify.py
\`\`\`

## Stage 4 — Cournot and literal Hotelling

\`\`\`bash
python code/stage04_verify.py
\`\`\`

## Stage 4 — Hotelling undominated-price re-audit

\`\`\`bash
python code/stage04_hotelling_refinement_verify.py
\`\`\`

Pinned dependency:

\`\`\`text
sympy==1.14.0
\`\`\`

The refinement script verifies the exact piecewise Hotelling payoff identities, branch thresholds, deviation-gain quadratic, critical cap, and the Stage-1 \(1/90\) rational counterexample.

Important distinctions:

- literal source Nash multiplicity is not erased;
- deletion of \(p<c\) is explicitly labeled weak-dominance refinement;
- no trembling-hand/proper-equilibrium claim is inferred from the script;
- solver failure is never evidence against a deviation.


## Stage 7 — welfare / benchmark verification

\`\`\`bash
python code/stage07_welfare_verify.py
\`\`\`

Checks:

- exact Cournot CS / welfare identity;
- restricted common-sourcing welfare benchmark;
- private-versus-restricted sourcing comparison;
- welfare non-invariance across the certified Cournot equilibrium set;
- exact Hotelling CS / welfare cancellation of prices;
- fixed-sourcing efficient Hotelling allocation;
- fixed-allocation social sourcing benchmark.

This code verifies algebra only. It does not convert a restricted benchmark into a first-best claim or resolve equilibrium selection.
