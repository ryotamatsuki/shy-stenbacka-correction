# Stage 7 Welfare and Benchmark Register

Status: **CERTIFIED FOR STAGE 7**

## 1. Accounting convention

All input-production costs and monitoring costs in the source model are treated as real resource costs.

Competitive subcontractors earn zero rents in the source model, so payments to them are not added again as social surplus.

Product-market prices are transfers between consumers and final-good producers and cancel from total welfare.

No tax, subsidy, bargaining transfer, externality, or labor-distribution term is present in the source model.

---

## 2. Cournot exact consumer surplus and welfare

Inverse demand is

\[
p(Q)=a-bQ.
\]

Hence exact consumer surplus is

\[
CS_C(Q)
=
\int_0^Q(a-bz)\,dz-p(Q)Q
=
\frac b2Q^2.
\]

With

\[
c_j(i_j)=C_0-Hi_j,
\qquad
C_0=H\phi+\frac{\gamma\phi^2}{2},
\]

producer surplus is

\[
PS_C
=
\sum_j
\left[
(p-c_j)q_j-i_j^2
\right].
\]

Therefore total welfare is

\[
\boxed{
W_C(q,i)
=
aQ-\frac b2Q^2
-\sum_j c_j(i_j)q_j
-\sum_j i_j^2
}
\]

or, using \(D=a-C_0\),

\[
\boxed{
W_C(q,i)
=
DQ-\frac b2Q^2
+
H\sum_j i_jq_j
-
\sum_j i_j^2.
}
\tag{W-C1}
\]

This identity is exact and does not assume equilibrium.

---

## 3. Cournot full planner

The unrestricted relevant planner problem within the reduced source technology is

\[
\max_{\substack{q_j\ge0\\0\le i_j\le\phi}}
\left\{
DQ-\frac b2Q^2
+
H\sum_j i_jq_j
-
\sum_j i_j^2
\right\}.
\tag{FB-C}
\]

Choice set:

- all firm outputs \(q_j\ge0\);
- every outsourcing level \(i_j\in[0,\phi]\);
- no restriction to symmetry;
- no requirement that all firms remain active.

This is the appropriate **first-best problem within the source's reduced technology**.

The correction paper does **not** use a closed-form solution to (FB-C) as a headline result.

Reason: the fixed monitoring cost creates a nonconvex allocation problem once sourcing and firm-level output are chosen jointly. Conditional on a firm's output \(q_j\), its socially optimal sourcing is

\[
i_j^{FB}(q_j)
=
\min\left\{
\phi,\,
\frac{Hq_j}{2}
\right\}.
\]

The induced cost-saving term is convex in \(q_j\) before the cap, creating an incentive to concentrate production. Hence a symmetric planner benchmark would not be the unrestricted first best and must not be labeled as such.

---

## 4. Cournot restricted-instrument sourcing benchmark

To compare the private symmetric outsourcing formula without solving a different nonconvex planner problem, define the following benchmark explicitly.

### Benchmark C-R

A regulator/planner:

1. chooses a **common sourcing level**
   \[
   s\in[0,\phi];
   \]
2. does **not** choose output;
3. leaves the Stage-II symmetric Cournot quantity game unchanged.

This is a:

\[
\boxed{\textbf{restricted-instrument equilibrium-welfare optimum}}
\]

not a first best.

At common sourcing \(s\),

\[
Q(s)
=
\frac{N(D+Hs)}{b(N+1)}.
\]

Exact Cournot-equilibrium welfare is

\[
\boxed{
W_C^{eq}(s)
=
\frac{N(N+2)(D+Hs)^2}
{2b(N+1)^2}
-
Ns^2.
}
\tag{W-C2}
\]

Under the source SOC this is strictly concave in \(s\).

The unconstrained restricted-welfare optimum is

\[
\bar s_R
=
\frac{H(N+2)D}
{2b(N+1)^2-H^2(N+2)},
\]

and the constrained benchmark is

\[
\boxed{
s_R^*
=
\min\{\phi,\bar s_R\}.
}
\tag{W-C3}
\]

The private symmetric Cournot action is

\[
s_P^*
=
\min\left\{
\phi,\,
\frac{HND}
{b(N+1)^2-H^2N}
\right\}.
\]

For the unconstrained roots,

\[
\bar s_P-\bar s_R
=
\frac{
DHb(N-2)(N+1)^2
}{
[b(N+1)^2-H^2N]
[2b(N+1)^2-H^2(N+2)]
}.
\]

Both denominators are positive under the source restrictions. Therefore

\[
\boxed{
s_P^*\ge s_R^*
\quad(N\ge2).
}
\tag{W-C4}
\]

More precisely:

- \(N=2\): the two unconstrained levels coincide exactly;
- \(N>2\): the private unconstrained symmetric level is strictly larger;
- the cap can turn strict inequality into equality.

This is **not** a statement that private sourcing exceeds the unrestricted first best.

---

## 5. Cournot multiplicity and welfare selection

The certified source-duopoly Stage-I game can have multiple pure equilibria.

Welfare is not invariant across those equilibria.

### Exact three-equilibrium regression

Normalize

\[
H=1,\quad
D=1,\quad
\rho=b/H^2=\frac35,\quad
\phi=2.
\]

The three pure equilibria are

\[
\left(\frac{10}{17},\frac{10}{17}\right),
\qquad
(1,0),
\qquad
(0,1).
\]

Using (W-C1),

\[
W\left(\frac{10}{17},\frac{10}{17}\right)
=
\frac{20}{17},
\]

whereas

\[
W(1,0)=W(0,1)=\frac32.
\]

Hence:

\[
\boxed{
\text{Cournot equilibrium multiplicity is welfare-material.}
}
\]

A selection-free welfare ranking based only on the symmetric equilibrium is invalid.

### Knife edge \(\rho=2/3\)

When the cap permits the equilibrium continuum

\[
x+y=\delta,
\]

normalized welfare is

\[
\boxed{
W(x,\delta-x)
=
\frac54\delta^2-\delta x+x^2.
}
\tag{W-C5}
\]

Thus welfare varies continuously across the certified equilibrium continuum.

---

## 6. Hotelling exact consumer surplus

The source utility is

\[
u_A(z)=\omega-p_A-\tau z,
\qquad
u_B(z)=\omega-p_B-\tau(1-z),
\]

with density \(n\) and full market coverage.

If A serves consumers \(z\in[0,x]\) and B serves \(z\in[x,1]\), exact consumer surplus is

\[
\boxed{
CS_H
=
n\left[
\omega
-p_Ax
-p_B(1-x)
-\frac{\tau}{2}
\left(
x^2+(1-x)^2
\right)
\right].
}
\tag{W-H1}
\]

Producer surplus is

\[
PS_H
=
n(p_A-c_A)x
+n(p_B-c_B)(1-x)
-i_A^2-i_B^2.
\]

Therefore

\[
\boxed{
W_H
=
n\left[
\omega
-c_Ax
-c_B(1-x)
-\frac{\tau}{2}
\left(
x^2+(1-x)^2
\right)
\right]
-i_A^2-i_B^2.
}
\tag{W-H2}
\]

Prices cancel exactly.

---

## 7. Hotelling fixed-sourcing efficient allocation

For fixed \(i_A,i_B\), equivalently fixed \(c_A,c_B\), the planner chooses only consumer allocation \(x\).

The exact efficient share of A is

\[
\boxed{
x_W
=
\operatorname{proj}_{[0,1]}
\left[
\frac12+\frac{c_B-c_A}{2\tau}
\right].
}
\tag{W-H3}
\]

The literal interior price equilibrium allocates

\[
x_{NE}
=
\frac12+\frac{c_B-c_A}{6\tau}.
\]

Therefore, while both are interior,

\[
\boxed{
x_W-x_{NE}
=
\frac{c_B-c_A}{3\tau}.
}
\tag{W-H4}
\]

If A is lower cost, the decentralized Hotelling allocation shifts too little demand toward A relative to the fixed-sourcing efficient allocation.

The planner reaches a corner once

\[
|c_B-c_A|\ge\tau,
\]

whereas the literal price equilibrium reaches a corner only once

\[
|c_B-c_A|\ge3\tau.
\]

This is a standard allocative-wedge diagnostic, not a claimed novel result.

---

## 8. Hotelling full planner

The unrestricted planner problem under the source full-coverage environment is

\[
\max_{\substack{x\in[0,1]\\
0\le i_A,i_B\le\phi}}
n\left[
\omega
-(C_0-Hi_A)x
-(C_0-Hi_B)(1-x)
-\frac{\tau}{2}
\left(x^2+(1-x)^2\right)
\right]
-i_A^2-i_B^2.
\tag{FB-H}
\]

This is the appropriate **first-best problem within the full-coverage source technology**.

The correction paper does not use a closed-form global solution of (FB-H) as a contribution claim.

For fixed allocation \(x\), however,

\[
i_A^W(x)
=
\min\left\{
\phi,\,
\frac{Hnx}{2}
\right\},
\]

\[
i_B^W(x)
=
\min\left\{
\phi,\,
\frac{Hn(1-x)}{2}
\right\}.
\]

---

## 9. Hotelling fixed-allocation sourcing benchmark

At the symmetric 50-50 allocation,

\[
x=\frac12,
\]

the fixed-allocation welfare-optimal sourcing level of each firm is

\[
\boxed{
i_{W,1/2}
=
\min\left\{
\phi,\,
\frac{Hn}{4}
\right\}.
}
\tag{W-H5}
\]

The source symmetric private stationary level is

\[
i_P
=
\min\left\{
\phi,\,
\frac{Hn}{6}
\right\}
\]

when that symmetric candidate is globally valid under the stated continuation concept.

Thus

\[
\boxed{
i_P\le i_{W,1/2}.
}
\tag{W-H6}
\]

This benchmark is explicitly a:

\[
\boxed{\textbf{fixed-allocation sourcing benchmark}}
\]

not a first best.

It does not support a general policy prescription because the unrestricted planner also chooses market allocation and because the literal Stage-I game can be continuation-selection dependent.

---

## 10. Benchmark-definition register

| Benchmark | Objective | Choice set | Fixed objects | Correct label |
|---|---|---|---|---|
| FB-C | (W-C1) | all \(q_j\ge0\), all \(i_j\in[0,\phi]\) | source technology | **first best within source reduced technology** |
| C-R | (W-C2) | one common \(s\in[0,\phi]\) | decentralized symmetric Cournot output | **restricted-instrument equilibrium-welfare optimum** |
| FB-H | (W-H2) | \(x\in[0,1]\), \(i_A,i_B\in[0,\phi]\) | full coverage, source technologies | **first best within source full-coverage technology** |
| H fixed-cost allocation | (W-H2) | \(x\in[0,1]\) | \(i_A,i_B\) fixed | **fixed-sourcing allocation optimum** |
| H 50-50 sourcing | (W-H2) | \(i_A,i_B\) | \(x=1/2\) fixed | **fixed-allocation sourcing benchmark** |

No other object may be called first best.
