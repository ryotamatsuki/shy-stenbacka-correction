# Stage 4 Preliminary Theorem Certificates

These certificates are construction-level. Stage 4A must attack them independently.

| ID | Exact claim | Attack performed | Evidence | State |
|---|---|---|---|---|
| C1 | Every feasible Cournot sourcing history has a unique quantity equilibrium from the sorted-cost active-set formula | KKT/active-set derivation; negative-quantity regression | \`audit/STAGE_04_MINIMAL_MODEL_GATE.md\`; \`code/stage04_verify.py\` | **PROVED** |
| C2 | Under the source SOC, own reduced Cournot payoff is globally strictly concave on \([0,\phi]\) | branch curvature + derivative-jump audit at entry/exit | Stage-4 report §4 | **PROVED** |
| C3 | Unique symmetric constrained Cournot action is \(i_C^*=\min\{\phi,HND/[b(N+1)^2-H^2N]\}\) | global concavity + KKT + cap regression | Stage-4 report §§4–5 | **PROVED** |
| C4 | \(i_C^*\) is weakly decreasing in \(N\), strictly on the interior branch for \(N>1\) | exact differentiation + cap branch | Stage-4 report §6; code | **PROVED** |
| C5 | The outsourced fraction is weakly decreasing in \(\phi\); the outsourced number rises on the cap branch and falls on the interior branch | exact derivatives + KKT | Stage-4 report §6; code | **PROVED** |
| C6 | The source-duopoly global BR is the piecewise \(B_\phi(y)\) in Stage 4 | inactive / both-active / monopoly regimes; kink comparison | Stage-4 report §7; code | **PROVED** |
| C7 | For \(4/9<\rho<2/3\), the global Cournot BR contains a slope-\(+2\) segment when feasible | exact kink branch + rational witness | Stage-4 report §8; code | **PROVED** |
| C8 | The source-duopoly pure Stage-I equilibrium correspondence has the three stated \(\rho\)-cases | fixed points of complete BR; deterministic adversarial checks | Stage-4 report §9; code | **PROVED** |
| H1 | Literal Hotelling price equilibrium is unique for \(|d|\le3\tau\) and a continuum for \(|d|>3\tau\) | complete clipped-demand BR derivation | \`audit/STAGE_04_HOTELLING_REAUDIT.md\` §§5–6; \`code/stage04_verify.py\` | **PROVED** |
| H2 | Every price \(p_j<c_j\) is weakly dominated by \(p_j=c_j\) | primitive payoff comparison for every rival price and every demand regime | Hotelling re-audit §3 | **PROVED** |
| H3 | After deleting below-cost weakly dominated prices, the Hotelling price continuation is unique for every cost gap | solve restricted global price BRs in all three cost-gap regimes | Hotelling re-audit §6 | **PROVED** |
| H4 | The refined constrained Stage-I Hotelling BR is exactly the finite-candidate argmax in (H-R2) | branch concavity, projection of branch stationary points, boundary/tie audit | Hotelling re-audit §§7–8; \`code/stage04_hotelling_refinement_verify.py\` | **PROVED** |
| H5 | Under the source SOC, the interior symmetric Hotelling candidate fails iff \(H^2n>27\tau/2\) and \(\phi>x_-\), with \(x_-=Hn/2-\sqrt{2n(2H^2n-27\tau)}/6\) | exact deviation-gain quadratic, roots, cap feasibility, branch-threshold proof | Hotelling re-audit §§9–13; refinement code | **PROVED** |
| H6 | At \(H=n=1,\tau=1/15,\phi=1\), \(i_A'=1/2\) against \(i_B=1/6\) is profitable under the unique undominated-price corner continuation with exact gain \(1/90\) | exact rational regression | Hotelling re-audit §14; refinement code | **PROVED** |

## Quantifier cautions

- C3 proves the unique **symmetric action**, not uniqueness of the general-\(N\) two-stage equilibrium.
- C8 is complete for pure Stage-I equilibria of the **source duopoly**.
- H1 is a statement about the literal source Nash game.
- H2–H6 are explicitly about one-round elimination of below-cost weakly dominated prices. They do **not** attribute \(p\ge c\) to the source paper.
- H3 is not labeled trembling-hand perfect or proper equilibrium.
- H5 characterizes survival of the symmetric pure Stage-I candidate under the refinement; it does not characterize all asymmetric refined-Hotelling Stage-I equilibria.

## Prohibited manuscript wording

Do not write:

- “the general-\(N\) Cournot game has a unique SPNE”;
- “Shy–Stenbacka assumed \(p\ge c\)”;
- “weak-dominance deletion leaves the Nash set unchanged”;
- “the Hotelling candidate is false in every literal-game SPNE”;
- “the refined Hotelling equilibrium is trembling-hand perfect” without a separate proof;
- “outsourcing is globally a strategic substitute” based only on the source interior derivative;
- “all refined Hotelling Stage-I equilibria are characterized.”

## Evidence maturity

All listed claims are construction-level \`PROVED\` only. None is theory-frozen before Stage 4A.
