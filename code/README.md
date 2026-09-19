# Verification Code

Code supplements analytical proof and does not replace it.

## Stage 1

\`\`\`bash
python code/stage01_verify.py
\`\`\`

## Stage 4

\`\`\`bash
python code/stage04_verify.py
\`\`\`

Pinned dependency:

\`\`\`text
sympy==1.14.0
\`\`\`

Stage 4 checks:

- exact general-\(N\) Cournot symmetric identities;
- the corrected equation-(14) derivative;
- primitive active-set Cournot continuation regressions;
- the outsourcing-cap regression;
- source-duopoly global-BR branch joins;
- exact positive-slope Proposition-5 counterexample;
- exact symmetric/asymmetric duopoly equilibrium regression;
- Hotelling corner-price multiplicity;
- the Stage-1 Hotelling deviation under two valid continuation selections.

Important: symbolic equality is tested algebraically with \`simplify(lhs-rhs)==0\`, not by fragile expression-tree equality.

Solver failure, NaN, invalid branch, or nonconvergence is never evidence against a deviation.
