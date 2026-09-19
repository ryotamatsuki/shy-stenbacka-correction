# Verification Code

Code supplements analytical proof and must never substitute for a global equilibrium argument.

Pinned dependency:

```text
sympy==1.14.0
```

## Stage 1

Run:

```bash
python code/stage01_verify.py
```

Expected first line:

```text
PASS: source-model Stage 1 symbolic checks
```

Important: the Stage-1 Hotelling corner-deviation assertion is retained as historical/regression evidence but its **interpretation is superseded by Stage 4**. Stage 4 proves that the same off-path Hotelling cost gap admits multiple valid price equilibria, so profitability of that outsourcing deviation is equilibrium-selection dependent.

## Stage 4 canonical check

Run:

```bash
python code/stage04_verify.py
```

Expected first line:

```text
PASS: Stage 4 exact construction checks
```

The Stage-4 script checks:

- the corrected general-(N) Cournot equation-(14) derivative;
- interior comparative statics and the outsourcing-cap transition identity;
- the unique nonnegative-quantity Cournot continuation through an independent active-set evaluator;
- the original negative-quantity history as a regression test;
- the original (i>phi) history and its corrected boundary best response;
- exact duopoly active/all-active/monopoly best-response formulas;
- an exact source-admissible example with three Stage-I equilibria;
- an exact positive-slope global-BR witness;
- Hotelling price-subgame multiplicity outside (|c_B-c_A|le3	au);
- the same Hotelling outsourcing deviation under two valid price continuations with opposite profitability;
- symbolic minimum- and maximum-selection deviation-gain formulas.

A fresh Python process was also used during Stage-4 construction to rerun the symbolic core identities successfully.

## Source-model discipline

The published monitoring cost is

[
M(i_j)=i_j^2.
]

No generalized monitoring-cost coefficient is used in canonical source-model proofs.

## Verification policy

Permitted roles include:

- symbolic simplification and factorization;
- inequality verification;
- exact parameter-region checks;
- direct primitive payoff reconstruction;
- deterministic counterexample/regression tests.

For every script record:

- software and package versions;
- exact parameter assumptions;
- deterministic seeds where relevant;
- expected output;
- the audit/manuscript claim checked.

Solver failure, NaN, invalid branch, or nonconvergence is `UNRESOLVED`, never evidence against a deviation.
