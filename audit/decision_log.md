# Decision Log

## 2026-09-19 — Source-model fidelity repair

The canonical source audit uses (M(i_j)=i_j^2), not a generalized (eta i_j^2).

---

## 2026-09-19 — Canonical workflow routing

The project follows `research-paper-workflow` v2.2. Repository existence does not imply canonical Stage 9 PASS.

---

## 2026-09-19 — Stage-2 novelty narrowing

The project survives as a source-specific correction/global re-characterization. König (2010) kills any generic novelty claim that more Cournot competition can reduce outsourcing.

---

## 2026-09-19 — Stage-3 architecture selection

Candidate E (unified Cournot + Hotelling global correction) was selected for testing, with Candidate C (complete Cournot correction) pre-authorized as the sole fallback.

---

## 2026-09-19 — Stage-4 Hotelling selection finding

### Finding

For (|c_B-c_A|>3	au), the source Hotelling price subgame has a continuum of pure equilibria.

The low-cost firm's continuation profit differs across those equilibria.

### Consequence

The earlier Stage-1 claim that the displayed corner outsourcing deviation unconditionally destroys Proposition 6 is **superseded**.

The correct finding is equilibrium-selection dependence.

A no-below-cost or weak-dominance refinement could select the high-price corner continuation, but no such refinement is stated in the source and none is added.

### Architecture decision

Candidate E is rejected as the canonical minimal architecture.

---

## 2026-09-19 — Stage-4 Cournot fallback activation

### Finding

The Cournot fallback closes analytically.

Under the source SOC, own reduced payoff is globally strictly concave even across downstream active-set changes.

The corrected symmetric general-(N) equilibrium is

[
i_C^*
=
minleft{
phi,,
rac{HND}{b(N+1)^2-H^2N}
ight}.
]

The equation-(14) sign is negative on the interior branch.

For the source duopoly, the global best response is piecewise and contains a slope-(+2) rival-exit regime whenever (4/9<b/H^2<2/3). The source therefore admits asymmetric Stage-I equilibria; at (b/H^2=2/3) it admits a continuum.

### Decision

Activate **Candidate C — Complete Cournot correction**.

Stage-4 verdict:

[
oxed{	ext{GO TO STAGE 4A}}.
]
