# Stage 4 Preliminary Theorem Certificates

These are construction-level certificates. Stage 4A must certify them independently.

| ID | Exact claim | Attack performed | Evidence artifact | Result | Limitation | State |
|---|---|---|---|---|---|---|
| C1 | Every feasible Cournot sourcing history has a unique quantity equilibrium given by the sorted-cost active-set formula | KKT/active-set derivation; negative-quantity regression | `STAGE_04_MINIMAL_MODEL_GATE.md`; `code/stage04_verify.py` | survives | linear demand / source model only | **PROVED** |
| C2 | Under source SOC, own reduced Cournot payoff is globally strictly concave on ([0,phi]) | branch Hessian + derivative-jump audit at entry/exit | Stage-4 report §4 | survives | source quadratic monitoring cost | **PROVED** |
| C3 | Unique symmetric constrained Cournot SPNE is (i_C^*=min{phi,HND/[b(N+1)^2-H^2N]}) | finite-deviation/global-concavity attack; cap regression | report §§4–5; code | survives | uniqueness is **symmetric**, not global across all (N)-firm asymmetric profiles | **PROVED** |
| C4 | (i_C^*) is weakly decreasing in (N), strictly on interior for (N>1) | exact symbolic differentiation + cap branch | report §6; code | survives | (N) derivative follows source's continuous-(N) comparative-static convention | **PROVED** |
| C5 | Outsourced number is increasing in (phi) on cap branch and decreasing interior; fraction is weakly decreasing | KKT/cap branch + symbolic derivative | report §6; code | survives | statement concerns source parameter domain (D>0) | **PROVED** |
| C6 | Source duopoly global BR is the stated piecewise (B_phi(y)) | enumerate inactive/all-active/monopoly continuations; kink comparisons | report §7; code | survives | pure strategies, source game | **PROVED** |
| C7 | For (4/9<ho<2/3), the global BR contains slope (+2) | explicit kink branch; exact rational witness | report §8; code | survives | cap can flatten the branch if too small | **PROVED** |
| C8 | Duopoly pure equilibrium correspondence has the three stated (ho)-cases | solve piecewise BR fixed points; adversarial parameter search | report §9; code | survives | source duopoly only | **PROVED** |
| H1 | Hotelling price equilibrium is unique for (|d_c|le3	au) and a continuum for (|d_c|>3	au) | complete clipped-demand BR derivation | report §10; code | survives | no additional no-loss refinement | **PROVED** |
| H2 | Earlier Stage-1 Hotelling corner-deviation rejection is selection-dependent | same deviation evaluated under two exact continuation equilibria | report §10; code | opposite profitability obtained | does not characterize all Stage-I SPNE | **PROVED** |

## Quantifier notes

### C3

Maximum defensible prose:

> Under the source parameter restrictions, the corrected **symmetric** Cournot SPNE outsourcing level is the constrained expression (i_C^*).

Prohibited prose:

> The Cournot game has a unique SPNE for general (N).

The latter is not proved and is false already in the source duopoly for some parameters.

### C8

This is a complete pure-strategy equilibrium characterization for the **source duopoly Stage-I game** after exact Cournot continuation.

### H1/H2

These are diagnostic results, not part of the Stage-4A canonical Cournot paper architecture unless later workflow stages explicitly reopen Hotelling.

## Evidence maturity

All listed claims are construction-level `PROVED` subject to independent Stage-4A attack.

No claim is promoted to theory freeze at Stage 4.
