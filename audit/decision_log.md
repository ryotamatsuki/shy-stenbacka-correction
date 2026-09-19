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


---

## 2026-09-19 — Stage-4A refinement kill test and Stage-4 amendment

The independent Stage-4A attack found that the earlier “undominated-price refinement” label was not defensible.

Although every \(p<c\) is weakly dominated by \(p=c\), the action \(p=c\) itself is weakly dominated by any fixed \(p=c+\varepsilon\). Therefore the corner equilibrium using \(p_{\rm high}=c_{\rm high}\) is not an undominated-strategy equilibrium and cannot be justified by symmetric elimination of all weakly dominated strategies.

The mathematics under the restricted strategy set \(p\ge c\) remains correct. Stage 4 is therefore amended, not abandoned:

- literal source game: corner multiplicity / incomplete backward induction;
- auxiliary no-loss game \(p\ge c\): unique pure corner continuation and exact Proposition-6 failure region;
- architecture: **HYBRID**, with Cournot as main theorem block and Hotelling as secondary source/robustness results.

This amendment is explicit and precedes Stage-4A recertification.


---

## 2026-09-19 — Stage-4A final certification

The amended Stage-4 HYBRID architecture was independently reconstructed and attacked.

### Independent result

- Cournot continuation uniqueness independently follows from a strictly concave exact potential with Hessian \(-b(I+\mathbf1\mathbf1^\top)\).
- Global Cournot own-payoff concavity survives active-set changes.
- The source-duopoly BR, Proposition-5 counterexample, asymmetric equilibria, and \(\rho=2/3\) continuum survive.
- Literal Hotelling corner multiplicity survives.
- The Stage-4A weak-dominance counterexample \(p=c\preceq c+\varepsilon\) is permanently retained.
- Under explicit \(p\ge c\), the pure Hotelling price continuation and exact Proposition-6 failure threshold survive.
- No material continuation remains unresolved.

### Verdict

\[
\boxed{\textbf{GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS}}
\]

Next stage:

\[
\boxed{\textbf{Stage 6 — Novelty Re-Kill}}
\]

Formalization is applicable; target map recorded for the later pre-freeze formal-verification gate.


---

## 2026-09-19 — Stage-6 novelty re-kill

### Parent-class attack

The Stage-4A results were stripped of outsourcing language and searched against standard parent classes.

Strong prior-art threats include:

- König (2010): negative competition–outsourcing effects in a close specification;
- Amir (2000): asymmetric R&D and endogenous exit in symmetric Cournot;
- Amir, Garcia & Knauff (2010): general symmetry-breaking classes;
- Amir, Halmenschlager & Jin (2011): R&D polarization / shake-outs;
- Buehler & Schmutzler (2008): investment asymmetry in successive oligopoly;
- Eckert, Klumpp & Su (2017): multiple asymmetric investment equilibria before Cournot;
- Lamantia, Pezzino & Tramontana (2018): discontinuous/piecewise innovation BRs and multiple equilibria;
- heterogeneous-cost spatial pricing and no-loss-price literature.

### Killed novelty narratives

The project may not claim novelty for generic negative competition effects, endogenous asymmetry, rival exit, piecewise-BR multiplicity, or no-loss Hotelling pricing.

### Surviving novelty

No located parent theorem directly absorbs the exact source correction package.

The key Cournot distinction is that the certified source reduced payoff is globally strictly concave in own sourcing under the paper's SOC, yet the downstream active-set kink makes the global outsourcing BR non-monotone and can produce coexistence of the symmetric equilibrium with an asymmetric pair.

The contribution remains a **new source-specific correction/result in a known model**, not a new general game-theory mechanism.

### Verdict

\[
\boxed{\textbf{STAGE 6 — GO}}
\]

Route:

\[
\boxed{\textbf{Stage 7 — Welfare / Generality / Institutional Validation}}
\]


---

## 2026-09-19 — Stage-7 welfare, generality, and institutional validation

### Welfare

Exact Cournot and Hotelling welfare identities were derived.

The unrestricted planner problems were written explicitly. Restricted sourcing benchmarks are labeled as restricted-instrument or fixed-allocation benchmarks and are not called first best.

The corrected Cournot duopoly is welfare-selection dependent. At the exact three-equilibrium regression

\[
(\rho,\delta,\phi)=(3/5,1,2),
\]

the symmetric equilibrium has welfare \(20/17\), while each asymmetric equilibrium has welfare \(3/2\).

At \(\rho=2/3\), welfare varies across the certified equilibrium continuum.

Therefore no selection-free global welfare claim is authorized.

### Generality

The exact sign, threshold, best-response, and equilibrium-correspondence results remain baseline functional-form results.

A wider decreasing-cost class supports the direction of the rival-exit threshold, but no general equilibrium theorem is promoted.

### Institutional validation

Empirical evidence supports production fragmentation and active monitoring/auditing of outsourced manufacturers. It does not validate the exact quadratic/output-independent monitoring technology.

### Exposition decision

Welfare remains appendix/prose material. Main text remains focused on S1–S3, with S4–S5 secondary.

### Verdict

\[
\boxed{\textbf{STAGE 7 — GO TO STAGE 7.5}}
\]


---

## 2026-09-19 — Stage-7.5 full-theory freeze decision

### Value assessment

The project is not a new general theory of outsourcing, and Stage 6 has already killed that positioning.

It nevertheless merits full-paper investment because the exact published model requires more than an algebraic corrigendum:

- Proposition 3 reverses sign;
- the all-active downstream formula is not globally valid;
- Proposition 5 fails globally;
- the source duopoly pure equilibrium set is qualitatively different from the published interpretation;
- the Hotelling section has a separate off-path continuation defect.

### Mechanism

Outsourcing lowers marginal cost. When a sourcing difference becomes large enough to change downstream participation, the continuation regime changes. That active-set switch changes the global sourcing best-response geometry and can generate equilibrium multiplicity/asymmetry even though own reduced sourcing payoff is globally strictly concave.

### Scope

The exact theorems remain source-model / baseline-functional-form results.

The manuscript should be a compact correction paper / theory note, not an extension-heavy general-theory paper.

### Verdict

\[
\boxed{\textbf{STAGE 7.5 — GO}}
\]

Route:

\[
\boxed{\textbf{Stage 7.5A — Generality / Quantifier Red-Team}}
\]
