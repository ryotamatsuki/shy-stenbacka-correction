# Stage 4 — Minimal Model Gate

Status: **PASS — GO TO STAGE 4A**

Audit date: 2026-09-19  
Canonical workflow: \`research-paper-workflow\` v2.2  
Stage-3 frozen input: \`ce32829fad98439cf97654e88d027d57756735d1\`

## 1. Executive verdict

Stage 3 selected Candidate E (unified Cournot + Hotelling correction), with Candidate C (complete Cournot correction) as the authorized fallback.

Stage 4 was partially reopened after identifying an economically material refinement issue in the Hotelling subgame. The re-audit proves that every below-marginal-cost price is weakly dominated by marginal-cost pricing. The literal source game still has off-path corner multiplicity, but after one-round elimination of these weakly dominated prices the Hotelling continuation is unique and Proposition 6 fails on an exact nonempty source-admissible region. The canonical architecture is therefore amended to **Candidate E′ — complete Cournot correction plus a two-layer Hotelling correction**.

\[
\boxed{\textbf{STAGE 4 — GO}}
\]

\[
\boxed{\textbf{ROUTE: STAGE 4A — INDEPENDENT MATHEMATICAL ADVERSARIAL CERTIFICATION}}
\]

The central construction results are:

1. Every feasible Cournot sourcing history has a unique nonnegative-quantity continuation equilibrium.
2. Under the source SOC,
   \[
   b>\left(\frac{HN}{N+1}\right)^2,
   \]
   each firm's reduced Stage-I Cournot payoff is globally strictly concave in own outsourcing, including across downstream active-set changes.
3. The corrected symmetric Cournot action is
   \[
   i_C^*
   =
   \min\left\{
   \phi,\,
   \frac{HND}{b(N+1)^2-H^2N}
   \right\},
   \qquad
   D=a-H\phi-\frac{\gamma\phi^2}{2}>0.
   \]
4. Equation (14) and Proposition 3 have the wrong sign: the corrected symmetric outsourcing level is weakly decreasing in \(N\), strictly decreasing on the interior branch for \(N>1\).
5. Proposition 5 is false as a global statement. In the source duopoly, the global best response can contain a slope-\(+2\) regime and asymmetric equilibria.
6. Hotelling has a two-layer correction. In the literal source game, \(|c_B-c_A|>3\tau\) generates a continuum of corner price equilibria. Every member of that continuum except the marginal-cost endpoint uses a weakly dominated below-cost price by the zero-demand high-cost firm. Under the undominated-price refinement the corner continuation is unique, and the source symmetric outsourcing candidate fails exactly when the conditions in audit/STAGE_04_HOTELLING_REAUDIT.md hold.

No new primitive is introduced.

---

## 2. Exact source model

Each firm chooses outsourcing

\[
i_j\in[0,\phi].
\]

Under the source normalization,

\[
c_j
=
H(\phi-i_j)+\frac{\gamma\phi^2}{2}
=
C_0-Hi_j,
\qquad
C_0=H\phi+\frac{\gamma\phi^2}{2}.
\]

Monitoring cost is

\[
M(i_j)=i_j^2.
\]

Define

\[
D=a-C_0>0.
\]

### Cournot Stage II

\[
q_j\ge0,
\qquad
p=a-b\sum_{k=1}^N q_k,
\]

and

\[
\Pi_j=(p-c_j)q_j-i_j^2.
\]

The equilibrium concept is SPNE.

---

## 3. Complete Stage-II Cournot continuation

For any induced cost vector \(c=(c_1,\ldots,c_N)\), sort costs

\[
c_{(1)}\le\cdots\le c_{(N)}.
\]

For \(m=1,\ldots,N\), define

\[
p_m
=
\frac{a+\sum_{r=1}^{m}c_{(r)}}{m+1}.
\]

There is a unique active set \(S\) of the lowest-cost firms such that

\[
c_j<p_S \quad(j\in S),
\qquad
c_j\ge p_S \quad(j\notin S),
\]

where

\[
p_S=\frac{a+\sum_{j\in S}c_j}{|S|+1}.
\]

The unique quantity equilibrium is

\[
q_j=
\begin{cases}
(p_S-c_j)/b, & j\in S,\\
0, & j\notin S.
\end{cases}
\]

A firm with \(c_j=p_S\) receives zero output.

Thus every feasible Stage-I history has a unique pure Cournot continuation.

**Continuation status:** \`SOLVED_EQUILIBRIUM\` on the entire source domain.

---

## 4. Global own-payoff concavity

Fix rivals' outsourcing and vary \(x=i_j\).

Suppose \(j\) is active with \(m\) total active firms. Let

\[
z_j=p-c_j>0.
\]

Then

\[
\pi_j^{op}=\frac{z_j^2}{b},
\qquad
\frac{dz_j}{dx}
=
H\frac{m}{m+1}.
\]

Hence on that branch,

\[
\frac{d^2\Pi_j}{dx^2}
=
2\frac{H^2m^2}{b(m+1)^2}-2.
\]

Because

\[
\frac{m}{m+1}\le\frac{N}{N+1},
\]

the source SOC implies strict negativity on every branch.

At own entry, \(z_j=0\), so the derivative joins continuously. At a rival-exit threshold, the marginal operating benefit falls from

\[
\frac{2H}{b}\frac{m}{m+1}z_j
\]

to

\[
\frac{2H}{b}\frac{m-1}{m}z_j,
\]

so the derivative jumps downward.

Therefore the reduced Stage-I payoff is globally strictly concave on \([0,\phi]\).

### Theorem C1

Under the source SOC, for every rivals' feasible sourcing profile, a firm's reduced Cournot payoff is globally strictly concave in its own outsourcing action.

**Status:** PROVED.

---

## 5. Corrected general-\(N\) symmetric Cournot equilibrium

At a symmetric profile \(i_j=s\), all firms are active and

\[
q(s)=\frac{D+Hs}{b(N+1)}.
\]

The own derivative is

\[
\frac{\partial\Pi_j}{\partial i_j}\Big|_{i=s}
=
\frac{2HN(D+Hs)}{b(N+1)^2}-2s.
\]

The unconstrained root is

\[
\bar i_C
=
\frac{HND}{b(N+1)^2-H^2N}.
\]

Global strict concavity makes the KKT condition sufficient, so the unique symmetric Stage-I equilibrium action is

\[
\boxed{
i_C^*=\min\{\phi,\bar i_C\}.
}
\]

The lower bound does not bind because \(D>0\).

### Status of source equation (13)

Equation (13) is algebraically correct as the unconstrained symmetric stationary point. It is globally optimal against symmetric rivals whenever \(\bar i_C\le\phi\). If \(\bar i_C>\phi\), the correct symmetric equilibrium is full outsourcing \(i_C^*=\phi\).

The source's omitted active sets make its proof incomplete, but do not invalidate a feasible interior symmetric candidate under the source SOC.

---

## 6. Corrected comparative statics

For the interior branch,

\[
\frac{\partial\bar i_C}{\partial N}
=
-
\frac{HDb(N^2-1)}
{\left[b(N+1)^2-H^2N\right]^2}
<0
\qquad(N>1).
\]

Hence

\[
\boxed{\frac{\partial i_C^*}{\partial N}\le0,}
\]

with strict inequality on the interior branch and local flatness when the cap binds.

This reverses equation (14) and Proposition 3.

Other interior derivatives are

\[
\frac{\partial\bar i_C}{\partial a}>0,
\qquad
\frac{\partial\bar i_C}{\partial\gamma}<0,
\qquad
\frac{\partial\bar i_C}{\partial\phi}<0.
\]

For the **number** of outsourced inputs, the \(\phi\)-comparative static changes at the cap:

\[
i_C^*=\phi
\]

on the full-outsourcing branch, so there

\[
\frac{\partial i_C^*}{\partial\phi}=1.
\]

For the **fraction**

\[
f_C^*=\frac{i_C^*}{\phi},
\]

the global result is clean: it is weakly decreasing in \(\phi\), and strictly decreasing on the interior branch because

\[
\frac{\partial}{\partial\phi}
\left(\frac{\bar i_C}{\phi}\right)
=
-
\frac{HN(2a+\gamma\phi^2)}
{2\phi^2[b(N+1)^2-H^2N]}
<0.
\]

---

## 7. Complete source-duopoly global best response

Set

\[
\delta=\frac{D}{H}>0,
\qquad
\rho=\frac{b}{H^2}>\frac49.
\]

Let \(y\) be the rival's outsourcing and \(x\) own outsourcing.

Define the rival-exit threshold

\[
U(y)=\delta+2y.
\]

On the both-active branch, the stationary point is

\[
A(y)=\frac{2(\delta-y)}{9\rho-4}.
\]

On the monopoly branch, the stationary point is

\[
M=\frac{\delta}{4\rho-1}.
\]

For \(y\ge\delta\),

\[
R(y)=0.
\]

For \(0\le y<\delta\):

### Case I: \(\rho\ge2/3\)

\[
R(y)=A(y).
\]

### Case II: \(1/2\le\rho<2/3\)

Let

\[
y_A
=
\frac{\delta(2-3\rho)}
{2(3\rho-1)}.
\]

Then

\[
R(y)=
\begin{cases}
U(y), & 0\le y\le y_A,\\
A(y), & y_A\le y<\delta.
\end{cases}
\]

### Case III: \(4/9<\rho<1/2\)

Let

\[
y_M
=
\frac{\delta(1-2\rho)}
{4\rho-1}.
\]

Then

\[
R(y)=
\begin{cases}
M, & 0\le y\le y_M,\\
U(y), & y_M\le y\le y_A,\\
A(y), & y_A\le y<\delta.
\end{cases}
\]

The source-domain best response is

\[
\boxed{
B_\phi(y)=\min\{\phi,R(y)\}.
}
\]

The joins satisfy

\[
M=U(y_M),
\qquad
U(y_A)=A(y_A).
\]

---

## 8. Proposition 5 is false globally

On the source's regular branch,

\[
A'(y)
=
-\frac{2}{9\rho-4}<0,
\]

which is equation (15)'s strategic-substitute effect.

But for

\[
\frac49<\rho<\frac23,
\]

the global best response contains

\[
R(y)=U(y)=\delta+2y
\]

and therefore

\[
\boxed{R'(y)=2>0.}
\]

The mechanism is downstream exit: the firm chooses just enough outsourcing to make the rival inactive. If the rival outsources more, that exit threshold rises, so own optimal outsourcing rises.

### Exact source-admissible witness

Take

\[
\rho=\frac35,\qquad
\delta=1,\qquad
\phi=2.
\]

Then

\[
R(0)=1,
\qquad
R\left(\frac1{20}\right)=\frac{11}{10}.
\]

Thus the global best response is strictly increasing on an admissible interval.

### Replacement for Proposition 5

Outsourcing is a strategic substitute on the both-active regular branch. It is **not** globally a strategic substitute throughout the source parameter domain.

---

## 9. Complete pure Stage-I equilibrium correspondence in the source duopoly

Define

\[
s=\frac{2\delta}{9\rho-2}.
\]

### Case A: \(\rho>2/3\)

The unique pure Stage-I equilibrium is

\[
\boxed{
(\min\{\phi,s\},\min\{\phi,s\}).
}
\]

### Case B: \(\rho=2/3\)

Then

\[
R(y)=\max\{0,\delta-y\}.
\]

If

\[
\phi<\frac{\delta}{2},
\]

the unique equilibrium is

\[
(\phi,\phi).
\]

If

\[
\phi\ge\frac{\delta}{2},
\]

there is a continuum:

\[
\boxed{
\mathcal E
=
\left\{
(x,\delta-x):
x\in
[\max\{0,\delta-\phi\},\,\min\{\phi,\delta\}]
\right\}.
}
\]

### Case C: \(4/9<\rho<2/3\)

If

\[
\phi\le s,
\]

the unique equilibrium is

\[
(\phi,\phi).
\]

If

\[
\phi>s,
\]

there are exactly three pure equilibria.

One is symmetric:

\[
(s,s).
\]

Define

\[
h=R(0),
\qquad
x_H=\min\{\phi,h\},
\qquad
x_L=R(x_H).
\]

Then the two asymmetric equilibria are

\[
\boxed{
(x_H,x_L),
\qquad
(x_L,x_H).
}
\]

For the witness \(\rho=3/5,\delta=1,\phi=2\), the three equilibria are

\[
\left(\frac{10}{17},\frac{10}{17}\right),
\qquad
(1,0),
\qquad
(0,1).
\]

This is a complete pure-strategy Stage-I equilibrium classification for the **source duopoly**.

---

## 10. Hotelling continuation audit

The source indifferent consumer is

\[
\hat x
=
\frac12+\frac{p_B-p_A}{2\tau}.
\]

The actual share of A is

\[
s_A
=
\min\left\{
1,\,
\max\left\{
0,\,
\hat x
\right\}
\right\}.
\]

Let

\[
d_c=c_B-c_A.
\]

### If \(|d_c|<3\tau\)

The price equilibrium is unique and interior:

\[
p_A^*
=
\frac{2c_A+c_B+3\tau}{3},
\qquad
p_B^*
=
\frac{c_A+2c_B+3\tau}{3}.
\]

### If \(d_c=3\tau\)

The unique boundary equilibrium is

\[
p_A^*=c_A+2\tau,
\qquad
p_B^*=c_B=c_A+3\tau.
\]

The case \(d_c=-3\tau\) is symmetric.

### If \(d_c>3\tau\)

A is the low-cost firm and serves the full market. There is a continuum of pure price equilibria:

\[
\boxed{
p_B\in[c_A+3\tau,c_B],
\qquad
p_A=p_B-\tau.
}
\]

The high-cost firm earns zero operating profit throughout. The low-cost firm's operating profit ranges from

\[
2n\tau
\]

to

\[
n(d_c-\tau).
\]

The case \(d_c<-3\tau\) is symmetric.

Therefore every price subgame is solved, but the Stage-I continuation payoff is set-valued outside the interior region because the source specifies no equilibrium-selection rule.

---

## 11. Supersession of the Stage-1 Hotelling claim

For the Stage-1 regression values

\[
H=n=1,\qquad
\tau=\frac1{15},\qquad
i_0=\frac16,\qquad
i'=\frac12,
\]

the symmetric source payoff is

\[
\Pi_{\rm sym}=\frac1{180}.
\]

For the same sourcing deviation \(i'=1/2\):

- lower-end valid corner continuation:
  \[
  \Pi_{\rm dev}^{L}=-\frac7{60}<\Pi_{\rm sym};
  \]
- upper-end valid corner continuation:
  \[
  \Pi_{\rm dev}^{H}=\frac1{60}>\Pi_{\rm sym}.
  \]

Hence the previous statement that this deviation **unconditionally** overturns Proposition 6 is rejected.

At the source symmetric interior action

\[
i_0=\frac{Hn}{6},
\]

the lowest-profit valid corner continuation is consistent with the source SOC and can deter large deviations. The highest-profit valid corner continuation yields maximal deviation gain

\[
\Delta\Pi_{\max}
=
\frac{n(2H^2n-27\tau)}{18}.
\]

Thus when

\[
H^2n>\frac{27}{2}\tau
\]

and the required deviation is feasible, the source equilibrium prediction becomes continuation-selection dependent.

### Correct diagnosis

The source Hotelling analysis omits:

1. the primitive cap \(i_j\le\phi\);
2. the corner price-equilibrium correspondence;
3. the off-path continuation-selection issue.

The literal-game multiplicity remains part of the audit. Separately, the re-audit proves from the source payoff that every \(p_j<c_j\) is weakly dominated by \(p_j=c_j\). Deleting only those dominated prices yields a unique corner continuation. This is reported explicitly as an **undominated-price refinement**, not as a hidden source primitive and not as a trembling-hand/proper-equilibrium theorem.

The exact refined Stage-I survival/failure region is derived in audit/STAGE_04_HOTELLING_REAUDIT.md. This strengthens rather than removes the Hotelling correction, so Candidate E′ is restored.

---

## 12. Continuation-completeness ledger

| History class | Outcome |
|---|---|
| Cournot, arbitrary feasible sourcing profile | \`SOLVED_EQUILIBRIUM\` — unique |
| Cournot, active-set thresholds | \`SOLVED_EQUILIBRIUM\` |
| Hotelling, \(|d_c|<3\tau\) | \`SOLVED_EQUILIBRIUM\` — unique |
| Hotelling, \(|d_c|=3\tau\) | \`SOLVED_EQUILIBRIUM\` — unique boundary |
| Hotelling, \(|d_c|>3\tau\) | \`MULTIPLE_EQUILIBRIA\` — exact continuum |
| Material \`UNRESOLVED\` | **0** |
| Material \`NUMERICAL_FAILURE\` | **0** |

Continuation-completeness verdict: **PASS**.

---

## 13. Independent verification and permanent regressions

\`code/stage04_verify.py\` reconstructs the Cournot continuation from primitive KKT/active-set conditions and checks the Hotelling corner equilibria directly from clipped demand.

Permanent exact regressions include:

1. the Stage-1 Cournot history where the source all-active formula produces negative output;
2. the source parameter point where equation (13) exceeds \(\phi\);
3. the duopoly positive-slope BR example \((\rho,\delta,\phi)=(3/5,1,2)\);
4. the three-equilibrium duopoly example
   \[
   (10/17,10/17),\ (1,0),\ (0,1);
   \]
5. the Hotelling deviation whose profitability flips across two valid corner continuations.

The Stage-4 verification assertions were also rechecked independently after replacing structural SymPy \`==\` comparisons by algebraic \`simplify(lhs-rhs)==0\` comparisons.

---

## 14. Candidate-proposition kill table

| Candidate proposition | Stage-4 result |
|---|---|
| CP1: equation-(14) sign correction | **PROVED** |
| CP2: corrected symmetric Cournot action | **PROVED** |
| CP3: exhaustive general-\(N\) asymmetric correspondence | **NOT RETAINED**; overbroad relative to correction need |
| CP4: complete Hotelling price continuation | **PROVED** |
| CP5: Hotelling symmetric candidate is globally defeated | **LITERAL GAME: selection-dependent; UNDOMINATED REFINEMENT: PROVED false on exact nonempty region** |
| CP6: one unified correction architecture | **RESTORED AS E′** — literal multiplicity + undominated-price refinement are stated separately |
| CP7: Proposition 5 needs global correction | **PROVED in stronger form** |

---

## 15. Canonical-form screen

### Cournot Stage II

- linear demand;
- nonnegative quantity orthant;
- heterogeneous constant marginal costs;
- unique active-set / linear-complementarity solution.

### Reduced Stage I

- box-constrained strategy set \([0,\phi]^N\);
- piecewise-quadratic payoffs;
- globally strictly concave own objective under the source SOC;
- regime switching inherited from downstream participation.

### Source duopoly

- piecewise-affine best response;
- slope values \(0\), \(+2\), and \(-2/(9\rho-4)\);
- multiplicity generated by the downstream-exit kink.

Parent classes passed to Stage 6:

- linear complementarity Cournot games;
- concave games;
- piecewise-affine best-response games;
- endogenous-participation cost-investment games.

No theorem-absorption claim is made at Stage 4.

---

## 16. Welfare / planner fields

**NOT APPLICABLE to the retained Stage-4 correction claims.**

The surviving contribution concerns equilibrium validity, feasibility, comparative statics, and strategic interaction. No new planner problem is introduced.

---

## 17. Preliminary theorem certificates

The retained Stage-4 claims are:

- **C1:** complete unique Cournot continuation — PROVED.
- **C2:** global own-payoff concavity under the source SOC — PROVED.
- **C3:** corrected unique symmetric Cournot action — PROVED.
- **C4:** weakly negative competition comparative static — PROVED.
- **C5:** corrected \(\phi\)-comparative statics — PROVED.
- **C6:** exact source-duopoly global BR — PROVED.
- **C7:** positive-slope BR region for \(4/9<\rho<2/3\) — PROVED.
- **C8:** complete pure Stage-I duopoly equilibrium correspondence — PROVED.
- **H1:** complete literal Hotelling price-equilibrium correspondence — PROVED.
- **H2:** below-cost prices are weakly dominated by marginal-cost pricing — PROVED.
- **H3:** undominated-price Hotelling continuation is unique for every cost gap — PROVED.
- **H4:** refined Stage-I BR has the finite-candidate characterization in the Hotelling re-audit — PROVED.
- **H5:** exact cap-aware symmetric survival/failure region — PROVED.
- **H6:** Stage-1 rational corner deviation is restored as a refined-game counterexample — PROVED.

All are construction-level certificates only. Stage 4A must independently attack them.

---

## 18. Canonical verdict and route

Canonical architecture after the Hotelling re-audit:

\[
\boxed{\textbf{Candidate E′ — RESTORED}}
\]

Stage verdict:

\[
\boxed{\textbf{GO}}
\]

Route:

\[
\boxed{\textbf{Stage 4A — Independent Mathematical Adversarial Certification Gate}}
\]

Stage 4A receives all frozen Cournot claims plus the Hotelling literal/refined theorem package in audit/STAGE_04_HOTELLING_REAUDIT.md. It must attack both layers independently and may not silently promote the refinement into a source primitive or into a trembling-hand/proper-equilibrium claim.
