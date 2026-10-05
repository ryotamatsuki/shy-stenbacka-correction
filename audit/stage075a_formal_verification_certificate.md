# Stage 7.5A Formal Verification Certificate

Final state:

\[
\boxed{\textbf{FORMAL VERIFICATION PASS}}
\]

Certificate date: 2026-09-19

## 1. Toolchain and provenance

- Proof assistant: Lean 4
- Lean toolchain: \`leanprover/lean4:v4.19.0\`
- Lean commit reported by CI: \`6caaee842e94\`
- Lake: \`5.0.0-6caaee8\`
- mathlib: immutable commit
  \`c44e0c8ee63ca166450922a373c7409c5d26b00b\`
- formal source:
  - \`ShyStenbackaFormal/Stage075A.lean\`
    - certified blob SHA: \`a634b04eb2ec13a632f10928974f8eab96d1d05c\`
  - \`ShyStenbackaFormal.lean\`
    - blob SHA: \`e4a44acff03704dbf427b792d9528cf9a0a3c602\`
- toolchain file blob:
  \`7aca1d8a939cc24c413eddd793671cdce7070b74\`
- Lake config blob:
  \`6669c6b90caf3c05912556109ead89c33400fe6c\`
- CI workflow blob:
  \`886c142e65d35d746cb1803e266aa0d687f7514e\`

Direct dependency is pinned to an immutable mathlib commit. The CI resolves that commit and uses its pinned dependency graph before building the project.

## 2. Clean-build evidence

Final green formal run:

- GitHub Actions run ID: \`35439005968\`
- job ID: \`105886467491\`
- certified branch commit: \`8c575f99daecacd85077ee2db3568dbd362c2004\`
- workflow conclusion: **success**
- build command: \`lake build\`

CI steps all passed:

1. checkout;
2. proof-escape audit;
3. pinned Lean installation;
4. pinned mathlib/dependency resolution;
5. formal build.

The build log ends with:

\`\`\`text
Build completed successfully.
\`\`\`

Earlier failed CI attempts are retained in repository history. They were used to repair build/bootstrap and proof-script issues rather than suppressed.

## 3. Placeholder / project-axiom audit

The workflow rejects project formal source containing:

- \`sorry\`;
- \`admit\`;
- a project declaration beginning with \`axiom\`.

The final green run passed this audit.

The formal source also emits \`#print axioms\` for the high-value theorems.

For the final green build, the reported dependencies are only:

\`\`\`text
[propext, Classical.choice, Quot.sound]
\`\`\`

for the listed formal theorems.

No certified theorem reports \`sorryAx\`.

No project-specific axiom is used.

## 4. Claim-to-formal-theorem map

| Paper / audit claim | Lean theorem | Component certified |
|---|---|---|
| C4 Cournot competition comparative-static core | \`C4_cross_identity\` | exact adjacent-market-size cross-multiplied identity |
| C4 discrete monotonicity core | \`C4_step_negative\` | strict decline between adjacent roots when both denominators are positive |
| C7 active / exit branch consistency | \`C7_active_exit_join\` | exact join at \(y_A\) |
| C7 monopoly / exit branch consistency | \`C7_monopoly_exit_join\` | exact join at \(y_M\) |
| C7 rival-exit branch direction | \`C7_exit_branch_slope_positive\` | positivity of slope \(2\) |
| H2 below-cost dominance algebra | \`H2_below_cost_profit_nonpos\`, \`H2_marginal_cost_profit_zero\` | operating-profit sign core under nonnegative demand |
| H2b attack on marginal-cost pricing | \`H2b_above_cost_profit_nonneg\`, \`H2b_above_cost_profit_strict\` | nonnegative / positive operating-profit core for \(c+\varepsilon\) |
| H5 no-loss deviation core | \`H5_vertex_gain_identity\` | exact gain at \(Hn/2\) |
| H5 positive-gain condition | \`H5_vertex_gain_positive\` | \(27\tau<2H^2n\Rightarrow\Delta(Hn/2)>0\) |
| H6 exact regression | \`H6_exact_regression\` | exact \(1/90\) gain |
| Stage-7 welfare-selection warning | \`W_three_eq_symmetric_value\` | exact comparison \(20/17<3/2\) |

Detailed quantifier/domain comparison is in
\`audit/stage075a_formal_statement_fidelity.md\`.

## 5. Encoded assumptions versus derived facts

### Encoded as hypotheses

The targeted Lean theorems take as hypotheses only the real-algebra / order assumptions needed for the encoded component, for example:

- positivity of \(H,D,b,n\);
- positivity of the relevant Cournot denominators;
- \(N\ge1\) in the continuous-real encoding of the adjacent-\(N\) inequality;
- nonnegative demand for the abstract operating-profit sign lemmas;
- the inequality \(27\tau<2H^2n\) for the positive Hotelling vertex-gain theorem.

### Derived inside Lean

The formal source mechanically derives:

- the relevant algebraic identities;
- signs implied by the stated assumptions;
- exact branch-join identities;
- the exact rational regression.

### Not derived inside Lean

Lean does not derive:

- the source economic primitives from the published paper;
- Nash equilibrium definitions for the full two-stage model;
- the complete Cournot active-set partition;
- global Stage-I payoff concavity;
- exhaustiveness of the complete duopoly BR;
- the entire C8 pure equilibrium correspondence;
- the literal Hotelling price-equilibrium correspondence;
- the finite-candidate no-loss Stage-I BR;
- the full necessary-and-sufficient cap/root characterization of H5-NL;
- mixed-equilibrium claims;
- literature novelty or institutional interpretation.

Those remain certified by the independent Stage-4A and Stage-7.5A analytic audits.

## 6. Statement fidelity

The formal C4 theorem is deliberately discrete-adjacent in its economic content:

\[
i_C(N+1)<i_C(N)
\]

provided the relevant denominators are positive.

This matches the final Stage-7.5A manuscript scope: the economic comparative static is stated over **admissible integer market sizes satisfying the source restrictions**. The continuous derivative is only an auxiliary calculation.

The formal H2/H2b lemmas certify the operating-profit sign logic only. They do not claim that the auxiliary no-loss game is obtained by eliminating all weakly dominated strategies.

The formal H5 theorem certifies a proof-critical gain calculation. It does not by itself certify the whole price subgame or the full iff cap region.

No manuscript claim may be enlarged merely because a narrower algebraic component is kernel-checked.

## 7. Model-boundary certificate

### Formally represented

- selected real-valued formulas;
- algebraic branch joins;
- selected sign inequalities;
- exact counterexample arithmetic.

### Not formally represented

- consumers / demand correspondence as economic structures;
- Nash / SPNE definitions;
- mixed strategies;
- full active-set correspondence;
- strategy-space compactness;
- all asymmetric equilibrium objects;
- planner optimization problems.

Accordingly, the correct description is:

\[
\boxed{
\text{targeted formal verification of the proof-critical algebra/order core}
}
\]

not “formal verification of the entire Shy–Stenbacka model.”

## 8. Why the selected target is sufficient for this gate

Stage 4A already provides independent clean-room mathematical certification of the complete headline pure-strategy objects.

The formal layer targets mechanically fragile, high-consequence components:

- the published sign correction;
- regime-join algebra behind the Proposition-5 correction;
- the Hotelling dominance/refinement-scope attack;
- the exact global-deviation gain;
- the permanent rational counterexample.

Full mechanization of the complete equilibrium correspondence would materially increase implementation cost without replacing the required independent economic-domain audit. It is therefore explicitly excluded rather than silently treated as proved.

## 9. Rollback rule

This certificate becomes stale if any of the following changes materially:

- the source-model formula used in C4;
- the duopoly BR branch definitions;
- the Hotelling gain expression;
- the no-loss strategy-domain interpretation;
- the quantifier/domain assumptions attached to the mapped manuscript claims.

A material change requires rerunning the affected analytic gate and obtaining a new green formal build before refreeze.

## 10. Final formal state

\[
\boxed{\textbf{FORMAL VERIFICATION PASS}}
\]

This certificate applies to the formal source blob and its exact unchanged descendants.
