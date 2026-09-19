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
\text{Stage 4 PASS}
\rightarrow
\textbf{Stage 4A NEXT}
}
\]

## Stage-4 final routing decision

Stage 4 was partially reopened only for the Hotelling canonical judgment.

The re-audit proves:

- below-cost Hotelling prices are weakly dominated by marginal-cost pricing;
- the literal source game has off-path corner multiplicity;
- deleting only those weakly dominated prices yields a unique price continuation for every cost gap;
- the source symmetric Hotelling outsourcing candidate then has an exact cap-aware global survival/failure condition.

Therefore the canonical architecture is restored as:

\[
\boxed{\textbf{Candidate E′}}
\]

consisting of:

1. the complete Cournot correction;
2. the literal Hotelling continuation diagnosis;
3. the undominated-price Hotelling refinement and exact Proposition-6 correction.

## Stage-4A frozen inputs

Stage 4A must independently attack, without repair:

### Cournot

1. sorted-cost continuation uniqueness;
2. global strict concavity across active-set changes;
3. corrected symmetric action \(i_C^*\);
4. corrected competition comparative static;
5. boundary comparative statics;
6. source-duopoly global BR;
7. complete pure duopoly equilibrium classification;
8. \(\rho=2/3\) continuum;
9. global failure of Proposition 5;
10. all Cournot regressions.

### Hotelling

11. literal clipped-demand price correspondence;
12. H-DOM weak-dominance theorem for \(p<c\);
13. unique price correspondence after below-cost deletion;
14. complete finite-candidate refined Stage-I BR characterization;
15. exact cap-aware symmetric survival/failure region;
16. Stage-1 exact \(1/90\) refined deviation regression;
17. strict distinction between literal Nash, weak-dominance deletion, and stronger refinements.

Stage 4A may not silently describe \(p\ge c\) as a source primitive or promote the result to trembling-hand/proper equilibrium.

## Fail-closed rule

No material retained continuation is unresolved. Multiplicity in the literal Hotelling game is characterized exactly rather than treated as solver failure.

## Repository-ordering note

Repository existence does not imply canonical Stage 9 PASS.
