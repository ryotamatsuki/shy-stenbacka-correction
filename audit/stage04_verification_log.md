# Stage 4 Verification Log

Date: 2026-09-19

## Exact symbolic / rational verification

The Stage-4 construction identities and permanent regression tests were re-executed after replacing fragile SymPy expression-tree equality checks with algebraic equality checks of the form `simplify(lhs-rhs)==0`.

Result:

```text
PASS: all Stage-4 exact construction checks
```

Verified items include:

- general-`N` Cournot symmetric formula and corrected `N` derivative;
- interior comparative-static identities;
- primitive active-set Cournot continuation;
- Stage-1 negative-quantity history;
- outsourcing-cap witness;
- duopoly branch joins;
- positive-slope global-BR witness;
- exact three-equilibrium duopoly regression at `rho=3/5, delta=1, phi=2`;
- Hotelling corner price-equilibrium multiplicity;
- opposite profitability of the same Stage-I Hotelling deviation under two valid corner continuations;
- exact high-selection deviation-gain threshold.

## Independent deterministic fixed-point stress check

As supporting evidence only, the complete source-duopoly Stage-I classification was independently compared against direct numerical fixed-point searches over a grid of representative `rho` values spanning:

- just above `4/9`;
- below and above `1/2`;
- below, at, and above `2/3`;
- larger `rho`.

For each representative `rho`, multiple outsourcing caps `phi` below and above the symmetric fixed point were tested from many starting points.

No counterexample to the Stage-4 three-case pure-equilibrium classification was found.

This deterministic search is **not** used as proof. The proof remains the analytical piecewise best-response derivation.

## Verification semantics

No failed solver call or invalid branch is counted as an unprofitable deviation. No material retained Cournot continuation remains unresolved.


## Hotelling re-audit verification

\`code/stage04_hotelling_refinement_verify.py\` was independently re-executed after the Stage-4 reopening.

Result:

\`\`\`text
PASS: Stage-4 Hotelling undominated-price re-audit
\`\`\`

Exact checks include:

- branch continuity at both Hotelling market-share thresholds;
- source interior stationary response;
- full-market stationary response \(Hn/2\);
- deviation-gain quadratic;
- \(\Delta\Pi_{\max}=n(2H^2n-27\tau)/18\);
- exact roots \(x_\pm\);
- proof ingredient \(x_->i_0+3\tau/H\) on \(27/2<H^2n/\tau<18\);
- Stage-1 regression gain \(1/90\);
- exact critical-cap value in that regression.

No numerical approximation is used as proof.
