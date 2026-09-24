# Stage 7 — Welfare, Generality & Institutional Validation

Status: **GO TO STAGE 7.5**

Audit date: 2026-09-19  
Canonical workflow: \`research-paper-workflow\` v2.2  
Frozen input: Stage-6 checkpoint \`e7b3a745e92c108fee4ecb85e1769bab59ce24a1\`

## 1. Executive verdict

Stage 7 passes, with an important scope decision:

\[
\boxed{
\textbf{WELFARE IS SUPPORTING DIAGNOSTIC, NOT A NEW HEADLINE CONTRIBUTION}
}
\]

The project remains a source-specific correction paper.

Exact welfare accounting is coherent, but equilibrium multiplicity in the corrected Cournot duopoly makes global welfare selection-dependent. Therefore the paper should not add broad welfare or policy claims merely to increase scope.

The most useful welfare results are benchmark diagnostics:

- exact Cournot and Hotelling total-surplus identities;
- a restricted common-sourcing Cournot welfare benchmark;
- fixed-sourcing Hotelling allocation efficiency;
- fixed-allocation Hotelling sourcing benchmark;
- an exact demonstration that Cournot multiple equilibria can carry different welfare.

Institutional evidence supports the broad source trade-off of outsourcing cost advantages versus monitoring/quality-control burdens, but does not validate the exact linear/quadratic functional forms.

Canonical verdict:

\[
\boxed{\textbf{GO TO STAGE 7.5}}
\]

---

## 2. Exact welfare derivation

Full derivations are in:

\`audit/stage07_welfare_benchmarks.md\`.

### Cournot

\[
CS_C=\frac b2Q^2.
\]

\[
W_C
=
aQ-\frac b2Q^2
-\sum_jc_jq_j
-\sum_ji_j^2.
\]

Using \(D=a-C_0\) and \(c_j=C_0-Hi_j\),

\[
W_C
=
DQ-\frac b2Q^2
+
H\sum_ji_jq_j
-
\sum_ji_j^2.
\]

### Hotelling

For share \(x\) served by A,

\[
CS_H
=
n\left[
\omega-p_Ax-p_B(1-x)
-\frac{\tau}{2}
(x^2+(1-x)^2)
\right].
\]

Total welfare is

\[
W_H
=
n\left[
\omega-c_Ax-c_B(1-x)
-\frac{\tau}{2}
(x^2+(1-x)^2)
\right]
-i_A^2-i_B^2.
\]

Prices cancel exactly.

Exact symbolic checks are in:

\`code/stage07_welfare_verify.py\`.

---

## 3. Planner-objective / choice-set register

### Cournot full first best

\[
\max_{q_j\ge0,\ 0\le i_j\le\phi}
\left[
DQ-\frac b2Q^2
+H\sum_ji_jq_j
-\sum_ji_j^2
\right].
\]

The planner chooses every firm-level quantity and sourcing level.

This is the only Cournot object labeled first best.

### Cournot restricted sourcing benchmark

Planner chooses one common sourcing level \(s\), then firms play the source Cournot quantity game.

This is labeled:

**restricted-instrument equilibrium-welfare optimum**.

### Hotelling full first best

Under source full coverage, planner chooses:

\[
x,\ i_A,\ i_B.
\]

It minimizes real production, monitoring, and transportation costs; prices are absent from the planner objective because they are transfers.

### Hotelling fixed-sourcing allocation benchmark

Planner chooses \(x\) only.

### Hotelling fixed-allocation sourcing benchmark

Planner chooses sourcing with consumer allocation fixed.

No restricted benchmark is called first best.

---

## 4. Private versus social decision map

### Cournot symmetric path

Private:

\[
\bar s_P
=
\frac{HND}
{b(N+1)^2-H^2N}.
\]

Restricted common-sourcing welfare optimum:

\[
\bar s_R
=
\frac{H(N+2)D}
{2b(N+1)^2-H^2(N+2)}.
\]

The exact gap is proportional to \(N-2\).

Therefore:

\[
s_P^*\ge s_R^*
\]

for \(N\ge2\), with exact equality of unconstrained levels at \(N=2\) and strict private over-sourcing for \(N>2\) when both solutions are interior.

This is not a first-best comparison.

### Hotelling allocation

For fixed costs,

\[
x_W=
\operatorname{proj}_{[0,1]}
\left[
\frac12+\frac{c_B-c_A}{2\tau}
\right],
\]

while the interior market equilibrium gives

\[
x_{NE}
=
\frac12+\frac{c_B-c_A}{6\tau}.
\]

Thus the decentralized allocation reacts only one-third as strongly to a marginal-cost difference.

### Hotelling symmetric fixed split

At \(x=1/2\),

\[
i_W=
\min\{\phi,Hn/4\},
\]

while the source private symmetric stationary level is

\[
i_P=
\min\{\phi,Hn/6\}
\]

when globally valid.

Thus private sourcing is weakly below this fixed-allocation welfare benchmark.

Again, this is not a first-best comparison.

---

## 5. Welfare and equilibrium selection

This is the central Stage-7 warning.

At the exact Stage-4A three-equilibrium Cournot regression,

\[
(\rho,\delta,\phi)=
\left(\frac35,1,2\right),
\]

the symmetric equilibrium has welfare

\[
\frac{20}{17},
\]

while each asymmetric equilibrium has welfare

\[
\frac32.
\]

Therefore:

\[
\boxed{
\text{the corrected Cournot equilibrium set is not welfare-invariant.}
}
\]

At the \(\rho=2/3\) equilibrium continuum,

\[
W(x,\delta-x)
=
\frac54\delta^2-\delta x+x^2,
\]

which varies with the equilibrium selection.

Consequences:

- no welfare statement may silently evaluate only the symmetric equilibrium;
- no selection-free welfare ordering is authorized for the global source-duopoly Stage-I game;
- any later welfare discussion must either characterize the entire equilibrium set or name a selection.

For the literal Hotelling price continuum, prices vary but the corner market allocation is fixed. Hence welfare at a **fixed sourcing history** is invariant to which corner price equilibrium is selected.

However, off-path price selection affects upstream sourcing incentives, so literal-game Stage-I welfare remains unresolved without a complete SPNE selection characterization.

---

## 6. Institutional validation

Institutional evidence is not needed for the mathematical correction, but the broad outsourcing trade-off is credible.

The source model itself interprets outsourcing as lower unit input costs combined with management / quality-control monitoring costs.

Empirical manufacturing work supports:

- production fragmentation / partial sourcing as a real organizational margin;
- coordination costs as relevant to fragmentation;
- active quality audits and contractual monitoring in outsourced manufacturing.

The strongest direct monitoring evidence used here is Handley & Gray (2013), which studies facility audits and contractual quality-control mechanisms using dyadic data from 95 outsourced-manufacturing relationships.

Fort (2017) provides direct U.S. manufacturing evidence that communication technology affects production fragmentation and interprets the pattern through coordination costs.

These sources validate the **existence** of coordination/monitoring frictions. They do not validate:

\[
M(i)=i^2,
\]

output independence of monitoring cost, or

\[
c(i)=C_0-Hi
\]

as general empirical laws.

Those remain tractability assumptions.

Institutional classifications are in:

\`audit/stage07_generality_institutional.md\`.

---

## 7. Generality verdict

No broad robustness theorem is added.

### Baseline-only results

The exact:

- Proposition-3 sign reversal formula;
- \(+2\) best-response slope;
- \(\rho\) thresholds;
- complete pure duopoly correspondence;
- Hotelling \(27\tau/2\) threshold

remain **baseline functional-form results**.

### Mechanism-level support

The rival-exit geometry has a plausible wider interpretation.

In a linear Cournot duopoly with a differentiable strictly decreasing marginal-cost function \(c(i)\), the rival-exit boundary can be written

\[
c(x)=2c(y)-a.
\]

Where differentiable,

\[
\frac{dx}{dy}
=
\frac{2c'(y)}{c'(x)}>0.
\]

Thus the **exit threshold itself** rises with rival cost reduction under a wider decreasing-cost class.

But Stage 7 does not upgrade this into a general global-BR or equilibrium theorem. Whether the kink is globally optimal depends on investment/monitoring curvature and other branches.

The correct classification is:

**restricted-class mechanism support / conjectured equilibrium generality**.

This is a Stage-7.5A attack target.

---

## 8. Empirical predictions

The corrected model suggests tests rather than policy prescriptions.

Most useful predictions:

1. Competition/outsource correlations should differ between all-active product markets and markets near firm exit.
2. In the all-active source branch, more Cournot competitors reduce the predicted symmetric outsourcing level.
3. Near an exit threshold, rival outsourcing can correlate positively with own outsourcing.
4. Ex ante similar duopolists can display persistent high/low sourcing asymmetry in the multiplicity region.
5. Hotelling outsourcing may appear locally insensitive to differentiation but become regime-sensitive once cost asymmetry pushes the market near a corner.

These are theoretical predictions. Stage 7 does not claim they are already empirically confirmed.

---

## 9. Result-to-exposition triage

The main paper should remain compact.

### Main text

- S1 sign reversal: proposition / displayed derivative.
- S2 global BR correction: proposition plus one BR figure after theory freeze.
- S3 pure equilibrium correspondence: theorem plus compact regime table or phase diagram.

### Secondary

- S4 literal Hotelling multiplicity: short proposition or appendix.
- S5 no-loss threshold: appendix proposition unless journal space permits.

### Welfare

No new welfare section is required for the core correction paper.

If included, welfare should be a short appendix or discussion subsection emphasizing:

- exact accounting;
- selection dependence;
- absence of a policy conclusion.

Adding a large welfare extension would weaken the paper's correction discipline.

---

## 10. Policy scope

Stage 7 authorizes no substantive policy recommendation.

In particular, the model does not justify:

- subsidies or taxes on outsourcing;
- regulation of sourcing levels;
- intervention to select an asymmetric or symmetric equilibrium;
- a pricing floor as public policy;
- merger policy conclusions.

The defensible implication is methodological:

> Product-market participation constraints and off-path continuation regimes must be respected when using organizational choices as strategic commitments.

---

## 11. Candidate Stage-7.5A attacks

Stage 7.5A must specifically attack:

1. baseline-vs-general wording for every theorem;
2. integer-\(N\) comparative-static wording;
3. general monitoring cost / cost-reduction functions;
4. exact \(\rho\)-boundary quantifiers;
5. all equilibrium-selection qualifiers in welfare prose;
6. all planner benchmark labels;
7. Hotelling full-coverage dependence;
8. pure-vs-mixed price scope;
9. conditional nature of \(p\ge c\);
10. any institutional sentence that upgrades linear/quadratic assumptions into facts.

---

## 12. Fatal / major concerns

No fatal correctness blocker was found.

Major scope risks to carry forward:

1. **Welfare selection dependence.** Global Cournot welfare cannot be stated selection-free.
2. **Functional-form dependence.** Most exact thresholds are baseline-only.
3. **Planner nonconvexity.** A symmetric sourcing benchmark is not the full first best.
4. **Hotelling full coverage.** Welfare and continuation results inherit the source's full-coverage environment.
5. **Institutional functional forms.** Exact monitoring/cost forms are not empirically established.

These are scope controls, not Stage-7 failures.

---

## 13. Canonical verdict

\[
\boxed{\textbf{GO TO STAGE 7.5}}
\]

Stage 7.5 must decide whether the certified source-specific correction package is valuable enough to freeze without adding extensions.

It must carry forward:

- the benchmark-definition register;
- the equilibrium-selection robustness table;
- the baseline-vs-generality classifications;
- the prohibition on selection-free welfare claims;
- the result-to-exposition triage.
