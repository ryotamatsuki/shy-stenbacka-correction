# Stage 10 Figure/Table Architecture Gate

Status: **IMPLEMENTED — PENDING FINAL STAGE-10 CLOSE RECORD**

Theory authority:

- \`audit/STAGE_08_CANONICAL_THEORY_FREEZE.md\`
- Stage-8 checkpoint \`2fbcf47ff18ea3650d307d90cbdeab78ddb63256\`

The architecture follows the workflow rule that every headline result receives one primary exposition vehicle. No visual is included merely for decoration.

| Frozen result / issue | Primary vehicle | Manuscript location | Generator / evidence | Status |
|---|---|---|---|---|
| C1 global nonnegative-quantity continuation | Lemma + active-set equations | Section 2/3 | analytic proof; Stage-4A certificate | implemented |
| C2 global own-payoff concavity | Lemma + branch-curvature equation | Section 3 | analytic proof; Stage-4A certificate | implemented |
| C3/C4 corrected symmetric action and Proposition-3 sign | Proposition + displayed derivative | Section 3 | exact analytic identity; Lean proof-critical core | implemented |
| C5 cap qualification / Corollary 4 | concise prose | Section 3 | Stage-4A / Stage-8 freeze | implemented |
| C7 global Proposition-5 failure | Proposition + **Figure 1** | Section 3 | \`code/stage10_generate_figure.py\` | implemented |
| C8 complete pure source-duopoly correspondence | Proposition + **Table 1** | Section 4 | theorem certificate; exact regression | implemented |
| H1 literal Hotelling continuation multiplicity | Proposition + equations | Section 5 | Stage-4A theorem certificate | implemented |
| H2/H2b weak-dominance facts | concise prose | Section 5 | primitive payoff comparison | implemented |
| H3--H6-NL no-loss robustness | Proposition + exact \(1/90\) regression | Section 5 | analytic certificate + exact code/Lean core | implemented |
| Cournot welfare selection | exact equation/regression, no figure | Section 6 | \`code/stage07_welfare_verify.py\` | implemented |
| Hotelling welfare diagnostics | concise equations/prose, no figure | Section 6 | Stage-7 welfare certificate | implemented |
| function-class limitation | counterexample prose | Section 6 | \`code/stage075a_scope_counterexamples.py\` | implemented |
| source-specific novelty boundary | related-literature prose | Section 7 | Stage-6 absorption map | implemented |

## Figure 1 — global source-duopoly best responses

Canonical witness:

\[
(\rho,\delta,\phi)=\left(\frac35,1,2\right).
\]

Exact generated values:

- \(y_A=1/8\);
- symmetric fixed point \(s=10/17\);
- \(B(0)=1\);
- \(B(1/20)=11/10\);
- equilibria \((10/17,10/17)\), \((1,0)\), and \((0,1)\).

Generator:

\`code/stage10_generate_figure.py\`.

Output consumed by LaTeX:

\`paper/generated/duopoly_best_response.tex\`.

The generator uses exact rational arithmetic and fails if the frozen regression identities change. The figure is therefore reproducible and regression-checked, while remaining an exposition object rather than proof.

## Table 1 — pure Stage-I equilibrium regimes

Table 1 is a theorem-scope table rather than a calibrated quantitative table. It summarizes the exact regime partition already proved in C8:

- \(\rho>2/3\);
- \(\rho=2/3\) with cap split;
- \(4/9<\rho<2/3\) with cap split.

No external data or arbitrary normalization is used.

## Deliberately omitted visuals

No welfare figure is used because welfare is selection-dependent in the Cournot multiplicity region and is not a headline contribution.

No Hotelling parameter-region figure is used at Stage 10 because the no-loss result is a secondary conditional robustness result; the exact inequalities and rational regression communicate the scope more directly.

No empirical/institutional figure is used because the paper does not estimate or calibrate the model.

## Gate result

Every headline Stage-8 result has an explicit primary exposition vehicle. The only quantitative figure is deterministically generated from the certified exact regression.
