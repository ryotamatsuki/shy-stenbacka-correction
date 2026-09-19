# Verification Code

Code supplements analytical proof and must never substitute for a global equilibrium argument.

## Stage 1 canonical check

Run:

```bash
python code/stage01_verify.py
```

Pinned dependency:

```text
sympy==1.14.0
```

Expected first line:

```text
PASS: source-model Stage 1 symbolic checks
```

The script checks with exact rational arithmetic:

- the corrected derivative of equation (13) with respect to (N);
- Corollary-4 interior comparative-static derivatives;
- a Cournot outsourcing-cap counterexample that stays on the all-active output branch for every feasible outsourcing pair;
- a separate Cournot history at which the paper's all-active equation (10) would imply negative output;
- a Hotelling outsourcing-cap counterexample;
- a Hotelling profitable deviation from the reported symmetric candidate into a corner market-share regime;
- the symbolic deviation-gain identity
  [
  DeltaPi=rac{n(2H^2n-27	au)}{18}.
  ]

## Source-model discipline

The published monitoring cost is (i_j^2). The canonical Stage-1 script contains no generalized monitoring-cost coefficient.

## Verification policy

Permitted roles include:

- symbolic simplification and factorization;
- inequality verification;
- exact parameter-region checks;
- numerical counterexample search when exact checks are unavailable;
- diagnostic plots.

For every future script record:

- software and package versions;
- exact parameter assumptions;
- deterministic seeds where relevant;
- expected output;
- the audit/manuscript claim checked.

Solver failure, NaN, invalid branch, or nonconvergence is `UNRESOLVED`, never evidence against a deviation.
