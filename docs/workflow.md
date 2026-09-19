# Canonical Workflow Routing

This repository follows \`ryotamatsuki/research-paper-workflow\` v2.2.

Pinned workflow commit:

\`42574d6c5931275ccff3ef7e8b4acc188077332a\`

## Current state

\[
\boxed{
\text{Stage 1 PASS}
\rightarrow
\text{Stage 2 PASS}
\rightarrow
\text{Stage 3 PASS}
\rightarrow
\text{Stage 4 PASS (AMENDED)}
\rightarrow
\text{Stage 4A PASS}
\rightarrow
\text{Stage 6 PASS}
\rightarrow
\text{Stage 7 PASS}
\rightarrow
\text{Stage 7.5 PASS}
\rightarrow
\text{Stage 7.5A PASS}
\rightarrow
\text{Stage 8 PASS}
\rightarrow
\textbf{Stage 9 NEXT}
}
\]

Stage 5 was not triggered.

## Stage-7.5A verdict

\[
\boxed{\textbf{GO — GENERALITY / QUANTIFIER CERTIFICATION PASS}}
\]

Formal gate:

\[
\boxed{\textbf{FORMAL VERIFICATION PASS}}
\]

## Frozen claim scopes entering Stage 8

### General-\(N\) Cournot

- unique pure downstream quantity continuation for every feasible sourcing history;
- globally strictly concave own reduced sourcing payoff under source SOC;
- unique **symmetric pure Stage-I action**;
- competition comparative static stated over admissible integer market sizes satisfying the source restrictions.

No general-\(N\) all-equilibrium uniqueness claim is authorized.

### Source duopoly

- complete **pure Stage-I** global best response and equilibrium correspondence;
- Proposition 5 false as a global strategic-substitutes claim;
- positive-slope rival-exit branch does not imply global strategic complements.

### Hotelling

- literal **pure-price** continuation: unique or exactly characterized multiple;
- auxiliary \(p\ge c\) game: conditional no-loss robustness only;
- no trembling-hand / proper / admissibility / mixed-equilibrium claim.

### Welfare

- exact accounting identities;
- planner/benchmark labels frozen;
- Cournot equilibrium welfare is selection-dependent where Stage-I multiplicity exists.

### Generality

Exact results remain baseline/source-functional-form theorems.

A Stage-7.5A convex-monitoring counterexample blocks any generic promotion of C7/C8.

## Formal verification boundary

Lean 4.19.0 + pinned mathlib commit
\`c44e0c8ee63ca166450922a373c7409c5d26b00b\`.

Final green formal run:
\`35439005968\`.

The formal layer certifies selected proof-critical algebra/order statements, not the complete economic game.

## Stage-8 verdict

\[
\boxed{\textbf{CANONICAL STAGE 8 — PASS}}
\]

\[
\boxed{\textbf{THEORY FROZEN}}
\]

Canonical freeze artifact:

\`audit/STAGE_08_CANONICAL_THEORY_FREEZE.md\`

Stage 8 freezes:

- canonical source model and strategy domains;
- theorem statements at the Stage-7.5A certified quantifiers;
- pure-strategy / pure-price solution-concept boundaries;
- welfare benchmark labels and selection dependence;
- source-specific novelty boundary;
- baseline-only generality boundary;
- formal-verification scope, toolchain, dependency, CI, and axiom/placeholder provenance;
- explicit claims not made;
- rollback rules for every post-freeze theory change.

No theorem widening or new extension is authorized after the freeze without rollback to the earliest affected gate.

## Stage-9 contract

Stage 9 must now convert the existing research repository into the production reproducibility layout required by workflow v2.2 without changing the frozen theory.
