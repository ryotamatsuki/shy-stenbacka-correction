# Stage 7 Generality, Selection, Institutional, and Exposition Register

Status: **CERTIFIED FOR STAGE 7**

## 1. Equilibrium-selection robustness

| Welfare / interpretation claim | Equilibrium-set status | Selection / refinement | All-equilibria proof or counterexample | Cross-component issue | Maximum defensible wording |
|---|---|---|---|---|---|
| Cournot exact welfare identity (W-C1) | all feasible profiles | none | accounting identity | none | exact for source model |
| Symmetric private vs C-R sourcing | symmetric Cournot path only | symmetric benchmark | not a claim over asymmetric equilibria | N/A | private common sourcing weakly exceeds restricted common-sourcing welfare optimum for \(N\ge2\) |
| Welfare of source-duopoly pure equilibria | multiple for certified regions | none | exact counterexamples show welfare differs | no separate markets | **selection-dependent** |
| \(\rho=2/3\) Cournot continuum | continuum | none | (W-C5) varies with equilibrium | N/A | no selection-free welfare ranking |
| Literal Hotelling price continuum at fixed sourcing | multiple price equilibria | literal Nash | prices cancel and corner allocation is the same | off-path selections may differ by history | welfare is invariant **within a fixed corner sourcing history** |
| Literal Hotelling Stage-I welfare | continuation-selection dependent | none | complete Stage-I equilibrium set not certified | off-path selections affect Stage-I incentives | **unresolved under multiplicity** |
| No-loss Hotelling symmetric candidate | conditional auxiliary game | explicit \(p\ge c\) | candidate survival theorem certified | no mixed-equilibrium claim | any welfare statement is **restriction-conditional** |
| Hotelling fixed-sourcing efficient share | planner allocation benchmark | none | exact optimization | N/A | standard fixed-sourcing efficiency diagnostic |

Cournot and Hotelling are alternative product-market specifications, not simultaneous markets. No cross-market equilibrium-selection aggregation is required.

---

## 2. Institutional evidence

The project is a correction of a theoretical source model. No empirical institution is needed for mathematical validity.

Institutional evidence is therefore used only to discipline interpretation.

| Model primitive / interpretation | Evidence | Classification | Limitation |
|---|---|---|---|
| Firms commonly fragment/partially outsource manufacturing activities | manufacturing fragmentation evidence, including Fort (2017) | **ESTABLISHED at broad phenomenon level** | does not imply continuum action |
| Outsourcing may provide production-cost advantages | source model; Bardhan–Whitaker–Mithas (2006); broader empirical literature | **SUGGESTIVE** | empirical performance effects are heterogeneous |
| Outsourced production requires monitoring / audits / quality-control governance | Handley & Gray (2013), dyadic contract-manufacturing data | **ESTABLISHED as an activity/cost category** | no evidence for exact quadratic cost |
| Monitoring cost is quadratic in number outsourced | source tractability assumption | **UNVERIFIED** | do not present as empirical fact |
| Monitoring cost is independent of output scale | source assumption | **UNVERIFIED** | important for planner nonconvexity |
| Outsourcing lowers marginal cost linearly by \(H\) per input | source Assumption 2 normalization | **UNVERIFIED as general empirical law** | baseline functional form only |
| Sourcing-induced cost asymmetry can force a product-market rival to zero output | theoretical implication | **UNVERIFIED empirically** | do not state as observed regularity |
| \(p\ge c\) no-loss pricing | auxiliary modeling restriction | **NOT AN INSTITUTIONAL FACT** | conditional robustness only |

The institutional evidence validates the broad trade-off “cost savings versus governance/monitoring burden,” not the source's exact functional forms.

---

## 3. Generality / robustness classification

| Claim | Baseline form/class | Evidence type | Assumptions used | Maximum defensible scope | Stage-7.5A attack target |
|---|---|---|---|---|---|
| S1 Proposition-3 sign reversal | linear demand, linear cost reduction, quadratic monitoring | exact proof | full source formula | **BASELINE FUNCTIONAL FORM** | try alternative demand / cost curvature |
| S2 positive-slope rival-exit BR segment | source duopoly | exact proof | linear Cournot, nonnegative output, source costs | **BASELINE FUNCTIONAL FORM** for global-BR theorem | test whether kink direction survives general \(c(i)\), \(M(i)\) |
| Exit threshold rises with rival cost reduction | linear Cournot + differentiable decreasing cost function | analytic mapping support | \(c'(i)<0\) | **CONJECTURED / RESTRICTED-CLASS MECHANISM SUPPORT** | formally prove or find counterexample |
| S3 complete pure duopoly correspondence | source normalized model | exact proof | linear demand/cost, quadratic monitoring, box constraint | **BASELINE FUNCTIONAL FORM** | attack every threshold/knife edge under quantifier review |
| C2 global own concavity | source functional form under source SOC | exact Stage-4A proof | linear Cournot + quadratic monitoring | **SUFFICIENT-CONDITION THEOREM WITHIN BASELINE CLASS** | identify minimal curvature conditions |
| S4 literal Hotelling corner multiplicity | linear Hotelling, full coverage, unrestricted prices | exact proof | linear transport, pure pricing | **BASELINE / RESTRICTED HOTELLING CLASS** | incomplete coverage; alternative transport costs |
| S5 no-loss Proposition-6 threshold | source Hotelling + explicit \(p\ge c\) | exact proof | pure prices, full coverage, linear transport | **BASELINE FUNCTIONAL FORM / RESTRICTION-CONDITIONAL** | mixed prices; incomplete coverage; cap knife edges |
| C-R welfare comparison | symmetric Cournot path | exact proof | common sourcing instrument, decentralized output | **RESTRICTED-INSTRUMENT BENCHMARK** | compare against full planner; ensure no first-best language |
| H fixed-allocation welfare comparison | fixed \(x=1/2\) | exact proof | full coverage, fixed allocation | **FIXED-ALLOCATION BENCHMARK** | cap and allocation endogeneity |

No generic theorem about outsourcing, investment games, or spatial competition is claimed.

---

## 4. Two genuinely different interpretations

### Setting A — partial manufacturing outsourcing

Direct source interpretation:

- a continuum of required components;
- specialized suppliers have lower unit production cost;
- the final-good firm incurs monitoring/coordination cost as more lines are outsourced;
- downstream competition can make sourcing a strategic commitment.

Status: **DIRECT BASELINE INTERPRETATION**.

### Setting B — cost-reducing process / organizational investment before Cournot competition

Application-neutral mapping:

\[
x_j=i_j,
\qquad
c_j=C_0-Hx_j,
\qquad
K(x_j)=x_j^2.
\]

Then the source model is a continuous cost-reduction investment game followed by Cournot competition with nonnegative quantities.

Status: **EXACT ALGEBRAIC REINTERPRETATION OF THE BASELINE**, not a new general theorem.

This second setting confirms that the active-set logic is not semantically tied to the word “outsourcing.” It does not establish robustness to different demand, cost, or investment functions.

---

## 5. Empirical predictions implied by the frozen model

These are model predictions, not established facts.

1. **All-active Cournot region:** holding source primitives fixed, the corrected symmetric outsourcing level decreases with the number of firms on the interior branch.

2. **Duopoly exit-kink region:** an increase in a rival's outsourcing can increase own optimal outsourcing because more own cost reduction is needed to push the rival to zero downstream output.

3. **Equilibrium asymmetry:** even ex ante identical source-duopoly firms can settle at high/low outsourcing profiles in the certified multiplicity region.

4. **Regime sensitivity:** estimated outsourcing responses to competitive pressure should differ sharply between samples where all downstream firms remain active and samples near exit/zero-output thresholds.

5. **Hotelling local-vs-global prediction:** the published local symmetric outsourcing formula is independent of \(\tau\), but once sufficiently large cost gaps/corner continuations are relevant, global equilibrium validity can depend on \(\tau\).

6. **Monitoring technology:** lower monitoring/coordination cost should enlarge the economically relevant outsourcing region; the exact source quadratic form is not claimed empirically.

These predictions could discipline future empirical work but are not required for the correction paper to be valid.

---

## 6. Result-to-exposition triage

| Headline result | Economic object | Candidate vehicle | Why | Verified source | Stage-10 action |
|---|---|---|---|---|---|
| S1 Eq14 / Proposition-3 reversal | competition comparative static | theorem/proposition + one displayed derivative | correction is algebraically sharp | Stage 4A + Stage 6 | main text |
| S2 global Proposition-5 failure | piecewise global BR | proposition + BR figure | figure shows negative branch, \(+2\) exit kink, cap | Stage 4A | main text; create figure only after freeze |
| S3 complete pure duopoly correspondence | equilibrium-set phase structure | theorem + compact regime table / phase diagram | multiplicity is easier to audit visually | Stage 4A | main text theorem; table/figure candidate |
| S4 literal Hotelling multiplicity | off-path continuation set | concise proposition + prose/table | avoid letting secondary result dominate paper | Stage 4A | short main-text or appendix |
| S5 no-loss failure threshold | conditional robustness region | appendix proposition; optional parameter-region figure | conditional auxiliary model | Stage 4A | appendix unless journal space permits |
| Cournot restricted welfare benchmark | private/social common-sourcing wedge | concise prose/table | not first-best and selection-sensitive | Stage 7 | appendix/prose only |
| Hotelling welfare diagnostics | allocation / fixed-split sourcing | concise appendix prose | standard and secondary | Stage 7 | omit from headline contribution |

There is no figure quota. Welfare graphics are not recommended at present.

---

## 7. Policy scope and limits

No tax, subsidy, mandate, merger rule, outsourcing restriction, or industrial-policy instrument is modeled.

Therefore Stage 7 authorizes **no policy prescription** such as:

- subsidize outsourcing;
- tax outsourcing;
- prevent outsourcing-induced exit;
- mandate no-loss pricing;
- prefer symmetric or asymmetric equilibria.

Permitted interpretation:

> The corrected model cautions against treating outsourcing as globally monotone in competitive intensity or globally strategic-substitute behavior when downstream participation can change.

Permitted empirical implication:

> Empirical analyses may need to distinguish interior/all-active observations from observations near market-exit regimes.

---

## 8. Stage-7.5A counterexample targets

1. Attempt to reverse S1 under nonlinear inverse demand while keeping economically regular demand.
2. Replace quadratic monitoring by a general convex \(M(i)\); test whether C2 global concavity and C7 kink optimality survive.
3. Replace linear cost reduction by a decreasing nonlinear \(c(i)\); test the rival-exit threshold geometry.
4. Attack C8 at every equality / knife edge: \(\rho=4/9,1/2,2/3\), \(\phi=s\), \(y=y_M,y_A\).
5. Verify no theorem silently treats integer \(N\) comparative statics as a continuous-\(N\) primitive beyond a derivative device.
6. Attack all welfare benchmark labels against the full planner choice sets.
7. Use the exact multiple Cournot equilibria to reject any selection-free welfare prose.
8. Hotelling: test incomplete market coverage / finite reservation utility.
9. Hotelling: test whether any manuscript wording upgrades pure-price uniqueness under \(p\ge c\) to mixed-equilibrium uniqueness.
10. Institutional: reject any sentence presenting quadratic/output-independent monitoring cost as empirically established.
