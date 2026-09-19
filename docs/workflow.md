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
\textbf{Stage 6 NEXT}
}
\]

## Stage-4A verdict

\[
\boxed{\textbf{GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS}}
\]

Stage 4A initially found one material Hotelling solution-concept defect and correctly routed it back to Stage 4:

- \(p<c\) is weakly dominated by \(p=c\);
- but \(p=c\) is itself weakly dominated by \(p=c+\varepsilon\);
- therefore \(p\ge c\) cannot be described as “elimination of all weakly dominated strategies.”

Stage 4 was amended to the HYBRID architecture and Stage 4A was repeated.

## Certified scope

### Cournot

- unique Stage-II continuation for every feasible sourcing history;
- global own-payoff strict concavity;
- corrected symmetric general-\(N\) action;
- Proposition-3 sign reversal;
- exact source-duopoly global BR;
- Proposition-5 global failure;
- complete pure source-duopoly Stage-I equilibrium correspondence.

### Hotelling

- literal pure-price equilibrium correspondence, including corner multiplicity;
- exact dominance facts \(p<c\preceq c\) and \(c\preceq c+\varepsilon\);
- conditional pure-price continuation under explicit \(p\ge c\);
- complete finite-candidate pure Stage-I BR under that restriction;
- exact cap-aware symmetric survival/failure region;
- exact \(1/90\) regression.

No mixed-equilibrium uniqueness, trembling-hand, proper-equilibrium, or complete asymmetric Hotelling Stage-I claim is certified.

## Formal verification

\[
\boxed{\textbf{FORMALIZATION APPLICABLE}}
\]

Preliminary target map:
\`audit/stage04a_formalization_target_map.md\`.

Formal implementation is deferred to the required pre-freeze gate and is not counted as Stage-4A evidence.

## Routing

Stage 4A GO routes directly to:

\[
\boxed{\textbf{Stage 6 — Novelty Re-Kill}}
\]

Stage 5 is not triggered because no economic primitive repair was required.
