# Stage 10 — Figure / Table Architecture Gate

Status: **PASS**

Date: 2026-09-19  
Workflow: `research-paper-workflow` v2.2  
Theory authority: `audit/STAGE_08_CANONICAL_THEORY_FREEZE.md`

## Governing rule

Every retained exposition vehicle must reduce the cost of understanding a certified result.  Figures and tables do not create new evidence and may not widen theorem scope.

## Architecture

| Result / object | Primary exposition vehicle | Secondary vehicle | Generator / source | Scope control |
|---|---|---|---|---|
| Corrected Proposition 3 / equation-(14) sign | Proposition + displayed derivative | concise Introduction summary | analytic frozen proof; Python regression suite | admissible integer (N); strict only off cap |
| Global failure of Proposition 5 | Proposition | **Figure 1: exact global BR witness** | `code/stage10_generate_figure.py` | source duopoly; pure Stage I; no global-complements claim |
| Complete pure source-duopoly equilibrium correspondence | Proposition | **Table 1: parameter regimes** | exact theorem certificate | pure Stage I only; no mixed completeness |
| Exact three-equilibrium witness | Figure 1 + displayed exact triple | prose | exact rational generator assertions | ((\rho,\delta,\phi)=(3/5,1,2)) only |
| Literal Hotelling continuation | Proposition | concise prose | analytic Stage-4A certificate | pure-price equilibria only |
| Auxiliary no-loss Hotelling failure region | Proposition | exact (1/90) numerical illustration | analytic certificate + exact regression scripts | explicit (p_j\ge c_j); pure scope |
| Cournot welfare selection dependence | displayed exact inequality | prose | `code/stage07_welfare_verify.py` + Lean core | no selection-free welfare ranking |
| Hotelling welfare diagnostics | concise equations / prose | none | Stage-7 welfare certificate | benchmark labels remain restricted |
| Functional-form limitation | exact counterexample in prose | none | `code/stage075a_scope_counterexamples.py` | blocks generic convex-monitoring theorem |
| Institutional bridge | concise prose | citations | frozen Stage-7 institutional record | no empirical validation of exact quadratic technology |
| Literature / theorem-absorption boundary | prose | citations | Stage-6 absorption map | source-specific correction only |
| Formal-verification scope | concise prose | repository provenance | Stage-7.5A formal certificate | proof-critical core only |

## Figure 1 regression design

Figure 1 uses the exact source-admissible witness

[
\rho=\frac35,qquad
\delta=1,qquad
\phi=2.
]

The generator asserts

[
y_A=\frac18,qquad
s=\frac{10}{17},
]

and exact best-response values including

[
B(0)=1,qquad
B\left(\frac1{20}\right)=\frac{11}{10},qquad
B(1)=0.
]

It also asserts (B(s)=s) before writing the TikZ input.  Thus the figure preserves the actual sign, thresholds, action scale, and equilibrium coordinates rather than using arbitrary normalization.

Canonical generator:

`code/stage10_generate_figure.py`.

Generated output:

`paper/generated/duopoly_best_response.tex`.

The generated output is a build artifact; the Python generator is canonical.

## Table 1 design

Table 1 reports the exact five pure-equilibrium regimes from the frozen C8 correspondence.  No cell summarizes mixed equilibria or general-(N) Stage-I uniqueness.

## Omitted visuals

No welfare figure is retained.  The welfare contribution is diagnostic and selection-sensitive; the exact inequality is clearer than a graph.

No Hotelling parameter-region figure is retained.  The result is secondary and the exact inequalities in Proposition~H5-NL are sufficiently compact.

No generic mechanism phase diagram is retained because the Stage-6/7.5A audits prohibit presenting the source-functional-form thresholds as a general investment-game taxonomy.

## Gate verdict

Every headline result has an explicit primary exposition vehicle.  Every quantitative visual is generated from exact verified values, has retained generator source, and is interpreted in the manuscript.

[
\boxed{\textbf{FIGURE / TABLE ARCHITECTURE GATE — PASS}}
]
