# Decision Log

## 2026-09-19 — Source-model fidelity repair

### Decision

The canonical source audit uses the published monitoring cost

[
M(i_j)=i_j^2
]

with no free coefficient.

### Reason

Predecessor scratch/audit material in `ryotamatsuki/ozshypapers` introduced a generalized monitoring-cost coefficient (eta), writing (eta i_j^2). That is mathematically legitimate as an extension, but it is not the published Shy–Stenbacka (2005) source model.

Under the v2.2 Stage-1 rule against silent theory drift, that generalized coefficient cannot be used to certify a correction of the published model.

### Action

All canonical Stage-1 symbolic identities and counterexamples were independently re-derived with coefficient one.

### Result

The material defects survive source-faithful reconstruction:

- equation (14) sign reversal;
- missing (ile\phi) bound in Cournot;
- Cournot active-set continuation failure;
- missing (ile\phi) bound in Hotelling;
- profitable Hotelling corner deviation.

The generalized (eta)-model is retained only as noncanonical predecessor history.

---

## 2026-09-19 — Canonical workflow routing

### Decision

Replace the bootstrap repository's custom Stage-0–8 labels with the canonical `research-paper-workflow` v2.2 routing.

### Consequence

Current state:

[
	ext{Stage 1 PASS} ightarrow 	ext{Stage 2 NEXT}.
]

The fact that a GitHub repository already exists does not constitute canonical Stage 9 PASS.
