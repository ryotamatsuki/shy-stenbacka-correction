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
- Stage 4 — Minimal Model Gate, including Hotelling re-audit

Canonical Stage-4 reports:

- \`audit/STAGE_04_MINIMAL_MODEL_GATE.md\`
- \`audit/STAGE_04_HOTELLING_REAUDIT.md\`
- \`audit/stage04_continuation_ledger.md\`
- \`audit/stage04_theorem_certificates.md\`
- \`audit/stage04_verification_log.md\`

## Canonical Stage-4 architecture

After reopening only the Hotelling judgment, the architecture is:

**Candidate E′ — Complete Cournot correction + two-layer Hotelling correction.**

### Cournot core

1. every feasible sourcing profile has a unique nonnegative-quantity continuation;
2. own reduced Stage-I payoff is globally strictly concave under the source SOC;
3. corrected symmetric action:
   \[
   i_C^*=
   \min\left\{
   \phi,\,
   \frac{HND}{b(N+1)^2-H^2N}
   \right\};
   \]
4. equation (14) / Proposition 3 has the wrong sign;
5. Proposition 5 is false globally: the source duopoly BR can contain a slope-\(+2\) rival-exit segment;
6. the source duopoly has a complete pure-equilibrium classification with asymmetric equilibria and a continuum at \(b/H^2=2/3\).

### Hotelling two-layer correction

**Literal source game.** For \(|c_B-c_A|>3\tau\), the corner price subgame has a continuum of Nash equilibria because the zero-demand high-cost firm can use below-cost prices. The source does not specify an off-path selection rule.

**Undominated-price refinement.** Every price \(p_j<c_j\) is weakly dominated by \(p_j=c_j\). After deleting those prices, the corner continuation is unique. Under the source SOC, the source interior symmetric action fails exactly when

\[
\frac{27}{2}\tau<H^2n<18\tau
\]

and

\[
\phi>
\frac{Hn}{2}
-
\frac{\sqrt{2n(2H^2n-27\tau)}}{6}.
\]

The Stage-1 example \(H=n=1,\tau=1/15,\phi=1\) again gives an exact profitable deviation with gain \(1/90\) under this refinement.

The repository never attributes \(p\ge c\) to the published source and does not call the refinement trembling-hand perfect or proper equilibrium.

## Verification

- \`code/stage01_verify.py\`
- \`code/stage04_verify.py\`
- \`code/stage04_hotelling_refinement_verify.py\`

All retained exact symbolic identities and rational regression tests pass.

## Branch policy

Current audit branch:

\`audit/full-equilibrium-correspondence\`

\`main\` remains stable. No theory-freeze claim is made before Stage 4A and later gates pass.
