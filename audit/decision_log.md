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


---

## 2026-09-19 — Stage-4 construction decision

Stage 4 closes with **GO** for Candidate C — Complete Cournot correction, routed to Stage 4A.

The unified Candidate E is rejected as the minimal canonical architecture because the source Hotelling price subgame has a continuum of valid off-path equilibria for sufficiently asymmetric costs. The Stage-1 Hotelling profitable-deviation result is therefore superseded as an unconditional rejection and retained instead as a continuation-selection diagnostic.

Cournot construction results now frozen for Stage 4A include: global continuation uniqueness, global own-payoff concavity, corrected capped symmetric action, reversed Proposition-3 sign, complete duopoly global BR, and the complete pure duopoly equilibrium correspondence.


---

## 2026-09-19 — Stage-4 Hotelling re-open and final amendment

### Trigger

The previous Stage-4 architecture dropped Hotelling because the literal corner price subgame is multiple when \(|c_B-c_A|>3\tau\).

A re-audit was required because the multiplicity relies on zero-demand high-cost firms choosing prices below marginal cost.

### Mathematical finding

For every \(p_j<c_j\),

\[
p_j=c_j
\]

weakly dominates \(p_j\) under the source Hotelling payoff.

The literal Nash continuum therefore remains a valid source-game diagnosis, but all corner equilibria except the marginal-cost endpoint use weakly dominated prices.

After one-round deletion of these below-cost prices:

- the corner continuation is unique;
- the refined Stage-I payoff is single-valued;
- the source symmetric candidate fails exactly when
  \[
  27\tau/2<H^2n<18\tau
  \]
  and
  \[
  \phi>
  Hn/2-\sqrt{2n(2H^2n-27\tau)}/6.
  \]

The Stage-1 example gives exact gain \(1/90\) under this refinement.

### Architecture decision

The prior Cournot-only routing is superseded.

\[
\boxed{\textbf{RESTORE Candidate E′}}
\]

Candidate E′ = complete Cournot correction + literal/refined Hotelling correction.

Stage-4 verdict remains **GO → Stage 4A**.

No trembling-hand/proper-equilibrium claim is made.
