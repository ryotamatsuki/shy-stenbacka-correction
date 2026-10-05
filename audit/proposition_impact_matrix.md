# Proposition Impact Matrix

Status: **STAGE-4 AMENDED AFTER STAGE-4A REFINEMENT ATTACK**

| Published result | Canonical Stage-4 classification | Corrected result |
|---|---|---|
| Proposition 3 | **INCORRECT** | \(i_C^*=\min\{\phi,\bar i_C\}\) is weakly decreasing in \(N\), strictly decreasing on the interior branch for \(N>1\). |
| Corollary 4 | **PARTLY SURVIVES WITH BOUNDARY QUALIFICATION** | Interior signs survive; cap branches make global statements weak/piecewise. |
| Proposition 5 | **FALSE AS A GLOBAL CLAIM** | The all-active Cournot BR is decreasing, but for \(4/9<b/H^2<2/3\) the global duopoly BR can contain a slope-\(+2\) rival-exit segment and asymmetric equilibria. |
| Proposition 6 / Eq. (25)–(26) | **LITERAL GAME: NOT GLOBALLY ESTABLISHED; NO-LOSS ROBUSTNESS: FALSE ON AN EXACT NONEMPTY REGION** | Literal corner continuations are multiple. Under the auxiliary restriction \(p_j\ge c_j\), the pure corner continuation is unique and the symmetric candidate fails exactly on the cap-aware region below. |

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

## Proposition 6 — literal source game

For \(|c_B-c_A|>3\tau\), the zero-demand high-cost firm has a continuum of best-response prices, creating multiple pure price continuations. The source gives no off-path selection rule, so the published interior backward induction is incomplete.

## Proposition 6 — explicit no-loss robustness

Every \(p_j<c_j\) is weakly dominated by \(p_j=c_j\), which makes a no-loss restriction economically recognizable. But \(p_j=c_j\) is itself weakly dominated by \(p_j=c_j+\varepsilon\); therefore \(p_j\ge c_j\) is **not** presented as elimination of all weakly dominated strategies.

Under the explicit restriction \(p_j\ge c_j\), define

\[
i_0=\frac{Hn}{6},
\qquad
x_-=
\frac{Hn}{2}
-
\frac{\sqrt{2n(2H^2n-27\tau)}}{6}.
\]

For \(\phi>i_0\), the symmetric candidate fails exactly when

\[
\boxed{
\frac{27}{2}\tau<H^2n<18\tau
\quad\text{and}\quad
\phi>x_-.
}
\]

## Architecture

\[
\boxed{\textbf{HYBRID}}
\]

- main theorem block: Cournot correction;
- secondary source-faithful Hotelling result: literal continuation multiplicity/incomplete proof;
- secondary robustness result: exact failure region under explicit no-loss price restriction.
