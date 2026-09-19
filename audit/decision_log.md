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
- missing (ilephi) bound in Cournot;
- Cournot active-set continuation failure;
- missing (ilephi) bound in Hotelling;
- profitable Hotelling corner deviation.

The generalized (eta)-model is retained only as noncanonical predecessor history.

---

## 2026-09-19 — Canonical workflow routing

### Decision

Replace the bootstrap repository's custom Stage-0–8 labels with the canonical `research-paper-workflow` v2.2 routing.

### Consequence

Stage 1 closed with `GO TO NOVELTY GATE`.

The fact that a GitHub repository already exists does not constitute canonical Stage 9 PASS.

---

## 2026-09-19 — Stage-2 novelty narrowing

### Decision

The project survives the Literature Frontier / Novelty Kill Gate, but the contribution is narrowed to a **source-specific correction and global equilibrium re-characterization**.

### Strongest prior-art threat

Jan König (2010), *Outsourcing motives, competitiveness and taxation*.

König explicitly adapts the Shy–Stenbacka framework and, for a marginal-cost-saving outsourcing motive in a different constant-cost specification, obtains less outsourcing when the number of firms rises.

### What is killed

Do not claim novelty for:

- “more competition can reduce outsourcing”;
- strategic substitutability of outsourcing;
- partial outsourcing;
- continuum-input modeling;
- Cournot/Hotelling sourcing analysis as such.

### What survives

No located prior paper was found to:

- correct equation (14) within the published 2005 source model;
- identify the omitted (ilephi) bound;
- identify the Cournot active-set continuation defect;
- identify the Hotelling corner-continuation profitable deviation.

These claims remain `POTENTIALLY NOVEL`, not universally proven priority claims.

### Routing

[
	ext{Stage 2 PASS} ightarrow 	ext{Stage 3 NEXT}.
]

Stage 3 must compare minimal correction architectures without modifying the source primitives merely for novelty.
