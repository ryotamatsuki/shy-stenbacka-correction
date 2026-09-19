# Proposition Impact Matrix

Status: **STAGE-4 RE-AUDIT COMPLETE; STAGE 4A CERTIFICATION NEXT**

| Published result | Canonical Stage-4 classification | Corrected result |
|---|---|---|
| Proposition 3 | **INCORRECT** | \(i_C^*=\min\{\phi,\bar i_C\}\) is weakly decreasing in \(N\), strictly decreasing on the interior branch for \(N>1\). |
| Corollary 4 | **PARTLY SURVIVES WITH BOUNDARY QUALIFICATION** | Interior signs survive. The outsourced fraction has weak global versions under the cap; the outsourced number rises one-for-one with \(\phi\) on the full-outsourcing branch and falls with \(\phi\) on the interior branch. |
| Proposition 5 | **FALSE AS A GLOBAL CLAIM** | The all-active Cournot BR is decreasing, but for \(4/9<b/H^2<2/3\) the global duopoly BR contains a slope-\(+2\) rival-exit segment. Asymmetric equilibria arise. |
| Proposition 6 / Eq. (25)–(26) | **LITERAL GAME: NOT GLOBALLY ESTABLISHED; UNDOMINATED-PRICE REFINEMENT: FALSE ON AN EXACT NONEMPTY REGION** | The source omits \(i\le\phi\), extrapolates the interior Hotelling price branch, and gives no corner selection. Literal corner equilibria are multiple. Every below-cost corner price is weakly dominated. After deleting those prices, the corner continuation is unique and the symmetric candidate fails exactly when \(27\tau/2<H^2n<18\tau\) and \(\phi>x_-\). |

## Cournot replacement

\[
\bar i_C=\frac{HND}{b(N+1)^2-H^2N},
\qquad
i_C^*=\min\{\phi,\bar i_C\}.
\]

For \(N>1\),

\[
\frac{\partial\bar i_C}{\partial N}
=
-\frac{HDb(N^2-1)}
{[b(N+1)^2-H^2N]^2}<0.
\]

## Proposition 5 replacement

With

\[
\delta=D/H,\qquad \rho=b/H^2,
\]

the rival-exit kink is

\[
U(y)=\delta+2y.
\]

For \(4/9<\rho<2/3\), it is part of the global BR on a nonempty feasible interval and

\[
U'(y)=2>0.
\]

## Proposition 6 two-layer replacement

### Literal source game

For \(|c_B-c_A|>3\tau\), the zero-demand high-cost firm can use a continuum of best-response prices, many below its marginal cost. The Stage-I continuation payoff is therefore selection-dependent. The source's interior backward induction is incomplete.

### Undominated-price refinement

For every \(p_j<c_j\),

\[
p_j=c_j
\]

weakly dominates \(p_j\).

Deleting these prices selects the unique corner continuation. Define

\[
i_0=\frac{Hn}{6},
\qquad
x_-=
\frac{Hn}{2}
-
\frac{\sqrt{2n(2H^2n-27\tau)}}{6}.
\]

If the cap binds, \((\phi,\phi)\) is the corrected symmetric equilibrium. If \(\phi>i_0\), the source symmetric candidate \((i_0,i_0)\) fails exactly when

\[
\boxed{
\frac{27}{2}\tau<H^2n<18\tau
\quad\text{and}\quad
\phi>x_-.
}
\]

At equality \(\phi=x_-\), the nonlocal deviation ties but does not strictly improve payoff.

## Architecture

The canonical Stage-4 architecture is restored Candidate **E′**:

1. complete Cournot correction;
2. literal Hotelling continuation diagnosis;
3. undominated-price Hotelling refinement and exact Proposition-6 failure region.
