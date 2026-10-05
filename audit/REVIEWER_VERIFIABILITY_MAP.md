# Reviewer-Verifiability Map

Status: **FULL APPLICABILITY — MAP COMPLETE**

Date: 2026-10-05

Workflow authority:
- prospective v2.7 reviewer-verifiability refinement;
- `checklists/REVIEWER_VERIFIABILITY_CHECKLIST.md`.

Target reader: a competent industrial-organization theory referee.

## Headline-result map

| Claim | Manuscript location | Proof / derivation location | Machine/formal support | Reviewer-verifiability state |
|---|---|---|---|---|
| Global Cournot continuation | Sec. 3, Lemma “Global Cournot continuation” | Appendix: proof of the two Cournot lemmas | deterministic regression suite; no full Lean theorem | PASS |
| Global own-payoff concavity | Sec. 3, Lemma “Global own-payoff concavity” | Appendix: branch curvature, own-entry continuity, rival-exit derivative jump | deterministic checks | PASS |
| Corrected symmetric Cournot action / Prop. 3 sign | Sec. 3, Proposition “Corrected symmetric Cournot action” and Eq. dIdN | Appendix: unilateral FOC, positivity of denominator, cap projection, comparative-static derivative | Lean C4 core + Python | PASS |
| Prop. 5 global strategic-substitutes failure | Sec. 3, global BR and Proposition “Global failure of strategic substitutability” | Appendix: three reduced-payoff branches, A/U/M objects, join points, cap-survival conditions | Lean branch-join/slope core + Python | PASS |
| Complete pure source-duopoly correspondence | Sec. 4, Proposition “Complete pure Stage-I correspondence...” | Appendix: three rho regimes, contraction, knife-edge system, crossing and exhaustive asymmetric branch exclusion | deterministic exact regressions; not fully Lean-formalized | PASS |
| Literal Hotelling pure-price continuation | Sec. 5, Proposition “Literal pure-price continuation” | Appendix: exact price best-response correspondence and mutual-BR solution | deterministic checks | PASS after typo repair |
| Weak-dominance boundary | Sec. 5, dominance discussion | Appendix: payoff comparison at p<c, p=c, p=c+epsilon | selected Lean sign core | PASS |
| Auxiliary no-loss Hotelling failure region | Sec. 5, no-loss proposition | Appendix: unique restricted continuation, Delta(x), vertex, roots, cap cases | Python + selected Lean H5/H6 core | PASS |
| Formal-verification scope | Statements and Declarations / Code availability | `formal/README.md`; formal statement-fidelity map | Lean 4.19.0 / pinned mathlib | PASS after v2.7 disclosure clarification |

## Bridge equations that must remain visible

The following are proof-critical bridges and are therefore protected against exposition compression:

1. active-set price and quantity:
   `p_S=(a+sum_{j in S}c_j)/(|S|+1)`, `q_j=(p_S-c_j)/b`;
2. branch curvature:
   `Pi_j''(x)=2H^2m^2/[b(m+1)^2]-2`;
3. symmetric root and corrected derivative:
   `bar i_C=HND/[b(N+1)^2-H^2N]` and the displayed negative derivative;
4. source-duopoly branch objects:
   `A(y)`, `U(y)`, `M`, `y_A`, `y_M`, and `B_phi=min{phi,R}`;
5. symmetric fixed point `s=2delta/(9rho-2)`;
6. literal Hotelling clipped share and exact price best response in the Appendix;
7. no-loss gain `Delta(x)`, its vertex `x_M`, and lower root `x_-`.

## Delegated material

Routine expansions, regression enumeration, exact arithmetic checks, and Lean kernel details may remain in code/audit/formal artifacts. The manuscript itself retains:
- the object being solved;
- its domain;
- the certified or analytically proved property;
- the implication for the economic claim.

## Formal mapping boundary

The manuscript now expressly states that Lean certifies selected algebra/order cores only. It does not ask a referee to infer that the whole equilibrium model is formalized.

The authoritative mapping remains:
- `audit/stage075a_formal_statement_fidelity.md`.

Verdict:

**PASS — THE MANUSCRIPT CONTAINS THE REQUIRED PROOF-CRITICAL BRIDGES AND PRECISE DELEGATION BOUNDARIES.**
