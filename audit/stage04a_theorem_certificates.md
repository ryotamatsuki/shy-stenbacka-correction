# Stage 4A Independent Theorem Certificates

Status: **PASS**

Certification date: 2026-09-19  
Canonical Stage-4 architecture: **HYBRID**  
Independent evidence:
- \`audit/stage04a_cleanroom_derivation.md\`
- \`code/stage04a_independent_verify.py\`
- exact Stage-4 regression artifacts

## Certificate table

| ID | Exact certified scope | Candidate-deviation audit | Alternative-equilibrium audit | Indifference / selection audit | Independent reconstruction | Surviving limitation | State |
|---|---|---|---|---|---|---|---|
| C1 | For every feasible source Cournot cost vector, the Stage-II pure quantity Nash equilibrium is unique | KKT over \(q\ge0\) | uniqueness from strictly concave potential | zero-output threshold checked | independent potential \(\Phi\) with negative-definite Hessian | none at Stage II | **PASS** |
| C2 | Under \(b>(HN/(N+1))^2\), own reduced Cournot payoff is globally strictly concave on \([0,\phi]\) for every fixed rival sourcing profile | all active-set pieces; entry/exit boundaries | N/A — concavity claim | derivative continuity at own entry and downward jumps at rival exit | clean-room derivative reconstruction | source linear-demand/quadratic-monitoring model only | **PASS** |
| C3 | Unique symmetric Cournot Stage-I action is \(i_C^*=\min\{\phi,HND/[b(N+1)^2-H^2N]\}\) | full feasible own-deviation domain via C2 | only symmetric uniqueness claimed | cap boundary checked | C2 + independent symmetric KKT | no general-\(N\) asymmetric uniqueness claim | **PASS** |
| C4 | \(i_C^*\) is weakly decreasing in \(N\); interior branch strictly decreases for \(N>1\) | cap/interior branches | N/A | cap flatness recorded | exact independent derivative factorization | \(N\) interpreted through continuous extension for sign proof | **PASS** |
| C5 | Cournot \(\phi\)-comparative statics are piecewise: outsourced number rises with cap on full-outsourcing branch and falls on interior branch; fraction is weakly decreasing | both cap/interior branches | N/A | switching boundary checked | direct differentiation | source functional form | **PASS** |
| C6 | Source-duopoly pure global BR is the Stage-4 piecewise \(B_\phi\) | zero-output, both-active, rival-exit, monopoly, cap | N/A | kink joins checked | branch reconstruction from primitive Cournot continuation | pure Stage-I BR | **PASS** |
| C7 | For \(4/9<\rho<2/3\), a feasible global-BR segment has slope \(+2\), so Proposition 5 is false globally | exact finite-deviation branch | N/A | regime switch is mechanism | independent branch comparison + rational witness | does not claim complements everywhere | **PASS** |
| C8 | Complete **pure** Stage-I equilibrium correspondence for source duopoly has the three stated \(\rho\)-cases | all BR pieces/cap | explicit fixed-point search; continuum at \(\rho=2/3\); exactly three when stated | ties retained | contraction proof / branch-intersection proof + independent exact evaluator | no mixed Stage-I classification | **PASS** |
| H1 | Literal source Hotelling **pure-price** equilibrium: unique for \(|d|\le3\tau\), continuum for \(|d|>3\tau\) | global clipped-demand price deviations | complete pure-price correspondence | zero-demand high-cost indifference explicitly changes opponent price/profit | clean-room price-BR derivation | no mixed-price classification | **PASS** |
| H2 | Every \(p<c\) is weakly dominated by \(p=c\) | all rival prices / all demand regimes | N/A | zero-demand equality included | primitive payoff sign argument | does not imply all-weak-dominance refinement | **PASS** |
| H2b | \(p=c\) is weakly dominated by every fixed \(p=c+\varepsilon\), \(\varepsilon>0\) | all rival prices | N/A | this kills prior “undominated-price” label | independent primitive payoff attack | dominance chains beyond this are not used | **PASS** |
| H3-NL | In auxiliary game with explicit \(p_j\ge c_j\), pure Hotelling price equilibrium is unique for every cost gap | all restricted price deviations | alternative pure corner prices explicitly eliminated by mutual-BR test | high-cost BR indifference rechecked | clean-room restricted BR derivation | conditional model; no mixed uniqueness | **PASS** |
| H4-NL | Under \(p_j\ge c_j\), pure Stage-I BR equals finite-candidate argmax (H-NL2) | zero-demand/interior/full-market/cap/boundaries | N/A | ties retained | branchwise strict concavity + projection | conditional no-loss model | **PASS** |
| H5-NL | Under source SOC and \(p_j\ge c_j\), interior symmetric candidate fails iff \(27\tau/2<H^2n<18\tau\) and \(\phi>x_-\) | all local and nonlocal pure deviations | only symmetric-candidate survival claimed | branch threshold and tie at \(\phi=x_-\) checked | independent gain quadratic/root/order proof | no complete asymmetric Stage-I set | **PASS** |
| H6-NL | Exact regression \(H=n=1,\tau=1/15,\phi=1\): \(1/2\) deviation against \(1/6\) gains \(1/90\) | exact direct payoff | N/A | no selection ambiguity in restricted pure price continuation | independent rational evaluator | conditional on \(p\ge c\) | **PASS** |

## Welfare / benchmark fields

**NOT APPLICABLE.**

No Stage-4A headline claim is a planner, welfare, first-best, second-best, or welfare-selection theorem.

## Formal verification applicability

\[
\boxed{\textbf{FORMALIZATION APPLICABLE}}
\]

Target map: \`audit/stage04a_formalization_target_map.md\`.

Implementation is deferred to the formal-verification gate before theory freeze; this does not weaken the Stage-4A independent mathematical certification.

## Final certificate state

No material field is \`NOT TESTED\`.

No material continuation is \`UNRESOLVED\`.

No numerical search is used as proof.

\[
\boxed{\textbf{PASS}}
\]
