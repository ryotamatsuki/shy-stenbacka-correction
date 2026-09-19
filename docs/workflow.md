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
\textbf{Stage 4A IN PROGRESS}
}
\]

## Stage-4 amendment triggered by Stage 4A

The independent red-team found that the earlier label “undominated-price refinement” was too strong.

Facts:

1. every \(p<c\) is weakly dominated by \(p=c\);
2. but \(p=c\) is itself weakly dominated by any fixed \(p=c+\varepsilon\);
3. therefore retaining \(p=c\) while deleting only \(p<c\) is not equivalent to eliminating all weakly dominated strategies.

The Hotelling auxiliary model is therefore now stated explicitly as a **no-loss price restriction**

\[
p_j\ge c_j,
\]

not as an admissibility/trembling-hand/proper-equilibrium result.

## Canonical architecture

\[
\boxed{\textbf{HYBRID}}
\]

- Cournot = main source-faithful theorem package.
- Hotelling literal game = secondary source correction.
- Hotelling \(p\ge c\) game = secondary conditional robustness theorem.

## Stage-4A attack set

Stage 4A must independently certify:

### Cournot

1. continuation uniqueness;
2. global own-payoff concavity;
3. corrected symmetric action;
4. competition comparative static;
5. cap comparative statics;
6. source-duopoly global BR;
7. complete pure duopoly equilibrium correspondence;
8. \(\rho=2/3\) continuum;
9. Proposition-5 counterexample.

### Hotelling

10. literal pure price correspondence;
11. below-cost dominance H-DOM1;
12. marginal-cost weak-dominance countercheck H-DOM2;
13. pure price equilibrium under explicit \(p\ge c\);
14. finite-candidate pure Stage-I BR under \(p\ge c\);
15. exact cap-aware symmetric survival/failure region;
16. exact \(1/90\) regression;
17. strict scope separation between literal source and auxiliary no-loss game.

## Formal verification

Formalization is **applicable** because headline results depend on exact inequalities, piecewise case logic, equilibrium multiplicity, regime boundaries, and correction of published mathematical claims.

Stage 4A must record a target map; implementation remains for the later formal-verification gate before theory freeze.
