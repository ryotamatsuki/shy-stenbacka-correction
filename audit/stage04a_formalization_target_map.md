# Stage 4A Preliminary Formal-Verification Target Map

Decision:

\[
\boxed{\textbf{FORMALIZATION APPLICABLE}}
\]

Reason: the correction project contains published-result reversals, exact parameter inequalities, piecewise best responses, equilibrium multiplicity, boundary logic, and an exact nonlocal-deviation threshold. Targeted kernel-checked formalization would materially reduce residual proof risk.

Implementation is not required for Stage 4A. The formal-verification gate must close before theory freeze at Stage 7.5A.

| Claim | Proof-critical component | Proposed target | Excluded from first target | Assurance gain |
|---|---|---|---|---|
| C1 | unique Cournot continuation | strict concavity of potential \(\Phi\) and KKT uniqueness on nonnegative orthant | full economic interpretation | certifies continuation uniqueness independently of active-set code |
| C2 | global own-payoff concavity | branch curvature plus downward derivative jumps at rival exits | automated enumeration of arbitrary active-set order | certifies fragile globality step |
| C4 | Proposition-3 sign reversal | exact factorization of \(\partial\bar i_C/\partial N\) and denominator positivity | integer-\(N\) exposition | high-value published sign correction |
| C6/C7 | duopoly global BR / Prop.5 failure | branch thresholds \(y_M,y_A\), join identities, nonempty slope-\(+2\) region | prose interpretation | certifies piecewise case logic |
| C8 | complete pure duopoly correspondence | fixed-point classification for \(\rho>2/3,\rho=2/3,4/9<\rho<2/3\) with cap | general-\(N\) asymmetric game | certifies multiplicity/exactly-three/continuum claims |
| H1 | literal Hotelling price correspondence | global clipped-demand price BR and corner continuum | mixed price equilibria | certifies source-faithful continuation result |
| H2/H2b | dominance facts | \(p<c\preceq c\) and \(c\preceq c+\varepsilon\) under nonnegative demand | refinement philosophy | prevents future mislabeling |
| H5-NL | no-loss symmetric failure region | gain quadratic, roots, ordering \(x_->i_0+3\tau/H\), equivalence with cap condition | source-game attribution | certifies exact robustness threshold |
| H6-NL | exact regression | rational \(1/90\) gain | none | permanent executable counterexample |

## Preferred proof assistant

Lean 4 + mathlib.

## Priority order

1. C4 sign reversal.
2. H5-NL threshold and H6-NL exact regression.
3. C6/C7 branch joins and positive-slope region.
4. C8 pure duopoly fixed-point classification.
5. H2/H2b dominance.
6. C1/C2 global concavity core.
7. H1 full literal price correspondence.

## Model-boundary requirement

Formal artifacts must distinguish:

- statements proved from algebra/order hypotheses;
- economic primitives supplied as assumptions;
- literal source game versus auxiliary no-loss game;
- pure equilibrium versus any mixed-equilibrium object not formalized.

No formal theorem may encode \(p\ge c\) as if it were a source assumption.
