# Stage 9 — Repository / Reproducibility Setup

Status:

\[
\boxed{\textbf{CANONICAL STAGE 9 — PASS}}
\]

Date: 2026-09-19  
Workflow: `research-paper-workflow` v2.2  
Pinned workflow commit: `42574d6c5931275ccff3ef7e8b4acc188077332a`  
Stage-8 theory-freeze input: `2fbcf47ff18ea3650d307d90cbdeab78ddb63256`

## 1. Objective

Stage 9 converts the already-existing research repository into the canonical
production/reproducibility repository required after theory freeze.

Repository existence before Stage 9 did not count as Stage-9 completion. The
gate closes only after the frozen theory, verification code, formal source,
manuscript entry point, build commands, dependency pins, CI, negative-regression
evidence, and provenance records are connected by auditable reproduction paths.

No theory change is authorized or introduced here.

## 2. Stage-8 input integrity

The Stage-8 canonical theory record remains:

`audit/STAGE_08_CANONICAL_THEORY_FREEZE.md`.

Stage 9 does not modify:

- source-model primitives;
- strategy domains;
- equilibrium concepts;
- theorem statements or quantifiers;
- source-duopoly equilibrium correspondence;
- welfare benchmark definitions;
- novelty/generality boundaries;
- formal theorem statements or encoded hypotheses.

The Stage-7.5A formal source, Lean toolchain, mathlib pin, and certificate blobs
are unchanged from the certified green formal run.

## 3. Production repository layout

The Stage-9 production layout is now explicit.

### Manuscript

- `paper/manuscript.tex`
- `paper/references.bib`
- `paper/sections/01_introduction.tex`
- `paper/sections/02_model.tex`
- `paper/sections/03_best_responses.tex`
- `paper/sections/04_equilibrium.tex`
- `paper/sections/05_implications.tex`
- `paper/sections/06_conclusion.tex`
- `paper/README.md`

The manuscript remains deliberately skeletal. Stage 9 establishes modular
architecture only; Stage 10 supplies substantive exposition.

### Mathematical verification code

- `code/stage01_verify.py`
- `code/stage04_verify.py`
- `code/stage04_hotelling_refinement_verify.py`
- `code/stage04a_independent_verify.py`
- `code/stage07_welfare_verify.py`
- `code/stage075a_scope_counterexamples.py`
- `code/README.md`

### Theorem / scope certification

The canonical certificate files remain under `audit/` to preserve their
Stage provenance.

A discoverability index is provided at:

`theorem_certificates/README.md`.

This is the project-equivalent implementation of the workflow's recommended
`theorem_certificates/` store; the index does not duplicate or fork canonical
certificate content.

### Formal verification

Canonical formal source remains at:

- `ShyStenbackaFormal/Stage075A.lean`
- `ShyStenbackaFormal.lean`
- `lakefile.toml`
- `lean-toolchain`

A compatibility/discoverability index is provided at:

`formal/README.md`.

### Negative/regression provenance

Permanent counterexamples and scope-kill tests are indexed at:

`audit/counterexample_regression_register.md`.

They include:

- literal Hotelling pure-price multiplicity;
- the failed “undominated-price refinement” interpretation;
- Proposition-5 positive-slope global-BR witness;
- exact three-equilibrium Cournot regression;
- welfare selection inequality;
- exact `1/90` no-loss Hotelling deviation;
- convex-monitoring function-class counterexample.

## 4. Environment and dependency specification

### Python

Runtime:

```text
Python 3.12
```

Pin:

`.python-version`.

Dependency lock:

```text
sympy==1.14.0
```

in `requirements.txt`.

### Lean

Toolchain:

```text
leanprover/lean4:v4.19.0
```

Mathlib:

```text
c44e0c8ee63ca166450922a373c7409c5d26b00b
```

Both remain identical to the Stage-7.5A formal certificate.

### TeX

The manuscript build is executed in CI on Ubuntu with `latexmk` and the
required TeX Live packages installed explicitly by the workflow.

## 5. Single-entry reproduction commands

Repository-level `Makefile` now defines:

```bash
make verify-python
make verify-formal
make verify
make paper
```

The reproduction guide is:

`REPRODUCIBILITY.md`.

This file records environment setup, command order, canonical evidence paths,
and the limits of what a green build certifies.

## 6. Python CI gate

Workflow:

`.github/workflows/python-verification.yml`.

The workflow:

1. checks out the repository;
2. installs the runtime from `.python-version`;
3. installs the exactly pinned `requirements.txt`;
4. byte-compiles `code/`;
5. runs the complete `make verify-python` suite.

Green Stage-9 run:

- run ID: `35442666402`;
- head: `b4e8e2d807b6342d5cdd73286afbd8e2baecfadb`;
- conclusion: **success**.

A subsequent pull-request run at the Stage-9 manuscript-CI commit also passed:

- run ID: `35442684260`;
- head: `32b297e7ee0370886de289eecde191d60a4a6464`;
- conclusion: **success**.

No Python verification failure remains unresolved.

## 7. Lean formal CI gate

Workflow:

`.github/workflows/lean.yml`.

The Stage-7.5A final green evidence remains controlling because Stage 9 did not
modify any formal source, toolchain, Lake configuration, or workflow blob.

Certified run:

- run ID: `35439005968`;
- formal-source commit: `8c575f99daecacd85077ee2db3568dbd362c2004`;
- conclusion: **success**;
- `lake build`: success;
- proof-escape audit: success;
- no `sorry`, `admit`, project-specific `axiom`, or `sorryAx` in the
  certified theorem output.

Formal coverage remains **PROOF-CRITICAL CORE**, not full-model mechanization.

## 8. Manuscript build gate

Workflow:

`.github/workflows/manuscript.yml`.

The workflow creates a clean Ubuntu TeX environment and executes:

```bash
make paper
```

Green Stage-9 push run:

- run ID: `35442682700`;
- head: `32b297e7ee0370886de289eecde191d60a4a6464`;
- conclusion: **success**.

All steps passed:

1. checkout;
2. TeX tool installation;
3. manuscript skeleton build.

Thus the Stage-10 authoring entry point is known to compile before substantive
section construction begins.

## 9. Artifact manifest

Canonical Stage-9 evidence map:

`audit/stage09_artifact_manifest.md`.

The manifest records content-addressed blob SHAs for:

- Stage-8 freeze and theorem/scope certificates;
- Lean source/toolchain/config;
- Python runtime/dependencies/scripts/workflow;
- manuscript source/layout/workflow;
- reproduction entry points.

The final Stage-9 branch commit pins the complete repository tree.

## 10. Reproducibility semantics

The following distinctions are permanent.

A green Python run is reproducibility evidence for the encoded algebra and exact
regressions; it is not an independent replacement for the analytic proof.

A green Lean build certifies the encoded theorem statements under encoded
hypotheses; it does not certify unformalized equilibrium construction or the
complete economic game.

A green manuscript build certifies source/build integrity only; it does not
certify mathematical correctness or journal compliance.

The Stage-8 theory freeze remains controlling over all three layers.

## 11. Stage-9 kill tests

### Competing canonical copies

**PASS.**

Indexes point to authoritative files rather than duplicating theorem/formal
content.

### Unpinned proof dependency

**PASS.**

SymPy, Lean, and mathlib are pinned at the declared Stage-9 scope.

### Missing one-command verification path

**PASS.**

`Makefile` provides the canonical entry points.

### Verification scripts not exercised in CI

**PASS.**

The full Python verification suite has a green clean-run CI result.

### Formal source disconnected from CI

**PASS.**

The formal source remains attached to the certified Lean workflow.

### Manuscript source not buildable from repository structure

**PASS.**

The modular Stage-9 skeleton has a green clean-environment smoke build.

### Counterexamples lost during production cleanup

**PASS.**

A permanent regression register is present.

### Theory drift during repository setup

**PASS.**

No Stage-8 theorem, model, quantifier, or solution-concept object was changed.

## 12. Open items correctly deferred downstream

The following are not Stage-9 blockers:

- substantive manuscript prose — Stage 10;
- final figure/table architecture — Stage 10 and Stage 13;
- fresh hostile referee attack on the completed manuscript — Stage 11;
- journal choice and live journal requirements — Stage 12 onward;
- submission-level clean rebuild and final PDF inspection — Stage 14;
- immutable submission tag/archive — Stage 15.

These are downstream workflow obligations, not missing Stage-9 evidence.

## 13. Verdict

No material Stage-9 reproducibility field remains unresolved.

\[
\boxed{\textbf{CANONICAL STAGE 9 — PASS}}
\]

\[
\boxed{\textbf{PRODUCTION REPOSITORY / REPRODUCIBILITY SETUP COMPLETE}}
\]

Route:

\[
\boxed{\textbf{STAGE 10 — SECTION-BY-SECTION PAPER CONSTRUCTION}}
\]

Stage 10 may add exposition and exposition vehicles only within the canonical
Stage-8 theory boundary. Any substantive theory change requires rollback under
the Stage-8 change-control rules.
