# Stage 7.5A Claim-Scope Ledger

Status: **PASS — SCOPE AUDIT COMPLETE / FORMAL VERIFICATION PASS**

Date: 2026-09-19

This ledger states the maximum manuscript wording licensed by the frozen Stage-4A / Stage-6 / Stage-7 evidence.

## 1. Primary Cournot claims

| ID | Formal scope | Equilibrium-set quantifier | Maximum defensible wording | Prohibited stronger wording |
|---|---|---|---|---|
| C1 | For every feasible source outsourcing history \(i\in[0,\phi]^N\), the downstream linear-Cournot game with nonnegative quantities has one pure Nash quantity vector | **unique pure Stage-II quantity equilibrium** | “the downstream pure quantity continuation is unique for every feasible sourcing history” | “the downstream game has a unique Nash equilibrium” if mixed strategies are intended |
| C2 | For integer \(N\ge2\), source SOC, and every fixed rival sourcing profile, firm \(j\)'s reduced payoff under the certified pure Cournot continuation is globally strictly concave in \(i_j\in[0,\phi]\) | payoff property, not equilibrium uniqueness | “own reduced sourcing payoff is globally strictly concave” | “the Stage-I game has a unique equilibrium” |
| C3 | Under the source restrictions, the unique **symmetric pure Stage-I action** is \(i_C^*=\min\{\phi,\bar i_C\}\) | uniqueness only within symmetric pure profiles | “the unique symmetric pure sourcing action is …” | “the general-\(N\) SPNE is unique” |
| C4 | For the interior formula \(\bar i_C(N)\), the continuous extension has negative derivative for \(N>1\). For integer market sizes, adjacent corrected roots strictly fall whenever the source restrictions required for the equilibrium theorem hold at both compared market sizes. The capped action is weakly decreasing on any such admissible integer comparison set. | symmetric pure action only | “among market sizes satisfying the source restrictions, the corrected symmetric outsourcing level is weakly decreasing in the number of firms, and strictly decreasing when the compared actions are off the cap” | “outsourcing always strictly falls with competition” or any comparison to a market size outside the source theorem’s admissible domain |
| C5 | On the source feasible domain \(D(\phi)>0\): outsourced number rises one-for-one on the cap branch and falls on the interior branch; outsourced fraction is weakly decreasing | symmetric pure action only | branch-qualified comparative statics | unqualified “outsourcing falls with \(\phi\)” |

## 2. Source-duopoly Cournot claims

Throughout:

\[
\delta>0,\qquad \rho=b/H^2>\frac49,\qquad \phi>0.
\]

| ID | Formal scope | Equilibrium-set quantifier | Maximum defensible wording | Prohibited stronger wording |
|---|---|---|---|---|
| C6 | Exact constrained **pure** best response \(B_\phi(y)\) for every \(y\in[0,\phi]\) | all pure unilateral sourcing deviations | “complete pure global best response” | “complete best response including mixed strategies” |
| C7 | For \(4/9<\rho<2/3\), whenever the rival-exit piece is feasible, a pure-BR segment equals \(U(y)=\delta+2y\) and has slope \(+2\) | existence of a positive-slope BR segment, not global complementarity | “Proposition 5 is false as a global strategic-substitutes claim” | “outsourcing is globally a strategic complement” |
| C8-A | \(\rho>2/3\): exactly one pure Stage-I equilibrium, symmetric | **unique pure Stage-I equilibrium** | “the source duopoly has a unique pure equilibrium in this region” | mixed-equilibrium uniqueness |
| C8-B | \(\rho=2/3,\ \phi<\delta/2\): exactly \((\phi,\phi)\) | unique pure | exact case wording | generic uniqueness at \(\rho=2/3\) |
| C8-C | \(\rho=2/3,\ \phi\ge\delta/2\): continuum \(x+y=\delta\) subject to the sourcing box | complete pure continuum | “a continuum of pure equilibria” | “a unique equilibrium” |
| C8-D | \(4/9<\rho<2/3,\ \phi\le s\): exactly \((\phi,\phi)\) | unique pure | exact case wording | strict-\(\phi<s\) wording that omits equality |
| C8-E | \(4/9<\rho<2/3,\ \phi>s\): exactly \((s,s),(x_H,x_L),(x_L,x_H)\) | complete pure set | “exactly three pure Stage-I equilibria” | “exactly three Nash equilibria” without “pure Stage-I” |

The source-SOC boundary \(\rho=4/9\) is excluded because the source restriction is strict.

The internal BR subcase boundary \(\rho=1/2\) is included in the certified partition; it is not an additional equilibrium-classification regime.

## 3. Literal Hotelling claims

Assume the source full-coverage linear Hotelling environment, \(\tau>0\), pure pricing, and the literal price strategy domain as reconstructed from the published model.

Let \(d=c_B-c_A\).

| ID | Formal scope | Equilibrium-set quantifier | Maximum defensible wording | Prohibited stronger wording |
|---|---|---|---|---|
| H1-a | \(|d|<3\tau\) | unique **pure-price** equilibrium | “unique pure-price equilibrium” | “unique equilibrium” if mixed prices are included |
| H1-b | \(|d|=3\tau\) | unique pure boundary equilibrium | exact boundary wording | treating equality as interior |
| H1-c | \(|d|>3\tau\) | complete continuum of pure corner price equilibria | “literal pure-price continuation is multiple” | “the source model has no equilibrium” |
| H1-d | fixed corner sourcing history | welfare invariant across the pure price continuum because allocation is identical and prices are transfers | all certified pure corner price equilibria at that fixed history | “two-stage welfare is selection-invariant” |

The literal Stage-I reduced payoff is not single-valued off path once corner price multiplicity is reached.

## 4. Auxiliary no-loss Hotelling claims

The following claims are **not source-game theorems**. They are conditional on the explicit auxiliary strategy restriction

\[
p_j\ge c_j.
\]

| ID | Formal scope | Equilibrium-set quantifier | Maximum defensible wording | Prohibited stronger wording |
|---|---|---|---|---|
| H2 | Every \(p<c\) is weakly dominated by \(p=c\) | pointwise against every rival pure price | exact dominance fact | “\(p=c\) is undominated” |
| H2b | For every \(\varepsilon>0\), \(p=c+\varepsilon\) weakly dominates \(p=c\) | pointwise against every rival pure price | exact dominance fact | “deleting weakly dominated strategies selects \(p=c\)” |
| H3-NL | With \(p_j\ge c_j\), the price subgame has a unique **pure** equilibrium for every cost gap | unique pure within the auxiliary game | “unique pure price continuation under the no-loss restriction” | “unique equilibrium” or “refinement-selected equilibrium” |
| H4-NL | The finite-candidate formula exhausts pure Stage-I unilateral deviations under the no-loss game | complete pure BR | exact conditional wording | literal-source BR claim |
| H5-NL | Under source SOC, the interior symmetric candidate fails iff \(27\tau/2<H^2n<18\tau\) and \(\phi>x_-\) | survival/failure of the stated symmetric pure candidate only | “the published symmetric candidate fails on this exact region under \(p\ge c\)” | “Proposition 6 is false in every literal-source SPNE” |
| H5-boundary | At \(\phi=x_-\), the nonlocal deviation ties rather than strictly improves | candidate remains a best response; BR may be non-singleton | exact tie wording | treating weak inequality as failure |
| H6-NL | \(H=n=1,\tau=1/15,\phi=1\) gives exact gain \(1/90\) from \(1/2\) against \(1/6\) | one exact conditional counterexample | “exact counterexample under the no-loss game” | selection-free literal-game counterexample |

No trembling-hand, proper-equilibrium, admissibility, iterated-dominance, or mixed-price uniqueness claim is licensed.

## 5. Welfare and benchmark scope

| Claim | Quantifier / selection status | Correct benchmark label | Maximum wording |
|---|---|---|---|
| Cournot welfare identity | all feasible source profiles | accounting identity | exact within source model |
| Cournot common-sourcing benchmark C-R | symmetric common sourcing, decentralized Cournot output | **restricted-instrument equilibrium-welfare optimum** | never “first best” |
| Cournot welfare across multiple Stage-I equilibria | not invariant | none | **selection-dependent** |
| \(\rho=2/3\) welfare | varies across equilibrium continuum | none | no selection-free ranking |
| Full Cournot planner FB-C | chooses all \(q_j,i_j\) | **first best within source reduced technology** | full choice-set label required |
| Hotelling full planner FB-H | chooses allocation and sourcing under full coverage/fixed endpoints | **first best within source full-coverage technology** | qualification required |
| Hotelling fixed-sourcing share optimum | sourcing fixed | **fixed-sourcing allocation optimum** | not first best |
| Hotelling 50–50 sourcing comparison | allocation fixed at \(1/2\) | **fixed-allocation sourcing benchmark** | not first best |
| Literal Hotelling corner-price welfare | invariant only at fixed sourcing history | none | do not extend through Stage-I selection |

## 6. Baseline / robustness / generality classification

### Baseline source functional-form theorems

C1–C8 and H1 are exact results in the source's linear/quadratic environments.

### Conditional robustness theorem

H3-NL–H6-NL are exact results in the auxiliary no-loss price game.

### Restricted-class mechanism support only

For linear Cournot with a differentiable decreasing cost function \(c(i)\), the rival-exit boundary

\[
c(x)=2c(y)-a
\]

has local slope

\[
\frac{dx}{dy}=\frac{2c'(y)}{c'(x)}>0
\]

where the implicit derivatives exist.

This supports the exit-threshold intuition only. It is **not** a general theorem that the global best response contains an increasing segment or that asymmetric equilibria exist.

### No intended broad general theorem

No headline result is claimed for arbitrary convex monitoring costs, arbitrary decreasing cost functions, nonlinear demand, incomplete Hotelling coverage, or mixed strategies.

## 7. Function-class adversarial audit

No manuscript headline theorem currently quantifies over a broad function class. Therefore no broad class survives by default.

Counterexample pressure nevertheless confirms the scope discipline:

- sufficiently strong alternative monitoring curvature can make exit-inducing sourcing too costly to be globally optimal even though the rival-exit boundary still exists;
- nonlinear demand changes the algebra behind the exact \(N\)-comparative static and \(\rho\)-thresholds;
- incomplete Hotelling coverage adds an outside-option boundary absent from H1/H5-NL.

Accordingly, the exact source results remain **BASELINE FUNCTIONAL FORM**, and the wider active-set story remains interpretation unless separately proved.

## 8. Required Stage-10 wording controls

Use:

- “unique symmetric pure Stage-I action,” not “unique equilibrium,” for general \(N\);
- “complete pure Stage-I equilibrium correspondence of the source duopoly,” not “complete equilibrium correspondence”;
- “unique pure-price equilibrium,” not unqualified “unique price equilibrium,” where mixed-price objects are not certified;
- “under the explicit no-loss restriction \(p\ge c\),” before every H3-NL–H6-NL claim;
- “weakly decreasing across admissible integer market sizes satisfying the source restrictions” for the economic comparative static; a derivative may be reported only as the continuous-extension calculation;
- “selection-dependent” for global welfare in the Cournot multiplicity regions.

Do not use:

- “generic”;
- “for all equilibria” unless explicitly certified;
- “refinement-selected” for the no-loss game;
- “first best” for C-R or fixed-allocation Hotelling benchmarks;
- “Proposition 6 is globally false” without the no-loss conditional clause.

## 9. Evidence links

- Stage-4A certificates: \`audit/stage04a_theorem_certificates.md\`
- clean-room derivation: \`audit/stage04a_cleanroom_derivation.md\`
- Stage-6 novelty control: \`audit/STAGE_06_NOVELTY_REKILL.md\`
- Stage-7 welfare/selection: \`audit/STAGE_07_WELFARE_GENERALITY.md\`
- benchmark register: \`audit/stage07_welfare_benchmarks.md\`
- targeted Lean source: \`ShyStenbackaFormal/Stage075A.lean\`

Formal-verification state: **FORMAL VERIFICATION PASS**. See `audit/stage075a_formal_verification_certificate.md`.
