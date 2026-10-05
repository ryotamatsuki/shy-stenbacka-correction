# Counterexample and Regression Register

Status: **PERMANENT RESEARCH PROVENANCE**

This register indexes exact negative results that must remain reproducible after the Stage-8 theory freeze.

## R1 — literal Hotelling off-path multiplicity

When

\[
|c_B-c_A|>3\tau,
\]

the literal source price subgame has a continuum of pure corner equilibria.

Purpose:

- blocks the published interior continuation from being used globally;
- blocks a selection-free literal Stage-I reduced payoff off path.

Evidence:

- `audit/STAGE_04_HOTELLING_REAUDIT.md`
- `audit/stage04a_cleanroom_derivation.md`

## R2 — weak-dominance provenance failure

Although every `p<c` is weakly dominated by `p=c`, for every fixed `\varepsilon>0` the action `p=c+\varepsilon` weakly dominates `p=c`.

Purpose:

- permanently blocks the label “undominated-price refinement”;
- requires the `p\ge c` result to be presented as an explicit auxiliary no-loss strategy restriction.

Evidence:

- `audit/STAGE_04A_MATH_RED_TEAM.md`
- `audit/stage04a_theorem_certificates.md`

## R3 — Proposition-5 global failure

For the source duopoly with

\[
4/9<\rho<2/3,
\]

the exact pure global BR can contain

\[
U(y)=\delta+2y,
\]

with slope `+2`.

Purpose:

- blocks a global strategic-substitutes claim;
- does not license a global strategic-complements claim.

Evidence:

- `audit/stage04a_cleanroom_derivation.md`
- `code/stage04a_independent_verify.py`

## R4 — exact three-equilibrium regression

At

\[
(\rho,\delta,\phi)=(3/5,1,2),
\]

the pure Stage-I equilibria are

\[
(10/17,10/17),\qquad(1,0),\qquad(0,1).
\]

Purpose:

- regression test for the complete pure source-duopoly correspondence;
- exact witness that multiplicity/asymmetry is not numerical noise.

Evidence:

- `audit/stage04a_cleanroom_derivation.md`
- `code/stage04a_independent_verify.py`

## R5 — welfare selection

At the same three-equilibrium regression,

\[
W(10/17,10/17)=20/17<3/2=W(1,0)=W(0,1).
\]

Purpose:

- blocks selection-free welfare statements.

Evidence:

- `audit/stage07_welfare_benchmarks.md`
- `code/stage07_welfare_verify.py`
- Lean theorem `W_three_eq_symmetric_value`

## R6 — no-loss Hotelling exact deviation

At

\[
H=n=1,\qquad\tau=1/15,\qquad\phi=1,
\]

the deviation from `1/6` to `1/2` yields exact gain

\[
1/90.
\]

Purpose:

- exact regression for the conditional no-loss Hotelling failure result.

Evidence:

- `code/stage04_hotelling_refinement_verify.py`
- `code/stage04a_independent_verify.py`
- Lean theorem `H6_exact_regression`

## R7 — convex-monitoring generality kill test

Hold

\[
\delta=1,\qquad\rho=3/5,\qquad y=0,
\]

but replace the source monitoring cost by

\[
M(x)=10x^2.
\]

The rival-exit boundary remains at `x=1`, yet

\[
\Pi_A(0;0)=5/27,
\qquad
\Pi_A(1;0)=-25/3.
\]

Purpose:

- blocks promotion of C7/C8 to arbitrary convex monitoring technologies.

Evidence:

- `audit/stage075a_function_class_counterexamples.md`
- `code/stage075a_scope_counterexamples.py`

## Retention rule

These records are intentionally negative. Later manuscript simplification may omit some from the main text, but the repository must retain them as regression and scope-control evidence.
