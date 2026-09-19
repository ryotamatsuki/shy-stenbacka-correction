# Paper source

Stage 10 manuscript construction is modular and bound by the canonical Stage-8 theory freeze.

Canonical entry point:

- \`paper/manuscript.tex\`

Sections:

- \`sections/01_introduction.tex\`
- \`sections/02_model.tex\`
- \`sections/03_best_responses.tex\`
- \`sections/04_equilibrium.tex\`
- \`sections/05_implications.tex\`
- \`sections/05a_welfare_scope.tex\`
- \`sections/05b_related_literature.tex\`
- \`sections/06_conclusion.tex\`
- \`sections/appendix.tex\`

Bibliography:

- \`references.bib\`

Figure generator:

- \`../code/stage10_generate_figure.py\`

Generated figure input:

- \`generated/duopoly_best_response.tex\` (created by the build; not canonical source)

Build from repository root:

\`\`\`bash
make paper
\`\`\`

The build first regenerates the exact Stage-10 best-response figure and then runs \`latexmk\`.

The Stage-8 freeze controls all theorem wording. In particular, the manuscript claims complete equilibrium characterization only for the **pure Stage-I source duopoly** and pure-price Hotelling continuations within their stated domains.
