# Shy–Stenbacka Correction

Reproducible correction and adversarial equilibrium audit of Shy & Stenbacka (2005).

## Canonical status

\[
\boxed{\textbf{STAGE 4 — PASS}}
\]

\[
\boxed{\textbf{NEXT: STAGE 4A — INDEPENDENT MATHEMATICAL ADVERSARIAL CERTIFICATION}}
\]

Workflow: \`research-paper-workflow\` v2.2.

Completed:

- Stage 1 — Source & Mathematical Audit
- Stage 2 — Literature Frontier / Novelty Kill Gate
- Stage 3 — Candidate Mechanism Search
- Stage 4 — Minimal Model Gate

Canonical reports:

- \`audit/STAGE_01_SOURCE_MATHEMATICAL_AUDIT.md\`
- \`audit/STAGE_02_LITERATURE_NOVELTY_GATE.md\`
- \`audit/STAGE_03_MECHANISM_SEARCH.md\`
- \`audit/STAGE_04_MINIMAL_MODEL_GATE.md\`

## Stage-4 canonical paper architecture

Stage 3's unified Cournot + Hotelling Candidate E was rejected as the minimal paper architecture because the source Hotelling price subgame has off-path equilibrium multiplicity.

The canonical object routed to Stage 4A is:

**Candidate C — Complete Cournot correction.**

Main Stage-4 results:

1. every feasible Cournot sourcing profile has a unique nonnegative-quantity continuation;
2. the reduced Stage-I payoff is globally strictly concave in own outsourcing under the source SOC;
3. the corrected symmetric action is
   \[
   i_C^*=\min\left\{\phi,\frac{HND}{b(N+1)^2-H^2N}\right\};
   \]
4. the source equation-(14)/Proposition-3 competition effect has the wrong sign;
5. Proposition 5 is false globally: the source duopoly BR can contain a slope-\(+2\) rival-exit segment;
6. the source duopoly has a complete pure-equilibrium classification, including asymmetric equilibria and a continuum at \(b/H^2=2/3\).

## Hotelling diagnostic

The Hotelling continuation is unique for \(|c_B-c_A|\le3\tau\) and multiple for larger cost gaps.

The earlier Stage-1 conclusion that a corner deviation simply defeats Proposition 6 is superseded: the same sourcing deviation can be profitable or unprofitable under different valid off-path price equilibria.

No no-below-cost refinement or other new selection rule is imposed.

## Verification

- \`code/stage01_verify.py\`
- \`code/stage04_verify.py\`
- \`audit/stage04_continuation_ledger.md\`
- \`audit/stage04_theorem_certificates.md\`

Exact symbolic identities, rational counterexamples, continuation regressions, and the duopoly equilibrium classification have been checked.

## Branch policy

Current audit branch:

\`audit/full-equilibrium-correspondence\`

\`main\` remains the stable project history. No theory-freeze claim is made before Stage 4A and later gates pass.
