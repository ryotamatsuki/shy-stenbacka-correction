# Verification Code

The verification scripts supplement analytical proof and do not replace the theorem certificates.

Pinned Python environment:

```text
Python 3.12
sympy==1.14.0
```

Run the complete frozen Python suite from repository root:

```bash
make verify-python
```

## Stage 1

```bash
python code/stage01_verify.py
```

Reproduces the source-model algebra used by the Stage-1 audit.

## Stage 4 — Cournot and literal Hotelling

```bash
python code/stage04_verify.py
```

Checks the Stage-4 construction algebra and exact regression objects.

## Stage 4 — Hotelling no-loss re-audit

```bash
python code/stage04_hotelling_refinement_verify.py
```

Verifies the exact piecewise Hotelling payoff identities, branch thresholds,
deviation-gain quadratic, critical cap, and the Stage-1 exact `1/90`
counterexample.

Important distinctions:

- literal source Nash multiplicity is not erased;
- `p<c` is weakly dominated by `p=c`, but the auxiliary `p\ge c` game is
  explicitly a no-loss strategy restriction, not elimination of all weakly
  dominated strategies;
- no trembling-hand/proper-equilibrium claim is inferred;
- solver failure is never evidence against a deviation.

## Stage 4A — independent adversarial reconstruction

```bash
python code/stage04a_independent_verify.py
```

Provides a separately written exact evaluator/regression path for the global
Cournot and conditional Hotelling attacks. The analytic clean-room proof remains
canonical in `audit/stage04a_cleanroom_derivation.md`.

## Stage 7 — welfare / benchmark verification

```bash
python code/stage07_welfare_verify.py
```

Checks:

- exact Cournot CS / welfare identity;
- restricted common-sourcing welfare benchmark;
- private-versus-restricted sourcing comparison;
- welfare non-invariance across the certified Cournot equilibrium set;
- exact Hotelling CS / welfare cancellation of prices;
- fixed-sourcing efficient Hotelling allocation;
- fixed-allocation social sourcing benchmark.

This code verifies algebra only. It does not convert a restricted benchmark into
a first-best claim or resolve equilibrium selection.

## Stage 7.5A — function-class kill test

```bash
python code/stage075a_scope_counterexamples.py
```

Reproduces the convex-monitoring counterexample that blocks promotion of the
source-specific C7/C8 results to an arbitrary convex monitoring-cost class.

## CI

`.github/workflows/python-verification.yml` compiles all Python scripts and runs
the full `make verify-python` suite using the pinned dependency file.

The Stage-8 theory freeze controls interpretation of all script output.


## Stage 10 — figure architecture regression

\`\`\`bash
python code/stage10_generate_figure.py
\`\`\`

The generator uses exact rational arithmetic to certify the exposition witness

\[
(\rho,\delta,\phi)=(3/5,1,2),
\]

including \(y_A=1/8\), \(s=10/17\), the positive-slope best-response point
\(B(1/20)=11/10\), and the three pure equilibria. It then writes the TikZ source
used by the manuscript figure.

The generated figure is an exposition object, not a substitute for the analytic
proof or the Stage-4A theorem certificate.
