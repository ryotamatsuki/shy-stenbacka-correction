# Canonical Workflow Routing

This repository follows `ryotamatsuki/research-paper-workflow` **v2.2**.

Pinned workflow commit:

`42574d6c5931275ccff3ef7e8b4acc188077332a`

## Current canonical state

[
oxed{
	ext{Stage 1 PASS}
ightarrow
	ext{Stage 2 PASS}
ightarrow
	ext{Stage 3 PASS}
ightarrow
	ext{Stage 4 PASS}
ightarrow
	extbf{Stage 4A NEXT}
}
]

Stage-1 verdict: **GO TO NOVELTY GATE**.  
Stage-2 verdict: **GO TO MECHANISM SEARCH**.  
Stage-3 verdict: **GO TO MINIMAL MODEL**.  
Stage-4 verdict: **GO TO STAGE 4A**.

## Canonical Stage-4 object

Stage 4 tested Candidate E and activated the Stage-3 authorized fallback.

The object passed to Stage 4A is:

**Candidate C — Complete Cournot correction.**

It includes:

- exact Stage-II active-set continuation for every feasible sourcing history;
- global strict concavity of own Stage-I payoff under the source SOC;
- corrected constrained symmetric general-(N) equilibrium;
- corrected competition and boundary comparative statics;
- complete global duopoly best response;
- complete source-duopoly pure Stage-I equilibrium correspondence.

## Candidate E status

The unified Cournot + Hotelling architecture is not the canonical minimal paper.

The Hotelling price subgame has multiple pure continuations for sufficiently asymmetric costs, and the source has no equilibrium-selection rule. The finding is retained as an audit result but is not repaired by introducing a new refinement.

## Stage-4A contract

Stage 4A must independently attack the Cournot construction and may not silently repair it.

It must test:

1. all-active and reduced-active-set Cournot continuations;
2. global concavity across regime boundaries;
3. the cap correction;
4. equation-(14) sign;
5. the duopoly piecewise best response;
6. the positive-slope regime;
7. asymmetric equilibria;
8. the (ho=2/3) continuum;
9. regression artifacts.

A Stage-4A failure returns the exact failed theorem; it does not authorize a new primitive.

## Important ordering note

The repository exists before canonical Stage 9 only for provenance. This does **not** constitute Stage 9 PASS.

## Fail-closed rule

Material unresolved continuations or failed theorem certificates block later theory freeze.
