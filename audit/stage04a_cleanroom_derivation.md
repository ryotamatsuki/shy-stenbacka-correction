# Stage 4A Clean-Room Mathematical Reconstruction

Date: 2026-09-19  
Role: independent hostile mathematical referee  
Frozen construction input: amended Stage 4 HYBRID architecture

This derivation does not treat the Stage-4 formulas as proof. It reconstructs the high-stakes objects by independent routes and records the attacks needed for Stage-4A certification.

## 1. Cournot continuation — independent potential proof

For fixed marginal costs \(c_1,\ldots,c_N\), firm \(j\)'s quantity payoff is

\[
\pi_j(q)
=
\left(a-b\sum_k q_k-c_j\right)q_j.
\]

Its own first derivative is

\[
\frac{\partial\pi_j}{\partial q_j}
=
a-c_j-bQ-bq_j.
\]

Define

\[
\Phi(q)
=
\sum_j(a-c_j)q_j
-\frac b2 Q^2
-\frac b2\sum_jq_j^2.
\]

Then

\[
\frac{\partial\Phi}{\partial q_j}
=
\frac{\partial\pi_j}{\partial q_j}.
\]

The Hessian is

\[
\nabla^2\Phi
=
-b(I+\mathbf 1\mathbf 1^\top),
\]

which is negative definite for \(b>0\).

Therefore \(\Phi\) is strictly concave on the convex strategy domain

\[
\mathbb R_+^N.
\]

Its KKT point is unique, so the Cournot quantity game has a unique Nash quantity vector for every feasible sourcing history.

This is independent of the Stage-4 sorted-active-set proof.

The KKT system gives, for an active set \(S\),

\[
p_S=\frac{a+\sum_{k\in S}c_k}{|S|+1},
\qquad
q_j=\frac{p_S-c_j}{b}
\quad(j\in S),
\]

with inactive firms satisfying \(c_j\ge p_S\).

**C1 clean-room status: PASS.**

---

## 2. Cournot reduced payoff — global concavity attack

Fix rivals' sourcing profile and vary \(x=i_j\).

Once firm \(j\) is active, lowering its cost by increasing \(x\) can only push high-cost rivals out; it cannot cause an exited higher-cost rival to re-enter as \(j\)'s own cost falls further.

On a branch with \(m\) active firms including \(j\),

\[
z_j=p-c_j
\]

has slope

\[
\frac{dz_j}{dx}
=
H\frac{m}{m+1}.
\]

Hence

\[
\Pi_j''(x)
=
2\frac{H^2m^2}{b(m+1)^2}-2.
\]

The source restriction

\[
b>\left(\frac{HN}{N+1}\right)^2
\]

implies strict negativity because

\[
\frac m{m+1}\le\frac N{N+1}.
\]

At own entry, \(z_j=0\), so the derivative is continuous.

At a rival-exit threshold, \(z_j>0\) and the marginal operating benefit drops from

\[
\frac{2Hz_j}{b}\frac m{m+1}
\]

to

\[
\frac{2Hz_j}{b}\frac{m-1}{m}.
\]

The drop equals

\[
\frac{2Hz_j}{bm(m+1)}>0.
\]

Thus the derivative of the complete reduced payoff is strictly decreasing across smooth pieces and has only downward jumps. The full payoff is globally strictly concave.

**C2 clean-room status: PASS.**

C3 follows from the symmetric KKT condition; C4 and C5 are then direct exact comparative statics with the cap retained.

---

## 3. Cournot source-duopoly BR — clean-room branch reconstruction

Normalize

\[
\delta=D/H>0,
\qquad
\rho=b/H^2>\frac49.
\]

Against rival outsourcing \(y\), the only material continuation regimes are:

1. own zero output;
2. both firms active;
3. rival zero output / own monopoly.

The rival-exit threshold is

\[
U(y)=\delta+2y.
\]

The both-active stationary point is

\[
A(y)=\frac{2(\delta-y)}{9\rho-4}.
\]

The monopoly stationary point is

\[
M=\frac{\delta}{4\rho-1}.
\]

Comparing the stationary points with the switching threshold yields exactly the Stage-4 breakpoints

\[
y_A=
\frac{\delta(2-3\rho)}
{2(3\rho-1)}
\]

and, for \(\rho<1/2\),

\[
y_M=
\frac{\delta(1-2\rho)}
{4\rho-1}.
\]

The branch joins satisfy

\[
A(y_A)=U(y_A),
\qquad
M=U(y_M).
\]

The cap is applied only after obtaining the unconstrained global maximizer:

\[
B_\phi(y)=\min\{\phi,R(y)\}.
\]

In particular, when

\[
\frac49<\rho<\frac23,
\]

the kink branch is nonempty and

\[
U'(y)=2>0.
\]

This independently rejects a global strategic-substitutes interpretation of Proposition 5.

**C6/C7 clean-room status: PASS.**

---

## 4. Alternative-equilibrium audit for source duopoly

The fixed-point system is

\[
x=B_\phi(y),
\qquad
y=B_\phi(x).
\]

### 4.1 \(\rho>2/3\)

The uncapped active branch has absolute slope

\[
\frac{2}{9\rho-4}<1.
\]

The capped/zero pieces have slope zero. Thus \(B_\phi\) is globally Lipschitz with constant strictly below one. The two-player map

\[
T(x,y)=(B_\phi(y),B_\phi(x))
\]

is a contraction in the sup norm.

Hence the pure Stage-I equilibrium is unique and symmetric:

\[
(\min\{\phi,s\},\min\{\phi,s\}),
\qquad
s=\frac{2\delta}{9\rho-2}.
\]

### 4.2 \(\rho=2/3\)

The exact response reduces to

\[
B_\phi(y)=\min\{\phi,\max\{0,\delta-y\}\}.
\]

If \(\phi<\delta/2\), the unique solution is \((\phi,\phi)\).

If \(\phi\ge\delta/2\), the complete solution set is

\[
x+y=\delta,
\qquad
0\le x,y\le\phi,
\]

equivalently

\[
x\in
[\max\{0,\delta-\phi\},\min\{\phi,\delta\}].
\]

Thus the continuum is genuine and must not be described as a unique equilibrium.

### 4.3 \(4/9<\rho<2/3\)

The symmetric fixed point is

\[
s=\frac{2\delta}{9\rho-2}.
\]

If \(\phi\le s\), cap monotonicity makes \((\phi,\phi)\) the unique fixed point.

If \(\phi>s\), branch-by-branch intersection of the complete response graph with its transpose produces exactly one symmetric fixed point and one ordered asymmetric pair plus its mirror. Writing

\[
h=R(0),\qquad
x_H=\min\{\phi,h\},\qquad
x_L=R(x_H),
\]

the exact three pure equilibria are

\[
(s,s),\qquad
(x_H,x_L),\qquad
(x_L,x_H).
\]

No additional intersection remains on the flat, kink, active, zero, or cap pieces.

Exact rational regression:

\[
\rho=\frac35,\quad\delta=1,\quad\phi=2
\]

gives

\[
\left(\frac{10}{17},\frac{10}{17}\right),
\quad
(1,0),
\quad
(0,1).
\]

A separately written primitive-payoff evaluator in
\`code/stage04a_independent_verify.py\`
attacks these equilibria with exact rational finite deviations.

**C8 alternative-equilibrium status: PASS for pure Stage-I equilibrium scope.**

No general-\(N\) asymmetric uniqueness claim is certified.

---

## 5. Hotelling literal price game — independent reconstruction

For A,

\[
s_A(p_A,p_B)
=
\min\left\{
1,\max\left\{
0,\frac12+\frac{p_B-p_A}{2\tau}
\right\}
\right\}.
\]

Operating profit is

\[
\pi_A^P=n(p_A-c_A)s_A.
\]

The global pure price best response has three pieces:

- zero-demand best responses when the rival is sufficiently cheap;
- the standard interior quadratic optimum;
- the full-market boundary when the rival is sufficiently expensive.

Solving both best responses yields:

\[
|c_B-c_A|<3\tau
\]

— unique interior equilibrium;

\[
|c_B-c_A|=3\tau
\]

— unique zero-share boundary equilibrium;

and, for

\[
c_B-c_A>3\tau,
\]

\[
p_B=s,\qquad p_A=s-\tau,
\qquad
s\in[c_A+3\tau,c_B].
\]

Mirror the result when B is low-cost.

The high-cost firm earns zero throughout the continuum, but changing its payoff-equivalent price changes the low-cost firm's equilibrium price and profit. The indifference is therefore economically and strategically material.

**H1 clean-room / indifference status: PASS.**

---

## 6. Dominance attack

For any

\[
p<c,
\]

\[
(p-c)D(p,r)\le0
\]

for every rival price \(r\), whereas price \(c\) yields exactly zero operating profit. Hence \(p=c\) weakly dominates every \(p<c\).

But for any fixed \(\varepsilon>0\),

\[
(c+\varepsilon-c)D(c+\varepsilon,r)
=
\varepsilon D(c+\varepsilon,r)\ge0
\]

for every \(r\), with strict inequality for rival prices giving positive demand.

Thus

\[
c+\varepsilon
\]

weakly dominates \(c\).

Consequently:

- H-DOM1 is correct;
- the earlier label “undominated-price equilibrium” is incorrect;
- the auxiliary restriction \(p\ge c\) must be stated as a no-loss strategy restriction, not as deletion of all weakly dominated strategies.

This failure was preserved as a permanent Stage-4A regression and routed back to Stage 4 before recertification.

**H2/H2b clean-room status: PASS.**

---

## 7. Explicit no-loss price game

Now impose as an auxiliary strategy restriction

\[
p_j\ge c_j.
\]

For \(c_B-c_A>3\tau\), the literal corner family requires

\[
p_B\le c_B.
\]

The auxiliary restriction requires

\[
p_B\ge c_B.
\]

Thus a pure corner equilibrium must have

\[
p_B=c_B,\qquad p_A=c_B-\tau.
\]

Although B's restricted best-response set to \(p_A=c_B-\tau\) contains all prices weakly above \(c_B\), any \(p_B>c_B\) makes A's best response \(p_B-\tau\), which in turn places B in its interior-response region and destroys mutual best response unless \(p_B=c_B\).

Therefore the pure price equilibrium is unique within the no-loss restricted game.

Mirror for the other cost ordering.

**H3-NL candidate-deviation and alternative-pure-equilibrium status: PASS.**

No mixed-equilibrium uniqueness claim is made.

---

## 8. No-loss Stage-I global deviation audit

Against rival sourcing \(y\), the complete reduced pure-continuation payoff is

\[
V_y^{NL}(x)=
\begin{cases}
-x^2,&x-y\le-3\tau/H,\\[4pt]
\dfrac{n[3\tau+H(x-y)]^2}{18\tau}-x^2,
&|x-y|\le3\tau/H,\\[8pt]
n[H(x-y)-\tau]-x^2,
&x-y\ge3\tau/H.
\end{cases}
\]

Each branch is strictly concave under the source SOC.

Therefore every global best response lies among:

- the zero-demand branch optimum \(0\);
- the interior stationary point projected onto its feasible branch;
- the full-market stationary point \(Hn/2\) projected onto its feasible branch.

This independently establishes the finite-candidate characterization.

For the symmetric interior candidate

\[
i_0=\frac{Hn}{6},
\]

only the upward low-cost corner branch can create a nonlocal profitable deviation. The exact gain is

\[
\Delta(x)
=
-\frac{
36x^2-36Hnx+5H^2n^2+54n\tau
}{36}.
\]

Its maximum is

\[
\Delta_{\max}
=
\frac{n(2H^2n-27\tau)}{18}.
\]

When \(2H^2n>27\tau\), the lower zero is

\[
x_-=
\frac{Hn}{2}
-
\frac{\sqrt{2n(2H^2n-27\tau)}}6.
\]

Under the source SOC and the positive-gain condition,

\[
x_->i_0+\frac{3\tau}{H},
\]

so the root lies inside the correct corner branch.

Therefore the symmetric source candidate fails in the no-loss restricted game iff

\[
\frac{27}{2}\tau<H^2n<18\tau
\]

and

\[
\phi>x_-.
\]

The condition \(Hn/2\le\phi\) is sufficient but not necessary.

Exact regression:

\[
H=n=1,\quad\tau=1/15,\quad\phi=1
\]

gives

\[
i_0=1/6,\qquad
i_A'=1/2,
\qquad
\Delta\Pi=1/90.
\]

**H4-NL/H5-NL/H6-NL clean-room status: PASS within their explicit conditional pure-strategy scope.**

---

## 9. Scope exclusions

This Stage-4A reconstruction does not certify:

- uniqueness of general-\(N\) Stage-I Cournot equilibrium;
- mixed-strategy Cournot Stage-I equilibrium correspondence;
- complete asymmetric Stage-I Hotelling equilibrium correspondence;
- mixed price-equilibrium uniqueness in the no-loss Hotelling game;
- trembling-hand perfection, proper equilibrium, or admissibility;
- a welfare result.

Those objects are not required by the current headline correction claims.
