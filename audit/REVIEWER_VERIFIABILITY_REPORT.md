# Reviewer-Verifiability Report

Status: **PASS — REVIEWER VERIFIABILITY**

Date: 2026-10-05

Workflow authority:
- `research-paper-workflow` current main `7d754032f292205264bd404116b561366836c7fd`;
- prospective v2.7 refinement;
- `checklists/REVIEWER_VERIFIABILITY_CHECKLIST.md`.

Review actor: **AI**. This is an AI-side clean-room exposition audit, not external-human peer review.

## Review package and method

The reconstruction pass used the manuscript-facing package as the primary evidence:
- `paper/manuscript.tex`;
- all `paper/sections/*.tex`;
- especially `paper/sections/appendix.tex`.

Production derivation/code was not needed to infer the core proof chains. Audit/formal records were consulted afterward to verify that delegated computation/formal claims were bounded correctly.

Passing standard:
> a competent IO-theory referee can identify each proof object, follow the non-routine bridges, and see why the result follows without reverse-engineering production code.

## Reconstruction results

### A. Global Cournot continuation

Reconstructed chain:

source costs and nonnegative quantities
→ exact potential
→ negative-definite Hessian plus coercivity
→ unique potential maximizer
→ KKT = quantity Nash conditions
→ active-set price `p_S`
→ active/inactive quantity formula.

Result: **PASS**. No missing conceptual bridge.

### B. Global own-payoff concavity

Reconstructed chain:

fixed rival sourcing
→ smooth active-set branch
→ `dz_j/dx=Hm/(m+1)`
→ negative branch curvature under source SOC
→ own-entry derivative continuity at zero margin
→ rival exits create only downward marginal-benefit jumps
→ globally decreasing one-sided derivative
→ global strict concavity.

Result: **PASS**. The Appendix supplies the critical global-joining argument rather than relying on branchwise SOCs alone.

### C. Corrected symmetric sourcing action / Proposition 3

Reconstructed chain:

symmetric output formula
→ unilateral sourcing derivative at symmetry
→ stationary root
→ source SOC implies positive denominator
→ global concavity makes KKT sufficient
→ cap projection
→ displayed derivative of the continuous extension
→ admissible-integer economic comparison.

Result: **PASS**. Local/global and continuous/integer distinctions are explicit.

### D. Proposition 5 / global best response

Reconstructed chain:

three exact reduced-payoff regimes
→ stationary/boundary objects `A(y), U(y), M`
→ join points `y_A,y_M`
→ global branch sequence using one-sided derivative signs + concavity
→ source cap
→ exact conditions for survival of a nondegenerate `U(y)=delta+2y` segment
→ positive slope `+2`
→ existential falsification of unqualified global strategic substitutability.

Result: **PASS**. The cap qualifier that caused the historical certification regression is now visible in both theorem and proof.

### E. Complete pure Stage-I source-duopoly correspondence

Reconstructed chain:

mutual fixed-point equations
→ `rho>2/3`: global contraction
→ `rho=2/3`: exact clipped affine response and continuum
→ `4/9<rho<2/3`: crossing property around `s`
→ unique capped symmetric case when `phi<=s`
→ exhaustive asymmetric split `x_H<delta` versus `x_H>=delta`
→ branch exclusion
→ exactly one ordered asymmetric pair plus its mirror.

Result: **PASS**. The proof establishes completeness of the **pure Stage-I** set rather than relying on Figure 1.

### F. Literal Hotelling continuation

Reconstructed chain:

clipped full-coverage demand
→ exact own-price best-response correspondence
→ solve mutual best responses
→ unique interior/boundary cases for `|d|<=3tau`
→ continuum interval for `|d|>3tau`
→ low-cost profit varies with the selected zero-demand rival price
→ Stage-I continuation payoff is set-valued.

Result: **PASS after one presentation repair**.

Defect found during this retrofit:
- Appendix contained `p_B=z,qquad p_A=...`.
- Repaired to `p_B=z,\qquad p_A=...`.
- This was typographical/presentation-only and did not alter the theorem.

### G. Weak-dominance facts and no-loss game

Reconstructed chain:

below-cost operating payoff comparison
→ `p=c` weakly dominates each fixed `p<c`
→ any fixed `c+epsilon` also weakly dominates `c`
→ no “undominated-price refinement” claim
→ impose `p>=c` only as auxiliary strategy restriction
→ restricted continuation unique
→ derive `Delta(x)`
→ vertex and exact roots
→ cap-feasibility cases
→ exact failure region.

Result: **PASS**.

### H. Formal/computational delegation

The previous manuscript statement that formal verification covered “selected proof-critical statements” was correct but too opaque for the prospective v2.7 standard.

Repair:
- `paper/sections/07_reproducibility.tex` now names the classes of objects Lean certifies: the competition-sign core, BR branch-join/slope identities, selected no-loss deviation-gain identities, and a welfare inequality;
- it explicitly states that global continuation construction, the complete pure correspondence, and economic interpretation remain analytic.

Result: **PASS after repair**.

## Gap classification

| Finding | Classification | Action |
|---|---|---|
| malformed `qquad` in Hotelling proof | ROUTINE / PRESENTATION | fixed |
| formal-verification description too generic for v2.7 | BRIDGE NEEDED | repaired in Statements and Declarations |
| missing v2.7 map/report | GOVERNANCE / EVIDENCE | added |
| substantive unproved theorem discovered | none | no rollback |

## Compression-without-damage verdict

The v2.5 streamlining did not remove any proof-critical bridge identified by the current v2.7 map. Figure 1 and Table 1 remain useful exposition devices, but neither substitutes for the analytic proof.

## Final verdict

**PASS — REVIEWER VERIFIABILITY.**

A specialist referee can reconstruct every headline proof chain from the manuscript-facing package. No material result depends on an undefined object, an opaque solver output, or a formal certificate whose economic implication is unstated.

This pass is not an EXTERNAL HUMAN review and does not alter the theory freeze.
