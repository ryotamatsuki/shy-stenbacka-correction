# Stage 4 — Minimal Model Gate

Status: **PASS — GO TO STAGE 4A**

Audit date: 2026-09-19  
Canonical workflow: `research-paper-workflow` v2.2  
Stage-3 frozen input: `ce32829fad98439cf97654e88d027d57756735d1`

## 1. Executive verdict

Stage 3 selected Candidate E, a unified Cournot + Hotelling global correction, with Candidate C (complete Cournot correction) as the only authorized fallback.

Stage 4 finds:

1. **Hotelling blocks Candidate E as the minimal canonical paper architecture.**  
   The source price subgame is unique only while the cost gap satisfies (|c_B-c_A|le 3	au). For larger cost gaps there is a continuum of valid pure price equilibria. The off-path continuation payoff of the low-cost firm therefore depends on equilibrium selection. The source paper states no no-below-cost restriction or equilibrium refinement that selects one continuation. Hence there is no single source-determined reduced Stage-I payoff outside the interior-share region.

2. **Candidate C closes analytically.**  
   In the Cournot model, the Stage-II equilibrium is unique at every feasible outsourcing history once nonnegative quantities are respected. Under the source restriction
   [
   b>left(rac{HN}{N+1}ight)^2,
   ]
   each firm's reduced Stage-I payoff is globally strictly concave in own outsourcing even across downstream active-set changes.

3. The reported symmetric Cournot stationary point is therefore globally valid whenever feasible. The missing primitive constraint changes it to
   [
   i_C^*=minleft{phi,,
   rac{HND}{b(N+1)^2-H^2N}
   ight},
   qquad
   Dequiv a-Hphi-rac{gammaphi^2}{2}>0.
   ]

4. The corrected competition comparative static is weakly negative:
   [
   rac{partial i_C^*}{partial N}le0,
   ]
   and is strictly negative whenever the upper outsourcing bound does not bind and (N>1).

5. The duopoly strategic-substitutes claim requires a stronger correction. On the global constrained game, the best response is piecewise. In a nonempty parameter region allowed by the paper, it contains a **slope (+2) regime** caused by the incentive to outsource just enough to drive the rival out of the downstream Cournot market. Asymmetric equilibria then arise.

Canonical verdict:

[
oxed{	extbf{STAGE 4 — GO}}
]

Route:

[
oxed{	extbf{GO TO STAGE 4A — INDEPENDENT MATHEMATICAL ADVERSARIAL CERTIFICATION}}
]

The object sent to Stage 4A is **Candidate C — Complete Cournot correction**, not Candidate E.

---

## 2. Exact source model and strategy sets

### Stage I

There are (Nge2) final-good firms. Firm (j) chooses its measure of outsourced inputs

[
i_jin[0,phi].
]

Under Assumption 2 of the source article,

[
c_j
=
H(phi-i_j)+rac{gammaphi^2}{2}
=
C_0-Hi_j,
]

where

[
C_0
=
Hphi+rac{gammaphi^2}{2}.
]

Monitoring cost is exactly

[
M(i_j)=i_j^2.
]

Define

[
D=a-C_0
=
a-Hphi-rac{gammaphi^2}{2}>0.
]

### Stage II

Each firm chooses

[
q_jge0.
]

Inverse demand is

[
p=a-bQ,
qquad
Q=sum_{j=1}^Nq_j.
]

Firm (j)'s total payoff is

[
Pi_j=(p-c_j)q_j-i_j^2.
]

The equilibrium concept is subgame-perfect equilibrium.

No new primitive has been introduced.

---

## 3. Stage-II Cournot continuation for every feasible history

Fix any outsourcing profile (iin[0,phi]^N), hence any induced cost vector (c).

Order costs:

[
c_{(1)}le c_{(2)}lecdotsle c_{(N)}.
]

For (m=1,ldots,N), define

[
p_m
=
rac{a+sum_{r=1}^m c_{(r)}}{m+1}.
]

There is a unique (m) such that

[
c_{(m)}<p_mle c_{(m+1)},
]

where (c_{(N+1)}=infty).

The unique Cournot equilibrium is

[
q_{(r)}
=
rac{p_m-c_{(r)}}{b}>0
qquad(rle m),
]

and

[
q_{(r)}=0
qquad(r>m).
]

A cost exactly equal to the equilibrium price receives zero output.

### Continuation status

Every feasible Stage-I outsourcing profile has a unique pure Stage-II continuation:

[
oxed{	exttt{SOLVED_EQUILIBRIUM}}
]

No Cournot continuation is `UNRESOLVED`, `NUMERICAL_FAILURE`, or selection-dependent.

The Stage-1 counterexample where equation (10) yielded a negative quantity is retained as a regression test. Under the corrected continuation it is simply a one-active-firm Cournot equilibrium.

---

## 4. Global concavity of the reduced Stage-I Cournot payoff

Fix firm (j)'s rivals' outsourcing choices and vary (x=i_j).

Suppose that at a given (x), firm (j) and (m-1) rivals are active downstream. Let

[
z_j=p-c_j>0.
]

Then operating profit is

[
pi_j^{op}
=
rac{z_j^2}{b}.
]

Within this fixed active-set regime,

[
rac{dz_j}{dx}
=
Hrac{m}{m+1}.
]

Therefore

[
rac{d^2Pi_j}{dx^2}
=
2rac{H^2m^2}{b(m+1)^2}-2.
]

Because

[
rac{m}{m+1}
le
rac{N}{N+1},
]

the source restriction

[
b>
left(rac{HN}{N+1}ight)^2
]

implies

[
rac{d^2Pi_j}{dx^2}<0
]

on every active-set branch.

### Active-set boundaries

Two types of boundary can occur as (x) rises.

1. **Firm (j) enters.** At entry, (z_j=0), so the operating-profit derivative is zero on both sides. The total-payoff derivative is continuous.

2. **A rival exits.** If total active firms fall from (m) to (m-1), (z_j) is continuous but the operating-profit marginal benefit falls from
   [
   rac{2H}{b}rac{m}{m+1}z_j
   ]
   to
   [
   rac{2H}{b}rac{m-1}{m}z_j.
   ]
   Thus the derivative jumps **downward**.

Hence the reduced payoff is globally strictly concave on

[
[0,phi].
]

This is the key construction-level result: the source's local concavity calculation was incomplete as a proof, but after solving the omitted active sets, global strict concavity actually survives.

---

## 5. Corrected general-(N) symmetric Cournot equilibrium

At a symmetric profile (i_j=s), all (N) firms are active because (D>0).

Each produces

[
q(s)
=
rac{D+Hs}{b(N+1)}.
]

The derivative of firm (j)'s reduced payoff at a symmetric profile is

[
rac{partialPi_j}{partial i_j}Big|_{i=s}
=
rac{2HN(D+Hs)}{b(N+1)^2}-2s.
]

The unconstrained stationary solution is

[
ar i_C
=
rac{HND}
{b(N+1)^2-H^2N}.
]

Because own payoff is globally strictly concave, the unique symmetric constrained best response is

[
oxed{
i_C^*
=
min{phi,ar i_C}.
}
]

The lower bound never binds because (D>0).

### Exact status of published equation (13)

- **Algebraically correct** as the unconstrained symmetric stationary point.
- **Globally optimal against the symmetric rivals** whenever (ar i_Clephi).
- **Infeasible** when (ar i_C>phi); the correct symmetric equilibrium is full outsourcing (i_C^*=phi).

Thus the Stage-1 wording “equation (13) is globally invalid because active sets are omitted” is too strong and is superseded by this Stage-4 result.

The active-set omission is a proof-completeness defect, but under the source SOC it does not destroy the feasible interior symmetric candidate.

---

## 6. Corrected comparative statics

For the interior branch,

[
ar i_C
=
rac{HND}
{b(N+1)^2-H^2N}.
]

### Competition intensity

Exact symbolic differentiation gives

[
rac{partialar i_C}{partial N}
=
-
rac{HDb(N^2-1)}
{left[b(N+1)^2-H^2Night]^2}<0
qquad(N>1).
]

Therefore the constrained equilibrium satisfies

[
oxed{
rac{partial i_C^*}{partial N}le0,
}
]

with strict inequality on the interior branch and zero locally while the full-outsourcing cap binds.

This reverses equation (14) and Proposition 3.

### Demand intercept

On the interior branch,

[
rac{partialar i_C}{partial a}
=
rac{HN}{b(N+1)^2-H^2N}>0.
]

Globally, (i_C^*) is weakly increasing in (a): it becomes flat at the cap.

### Input-cost slope (gamma)

[
rac{partialar i_C}{partialgamma}
=
-
rac{HNphi^2}
{2[b(N+1)^2-H^2N]}<0.
]

Globally, (i_C^*) is weakly decreasing in (gamma).

### Total input measure (phi)

On the interior branch,

[
rac{partialar i_C}{partialphi}
=
-
rac{HN(H+gammaphi)}
{b(N+1)^2-H^2N}<0.
]

But when the outsourcing cap binds,

[
i_C^*=phi,
]

so

[
rac{partial i_C^*}{partialphi}=1.
]

Hence the **number** of outsourced inputs is not globally decreasing in (phi). It rises one-for-one in the full-outsourcing region and falls after the unique transition to the interior regime.

The transition solves

[
HN a-rac{HNgamma}{2}phi^2
=
b(N+1)^2phi.
]

The outsourcing **fraction** behaves more cleanly:

[
rac{i_C^*}{phi}
=
1
]

on the cap branch, while on the interior branch

[
rac{partial}{partialphi}
left(rac{ar i_C}{phi}ight)
=
-
rac{HN(2a+gammaphi^2)}
{2phi^2[b(N+1)^2-H^2N]}<0.
]

Therefore the fraction is weakly decreasing in (phi), not globally strictly decreasing.

---

## 7. Complete source-duopoly global best response

The source itself turns to duopoly for Proposition 5, so the complete global strategic-interaction audit is carried out for (N=2).

Normalize

[
delta=rac{D}{H}>0,
qquad
ho=rac{b}{H^2}>rac49.
]

Let (y) denote the rival's outsourcing and (x) own outsourcing.

### Downstream regimes

Define

[
L(y)=rac{y-delta}{2},
qquad
U(y)=delta+2y.
]

The unique Stage-II continuation is:

- **own firm inactive:** (xle L(y));
- **both firms active:** (L(y)<x<U(y));
- **rival inactive / own firm monopoly:** (xge U(y)).

At equality the exiting firm's quantity is zero.

The corresponding reduced payoffs are

[
V_0(x)=-x^2,
]

[
V_A(x;y)
=
rac{(delta+2x-y)^2}{9ho}-x^2,
]

and

[
V_M(x)
=
rac{(delta+x)^2}{4ho}-x^2.
]

All are strictly concave under (ho>4/9), and the derivative jumps downward at regime switches.

### Branch stationary points

On the both-active branch,

[
A(y)
=
rac{2(delta-y)}{9ho-4}.
]

On the monopoly branch,

[
M
=
rac{delta}{4ho-1}.
]

The monopoly-entry kink is

[
U(y)=delta+2y.
]

### Unconstrained global best response (R(y))

For (ygedelta),

[
R(y)=0.
]

For (0le y<delta):

#### Case I: (hoge2/3)

[
R(y)=A(y).
]

At (ho=2/3), this becomes

[
R(y)=delta-y.
]

#### Case II: (1/2leho<2/3)

Define

[
y_A
=
rac{delta(2-3ho)}
{2(3ho-1)}.
]

Then

[
R(y)
=
egin{cases}
U(y), & 0le yle y_A,\
A(y), & y_Ale y<delta.
end{cases}
]

#### Case III: (4/9<ho<1/2)

Define additionally

[
y_M
=
rac{delta(1-2ho)}
{4ho-1}.
]

Then

[
R(y)
=
egin{cases}
M, & 0le yle y_M,\
U(y), & y_Mle yle y_A,\
A(y), & y_Ale y<delta.
end{cases}
]

The constrained source best response is simply

[
oxed{
B_phi(y)=min{phi,R(y)}.
}
]

This follows from global strict concavity.

---

## 8. Proposition 5: local strategic substitutes become a regime-switch result

The published equation (15) corresponds to the regular both-active branch (A(y)), whose slope is

[
A'(y)
=
-rac{2}{9ho-4}<0.
]

This is correct locally.

But when

[
rac49<ho<rac23,
]

the global best response contains the kink branch

[
R(y)=U(y)=delta+2y,
]

and therefore

[
oxed{
R'(y)=2>0.
}
]

The mechanism is exact:

> A sufficiently aggressive outsourcer prefers to choose the **minimum outsourcing needed to make the rival inactive**. If the rival outsources more, that foreclosure/exit threshold rises, so the firm's own optimal outsourcing rises as well.

Thus outsourcing is not globally a strategic substitute throughout the source parameter domain.

For (hoge2/3), the unconstrained global best response is decreasing; the source statement survives in a weak constrained form because the cap can create flat segments.

---

## 9. Complete pure Stage-I equilibrium correspondence in the source duopoly

Define the symmetric interior fixed point

[
s
=
rac{2delta}{9ho-2}.
]

### Case A: (ho>2/3)

There is a unique pure Stage-I equilibrium:

[
oxed{
(min{phi,s},min{phi,s}).
}
]

### Case B: (ho=2/3)

Then

[
R(y)=max{0,delta-y}.
]

If

[
phi<rac{delta}{2},
]

the unique equilibrium is

[
(phi,phi).
]

If

[
phigerac{delta}{2},
]

there is a continuum:

[
oxed{
mathcal E
=
left{
(x,delta-x):
xin
[max{0,delta-phi},min{phi,delta}]
ight}.
}
]

### Case C: (4/9<ho<2/3)

If

[
phile s,
]

the unique equilibrium is

[
(phi,phi).
]

If

[
phi>s,
]

there are exactly three pure equilibria.

One is symmetric:

[
(s,s).
]

Define

[
h=R(0),
qquad
x_H=min{phi,h},
qquad
x_L=R(x_H).
]

Then the other two are

[
oxed{
(x_H,x_L)
quad	ext{and}quad
(x_L,x_H).
}
]

For sufficiently large (phi), these specialize to one aggressively outsourcing active firm and one zero-outsourcing inactive rival.

### Exact source-admissible witness

Take

[
ho=rac35,qquad
delta=1,qquad
phi=2.
]

Then

[
s=rac{10}{17},
]

and the three equilibria are

[
left(rac{10}{17},rac{10}{17}ight),
qquad
(1,0),
qquad
(0,1).
]

Moreover,

[
R(0)=1,
qquad
Rleft(rac1{20}ight)=rac{11}{10},
]

directly displaying the positive-slope global best-response region.

This witness satisfies the source concavity restriction (ho>4/9).

---

## 10. Hotelling audit and why Candidate E is dropped

The source's Hotelling consumer choice compares only brands (A) and (B); the paper then maximizes prices using the interior indifferent-consumer formula. No (p_jge c_j) restriction or weak-dominance refinement is stated.

Let

[
d_c=c_B-c_A.
]

Using the complete clipped market shares, the price subgame is:

### If (|d_c|le3	au)

The pure equilibrium is unique and equals the source equation (19):

[
p_A
=
rac{2c_A+c_B+3	au}{3},
qquad
p_B
=
rac{c_A+2c_B+3	au}{3}.
]

At (|d_c|=3	au), one firm has zero share.

### If (d_c>3	au)

Firm (A) is the low-cost firm. There is a continuum of pure price equilibria indexed by

[
sin[c_A+3	au,c_B]:
]

[
oxed{
p_B=s,qquad p_A=s-	au.
}
]

Firm (A) serves the entire market. Firm (B)'s operating profit is zero.

The low-cost firm's operating profit ranges from

[
2n	au
]

to

[
n(d_c-	au).
]

The mirror statement holds when (d_c<-3	au).

### Consequence for Stage I

The reduced Stage-I continuation payoff is a **correspondence**, not a single function, whenever an outsourcing deviation generates (|d_c|>3	au).

The earlier Stage-1 witness

[
H=n=1,quad
	au=rac1{15},quad
i_0=rac16,quad
i'=rac12
]

illustrates the selection dependence exactly.

The symmetric source payoff is

[
Pi_{m sym}=rac1{180}.
]

For the same deviation (i'=1/2):

- lower-end corner continuation:
  [
  Pi_{m dev}^{L}
  =
  -rac7{60}
  <
  Pi_{m sym};
  ]
- upper-end corner continuation:
  [
  Pi_{m dev}^{H}
  =
  rac1{60}
  >
  Pi_{m sym}.
  ]

Therefore the Stage-1 statement that this deviation **unconditionally** overturns Proposition 6 is rejected.

### General selection comparison

At the symmetric interior source candidate

[
i_0=rac{Hn}{6},
]

the least favorable low-cost corner continuation evaluated at the regime boundary gives

[
DeltaPi_{min}
=
rac{	au(H^2n-18	au)}{2H^2}<0
]

under the source local SOC

[
H^2n<18	au.
]

Thus a valid continuation selection exists that deters corner deviations.

By contrast, the high-profit corner selection yields an optimal deviation with gain

[
DeltaPi_{max}
=
rac{n(2H^2n-27	au)}{18},
]

which is positive when

[
H^2n>rac{27}{2}	au
]

and the required outsourcing action is feasible.

Hence the source Hotelling model has a genuine **off-path equilibrium-selection problem**. A no-below-cost refinement would remove the low-price zero-demand equilibria, but that refinement is not part of the published model and is not introduced here.

### Candidate-E verdict

[
oxed{	extbf{REJECT AS MINIMAL CANONICAL ARCHITECTURE}}
]

The Hotelling finding is retained as an audit result, but the paper architecture sent to Stage 4A is Cournot Candidate C.

---

## 11. Off-path continuation completeness audit

### Cournot fallback model

- Equilibrium concept: SPNE.
- Full Stage-I domain: ([0,phi]^N).
- Full Stage-II domain: (q_jge0).
- Active sets checked: all possible active-set sizes via sorted-cost characterization.
- Pure continuation existence: always.
- Pure continuation uniqueness: always.
- Number of unresolved Cournot continuations: **0**.
- Number of numerical failures: **0**.
- Final continuation verdict: **PASS**.

### Hotelling diagnostic

- Full price subgame solved analytically.
- Interior and full-market corner regimes checked.
- Pure equilibrium nonexistence: none found.
- Multiplicity: **yes** for (|c_B-c_A|>3	au).
- Selection assumption in source: none.
- Final verdict for a single reduced Stage-I payoff: **FAIL / SELECTION-DEPENDENT**, not unresolved.

---

## 12. Independent direct-payoff deviation audit

The verification artifact

`code/stage04_verify.py`

contains a direct Cournot active-set solver constructed from primitive KKT conditions. It does not call the published equation (10).

It reproduces:

1. the Stage-1 negative-quantity history as a valid one-active-firm equilibrium;
2. the cap witness where the published (i=6/5) is replaced by (i=1);
3. the exact duopoly three-equilibrium witness;
4. the Hotelling two-continuation witness in which the same outsourcing deviation is profitable under one valid price equilibrium and unprofitable under another.

All permanent counterexamples are retained as assertions.

---

## 13. Candidate-proposition kill table

| Candidate proposition from Stage 3 | Stage-4 result | Status |
|---|---|---|
| CP1: source-specific equation-(14) sign correction | Interior derivative strictly negative; constrained derivative weakly negative | **PROVED** |
| CP2: exact validity region of published symmetric Cournot candidate | Valid iff unconstrained candidate (ar i_Clephi); otherwise cap binds | **PROVED** |
| CP3: complete general-(N) asymmetric equilibrium correspondence | Not required by source's stated symmetric general-(N) scope; not claimed | **KILLED AS OVERBROAD SCOPE** |
| CP4: complete Hotelling price-continuation partition | Unique interior + multiple corner price equilibria | **PROVED** |
| CP5: source Hotelling candidate is globally false on a nonempty region | Depends on off-path price-equilibrium selection | **REJECTED AS SELECTION-FREE CLAIM** |
| CP6: one unified global correction principle supports one minimal paper | Hotelling multiplicity makes the unified reduced game non-single-valued | **REJECTED FOR CANONICAL PAPER ARCHITECTURE** |
| CP7: Proposition 5 needs global qualification | BR can have slope (+2); asymmetric/continuum equilibria arise | **PROVED** |

---

## 14. Canonical mathematical representation

### Cournot Stage II

Application-neutral class:

- linear-demand Cournot game;
- nonnegative action orthant;
- heterogeneous constant marginal costs;
- unique equilibrium characterized by active-set KKT / linear complementarity conditions.

Parent-class candidate:

- linear complementarity problem for Cournot quantities.

### Reduced Stage I

Application-neutral class:

- box-constrained ([0,phi]^N) game;
- piecewise-quadratic own payoffs;
- globally strictly concave own objective under the source SOC;
- endogenous regime switching inherited from the downstream complementarity problem.

For the source duopoly:

- best response is piecewise affine;
- slopes can be (0), (+2), or (-2/(9ho-4));
- equilibrium multiplicity is generated by the downstream-exit kink.

Parent classes to pass unchanged to Stage 6:

- concave games;
- piecewise-affine best-response games;
- complementarity-induced regime-switch games;
- strategic substitutes with endogenous participation/exit.

No theorem-absorption claim is made at Stage 4.

---

## 15. Mechanism decomposition

The corrected Cournot mechanism has three channels.

### Channel 1 — direct marginal-cost benefit

More outsourcing lowers own marginal cost by (H).

### Channel 2 — monitoring-cost curvature

The marginal monitoring cost is (2i_j), limiting outsourcing and generating an interior solution when the cap does not bind.

### Channel 3 — downstream regime switching

A sufficiently large own cost advantage can reduce a rival's equilibrium quantity to zero.

On the regular all-active branch, a rival's extra outsourcing lowers own optimal outsourcing: the source strategic-substitute effect.

Near the rival-exit threshold, however, own outsourcing has a discrete strategic role: it determines whether the rival remains active. The optimal response can therefore be to **track the exit threshold**, producing

[
rac{dBR}{di_k}=2.
]

This third channel is exactly what the source regular-branch calculation omits.

---

## 16. Consumer surplus and welfare

**NOT APPLICABLE TO THE CANONICAL STAGE-4 CLAIM SET.**

The correction concerns equilibrium existence, feasibility, comparative statics, and strategic interaction. No source welfare proposition is needed to establish the correction.

Adding a planner problem solely to satisfy a generic workflow field would change the project rather than audit the source model.

---

## 17. Private versus social decision

**NOT APPLICABLE.**

No planner benchmark is part of the surviving correction claim.

---

## 18. Limiting and boundary cases

### (H	o0)

[
i_C^*	o0.
]

The source no-cost-advantage benchmark is recovered.

### Outsourcing cap binding

[
i_C^*=phi.
]

Competition and demand comparative statics become locally flat until the interior branch is reached.

### Duopoly (hodownarrow4/9)

The all-active Stage-I curvature approaches zero from below. The source SOC boundary is therefore economically and mathematically material.

### Duopoly (ho=2/3)

A continuum of Stage-I equilibria appears.

### Duopoly (ho>2/3)

The global BR is decreasing and the pure Stage-I equilibrium is unique.

### Hotelling (|d_c|=3	au)

The unique interior formula reaches a zero-share boundary exactly. Multiplicity begins only beyond that boundary.

---

## 19. Nested-benchmark recovery

### C0 — source regular all-active Cournot branch

Recovered exactly:

- equation (13) as unconstrained symmetric stationary point;
- equation (15) as the both-active duopoly branch.

The corrected equation-(14) derivative has the opposite sign.

### C1 — globally all-active plus outsourcing cap

When parameter restrictions prevent downstream exit for every feasible history, the only correction is the box constraint:

[
i_C^*=min{phi,ar i_C}.
]

### Full Cournot model

Removing the global-all-active restriction creates the duopoly kink branch and the additional asymmetric/continuum equilibrium regions.

This is the full-model result unavailable from C0/C1 alone.

---

## 20. Full-model-only result table

| Result | Regular all-active benchmark | Full Cournot source game |
|---|---|---|
| Eq. (13) interior stationary point | Yes | Recovered when feasible |
| Correct (N)-comparative-static sign | Yes after algebra repair | Weakly negative after cap |
| Full-outsourcing boundary | No | Yes |
| Rival exit | No | Yes |
| Positive-slope BR region | No | **Yes** |
| Asymmetric Stage-I equilibria | Not generated by regular source argument | **Yes for (4/9<ho<2/3), (phi>s)** |
| Continuum at (ho=2/3) | Hidden by symmetric focus | **Yes** |

---

## 21. Numerical / computational counterexample audit

No numerical approximation is used as proof.

Exact rational regression cases are stored in `code/stage04_verify.py`.

A broader deterministic search was also used during construction to attack the proposed duopoly equilibrium classification. No counterexample to the stated piecewise classification was found. That search is supporting evidence only; the report's claims rely on the analytical best-response structure.

---

## 22. Permanent regression tests

Retained permanently:

1. Cournot feasible history where source equation (10) returns (q<0).
2. Cournot parameter point where source equation (13) gives (i>phi).
3. Cournot duopoly with (ho=3/5,delta=1,phi=2) yielding exactly the three displayed equilibria.
4. Hotelling cost-gap history with two distinct valid corner price equilibria.
5. Hotelling outsourcing deviation profitable under the upper continuation but unprofitable under the lower continuation.

---

## 23. Artefact audit

Canonical Stage-4 artifacts:

- `audit/STAGE_04_MINIMAL_MODEL_GATE.md`
- `audit/stage04_continuation_ledger.md`
- `audit/stage04_theorem_certificates.md`
- `code/stage04_verify.py`

Earlier Stage-1 Hotelling wording is superseded where inconsistent with this report.

No copyrighted source PDF is added.

---

## 24. Exact diagnosed blocker for Candidate E

The blocker is **not** lack of a price equilibrium.

It is:

> for (|c_B-c_A|>3	au), the source Hotelling price subgame has multiple pure equilibria that deliver different low-cost continuation profits, and the source specifies no equilibrium-selection/refinement rule.

Therefore a single-valued reduced Stage-I game cannot be inferred from the published primitives alone.

Adding a no-below-cost restriction or weak-dominance refinement would be a substantive selection modification and is not authorized at this stage.

---

## 25. Canonical stage verdict

For the authorized Cournot fallback Candidate C:

[
oxed{	extbf{GO}}
]

For the originally preferred unified Candidate E:

[
oxed{	extbf{REJECTED AS CANONICAL MINIMAL ARCHITECTURE}}
]

---

## 26. Next-stage contract

Stage 4A receives Candidate C unchanged.

It must independently attack:

1. the sorted-cost Cournot continuation proof;
2. global strict concavity across active-set changes;
3. the constrained symmetric equilibrium
   [
   i_C^*=min{phi,ar i_C};
   ]
4. the corrected weakly negative (N)-comparative static;
5. the (phi)-boundary comparative statics;
6. the complete duopoly best-response formula;
7. the three-case duopoly equilibrium correspondence;
8. the (ho=2/3) continuum;
9. the claim that Proposition 5 fails globally for (4/9<ho<2/3);
10. all permanent regression examples.

Stage 4A may not restore Candidate E, impose a Hotelling refinement, or silently repair any proof.
