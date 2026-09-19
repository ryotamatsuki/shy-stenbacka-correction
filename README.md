# Shy–Stenbacka Correction

Reproducible adversarial equilibrium audit and correction project for Shy & Stenbacka (2005).

## Project status

**Canonical Stage 3 — Candidate Mechanism Search: PASS**

[
oxed{	extbf{GO TO MINIMAL MODEL}}
]

Canonical workflow: `research-paper-workflow` **v2.2**, pinned at commit `42574d6c5931275ccff3ef7e8b4acc188077332a`.

Completed canonical stages:

- Stage 1 — Source & Mathematical Audit
- Stage 2 — Literature Frontier / Novelty Kill Gate
- Stage 3 — Candidate Mechanism Search

Canonical reports:

- `audit/STAGE_01_SOURCE_MATHEMATICAL_AUDIT.md`
- `audit/STAGE_02_LITERATURE_NOVELTY_GATE.md`
- `audit/STAGE_03_MECHANISM_SEARCH.md`

Next canonical stage:

- **Stage 4 — Minimal Model Gate**

## Selected Stage-4 architecture

**Candidate E — Unified regime-complete correction.**

The source model is not extended. The correction is organized around one common sequential-game mechanism:

[
	ext{outsourcing}
ightarrow
	ext{marginal-cost vector}
ightarrow
	ext{Stage-II regime}
ightarrow
	ext{continuation profit}
ightarrow
	ext{global Stage-I best response}.
]

The relevant Stage-II regime is:

- Cournot: the active producer set;
- Hotelling: interior versus corner market shares.

Stage 4 must solve both continuation games globally and then reconstruct the constrained SPNE correspondence.

## Fallback architecture

**Candidate C — Complete Cournot correction** is the only authorized fallback if Hotelling cannot be completely solved without disproportionate complexity.

A sign-only note and a clipping-only correction are not acceptable Stage-4 fallbacks.

## Contribution discipline

The project is a **source-specific correction and global equilibrium re-characterization in a known model**.

Do not claim novelty for:

- partial outsourcing;
- strategic outsourcing;
- strategic substitutes;
- “competition affects outsourcing”;
- “competition can reduce outsourcing” generically.

The strongest prior-art threat remains König (2010).

## Source-model discipline

The published monitoring cost is

[
M(i_j)=i_j^2.
]

No generalized (eta i_j^2), fixed cost, outside option, uncertainty, bargaining stage, supplier market power, or other new primitive is authorized for the Stage-4 core.

## Repository policy

- `main` is the stable project history.
- Mathematical audit work is developed on dedicated branches.
- No headline correction claim is final before global-equilibrium, adversarial, novelty re-kill, and formal-verification gates pass.
- Solver/branch failure is never interpreted as an unprofitable deviation.
- Search failure is never treated as proof of novelty.
- Copyrighted source PDFs are not committed unless redistribution is clearly permitted.

## Current branch

`audit/full-equilibrium-correspondence`

Current canonical state:

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
