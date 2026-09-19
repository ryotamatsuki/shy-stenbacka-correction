> **Independent-audit recertification (2026-09-20).** The historical PASS remains provenance, but its C7 cap-feasibility quantifier and C8 proof-completeness certification are superseded by `audit/STAGE_04A_RECERTIFICATION_2026-09-20.md`.

# Stage 4A — Independent Mathematical Adversarial Certification Gate

Status: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**

Certification date: 2026-09-19  
Workflow: \`research-paper-workflow\` v2.2  
Frozen input after required rollback/amendment: Stage-4 **HYBRID** architecture

## 1. Executive adversarial verdict

Stage 4A initially **broke one Stage-4 refinement claim**.

The construction had correctly proved that every Hotelling price \(p<c\) is weakly dominated by \(p=c\), but had then described the restricted \(p\ge c\) game as an “undominated-price refinement.”

The independent attack proved instead that, for every \(\varepsilon>0\),

\[
p=c+\varepsilon
\]

weakly dominates \(p=c\).

Therefore the prior refinement label was false.

Under the workflow fail-closed rule, the project was routed back to Stage 4. Stage 4 was amended:

- literal source Hotelling game: retain the exact corner multiplicity;
- auxiliary Hotelling robustness game: state \(p_j\ge c_j\) explicitly as a **no-loss strategy restriction**;
- do not identify this with elimination of all weakly dominated strategies, trembling-hand perfection, proper equilibrium, or a source assumption;
- architecture changed to **HYBRID**, with Cournot as the main theorem block.

Stage 4A was then repeated against the amended object.

No further correctness blocker was found.

\[
\boxed{\textbf{GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS}}
\]

Canonical route:

\[
\boxed{\textbf{Stage 6 — Novelty Re-Kill}}
\]

---

## 2. Independent reconstruction summary

### Cournot

The downstream quantity game was reconstructed independently as an exact potential game with

\[
\Phi(q)
=
\sum_j(a-c_j)q_j
-\frac b2Q^2
-\frac b2\sum_jq_j^2.
\]

Its Hessian is

\[
-b(I+\mathbf1\mathbf1^\top),
\]

which is negative definite. Hence the nonnegative-quantity continuation is unique for every feasible sourcing history independently of the Stage-4 active-set implementation.

The reduced Stage-I own payoff was re-audited across active-set changes. Branch curvature is strictly negative under the source SOC; own-entry derivatives join continuously; rival-exit transitions create downward derivative jumps. Global own strict concavity survives.

The source-duopoly BR and complete pure equilibrium correspondence were reconstructed branch by branch. The positive-slope rival-exit segment, asymmetric equilibria, and \(\rho=2/3\) equilibrium continuum all survive.

### Hotelling literal game

The price game was reconstructed from clipped consumer shares. The pure equilibrium is unique for \(|c_B-c_A|\le3\tau\) and is a continuum for larger cost gaps.

The zero-demand high-cost firm's payoff indifference is material: changing its equilibrium price changes the low-cost firm's equilibrium price and continuation profit.

### Hotelling no-loss robustness game

The independent weak-dominance attack invalidated the earlier “undominated-price” interpretation but not the restricted-game mathematics.

Conditional on the explicit auxiliary restriction

\[
p_j\ge c_j,
\]

the pure price continuation is unique. The complete pure Stage-I BR has the finite-candidate form in Stage 4, and the exact Proposition-6 failure condition remains

\[
\frac{27}{2}\tau<H^2n<18\tau
\]

and

\[
\phi>
x_-=
\frac{Hn}{2}
-
\frac{\sqrt{2n(2H^2n-27\tau)}}6.
\]

The exact Stage-1 regression gain remains

\[
\frac1{90}.
\]

---

## 3. Headline theorem-certificate summary

Detailed certificates are in \`audit/stage04a_theorem_certificates.md\`.

| Group | Claims | Stage-4A state |
|---|---|---|
| Cournot continuation/global concavity | C1–C2 | **PASS** |
| Cournot symmetric action/comparative statics | C3–C5 | **PASS** |
| Cournot duopoly global BR / Proposition 5 | C6–C7 | **PASS** |
| Cournot complete pure duopoly correspondence | C8 | **PASS** |
| Literal Hotelling pure-price correspondence | H1 | **PASS** |
| Hotelling dominance facts | H2, H2b | **PASS** |
| Explicit no-loss price game | H3-NL | **PASS — CONDITIONAL MODEL** |
| No-loss Stage-I BR / threshold | H4-NL–H5-NL | **PASS — CONDITIONAL MODEL** |
| Exact Hotelling regression | H6-NL | **PASS — CONDITIONAL MODEL** |

---

## 4. Candidate-deviation audit

### Cournot symmetric general-\(N\) candidate

Global own strict concavity converts the symmetric KKT condition into a global best response over the true interval \([0,\phi]\). Active-set-changing deviations are included.

**Result: PASS.**

### Cournot duopoly

Every zero-output, both-active, rival-exit, monopoly, and cap branch was included. Exact primitive-payoff attacks reproduce the claimed equilibria and the Proposition-5 counterexample.

**Result: PASS.**

### Literal Hotelling

No selection-free Stage-I candidate is certified outside the regular price region because the source game is multiple off path. This is a scope result, not a failure hidden by selection.

**Result: PASS WITH EXPLICIT SELECTION-DEPENDENT SCOPE.**

### No-loss Hotelling

All pure Stage-I branch deviations are reduced to a finite candidate set. The exact nonlocal corner deviation is included.

**Result: PASS WITH CONDITIONAL \(p\ge c\) SCOPE.**

---

## 5. Alternative-equilibrium / multiplicity audit

### Cournot Stage II

Unique quantity vector for every feasible cost vector.

### Cournot Stage I, general \(N\)

Only the unique **symmetric action** is claimed. No all-equilibria uniqueness claim is made.

### Cournot Stage I, source duopoly

The complete pure correspondence was independently attacked.

- \(\rho>2/3\): unique pure equilibrium.
- \(\rho=2/3\): exact continuum when the cap permits.
- \(4/9<\rho<2/3\): unique capped symmetric equilibrium when \(\phi\le s\); exactly three pure equilibria when \(\phi>s\).

**Result: PASS.**

### Literal Hotelling price game

Multiple corner equilibria are explicitly retained.

### No-loss Hotelling price game

Unique **pure** price equilibrium for every cost gap.

No mixed-equilibrium uniqueness claim is made.

---

## 6. Indifference / zero-payoff trigger audit

### Cournot

A threshold firm may have zero quantity. Reclassifying that firm as “active with zero quantity” versus inactive does not create a different quantity vector or payoff outcome. The economically relevant continuation remains unique.

### Literal Hotelling

The zero-demand high-cost firm has a continuum of payoff-equivalent prices. These actions are **not** irrelevant: they change the opponent's price and profit. This creates the exact continuation multiplicity recorded in H1.

### Weak dominance

The attack was applied symmetrically. It generated the Stage-4A failure:

\[
p=c
\]

is itself weakly dominated by \(p=c+\varepsilon\).

The project was corrected rather than suppressing this result.

**Result after rollback/amendment: PASS.**

---

## 7. Equilibrium-selection / refinement audit

The final model language distinguishes:

1. **literal source Nash game** — no price floor attributed to the source;
2. **auxiliary no-loss game** — explicit strategy restriction \(p_j\ge c_j\);
3. trembling-hand/proper/admissibility refinements — **not claimed**.

The no-loss result is conditional. It may be used as robustness evidence but not as a statement that the literal Nash multiplicity disappears under “all undominated strategies.”

**Result: PASS.**

---

## 8. Global boundary / regime audit

Certified boundaries include:

- \(i=0\);
- \(i=\phi\);
- Cournot own entry;
- Cournot rival exit;
- \(\rho=4/9,1/2,2/3\) neighboring regimes;
- Hotelling \(|d|=3\tau\);
- Hotelling sourcing branch switch \(x-y=\pm3\tau/H\);
- cap threshold \(\phi=i_0\);
- deviation tie \(\phi=x_-\);
- source SOC upper boundary approached from below.

No retained theorem uses an interior formula outside its certified regime.

---

## 9. Continuation audit

| Object | Status |
|---|---|
| Cournot quantity continuation, all feasible source histories | **SOLVED — UNIQUE** |
| Literal Hotelling pure price continuation | **SOLVED — UNIQUE OR EXACTLY CHARACTERIZED MULTIPLE** |
| No-loss Hotelling pure price continuation | **SOLVED — UNIQUE PURE** |
| Material unresolved continuation | **0** |
| Numerical failure used as evidence | **0** |

---

## 10. Counterexample search

The independent attack deliberately targeted:

- negative-output histories;
- cap-binding sourcing;
- Cournot rival exit;
- \(\rho\) near \(4/9,1/2,2/3\);
- Hotelling exact corner threshold;
- zero-demand price indifference;
- weak-dominance symmetry;
- high-cost price at marginal cost;
- nonlocal sourcing deviations;
- infeasible unconstrained corner optimum with feasible cap-boundary deviation.

Permanent regressions include:

1. Stage-1 Cournot negative-output history;
2. Cournot cap witness;
3. exact positive-slope BR witness;
4. exact three-equilibrium duopoly witness;
5. \(\rho=2/3\) continuum;
6. literal Hotelling corner continuum;
7. Hotelling \(p<c\preceq c\);
8. **new Stage-4A regression:** \(c\preceq c+\varepsilon\);
9. exact no-loss Hotelling \(1/90\) sourcing-deviation gain.

No surviving theorem was falsified after the Stage-4 amendment.

---

## 11. Welfare / benchmark-definition audit

**NOT APPLICABLE.**

No retained Stage-4A headline claim is a welfare/planner benchmark.

---

## 12. Evidence ledger

| Claim | Attack | Artifact | Result | Surviving limitation |
|---|---|---|---|---|
| C1 | independent potential-game reconstruction | \`audit/stage04a_cleanroom_derivation.md\`; \`code/stage04a_independent_verify.py\` | PASS | Stage II only |
| C2 | active-set curvature + kink-direction attack | same | PASS | source functional form |
| C3–C5 | KKT/cap/exact derivative attack | same + Stage-4 exact code | PASS | symmetric general-\(N\) scope |
| C6–C7 | independent duopoly branch reconstruction | same | PASS | pure strategies |
| C8 | alternative fixed-point search and exact primitive-payoff attack | same | PASS | pure source-duopoly Stage I |
| H1 | clipped-demand global price-BR reconstruction | same | PASS | pure price equilibrium |
| H2 | primitive payoff dominance | same | PASS | does not define refinement |
| H2b | symmetric dominance attack against \(p=c\) | same | PASS; forced Stage-4 amendment | no iterated-dominance claim |
| H3-NL | restricted mutual-BR attack | same | PASS | conditional \(p\ge c\), pure prices |
| H4–H5-NL | all branch/cap/nonlocal deviations | same | PASS | symmetric-candidate theorem |
| H6-NL | exact rational direct payoff | same | PASS | conditional \(p\ge c\) |

---

## 13. Formal-verification applicability

\[
\boxed{\textbf{FORMALIZATION APPLICABLE}}
\]

Reason: headline claims depend on published-sign reversal, piecewise cases, exact regime thresholds, multiplicity, and quantified inequalities.

Preliminary target map:

\`audit/stage04a_formalization_target_map.md\`.

Highest-priority targets are C4, H5-NL/H6-NL, C6/C7, and C8.

This prospective formalization is not counted as Stage-4A evidence and must be closed before theory freeze under the Stage-7.5A formal-verification gate.

---

## 14. Permanent regression tests created

New Stage-4A artifact:

\`code/stage04a_independent_verify.py\`.

It is deliberately separate from the Stage-4 production verification path.

The newly discovered dominance failure is permanently encoded:

\[
p=c+\varepsilon
\text{ weakly dominates }
p=c.
\]

This prevents the repository from reverting to the false “undominated-price equilibrium” interpretation.

---

## 15. Blocker status

The initial Stage-4A run found one material blocker:

> incorrect solution-concept characterization of the Hotelling \(p\ge c\) game.

Earliest affected stage: **Stage 4**.

That blocker was routed back, repaired at Stage 4, and the amended object was re-audited.

Current blocker count:

\[
\boxed{0}
\]

---

## 16. Canonical verdict and routing

\[
\boxed{\textbf{GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS}}
\]

The next canonical stage is:

\[
\boxed{\textbf{Stage 6 — Novelty Re-Kill}}
\]

Stage 5 is not triggered because no economic primitive repair is required. The correction was a theorem/refinement-scope repair at Stage 4.
