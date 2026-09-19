# Paper source

The manuscript is modularized at Stage 9 so Stage 10 can construct sections without changing the repository architecture.

Canonical entry point:

- `paper/manuscript.tex`

Section files:

- `sections/01_introduction.tex`
- `sections/02_model.tex`
- `sections/03_best_responses.tex`
- `sections/04_equilibrium.tex`
- `sections/05_implications.tex`
- `sections/06_conclusion.tex`

Bibliography:

- `references.bib`

Build from repository root:

```bash
make paper
```

Stage 9 does not populate substantive prose. Stage 10 must construct the paper from the canonical Stage-8 theory freeze and may not widen any theorem or solution concept.
