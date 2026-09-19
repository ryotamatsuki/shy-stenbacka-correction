# Reproducibility Guide

This repository is the production research repository for the Shy–Stenbacka correction project after the canonical Stage-8 theory freeze.

Canonical theory freeze input:

- Stage-8 checkpoint: `2fbcf47ff18ea3650d307d90cbdeab78ddb63256`
- freeze record: `audit/STAGE_08_CANONICAL_THEORY_FREEZE.md`
- workflow: `research-paper-workflow` v2.2
- workflow commit: `42574d6c5931275ccff3ef7e8b4acc188077332a`

Reproduction must not alter the frozen model, theorem scope, solution concepts, or benchmark definitions.

## 1. Python verification environment

Runtime:

```text
Python 3.12
```

Dependency lock:

```text
sympy==1.14.0
```

Setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the full Python verification suite:

```bash
make verify-python
```

This executes, in order:

1. `code/stage01_verify.py`
2. `code/stage04_verify.py`
3. `code/stage04_hotelling_refinement_verify.py`
4. `code/stage04a_independent_verify.py`
5. `code/stage07_welfare_verify.py`
6. `code/stage075a_scope_counterexamples.py`

The scripts are algebraic/regression evidence. They do not replace the analytic theorem certificates.

## 2. Lean formal verification environment

Pinned toolchain:

```text
leanprover/lean4:v4.19.0
```

Pinned mathlib commit:

```text
c44e0c8ee63ca166450922a373c7409c5d26b00b
```

Build:

```bash
lake update
lake exe cache get
make verify-formal
```

Formal source:

- `ShyStenbackaFormal/Stage075A.lean`
- root import: `ShyStenbackaFormal.lean`

The formal layer covers only the proof-critical core mapped in
`audit/stage075a_formal_statement_fidelity.md`.

It is not a complete mechanization of the economic model.

## 3. Combined verification

With Python, Lean, Lake, and the pinned dependencies installed:

```bash
make verify
```

GitHub Actions separately run:

- `.github/workflows/python-verification.yml`
- `.github/workflows/lean.yml`

The Python workflow compiles all verification scripts before running the frozen suite.
The Lean workflow rejects `sorry`, `admit`, and project-specific `axiom` declarations before `lake build`.

## 4. Manuscript build

The current Stage-9 manuscript is intentionally skeletal; substantive paper construction begins at Stage 10.

When a TeX environment with `latexmk` is installed:

```bash
make paper
```

Canonical manuscript inputs:

- `paper/manuscript.tex`
- `paper/references.bib`

Stage 10 may modularize the manuscript, but it may not change frozen theory without rollback under the Stage-8 change-control rules.

## 5. Certification and audit artifacts

The canonical theorem-certification records remain in `audit/`; the directory is the project's equivalent of the workflow's recommended `theorem_certificates/` store.

Index:

- `theorem_certificates/README.md`

The current Lean source remains in `ShyStenbackaFormal/`; this is the project's canonical formal source directory. A compatibility index is retained at:

- `formal/README.md`

Do not duplicate theorem text or formal source into competing canonical copies.

## 6. Counterexamples and regression evidence

Permanent negative/regression evidence is indexed in:

- `audit/counterexample_regression_register.md`

These counterexamples are part of the research provenance. They must not be deleted merely because they constrain manuscript claims.

## 7. Reproducibility boundary

A green build establishes only that the checked scripts/formal statements reproduce successfully under their declared scope.

It does not, by itself:

- widen pure-strategy results to mixed strategies;
- convert targeted Lean results into a formal proof of the full game;
- eliminate equilibrium-selection dependence;
- promote baseline source-functional-form results to general function-class theorems;
- authorize any theory change after Stage 8.

Any such change requires rollback to the earliest affected canonical gate.
