# Stage 4 Preliminary Theorem Certificates

These certificates are construction-level. Stage 4A must attack them independently.

| ID | Exact claim | Attack performed | Evidence | State |
|---|---|---|---|---|
| C1 | Every feasible Cournot sourcing history has a unique quantity equilibrium from the sorted-cost active-set formula | KKT/active-set derivation; negative-quantity regression | Stage-4 report; \`code/stage04_verify.py\` | **PROVED** |
| C2 | Under the source SOC, own reduced Cournot payoff is globally strictly concave on \([0,\phi]\) | branch curvature + derivative-jump audit at entry/exit | Stage-4 report §4 | **PROVED** |
| C3 | Unique symmetric constrained Cournot action is \(i_C^*=\min\{\phi,HND/[b(N+1)^2-H^2N]\}\) | global concavity + KKT + cap regression | Stage-4 report §§4–5 | **PROVED** |
| C4 | \(i_C^*\) is weakly decreasing in \(N\), strictly on the interior branch for \(N>1\) | exact differentiation + cap branch | Stage-4 report §6; code | **PROVED** |
| C5 | The outsourced fraction is weakly decreasing in \(\phi\); the outsourced number rises on the cap branch and falls on the interior branch | exact derivatives + KKT | Stage-4 report §6 | **PROVED** |
| C6 | The source-duopoly global BR is the piecewise \(B_\phi(y)\) in Stage 4 | inactive / both-active / monopoly regimes; kink comparison | Stage-4 report §7; code | **PROVED** |
| C7 | For \(4/9<\rho<2/3\), the global BR can contain slope \(+2\) | exact kink branch + rational witness | Stage-4 report §8; code | **PROVED** |
| C8 | The source-duopoly pure Stage-I equilibrium correspondence has the three \(\rho\)-cases in Stage 4 | fixed points of complete BR; broad deterministic adversarial check | Stage-4 report §9; code | **PROVED** |
| H1 | Hotelling price equilibrium is unique for \(|d_c|\le3\tau\) and a continuum for \(|d_c|>3\tau\) | complete clipped-demand BR derivation | Stage-4 report §10; code | **PROVED — DIAGNOSTIC** |
| H2 | The Stage-1 Hotelling corner-deviation rejection is selection-dependent | same deviation evaluated under two exact price equilibria | Stage-4 report §11; code | **PROVED — DIAGNOSTIC** |

## Quantifier cautions

C3 proves the unique **symmetric action**, not uniqueness of the general-\(N\) two-stage equilibrium.

C8 is complete for pure Stage-I equilibria of the **source duopoly**.

H1–H6 are part of restored Candidate E′. H1 concerns the literal source game; H2–H6 concern an explicitly labeled undominated-price refinement. No trembling-hand/proper-equilibrium claim is made.

## Prohibited manuscript wording

Do not write:

- “the general-\(N\) Cournot game has a unique SPNE”;
- “Proposition 6 is false” without the continuation-selection qualification;
- “the Hotelling outsourcing equilibrium does not exist”;
- “outsourcing is globally a strategic substitute”;
- “all general-\(N\) asymmetric equilibria are characterized.”

Maximum defensible wording is the exact certificate scope above.

## Evidence maturity

All claims are construction-level \`PROVED\` only. None is theory-frozen before Stage 4A.
