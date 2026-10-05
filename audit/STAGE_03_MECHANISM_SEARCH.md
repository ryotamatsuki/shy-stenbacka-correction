# Stage 3 — Candidate Mechanism Search

Status: **PASS — GO TO MINIMAL MODEL**

Audit date: 2026-09-19  
Canonical workflow: `research-paper-workflow` v2.2  
Stage-2 frozen input: `81d501d11602b223465b6219310094dd96c0d183`

## 1. Executive mechanism-search verdict

This is a correction project, so Stage 3 does **not** add a new economic primitive merely to manufacture novelty.

The surviving source-specific problem from Stage 2 has a single coherent structural interpretation:

> **Stage-I outsourcing changes marginal costs; sufficiently large cost differences can move the Stage-II product-market equilibrium across active-set or market-share regimes. Therefore the Stage-I payoff is piecewise and must be derived from the correct continuation equilibrium at every feasible history.**

This **regime-complete backward-induction architecture** unifies the Cournot and Hotelling defects already certified at Stage 1.

The preferred route is therefore:

[
oxed{	extbf{E — Unified global correction}}
]

comprising:

1. the source-specific equation-(14)/Proposition-3 sign correction;
2. the hard outsourcing domain (i_jin[0,phi]);
3. the complete Cournot continuation across active sets;
4. the complete Hotelling continuation across interior/corner market shares;
5. the resulting constrained Stage-I best responses and SPNE correspondence.

Canonical Stage-3 verdict:

[
oxed{	extbf{GO — GO TO MINIMAL MODEL}}
]

No new source primitives are authorized for Stage 4.

---

## 2. Ex-ante scoring rule

Because this is a correction paper, the candidate architecture is scored on correction value rather than on adding new economics.

Weights were fixed before scoring:

| Criterion | Weight |
|---|---:|
| Prior-art survival / source-specific distinctness | 25% |
| Correction completeness | 25% |
| Tractability | 20% |
| Mechanism clarity / conceptual unity | 15% |
| Referee defensibility | 10% |
| Paper economy / minimality | 5% |

Scores are on a 0–10 scale.

Welfare is not given a positive scoring weight because the frozen source question is equilibrium validity, not a welfare theorem. Every candidate is nevertheless assessed for welfare content below. Adding a planner or welfare criterion only to raise a score is prohibited.

---

## 3. Candidate architectures

### Candidate A — Sign-only correction

**One-sentence logic.** Correct equation (14), show that equation (13) implies (partial i/partial N<0), and replace Proposition 3.

**Strategic feedback loop.** None beyond the paper's own interior Cournot branch.

**Endogenous margins.** Symmetric interior outsourcing only.

**Minimum players/timing.** Source Cournot model; no change.

**New primitive/interaction.** None.

**Closest prior-art threat.** König (2010), who already derives a negative competition–outsourcing relation in a close variant.

**Expected result.** Published equation-(14) sign and Proposition-3 conclusion are reversed.

**Welfare content.** None; no welfare claim should be added.

**Institutional interpretation.** Correction of a published comparative static.

**Tractability risk.** Very low.

**Fatal referee attack.** “This is one derivative, and a related negative sign is already known; why is a standalone paper needed?”

**Score:** 6.10/10.

**Decision:** **REJECT AS STANDALONE ARCHITECTURE.** Retain as one theorem/result inside the preferred correction.

---

### Candidate B — Constraint clipping only

**One-sentence logic.** Keep the paper's continuation payoffs but replace reported outsourcing solutions with their projection onto ([0,phi]).

**Strategic feedback loop.** Local Stage-I payoff plus hard action-set boundary.

**Endogenous margins.** Outsourcing boundary only.

**Minimum players/timing.** Source game.

**New primitive/interaction.** None.

**Closest prior-art threat.** Generic constrained optimization; no source-specific conceptual depth.

**Expected result.** Piecewise interior/full-outsourcing solutions obtained by clipping.

**Welfare content.** None.

**Institutional interpretation.** Feasibility correction.

**Tractability risk.** Low.

**Fatal referee attack.** **Mathematically invalid globally.** Stage 1 already establishes feasible histories at which the Cournot all-active continuation and Hotelling interior-share continuation cease to be the relevant Stage-II equilibria. Clipping an invalid continuation payoff cannot repair the sequential game.

**Score:** 5.95/10.

**Decision:** **KILL.** This architecture fails before publication considerations.

---

### Candidate C — Complete Cournot correction

**One-sentence logic.** Solve the exact source Cournot game globally: every outsourcing profile induces a cost vector, the quantity subgame is solved with nonnegative quantities and endogenous active sets, and Stage-I best responses are derived from those continuation profits.

**Strategic feedback loop.**

[
i
ightarrow c(i)
ightarrow 	ext{Cournot active set}
ightarrow q,p,pi
ightarrow BR_i.
]

A unilateral outsourcing deviation can change not only own marginal cost but also which rivals remain active, changing the functional form of continuation profit.

**Endogenous margins.**

- continuous outsourcing (i_jin[0,phi]);
- Stage-II quantities (q_jge0);
- active-set membership;
- Stage-I equilibrium symmetry/asymmetry.

**Minimum players/timing.** The published (N)-firm two-stage Cournot game.

**New primitive/interaction.** None; the new object is global solution of the source game's existing interaction.

**Closest prior-art threat.** König (2010) for the sign/comparative-static direction, but not for source-model active-set correction.

**Expected nontrivial results.**

- exact active-set continuation formula;
- exact conditions under which the paper's equation (13) is a valid SPNE candidate;
- exact constrained best-response correspondence;
- possible boundary/asymmetric equilibria;
- corrected comparative-static statement.

**Welfare content.** Not required. Consumer surplus/total surplus may be computed only if needed to assess a source claim; no welfare extension should be added.

**Institutional interpretation.** Outsourcing-induced cost advantages can endogenously change the number of active final-good producers.

**Tractability risk.** Moderate: (N)-firm active-set combinatorics can become large. Symmetry/order structure must be exploited.

**Fatal referee attack.** “The active-set machinery overwhelms a correction whose economically salient error is just equation (14).”

**Score:** 8.20/10.

**Decision:** **TOP 2 / FALLBACK ROUTE.**

---

### Candidate D — Complete Hotelling correction

**One-sentence logic.** Solve the source Hotelling price subgame globally for every feasible cost difference, then use the resulting piecewise continuation payoff to re-solve Stage-I outsourcing.

**Strategic feedback loop.**

[
(i_A-i_B)
ightarrow(c_A-c_B)
ightarrow	ext{interior/corner market-share regime}
ightarrow(p_A,p_B,D_A,D_B)
ightarrow BR_A,BR_B.
]

**Endogenous margins.**

- continuous outsourcing;
- price competition;
- market-share regime;
- boundary/full-market capture;
- Stage-I equilibrium.

**Minimum players/timing.** Source two-firm Hotelling game.

**New primitive/interaction.** None.

**Closest prior-art threat.** Generic Hotelling corner-equilibrium literature, but no Stage-2 paper located the correction in this exact source game.

**Expected nontrivial results.**

- complete price-continuation correspondence as a function of (c_B-c_A);
- exact domain of equations (19)–(21);
- exact parameter region in which equation (25) survives/fails globally;
- corrected Stage-I best responses and equilibrium correspondence.

**Welfare content.** No new welfare theorem required.

**Institutional interpretation.** A sufficiently aggressive outsourcing deviation can lower cost enough to convert differentiated duopoly into a corner allocation.

**Tractability risk.** Moderate to high: price equilibrium at demand kinks/corners must be characterized globally and with exact tie/boundary conventions.

**Fatal referee attack.** “A standalone Hotelling correction ignores the independent and simpler headline sign error in Proposition 3.”

**Score:** 7.55/10.

**Decision:** **TOP 3 / IMPORTANT SUBPROBLEM, NOT PREFERRED STANDALONE ROUTE.**

---

### Candidate E — Unified regime-complete correction

**One-sentence logic.** Correct the published sign error and solve both source product-market specifications by global backward induction, using the same principle: outsourcing-induced cost gaps can move the continuation game across regimes, so local FOCs/SOCs do not establish SPNE.

**Strategic feedback loop.**

Common architecture:

[
oxed{
	ext{outsourcing}
ightarrow
	ext{marginal-cost vector}
ightarrow
	ext{Stage-II regime}
ightarrow
	ext{continuation profit}
ightarrow
	ext{global Stage-I best response}
}
]

with regime meaning:

- **Cournot:** active producer set;
- **Hotelling:** interior versus corner market shares.

**Endogenous margins.**

All source margins only:

- (i_jin[0,phi]);
- quantities or prices;
- active-set/market-share regime;
- global unilateral deviations;
- Stage-I equilibrium correspondence.

**Minimum players/timing.**

- published (N)-firm Cournot game;
- published two-firm Hotelling game;
- exactly the source timing.

**Minimum new primitive.** **Zero.**

**Closest prior-art threat.** König (2010) for the generic negative competition effect. It does not contain the global source-game correction.

**Expected nontrivial results.**

1. source-specific equation-(14)/Proposition-3 reversal;
2. necessary/sufficient conditions for the published Cournot candidate to remain feasible and globally valid;
3. complete Cournot constrained continuation and equilibrium correspondence;
4. complete Hotelling price continuation;
5. exact survival/failure region for the published Hotelling candidate;
6. a common methodological statement: source local SOCs certify regular branches, not the global sequential equilibrium.

**Welfare content.** No welfare extension is necessary. The paper's contribution is correction of equilibrium characterization. Welfare should enter only if an original welfare implication is shown to depend on the corrected equilibrium.

**Institutional interpretation.** Large organizational-cost changes can alter final-market participation/allocation regime, which feeds back to the organizational decision.

**Tractability risk.** Highest among admissible candidates. The paper remains viable only if both continuation games admit concise piecewise characterizations.

**Fatal referee attack.** “This is two unrelated corrections bundled together.”

**Response required at Stage 4.** Demonstrate that the same domain-complete backward-induction failure generates both defects and that the unified presentation is shorter and conceptually cleaner than two independent notes.

**Score:** 8.75/10.

**Decision:** **PREFERRED MINIMAL ARCHITECTURE.**

---

### Candidate F — Generalize monitoring costs with a free (eta)

**Logic.** Replace source (i_j^2) by (eta i_j^2).

**Decision:** **KILL / PROHIBITED.**

Reason: Stage 1 froze the source model and specifically repaired this theory drift. A generalized coefficient may be a later robustness exercise only after the source correction is solved, not the Stage-4 core.

---

### Candidate G — Add outside options/reservation utility/dynamics

**Logic.** Enrich the Hotelling or sourcing environment to create additional equilibrium regions.

**Decision:** **KILL / PROHIBITED.**

Reason: these are new primitives unrelated to correcting the published game. They dilute rather than strengthen the correction and create new literature obligations.

---

## 4. Candidate score table

| Candidate | Prior-art survival 25% | Completeness 25% | Tractability 20% | Clarity 15% | Referee defensibility 10% | Economy 5% | Weighted score |
|---|---:|---:|---:|---:|---:|---:|---:|
| A Sign-only | 6 | 2 | 10 | 8 | 4 | 10 | **6.10** |
| B Clipping-only | 7 | 3 | 9 | 6 | 3 | 9 | **5.95** |
| C Complete Cournot | 9 | 8 | 7 | 9 | 8 | 8 | **8.20** |
| D Complete Hotelling | 9 | 7 | 6 | 8 | 8 | 7 | **7.55** |
| E Unified global correction | 10 | 10 | 5 | 10 | 9 | 7 | **8.75** |

Candidates F/G are not scored because they violate frozen-stage constraints.

---

## 5. TOP candidates

### TOP 1 — E: Unified regime-complete correction

Selected for Stage 4.

### TOP 2 — C: Complete Cournot correction

Fallback if the Hotelling continuation cannot be completely characterized without disproportionate complexity.

### TOP 3 — D: Complete Hotelling correction

Retained as an essential subproblem of E and a possible independent correction only if the Cournot part becomes redundant after formal solution.

A and B are not eligible fallback routes: A is too narrow after Stage 2; B is mathematically incomplete.

---

## 6. Why the rejected candidates fail

### A fails contribution sufficiency

The sign error is real and must be corrected, but Stage 2 showed that the **economic direction** already appears in a close model. A one-derivative note is therefore exposed to a strong “too small / already economically known” referee attack.

### B fails equilibrium logic

The global game cannot be repaired by projection/clipping because the continuation payoff itself changes functional form outside the regular branch.

### F/G fail source fidelity

They alter the model rather than correct it.

---

## 7. Preferred minimal mechanism/generalization

The preferred object is not a new primitive mechanism but a **domain-complete sequential-equilibrium correction**.

### Core economic loop

Outsourcing lowers marginal cost:

[
c_j=C_0-Hi_j.
]

Relative outsourcing therefore generates relative marginal-cost changes. When the cost gap crosses a product-market threshold:

- a Cournot firm can enter/exit the active set;
- a Hotelling firm can move from an interior share to full-market capture/loss.

Consequently, continuation profit is **piecewise**, and the derivative of the paper's interior continuation payoff cannot be used globally.

This loop is already latent in the source primitives. Stage 4's job is to solve it, not embellish it.

---

## 8. Exact Stage-4 model skeleton

Stage 4 is authorized to solve **only** the following source model.

### Common sourcing technology

Inputs have total measure (phi>0).

Each firm (j) chooses

[
i_jin[0,phi].
]

Under the source's constant outsourcing advantage and normalization,

[
c_j=C_0-Hi_j,
qquad
C_0=Hphi+rac{gammaphi^2}{2},
]

with monitoring cost

[
M(i_j)=i_j^2.
]

No (eta), fixed cost, outside option, capacity constraint, bargaining stage, uncertainty, or new player may be introduced.

### Game C — Cournot

Stage I:
[
i_jin[0,phi],qquad j=1,ldots,N.
]

Stage II:
[
q_jge0,
qquad
p=a-bsum_{k=1}^Nq_k.
]

Operating payoff:
[
(p-c_j)q_j.
]

Total payoff:
[
Pi_j=(p-c_j)q_j-i_j^2.
]

Stage 4 must solve the quantity subgame for **every feasible cost vector generated by ([0,phi]^N)**, including active-set changes.

### Game H — Hotelling

Two firms at endpoints 0 and 1, consumer density (n), source transportation/differentiation parameter (	au>0), and the source's maintained market-coverage environment.

Stage I:
[
i_A,i_Bin[0,phi].
]

Stage II:
firms choose prices under the source demand system.

Total payoff:
[
Pi_j=(p_j-c_j)D_j-i_j^2.
]

Stage 4 must derive the price continuation for every feasible cost difference

[
c_B-c_A=H(i_A-i_B)in[-Hphi,Hphi],
]

including all interior and corner market-share regimes.

### Equilibrium concept

Subgame-perfect equilibrium by backward induction.

No Stage-I deviation may be evaluated using a Stage-II formula outside its validity domain.

---

## 9. Nested benchmark skeletons

These are **diagnostic benchmarks**, not separate candidate models.

### Benchmark C0 — Published Cournot regular branch

Assume:

- all firms active;
- outsourcing interior;
- the source quantity formula is valid.

Stage 4 must recover equation (13) and the corrected derivative of equation (14).

### Benchmark C1 — Constrained but globally all-active Cournot

Impose conditions sufficient to keep every feasible Stage-I history on the all-active quantity branch, but retain (i_jin[0,phi]).

Purpose: isolate pure outsourcing-bound effects from active-set effects.

### Benchmark H0 — Published Hotelling interior branch

Assume:

[
|H(i_A-i_B)|<3	au
]

for relevant histories and outsourcing interior.

Stage 4 must recover equations (19)–(25).

### Benchmark H1 — Constrained but globally interior-share Hotelling

Impose a condition such as

[
Hphile3	au
]

sufficient to prevent any feasible sourcing profile from leaving the interior-share branch, while retaining (i_jin[0,phi]).

Purpose: isolate the outsourcing cap from corner-price effects.

### Full model

Remove the global-regularity restrictions C1/H1 while retaining only the source primitives.

A headline result qualifies as a genuine global correction only if it changes when the relevant regularity restriction is removed.

---

## 10. Candidate propositions for Stage 4 to kill-test

These are **candidate propositions**, not current claims.

### CP1 — Source-specific sign correction

For every admissible interior Cournot candidate with (N>1),

[
rac{partial i_{C,mathrm{int}}}{partial N}<0.
]

Status entering Stage 4: algebraically Stage-1 certified; must be embedded in the correct equilibrium domain.

### CP2 — Cournot validity region

There exists an exact set of primitive inequalities under which the published symmetric Cournot candidate is a genuine SPNE of the source game.

Stage 4 must derive necessary/sufficient conditions or explicitly state the strongest proved characterization.

### CP3 — Cournot global correspondence

The source Cournot game has a complete piecewise equilibrium correspondence determined by outsourcing boundaries and downstream active-set regimes.

Stage 4 must determine whether this is analytically tractable for general (N). If not, the general-(N) claim fails closed; a duopoly or symmetric-only reduction requires returning to the allowed-scope decision rather than silently narrowing the theorem.

### CP4 — Hotelling continuation partition

The Stage-II Hotelling game admits a complete piecewise price-equilibrium characterization indexed by the cost gap (d=c_B-c_A).

Stage 4 must establish existence, uniqueness/multiplicity, and exact boundary/tie cases.

### CP5 — Hotelling failure region

There is a nonempty primitive region satisfying the paper's local SOC in which the published symmetric outsourcing candidate is not an SPNE because a unilateral deviation crosses into a corner price regime.

Status entering Stage 4: counterexample and a sufficient symbolic region are Stage-1 certified; Stage 4 must derive the exact global condition.

### CP6 — Common correction principle

The paper's local SOCs certify concavity only on regular continuation branches and are insufficient to establish global Stage-I optimality whenever feasible outsourcing histories can change the Stage-II regime.

Stage 4 must translate this methodological statement into exact source-specific propositions, not leave it as rhetoric.

### CP7 — Proposition 5 qualification

The strategic-substitute result survives globally only in an appropriately weak/piecewise form, or fails on some regime.

This is deliberately open. Stage 4 must not assume survival.

---

## 11. Stage-4 tractability kill switches

The preferred E architecture survives only if Stage 4 can meet all of the following:

1. **Cournot:** valid continuation solver/closed form for all material active sets or a proof that only a reduced set can occur in equilibrium/deviations.
2. **Hotelling:** complete price subgame at every feasible cost gap.
3. **Boundary semantics:** exact treatment of equality thresholds.
4. **Global deviations:** direct-payoff checks independent of the candidate solver.
5. **No silent scope reduction:** unresolved continuations block a global SPNE theorem.
6. **Paper economy:** the unified theorem structure must remain shorter/cleaner than presenting two unrelated corrections.

If Hotelling alone blocks complete solution while Cournot closes cleanly, Stage 4 should return **CONDITIONAL GO / pivot to C**, not weaken the SPNE standard.

---

## 12. Verdict and next-stage contract

[
oxed{	extbf{STAGE 3 — PASS}}
]

[
oxed{	extbf{GO TO MINIMAL MODEL}}
]

Stage 4 is instructed to test **Candidate E** with the source model frozen exactly as specified above.

### Stage-4 contract

- no new primitives;
- no (eta i_j^2);
- no new fixed costs;
- no outside option added to Hotelling;
- no dynamics/uncertainty/bargaining/supplier market power;
- solve off-path continuations rather than discard them;
- retain Stage-1 counterexamples as regression tests;
- recover the published regular branches as nested benchmarks;
- distinguish `SOLVED_EQUILIBRIUM`, `SOLVED_NO_EQUILIBRIUM`, `MULTIPLE_EQUILIBRIA`, `UNRESOLVED`, and `NUMERICAL_FAILURE`;
- if the unified architecture cannot be completely solved, fail closed and compare the fallback Cournot-only Route C.
