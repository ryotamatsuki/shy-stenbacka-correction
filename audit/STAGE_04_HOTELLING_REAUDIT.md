# Stage 4 Hotelling Re-audit — Literal Game and No-Loss Robustness

Status: **PASS — AMENDED AFTER STAGE-4A REFINEMENT ATTACK**

Audit date: 2026-09-19  
Originally reopened checkpoint: \`c55fec7004050857c652cd9f93533a23418da961\`

## 1. Executive verdict

The Hotelling correction has two layers, but they must not be conflated.

### Layer L — literal source game

The published article does not state \(p_j\ge c_j\). With globally clipped Hotelling demand, sufficiently asymmetric costs generate a continuum of pure corner price equilibria. The source's Stage-I backward induction is therefore incomplete off path unless a continuation selection is supplied.

### Layer NL — explicit no-loss price restriction

Every below-cost price \(p_j<c_j\) is weakly dominated by \(p_j=c_j\). This makes \(p_j\ge c_j\) an economically recognizable auxiliary restriction.

However, Stage 4A identified an important refinement point:

\[
p_j=c_j
\]

is itself weakly dominated by any fixed

\[
p_j=c_j+\varepsilon,\qquad \varepsilon>0,
\]

because \(p_j=c_j\) yields zero operating profit for every rival price, whereas \(c_j+\varepsilon\) yields nonnegative profit everywhere and strictly positive profit for some rival prices.

Therefore the restricted game \(p_j\ge c_j\) must **not** be described as “the equilibrium after elimination of all weakly dominated strategies,” “an undominated-strategy equilibrium,” trembling-hand perfection, or proper equilibrium.

It is an explicit **no-loss price strategy restriction** used as a robustness model.

Under this restriction the corner continuation is unique in pure strategies, and Proposition 6 fails on an exact nonempty parameter region satisfying the source SOC.

### Canonical architecture

\[
\boxed{\textbf{OUTCOME 3 — HYBRID}}
\]

- Cournot remains the canonical source-faithful main theorem architecture.
- Hotelling literal-game incompleteness is retained as a secondary source correction.
- The \(p_j\ge c_j\) result is retained as a secondary robustness theorem, explicitly conditional on the no-loss strategy restriction.

Stage-4 route remains

\[
\boxed{\textbf{GO → STAGE 4A}}
\]

after this amendment.

---

## 2. Exact source price strategy domain

The final published Hotelling section defines prices \(p_A,p_B\), the indifferent consumer, and interior price maximization. Appendix C qualifies the derivation by “as long as both firms produce.”

The published derivation does not state:

- \(p_j\ge0\);
- \(p_j\ge c_j\);
- a no-loss pricing restriction;
- elimination of weakly dominated strategies;
- a corner-equilibrium selection rule.

Hence \(p_j\ge c_j\) is not attributed to the source.

---

## 3. Dominance facts

Let realized demand satisfy

\[
D_j(p_j,p_k)\ge0.
\]

Operating profit is

\[
\pi_j^P(p_j,p_k)
=
(p_j-c_j)D_j(p_j,p_k).
\]

### H-DOM1 — below-cost prices

For every \(p_j<c_j\),

\[
\pi_j^P(p_j,p_k)\le0
\]

for every \(p_k\), while

\[
\pi_j^P(c_j,p_k)=0.
\]

Thus

\[
p_j=c_j
\]

weakly dominates every \(p_j<c_j\), strictly whenever the below-cost price attracts positive demand.

### H-DOM2 — marginal-cost pricing is not itself undominated

Fix any \(\varepsilon>0\). Since demand is nonnegative,

\[
\pi_j^P(c_j+\varepsilon,p_k)
=
\varepsilon D_j(c_j+\varepsilon,p_k)
\ge0
=
\pi_j^P(c_j,p_k)
\]

for every \(p_k\).

For rival prices at which \(D_j(c_j+\varepsilon,p_k)>0\), the inequality is strict.

Therefore

\[
\boxed{
c_j+\varepsilon
\text{ weakly dominates }
c_j.
}
\]

### Consequence

The no-loss restricted game \(p_j\ge c_j\) is **not** the game obtained by deleting all weakly dominated price strategies.

The weak-dominance argument justifies the economic relevance of excluding loss-making prices, but it does not by itself furnish a standard symmetric equilibrium refinement selecting the \(p_j=c_j\) corner point.

---

## 4. Literal price-equilibrium correspondence

Let

\[
d=c_B-c_A.
\]

Using clipped market shares:

### \(|d|<3\tau\)

Unique pure interior equilibrium:

\[
p_A^*
=
\frac{2c_A+c_B+3\tau}{3},
\qquad
p_B^*
=
\frac{c_A+2c_B+3\tau}{3}.
\]

### \(d=3\tau\)

Unique pure boundary equilibrium:

\[
p_A^*=c_A+2\tau,
\qquad
p_B^*=c_B.
\]

Mirror for \(d=-3\tau\).

### \(d>3\tau\)

A is low-cost and serves the whole market. Pure Nash equilibria are

\[
\boxed{
p_B=s,\qquad p_A=s-\tau,
\qquad
s\in[c_A+3\tau,c_B].
}
\]

All points except \(s=c_B\) use \(p_B<c_B\).

Mirror for \(d<-3\tau\).

Thus the literal source Stage-I continuation payoff is set-valued after sufficiently asymmetric sourcing histories.

This conclusion does not depend on the no-loss restriction.

---

## 5. Auxiliary no-loss price game

Now explicitly restrict each Stage-II price strategy to

\[
p_j\in[c_j,\infty).
\]

This is a robustness model, not a recovered hidden source assumption.

For cost \(c\) facing rival price \(r\), the restricted pure best response is

\[
BR^{NL}(r;c)=
\begin{cases}
[c,\infty),
& r\le c-\tau,\\[4pt]
\left\{\dfrac{r+\tau+c}{2}\right\},
& c-\tau<r<c+3\tau,\\[10pt]
\{r-\tau\},
& r\ge c+3\tau.
\end{cases}
\]

### No-loss pure price equilibrium

- If \(|d|<3\tau\): the same unique interior equilibrium.
- If \(|d|=3\tau\): the same unique boundary equilibrium.
- If \(d>3\tau\):
  \[
  \boxed{
  p_B=c_B,\qquad p_A=c_B-\tau.
  }
  \]
- Mirror for \(d<-3\tau\).

These statements concern **pure Nash equilibrium** of the restricted price game. No mixed-equilibrium uniqueness claim is made.

---

## 6. No-loss restricted Stage-I payoff

Let A choose \(x=i_A\), B choose \(y=i_B\), and define

\[
k=\frac{3\tau}{H}.
\]

Since

\[
c_B-c_A=H(x-y),
\]

A's reduced payoff in the no-loss restricted pure-continuation game is

\[
V_y^{NL}(x)
=
\begin{cases}
-x^2,
&
x-y\le-k,
\\[5pt]
\dfrac{n[3\tau+H(x-y)]^2}{18\tau}-x^2,
&
|x-y|\le k,
\\[10pt]
n[H(x-y)-\tau]-x^2,
&
x-y\ge k.
\end{cases}
\tag{H-NL1}
\]

The branches are continuous at \(x-y=\pm k\).

Under the source SOC

\[
H^2n<18\tau,
\]

every branch is strictly concave.

---

## 7. Complete constrained pure best response in the no-loss game

Define

\[
I_y=
[\max\{0,y-k\},\min\{\phi,y+k\}],
\]

\[
u(y)=
\frac{Hn(3\tau-Hy)}
{18\tau-H^2n}.
\]

Let \(x_I(y)\) be the projection of \(u(y)\) onto \(I_y\).

If \(y+k\le\phi\), define

\[
C_y=[y+k,\phi],
\qquad
x_C(y)=
\operatorname{proj}_{C_y}\left(\frac{Hn}{2}\right).
\]

The zero-demand branch has branch maximum at \(x=0\).

Therefore

\[
\boxed{
BR_A^{NL}(y)
=
\arg\max_{x\in K_y}
V_y^{NL}(x),
}
\tag{H-NL2}
\]

where

\[
K_y
=
\{0,x_I(y)\}
\cup
\{x_C(y):y+k\le\phi\}.
\]

Ties are retained. This is a complete finite-candidate characterization for pure best responses.

---

## 8. Symmetric pure equilibrium under the no-loss restriction

Define

\[
i_0=\frac{Hn}{6}.
\]

The source SOC implies

\[
i_0<\frac{3\tau}{H}.
\]

### Cap-binding region

If

\[
\phi\le i_0,
\]

then

\[
\boxed{(\phi,\phi)}
\]

is the corrected symmetric pure Stage-I equilibrium in the no-loss restricted game.

### Interior candidate

If

\[
\phi>i_0,
\]

the only symmetric interior candidate is

\[
(i_0,i_0).
\]

All interior-share deviations are unprofitable by strict branch concavity. A low-cost corner deviation \(x\) yields gain

\[
\Delta(x)
=
-\frac{
36x^2-36Hnx+5H^2n^2+54n\tau
}{36}.
\]

Its unconstrained maximizer is

\[
x_M=\frac{Hn}{2}
\]

with

\[
\Delta(x_M)
=
\frac{n(2H^2n-27\tau)}{18}.
\]

When \(2H^2n>27\tau\), let

\[
x_-=
\frac{Hn}{2}
-
\frac{\sqrt{2n(2H^2n-27\tau)}}{6}.
\]

Under

\[
\frac{27}{2}\tau<H^2n<18\tau,
\]

one has

\[
x_->i_0+\frac{3\tau}{H},
\]

so \(x_-\) lies strictly inside the low-cost corner domain.

Hence the symmetric source candidate fails in the no-loss restricted game iff

\[
\boxed{
\frac{27}{2}\tau<H^2n<18\tau
\quad\text{and}\quad
\phi>x_-.
}
\tag{H-NL3}
\]

At \(\phi=x_-\), the nonlocal deviation ties.

---

## 9. Exact regression

For

\[
H=n=1,\qquad
\tau=\frac1{15},\qquad
\phi=1,
\]

the source candidate is

\[
i_0=\frac16.
\]

The no-loss restricted corner deviation

\[
i_A'=\frac12
\]

against \(i_B=1/6\) gives

\[
\Pi_{\rm dev}=\frac1{60},
\qquad
\Pi_{\rm sym}=\frac1{180},
\]

so

\[
\boxed{
\Pi_{\rm dev}-\Pi_{\rm sym}
=
\frac1{90}>0.
}
\]

This is a valid exact counterexample to Proposition 6 **conditional on the no-loss price restriction**.

It is not a selection-free counterexample to every SPNE of the literal source game.

---

## 10. Corrected Proposition-6 classification

### Literal source game

**NOT GLOBALLY ESTABLISHED / SELECTION-DEPENDENT.**

The source omits the outsourcing cap and does not solve the corner price correspondence. Its interior Stage-I payoff cannot be extrapolated globally.

### No-loss restricted robustness model

**FALSE ON EXACT NONEMPTY REGION (H-NL3).**

This is a conditional robustness theorem for a transparent auxiliary strategy restriction.

### Manuscript language

Permitted:

> In the literal price game, the published backward induction is incomplete because sufficiently asymmetric costs generate multiple corner continuations. If prices below marginal cost are ruled out explicitly, the continuation becomes unique in pure strategies and the published symmetric sourcing candidate fails on an exact nonempty parameter region.

Prohibited:

> Eliminating weakly dominated strategies uniquely selects the corner equilibrium.

Prohibited:

> Shy and Stenbacka assumed prices weakly above marginal cost.

---

## 11. Architecture decision

The Stage-4A refinement attack downgrades the previous “RESTORE E′ as co-equal main architecture” decision.

Canonical architecture:

\[
\boxed{\textbf{HYBRID}}
\]

- **Main theorem block:** complete Cournot correction.
- **Secondary source-faithful Hotelling proposition:** literal corner multiplicity and proof incompleteness.
- **Secondary robustness proposition:** exact Proposition-6 failure region under explicit \(p_j\ge c_j\).

Recommended placement:

- concise Hotelling source-game result in main text;
- no-loss robustness proposition may remain in main text if space permits;
- complete best-response algebra and cap threshold in appendix;
- do not make the no-loss model the paper's primary correction.

---

## 12. Stage-4 amended verdict

Cournot claims: unchanged.

Hotelling claims: amended as above.

\[
\boxed{\textbf{STAGE 4 — GO}}
\]

\[
\boxed{\textbf{ARCHITECTURE — HYBRID}}
\]

Route:

\[
\boxed{\textbf{REPEAT STAGE 4A}}
\]
