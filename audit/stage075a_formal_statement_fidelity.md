# Stage 7.5A Formal Statement-Fidelity Map

Status: **PASS — FINAL GREEN BUILD VERIFIED**

## Formal boundary

The Lean artifact is a targeted proof-critical certificate. It does not encode or prove the entire economic game.

Formal source:

- `ShyStenbackaFormal/Stage075A.lean`
- root `ShyStenbackaFormal.lean`

Pinned environment:

- Lean `v4.19.0`;
- mathlib commit `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

## Paper-claim ↔ formal-theorem map

| Paper claim | Lean theorem | Encoded assumptions | Formally certified | Explicitly outside Lean |
|---|---|---|---|---|
| C4 discrete decline of interior symmetric Cournot root | `C4_cross_identity`, `C4_step_negative` | real parameters; positive H,D,b; (N\ge1); adjacent denominators positive | exact adjacent-(N) algebra and strict inequality | derivation of source formula from Nash equilibrium; integer typing of economic N; cap |
| C7 source-duopoly BR joins | `C7_active_exit_join`, `C7_monopoly_exit_join` | real δ,ρ and nonzero denominators | exact branch-join identities | proof that these branches exhaust the global BR; economic regime derivation |
| C7 positive rival-exit slope | `C7_exit_branch_slope_positive` | none beyond real arithmetic | positivity of slope 2 | global optimality / feasibility of the branch |
| H2 below-cost dominance sign core | `H2_below_cost_profit_nonpos`, `H2_marginal_cost_profit_zero` | nonnegative demand; (p<c) | operating-profit sign comparison skeleton | Hotelling demand derivation; full dominance mapping across strategy space |
| H2b marginal-cost price is itself dominated | `H2b_above_cost_profit_nonneg`, `H2b_above_cost_profit_strict` | ε>0; demand nonnegative/positive | above-cost profit sign skeleton | existence of positive-demand rival prices in economic model |
| H5 no-loss global-deviation threshold core | `H5_vertex_gain_identity`, `H5_vertex_gain_positive` | real parameters; (n>0); (27τ<2H^2n) for positivity theorem | exact gain at (Hn/2) and positivity implication | derivation of piecewise Stage-I payoff; cap/root necessity-and-sufficiency |
| H6 exact source-admissible regression | `H6_exact_regression` | constants encoded exactly | exact (1/90) gain | economic feasibility / price-continuation derivation |
| Stage-7 welfare-selection warning | `W_three_eq_symmetric_value` | exact rational welfare values supplied | (20/17<3/2) | derivation of those values from primitives |

## Conclusion-smuggling audit

The formal source:

- does not define a condition named “equilibrium” and then prove the same condition;
- does not encode the desired sign as an assumption;
- does not define the branch joins by equality;
- does not assume the (1/90) conclusion;
- does not contain a project-specific axiom.

The CI rejects:

- `sorry`;
- `admit`;
- project source lines declaring `axiom`.

## Axiom boundary

The expected `#print axioms` output may contain Lean/mathlib standard logical dependencies such as:

- `propext`;
- `Classical.choice`;
- `Quot.sound`.

The formal certificate fails if `sorryAx` appears for any certified theorem.

## Statement-fidelity limitation

A green build certifies only the encoded algebra/order statements.

The following remain certified analytically by Stage 4A rather than formally in Lean:

- construction of the Cournot active-set continuation;
- global own-payoff concavity across every active-set transition;
- complete pure source-duopoly equilibrium correspondence;
- literal Hotelling pure-price correspondence;
- the complete finite-candidate no-loss Stage-I BR;
- necessity and sufficiency of the full cap-aware H5-NL region;
- all economic interpretation and literature/novelty claims.

The paper and repository must not describe this targeted formalization as “formal verification of the whole Shy–Stenbacka model.”


## Final build state

The final targeted formal source built successfully in GitHub Actions run `35439005968` at certified formal-source commit `8c575f99daecacd85077ee2db3568dbd362c2004`.

The formal source blob used by the current branch is unchanged from that green build.

Final state:

[
oxed{	extbf{FORMAL VERIFICATION PASS}}
]
