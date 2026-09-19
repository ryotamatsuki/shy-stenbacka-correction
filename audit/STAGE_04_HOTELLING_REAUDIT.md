# Stage 4 Hotelling Re-audit — Undominated Pricing

Status: **PASS — AMEND STAGE 4 / RESTORE E′**

Audit date: 2026-09-19  
Reopened checkpoint: \`c55fec7004050857c652cd9f93533a23418da961\`

## 1. Executive re-audit verdict

The Stage-4 decision to drop Hotelling from the canonical paper architecture is amended.

The exact source game has two logically distinct layers:

1. **Literal source game:** the published Hotelling appendix does not state a price floor \(p_j\ge c_j\). With clipped demand, sufficiently asymmetric costs generate a continuum of corner price equilibria, so the Stage-I continuation payoff is selection-dependent.
2. **Undominated-price refinement:** every price \(p_j<c_j\) is weakly dominated by \(p_j=c_j\) under the source payoff function. Eliminating only those weakly dominated prices collapses the corner continuum to a unique continuation. Under this refinement, the source symmetric outsourcing candidate fails on a nonempty parameter region that satisfies the source SOC.

Therefore the earlier multiplicity diagnosis remains mathematically correct, but it is not an adequate reason to drop Hotelling. The economically stronger correction is the two-layer statement above.

Canonical architecture decision:

\[
\boxed{\textbf{OUTCOME 2 — RESTORE E′}}
\]

Candidate E′ consists of:

- the complete Cournot correction already certified at Stage 4;
- the literal Hotelling continuation-multiplicity result;
- the undominated-price Hotelling refinement;
- the exact refined survival/failure region for Proposition 6.

Stage-4 route remains:

\[
\boxed{\textbf{GO → STAGE 4A}}
\]

but Stage 4A must now independently certify both Cournot and the Hotelling two-layer correction.

---

## 2. Exact source price strategy domain

The final published article is Shy and Stenbacka (2005), *Canadian Journal of Economics*, 38(4), 1173–1190, DOI 10.1111/j.0008-4085.2005.00320.x.

In Section 4 the source defines prices \(p_A,p_B\), derives the indifferent consumer, and writes profits as

\[
\pi_A=(p_A-c_A)n\hat x-I_A^s,
\qquad
\pi_B=(p_B-c_B)n(1-\hat x)-I_B^s.
\]

Appendix C explicitly derives the price FOCs **“as long as both firms produce.”** It writes maximization over \(p_A\) and \(p_B\), but the published derivation does not state:

- \(p_j\ge0\);
- \(p_j\ge c_j\);
- a no-loss-pricing assumption;
- elimination of weakly dominated prices;
- a refinement for corner price subgames.

Thus the literal source does not supply the missing corner strategy-domain/refinement convention.

This source omission must be distinguished from the economic status of below-cost prices.

---

## 3. Formal dominance status of below-cost prices

Let firm \(j\)'s realized market share be

\[
s_j(p_j,p_k)\in[0,1].
\]

Ignoring the Stage-I monitoring cost, which is sunk in Stage II, operating profit is

\[
\pi_j^P(p_j,p_k)
=
n(p_j-c_j)s_j(p_j,p_k).
\]

Fix any price

\[
p_j<c_j.
\]

For every rival price \(p_k\),

\[
\pi_j^P(p_j,p_k)\le0.
\]

At the alternative price \(p_j'=c_j\),

\[
\pi_j^P(c_j,p_k)=0
\]

for every \(p_k\).

Therefore

\[
\pi_j^P(c_j,p_k)
\ge
\pi_j^P(p_j,p_k)
\quad
\forall p_k.
\]

The inequality is strict whenever the below-cost price attracts positive demand. Such rival prices exist; for example, at \(p_k=p_j\) the firm obtains a positive Hotelling share.

### Theorem H-DOM

For every \(p_j<c_j\), the pure price \(p_j=c_j\) weakly dominates \(p_j\).

This result follows directly from the source payoff and requires no new technology, preference, or cost assumption.

**Status: PROVED.**

---

## 4. What refinement is being used

Four concepts must not be conflated.

### 4.1 Primitive restriction

Writing

\[
p_j\ge c_j
\]

as part of the primitive strategy space would modify the literal statement of the source game.

### 4.2 One-round elimination of weakly dominated prices

Deleting

\[
p_j<c_j
\]

because of Theorem H-DOM is a refinement of the source Nash game based entirely on its own payoffs.

This is the refinement used below.

### 4.3 Trembling-hand perfection / proper equilibrium

No claim is made here that the continuous-price game has been fully characterized under trembling-hand perfection or proper equilibrium. That would require a separate perturbation/refinement construction.

### 4.4 Economic no-loss pricing

A no-loss-pricing convention has the same surviving price set \(p_j\ge c_j\) in this model, but the proof below does not rely on an informal convention: weak dominance is established directly.

### Literature positioning

Hotelling-style price-competition work sometimes explicitly imposes prices weakly above marginal cost and notes that this is justified because marginal-cost pricing gives weakly higher profit than below-cost pricing. Gill and Thanassoulis (2016, *Economic Journal*) provide a directly relevant example in a Hotelling-line price model.

Accordingly, the refined result should be described as **undominated-price equilibrium**, not as a hidden primitive assumption of Shy–Stenbacka.

---

## 5. Literal Hotelling price-equilibrium correspondence

Let

\[
d=c_B-c_A.
\]

With the consumer share clipped to \([0,1]\):

### 5.1 Interior region: \(|d|<3\tau\)

The unique price equilibrium is

\[
p_A^*
=
\frac{2c_A+c_B+3\tau}{3},
\qquad
p_B^*
=
\frac{c_A+2c_B+3\tau}{3}.
\]

Both firms have positive demand.

### 5.2 Boundary: \(d=3\tau\)

\[
p_A^*=c_A+2\tau,
\qquad
p_B^*=c_B=c_A+3\tau.
\]

Firm B has zero demand. The case \(d=-3\tau\) is symmetric.

### 5.3 Corner: \(d>3\tau\)

Firm A is low-cost and serves the whole market. The literal price game has the continuum

\[
\boxed{
p_B\in[c_A+3\tau,c_B],
\qquad
p_A=p_B-\tau.
}
\]

All points except the upper endpoint have

\[
p_B<c_B.
\]

Thus every equilibrium in the continuum except

\[
(p_A,p_B)=(c_B-\tau,c_B)
\]

uses a weakly dominated price by the zero-demand high-cost firm.

The \(d<-3\tau\) case is symmetric.

### Literal-game conclusion

The Stage-I reduced payoff is set-valued after sufficiently asymmetric sourcing histories.

This establishes a proof-completeness/selection defect in the published backward induction.

---

## 6. Undominated-price price-equilibrium correspondence

Delete all prices \(p_j<c_j\).

For a firm with cost \(c\) facing rival price \(r\), the restricted price best-response correspondence is

\[
BR^P(r;c)=
\begin{cases}
[c,\infty),
& r\le c-\tau,\\[4pt]
\left\{
\dfrac{r+\tau+c}{2}
\right\},
& c-\tau<r<c+3\tau,\\[10pt]
\{r-\tau\},
& r\ge c+3\tau.
\end{cases}
\]

At \(r=c-\tau\), every feasible \(p\ge c\) yields zero demand and zero operating profit. At \(r=c+3\tau\), the interior optimum and full-market boundary coincide.

Solving the two restricted BRs gives:

### 6.1 \(|d|<3\tau\)

The same unique interior equilibrium as the source formula.

### 6.2 \(d=3\tau\)

The same unique boundary equilibrium.

### 6.3 \(d>3\tau\)

The unique undominated-price equilibrium is

\[
\boxed{
p_B=c_B,
\qquad
p_A=c_B-\tau.
}
\]

Firm A serves the entire market.

No other point of the literal continuum survives because every \(p_B<c_B\) is weakly dominated.

The \(d<-3\tau\) case is symmetric.

### Classification

This is:

- a Nash equilibrium of the literal source game;
- the **unique Nash equilibrium after deletion of below-cost weakly dominated prices**;
- not labeled trembling-hand perfect here.

---

## 7. Refined Stage-I payoff

Let firm A choose \(x=i_A\) against rival outsourcing \(y=i_B\).

Because

\[
c_B-c_A=H(x-y),
\]

define

\[
t\equiv\frac{3\tau}{H}.
\]

Under undominated-price continuation, A's complete reduced payoff is

\[
V_y(x)=
\begin{cases}
-x^2,
& x\le y-t,\\[5pt]
\dfrac{n[3\tau+H(x-y)]^2}{18\tau}-x^2,
& |x-y|\le t,\\[10pt]
n[H(x-y)-\tau]-x^2,
& x\ge y+t.
\end{cases}
\tag{H-R1}
\]

The pieces agree in value at both regime boundaries.

The source SOC

\[
H^2n<18\tau
\tag{H-SOC}
\]

makes the interior piece strictly concave. The two corner pieces are also strictly concave, but the derivative jumps upward at the low-cost/full-market threshold \(x=y+t\). Therefore local concavity does not imply global concavity.

---

## 8. Complete constrained Stage-I best response

Define the source strategy set

\[
x\in[0,\phi].
\]

### Interior-share candidate

Let

\[
I_y
=
[\max\{0,y-t\},\ \min\{\phi,y+t\}],
\]

and

\[
u(y)
=
\frac{Hn(3\tau-Hy)}
{18\tau-H^2n}.
\]

Let

\[
x_I(y)
=
\operatorname{proj}_{I_y}u(y).
\]

### Low-cost corner candidate

If \(y+t\le\phi\), define

\[
C_y=[y+t,\phi],
\qquad
m=\frac{Hn}{2},
\]

and

\[
x_C(y)
=
\operatorname{proj}_{C_y}m.
\]

### Zero-demand candidate

The high-cost corner payoff is \(-x^2\), whose branch maximum is \(x=0\) whenever that branch is nonempty. Including \(x=0\) in the global candidate set is harmless in all cases.

Define

\[
K_y
=
\{0,x_I(y)\}
\cup
\{x_C(y):y+t\le\phi\}.
\]

Then the exact constrained best-response correspondence is

\[
\boxed{
BR_A(y)
=
\arg\max_{x\in K_y}V_y(x).
}
\tag{H-R2}
\]

Ties are retained as a correspondence.

This is a complete finite-candidate characterization: every branch is strictly concave under (H-SOC), so no other global maximizer can exist.

---

## 9. Symmetric candidate and the cap

Define

\[
i_0=\frac{Hn}{6}.
\]

Any symmetric pure Stage-I equilibrium must have action

\[
\hat i
=
\min\{\phi,i_0\}.
\]

Reason:

- at symmetric costs the price continuation is unique and interior;
- an interior symmetric Stage-I optimum must satisfy the source FOC and hence equals \(i_0\);
- if \(i_0\ge\phi\), the upper-bound KKT condition selects \(\phi\).

---

## 10. Cap-binding region

If

\[
\phi\le i_0,
\]

then

\[
(\phi,\phi)
\]

is a global refined SPNE.

There is no feasible upward deviation. On the interior branch, the derivative at the cap is

\[
\left.
\frac{\partial V_\phi(x)}{\partial x}
\right|_{x=\phi}
=
\frac{Hn}{3}-2\phi
=
2(i_0-\phi)
\ge0,
\]

so no downward interior deviation is profitable. A sufficiently large downward deviation gives zero operating profit and cannot beat the positive symmetric payoff under (H-SOC).

Thus the corrected cap solution is robust.

---

## 11. Interior symmetric candidate: exact global deviation test

Now assume

\[
\phi>i_0.
\]

At

\[
(i_A,i_B)=(i_0,i_0),
\]

the symmetric payoff is

\[
\Pi_0
=
\frac{n\tau}{2}-i_0^2
=
\frac{n(18\tau-H^2n)}{36}>0.
\]

All deviations that remain on the interior-share branch are unprofitable because that branch is strictly concave and stationary at \(i_0\).

High-cost corner deviations yield operating profit zero and are also unprofitable.

Only an upward low-cost corner deviation can defeat the candidate.

For \(x\ge i_0+3\tau/H\),

\[
\Pi_C(x)
=
n[H(x-i_0)-\tau]-x^2.
\]

The gain is

\[
\Delta(x)
=
\Pi_C(x)-\Pi_0
=
-\frac{
36x^2-36Hnx+5H^2n^2+54n\tau
}{36}.
\tag{H-R3}
\]

The unconstrained corner optimum is

\[
x_M=\frac{Hn}{2}.
\]

At that point,

\[
\boxed{
\Delta_{\max}
=
\frac{n(2H^2n-27\tau)}{18}.
}
\tag{H-R4}
\]

Thus a profitable corner deviation is possible only if

\[
H^2n>\frac{27}{2}\tau.
\]

---

## 12. Exact feasibility condition including \(\phi\)

When

\[
H^2n>\frac{27}{2}\tau,
\]

the two zeros of \(\Delta(x)\) are

\[
x_\pm
=
\frac{Hn}{2}
\pm
\frac{\sqrt{2n(2H^2n-27\tau)}}{6}.
\]

Under

\[
\frac{27}{2}\tau<H^2n<18\tau,
\]

the lower root satisfies

\[
x_-
>
i_0+\frac{3\tau}{H}.
\]

Therefore the entire interval just above \(x_-\) is already in the low-cost corner regime.

A profitable feasible deviation exists **if and only if**

\[
\boxed{
\frac{27}{2}\tau<H^2n<18\tau
\quad\text{and}\quad
\phi>x_-.
}
\tag{H-R5}
\]

The condition

\[
\frac{Hn}{2}\le\phi
\]

is sufficient but **not necessary**. Even when the unconstrained corner optimum is above the outsourcing cap, a boundary deviation \(x=\phi\) is profitable whenever

\[
x_-<\phi<\frac{Hn}{2}.
\]

At \(\phi=x_-\), the deviation ties but does not strictly improve payoff.

---

## 13. Exact refined survival region

Under the source SOC:

### Case A: cap binds

If

\[
\phi\le\frac{Hn}{6},
\]

the symmetric refined SPNE is

\[
(\phi,\phi).
\]

### Case B: interior source candidate

If

\[
\phi>\frac{Hn}{6},
\]

then

\[
\left(\frac{Hn}{6},\frac{Hn}{6}\right)
\]

is a refined SPNE **if and only if**

\[
H^2n\le\frac{27}{2}\tau
\]

or, when \(H^2n>27\tau/2\),

\[
\phi\le
\frac{Hn}{2}
-
\frac{\sqrt{2n(2H^2n-27\tau)}}{6}.
\]

Equivalently, it fails exactly under (H-R5).

---

## 14. Permanent Stage-1 regression

Take

\[
H=n=1,\qquad
\tau=\frac1{15},\qquad
\phi=1.
\]

Then

\[
i_0=\frac16,
\qquad
x_M=\frac12,
\]

and

\[
x_-=
\frac12-\frac{\sqrt{10}}{30}
<1.
\]

The source SOC holds:

\[
1<18/15.
\]

Under the unique undominated-price corner continuation, the deviation

\[
i_A'=\frac12
\]

against

\[
i_B=\frac16
\]

gives

\[
\Delta\Pi
=
\frac1{90}>0.
\]

Thus the Stage-1 numerical deviation is restored as a valid counterexample **under the undominated-price refinement**.

It is not an unconditional counterexample to every literal-game SPNE selection.

---

## 15. Corrected classification of Proposition 6

The previous two extreme labels are both too crude.

### Literal source game

Proposition 6 is **not globally established** because the source:

- extrapolates the interior-share formula beyond its domain;
- omits the outsourcing cap;
- does not characterize multiple corner price equilibria or specify off-path selection.

A symmetric sourcing candidate can be supported in parts of the literal game by price equilibria that use weakly dominated below-cost prices off path.

### Undominated-price refinement

After deleting below-cost weakly dominated prices:

- the Stage-II price continuation is unique for every cost gap;
- the Stage-I reduced payoff is single-valued;
- the cap-corrected symmetric sourcing action is globally valid outside (H-R5);
- inside (H-R5), the source symmetric candidate is **not** an SPNE.

Hence Proposition 6 is **refinement-fragile and false on a nonempty admissible region under undominated pricing**.

The source statement that outsourcing decisions are strategic substitutes is also only an interior-branch result; the complete refined Stage-I BR is the piecewise correspondence (H-R2).

---

## 16. Literal vs refined comparison

| Object | Literal source game | Undominated-price refinement |
|---|---|---|
| Below-cost price allowed | yes, absent explicit restriction | no |
| \(|d|<3\tau\) | unique interior price equilibrium | same |
| \(|d|=3\tau\) | unique boundary equilibrium | same |
| \(|d|>3\tau\) | continuum of corner equilibria | unique corner equilibrium |
| Stage-I continuation payoff | set-valued off path | single-valued |
| Source \(i_0=Hn/6\) | can be supportable via selection | exact survival condition |
| Proposition 6 | proof incomplete / selection-dependent | false on (H-R5) |
| Extra primitive assumption | none | none; one-round weak-dominance deletion |

---

## 17. Referee attacks

### Attack A — “Below-cost multiplicity is economically irrelevant.”

**Assessment:** substantially correct as an objection to using multiplicity as the headline result.

**Answer:** the literal multiplicity is retained only to diagnose the source proof. The economically relevant correction uses Theorem H-DOM and the undominated-price continuation.

### Attack B — “You added \(p\ge c\) after the fact.”

**Answer:** the paper must not claim that \(p\ge c\) was an explicit source primitive. Instead it proves from the source payoff that every \(p<c\) is weakly dominated and reports a separate undominated-price theorem. No preference, technology, or payoff primitive is changed.

### Attack C — “Weak-dominance elimination is not innocuous.”

**Answer:** correct. One-round elimination can remove Nash equilibria, and the paper should say so. It is a refinement, not an identity of equilibrium sets. No iterated deletion or stronger refinement is silently invoked.

### Attack D — “\(p_{\rm high}=c_{\rm high}\) is only one selection.”

**Answer:** in the literal game, correct. After deletion of weakly dominated below-cost prices, it is the unique corner equilibrium, so the objection no longer applies to the refined theorem.

### Attack E — “The profitable sourcing deviation may violate \(i\le\phi\).”

**Answer:** addressed exactly. Failure requires \(\phi>x_-\), not \(Hn/2\le\phi\). Thus the cap can block the deviation, but the exact failure region remains nonempty.

---

## 18. Route C vs Route E′

No numerical score is used.

### Route C — Cournot only

Strengths:

- shortest architecture;
- strongest algebraic correction;
- Proposition 3 sign reversal is indisputable;
- Proposition 5 global failure and asymmetric equilibria are substantial.

Weakness:

- the source abstract/conclusion also claims strategic substitutes under price competition;
- omitting Hotelling leaves a material source proposition and the second market structure only partially audited.

### Route E′ — Cournot + Hotelling two-layer correction

Strengths:

- covers both product-market structures in the source;
- Hotelling result is no longer based on economically implausible below-cost pricing;
- weak dominance is proved from source primitives;
- yields a clean exact failure/survival condition;
- conceptually unifies both corrections as failures of regular-branch extrapolation after sourcing changes the downstream regime.

Costs:

- requires careful separation of literal Nash from refined equilibrium;
- the paper must avoid presenting weak-dominance deletion as a source assumption or as harmless for the Nash equilibrium set;
- adds theorem and exposition length.

### Architecture decision

The strengthened Hotelling result is sufficiently substantive and economically defensible to restore the unified architecture.

\[
\boxed{\textbf{RESTORE E′}}
\]

Recommended manuscript prominence:

- Cournot sign reversal and global duopoly correction remain the first/main block.
- Hotelling is a second main theorem block, not a footnote or appendix-only curiosity.
- The literal multiplicity result should be concise.
- The undominated-price failure region should receive the substantive discussion.

---

## 19. Canonical amendment

Stage 4 remains a construction-level **GO**, but its architecture changes.

Old routing:

\[
\text{Candidate C only}
\]

New routing:

\[
\boxed{
\text{Candidate E′ =
Complete Cournot correction
+
Hotelling literal/refined correction}
}
\]

Stage 4A must independently attack:

1. all frozen Cournot claims from the previous Stage 4;
2. H-DOM weak dominance;
3. the literal Hotelling price correspondence;
4. the unique undominated-price correspondence;
5. the complete refined Stage-I BR candidate characterization;
6. the exact symmetric survival/failure condition (H-R5);
7. the Stage-1 rational regression.

No trembling-hand/proper-equilibrium claim is authorized without separate proof.
