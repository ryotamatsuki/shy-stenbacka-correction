# Shy–Stenbacka Correction

Reproducible adversarial equilibrium audit and correction project for Shy & Stenbacka (2005).

## Project status

**Canonical Stage 4 — Minimal Model Gate: PASS**

[
oxed{	extbf{GO TO STAGE 4A}}
]

Canonical workflow: `research-paper-workflow` **v2.2**, pinned at commit `42574d6c5931275ccff3ef7e8b4acc188077332a`.

Completed reports:

- `audit/STAGE_01_SOURCE_MATHEMATICAL_AUDIT.md`
- `audit/STAGE_02_LITERATURE_NOVELTY_GATE.md`
- `audit/STAGE_03_MECHANISM_SEARCH.md`
- `audit/STAGE_04_MINIMAL_MODEL_GATE.md`

Stage-4 supporting artifacts:

- `audit/stage04_continuation_ledger.md`
- `audit/stage04_theorem_certificates.md`
- `code/stage04_verify.py`

Next canonical stage:

- **Stage 4A — Independent Mathematical Adversarial Certification Gate**

## Stage-4 architecture decision

The Stage-3 preferred unified Cournot + Hotelling architecture was tested and **not retained** as the canonical minimal paper.

Reason: outside the Hotelling interior-share region, the source price subgame has multiple valid pure equilibria with different continuation profits. The source specifies no selection/refinement rule, so the reduced Stage-I payoff is not single-valued.

The pre-authorized fallback therefore activates:

[
oxed{	extbf{Candidate C — Complete Cournot correction}}
]

## Corrected Cournot core

Let

[
D=a-Hphi-rac{gammaphi^2}{2}>0.
]

The corrected symmetric outsourcing equilibrium is

[
oxed{
i_C^*
=
minleft{
phi,,
rac{HND}{b(N+1)^2-H^2N}
ight}.
}
]

The competition comparative static is weakly negative and strictly negative on the interior branch for (N>1).

The source equation-(14) sign is therefore reversed.

## New Stage-4 duopoly finding

The published strategic-substitutes result is only a regular both-active-branch result.

With

[
ho=rac b{H^2},
]

the source permits

[
rac49<ho<rac23,
]

and in this region the **global** outsourcing best response contains a regime with

[
rac{dBR}{di_k}=2>0.
]

The mechanism is downstream rival exit: a firm outsources just enough to make the rival's Cournot quantity zero.

Consequences include asymmetric Stage-I equilibria and, at (ho=2/3), a continuum of equilibria.

## Hotelling correction to the audit record

The earlier Stage-1 claim that one corner deviation unconditionally overturns the reported Hotelling candidate is superseded.

Correct Stage-4 finding:

- (|c_B-c_A|le3	au): unique source price equilibrium;
- (|c_B-c_A|>3	au): continuum of corner price equilibria;
- the same Stage-I outsourcing deviation can be profitable under one valid price continuation and unprofitable under another.

Thus the source has an off-path equilibrium-selection problem. No selection refinement is added.

## Source-model discipline

The published monitoring cost remains

[
M(i_j)=i_j^2.
]

No generalized (eta i_j^2), new fixed cost, outside option, bargaining stage, uncertainty, or supplier market power is introduced.

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
