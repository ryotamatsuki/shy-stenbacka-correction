# Stage 4 Preliminary Theorem Certificates

These certificates are construction-level. Stage 4A must attack them independently.

| ID | Exact claim | Evidence | State |
|---|---|---|---|
| C1 | Every feasible Cournot sourcing history has a unique pure quantity equilibrium from the sorted-cost active-set formula | Stage-4 report; \`code/stage04_verify.py\` | **PROVED** |
| C2 | Under the source SOC, own reduced Cournot payoff is globally strictly concave on \([0,\phi]\) | Stage-4 report §4 | **PROVED** |
| C3 | Unique symmetric constrained Cournot action is \(i_C^*=\min\{\phi,HND/[b(N+1)^2-H^2N]\}\) | Stage-4 report §§4–5 | **PROVED** |
| C4 | \(i_C^*\) is weakly decreasing in \(N\), strictly on the interior branch for \(N>1\) | Stage-4 report §6; code | **PROVED** |
| C5 | The outsourced fraction is weakly decreasing in \(\phi\); the outsourced number rises on the cap branch and falls on the interior branch | Stage-4 report §6 | **PROVED** |
| C6 | The source-duopoly global BR is the stated piecewise \(B_\phi(y)\) | Stage-4 report §7; code | **PROVED** |
| C7 | For \(4/9<\rho<2/3\), the global Cournot BR contains a slope-\(+2\) segment when feasible | Stage-4 report §8; exact witness | **PROVED** |
| C8 | The source-duopoly pure Stage-I equilibrium correspondence has the three stated \(\rho\)-cases | Stage-4 report §9; verification | **PROVED** |
| H1 | Literal Hotelling pure-price equilibrium is unique for \(|d|\le3\tau\) and a continuum for \(|d|>3\tau\) | \`audit/STAGE_04_HOTELLING_REAUDIT.md\` | **PROVED** |
| H2 | Every price \(p_j<c_j\) is weakly dominated by \(p_j=c_j\) | primitive payoff comparison | **PROVED** |
| H2b | \(p_j=c_j\) is itself weakly dominated by any fixed \(p_j=c_j+\varepsilon\), \(\varepsilon>0\) | primitive payoff comparison; Stage-4A independent verifier | **PROVED** |
| H3-NL | Under the explicit auxiliary restriction \(p_j\ge c_j\), the pure Hotelling price continuation is unique for every cost gap | restricted global price-BR derivation | **PROVED — CONDITIONAL MODEL** |
| H4-NL | Under \(p_j\ge c_j\), the constrained Stage-I pure BR is the finite-candidate argmax in (H-NL2) | branch concavity + projection + boundary audit | **PROVED — CONDITIONAL MODEL** |
| H5-NL | Under source SOC and \(p_j\ge c_j\), the interior symmetric candidate fails iff \(27\tau/2<H^2n<18\tau\) and \(\phi>x_-\) | exact gain quadratic, roots, cap feasibility | **PROVED — CONDITIONAL MODEL** |
| H6-NL | At \(H=n=1,\tau=1/15,\phi=1\), \(i_A'=1/2\) against \(i_B=1/6\) gains \(1/90\) under the no-loss restriction | exact rational regression | **PROVED — CONDITIONAL MODEL** |

## Quantifier and interpretation cautions

- C3 proves a unique **symmetric action**, not uniqueness of the general-\(N\) two-stage equilibrium.
- C8 is complete for **pure Stage-I equilibria of the source duopoly**.
- H1 concerns the literal source pure-price game.
- H2 does **not** imply that retaining only \(p\ge c\) is the same as deleting all weakly dominated strategies; H2b proves the contrary.
- H3-NL through H6-NL are conditional on an explicit no-loss price strategy restriction absent from the source.
- No trembling-hand, proper-equilibrium, admissibility, or mixed-equilibrium uniqueness claim is made.
- No complete asymmetric Hotelling Stage-I equilibrium correspondence is claimed.

## Prohibited manuscript wording

Do not write:

- “Shy–Stenbacka assumed \(p\ge c\)”;
- “elimination of weakly dominated strategies uniquely selects \(p_{\rm high}=c_{\rm high}\)”;
- “the no-loss equilibrium is an undominated-strategy equilibrium”;
- “the Hotelling candidate is false in every literal-game SPNE”;
- “the no-loss price equilibrium is unique over mixed strategies”;
- “the general-\(N\) Cournot game has a unique SPNE.”

## Evidence maturity

All claims remain construction-level until Stage 4A certification.
