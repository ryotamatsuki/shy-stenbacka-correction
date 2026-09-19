# Shy–Stenbacka Correction

Reproducible adversarial equilibrium audit and correction project for Shy & Stenbacka (2005).

## Project status

**Stage 0 — repository initialized.**

The project begins from the published version of the original article and reconstructs the model before any correction claim is frozen.

Primary audit targets:

- constrained best-response correspondences;
- the full-outsourcing boundary case \(i=\phi\);
- asymmetric deviations;
- the Hotelling-side equilibrium conditions;
- downstream effects on Proposition 3, Corollary 4, and Proposition 5;
- exact separation of interior, boundary, and excluded parameter regions.

## Repository policy

- `main` is the stable project history.
- Mathematical audit work is developed on dedicated branches.
- No headline correction claim is treated as final until the complete equilibrium correspondence has been checked.
- Published-version equations and propositions must be traceable to their exact source locations.
- Numerical or symbolic checks supplement, but do not replace, analytical proof.
- Copyrighted source PDFs are not committed unless redistribution is clearly permitted.

## Planned structure

```text
audit/        adversarial audit records and theorem-impact tracking
derivations/  clean mathematical derivations
paper/        correction-note manuscript and bibliography
code/         symbolic/numerical verification
sources/      source manifest and provenance notes
docs/         workflow, stage gates, and decisions
```

## Current branch

Initial mathematical work proceeds on:

`audit/full-equilibrium-correspondence`

## Reproducibility principle

Every correction claim should be recoverable from:

1. the published model as transcribed and canonicalized;
2. explicit feasible sets and boundary conditions;
3. complete unilateral-deviation checks;
4. a proposition-level impact map;
5. independently reproducible algebra/code where useful.
