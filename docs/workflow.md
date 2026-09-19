# Canonical Workflow Routing

This repository follows `ryotamatsuki/research-paper-workflow` **v2.2**.

Pinned workflow commit:

`42574d6c5931275ccff3ef7e8b4acc188077332a`

See `docs/WORKFLOW_PROVENANCE.md`.

## Current canonical state

[
oxed{
	ext{Stage 1 PASS}
ightarrow
	ext{Stage 2 PASS}
ightarrow
	ext{Stage 3 PASS}
ightarrow
	extbf{Stage 4 NEXT}
}
]

Stage-1 verdict: **GO TO NOVELTY GATE**.  
Stage-2 verdict: **GO TO MECHANISM SEARCH**.  
Stage-3 verdict: **GO TO MINIMAL MODEL**.

## Stage-3 selected architecture

Stage 4 tests **Candidate E — Unified regime-complete correction**.

Core loop:

[
	ext{outsourcing}
	o
	ext{cost vector}
	o
	ext{downstream regime}
	o
	ext{continuation payoff}
	o
	ext{global Stage-I best response}.
]

Cournot regime = active set.  
Hotelling regime = interior/corner market share.

No new source primitive is authorized.

## Authorized fallback

If the Hotelling global price continuation cannot be completely characterized while Cournot closes cleanly, Stage 4 may return a conditional pivot to **Candidate C — Complete Cournot correction**.

It may not silently drop unresolved Hotelling histories while retaining a global SPNE claim.

## Stage-4 prohibitions

- no generalized monitoring-cost coefficient;
- no fixed cost added to create thresholds;
- no outside option added to Hotelling;
- no dynamics, uncertainty, bargaining, or supplier market power;
- no clipping of an invalid continuation formula as a substitute for solving the continuation game;
- no use of FOC/SOC alone as a global equilibrium certificate.

## Important ordering note

The repository was created before canonical Stage 9 for provenance. This does **not** constitute Stage 9 PASS.

## Fail-closed equilibrium rule

Any material continuation must be classified as one of:

- `SOLVED_EQUILIBRIUM`
- `SOLVED_NO_EQUILIBRIUM`
- `MULTIPLE_EQUILIBRIA`
- `UNRESOLVED`
- `NUMERICAL_FAILURE`

Material `UNRESOLVED` or `NUMERICAL_FAILURE` blocks a global SPNE theorem.

## Branch policy

- `main`: stable project history.
- `audit/full-equilibrium-correspondence`: current staged audit.
