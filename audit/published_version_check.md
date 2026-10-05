# Published-Version Verification

Status: **PASS — SOURCE IDENTITY FROZEN**

Audit date: 2026-09-19.

## Bibliographic identity

- Authors: Oz Shy and Rune Stenbacka
- Year: 2005
- Title: **Partial outsourcing, monitoring cost, and market structure**
- Journal: *Canadian Journal of Economics / Revue canadienne d'économique*
- Volume / issue: **38(4)**
- Pages: **1173–1190**
- First published online: **27 October 2005**
- Issue date: **November 2005**
- DOI: **10.1111/j.0008-4085.2005.00320.x**
- Publisher landing page: https://doi.org/10.1111/j.0008-4085.2005.00320.x
- JSTOR stable record: https://www.jstor.org/stable/3696079

## Evidence layers

### A. Fresh publisher / bibliographic identity check

Wiley's current article page and volume/issue contents were rechecked on 2026-09-19. They identify the title, authors, volume, issue, pages, DOI, and first-publication date above. JSTOR independently places the article at pp. 1173–1190 in volume 38(4).

### B. Equation/proposition transcription

A publicly accessible full-text transcription was cross-checked for the source model and equation/proposition numbering. It contains the published sequence through equations (1)–(26), including:

- equation (5): marginal cost under constant outsourcing advantage;
- equation (6): monitoring cost (i_j^2);
- equations (8)–(15): Cournot restrictions, solution, comparative static, and duopoly best response;
- Proposition 3, Corollary 4, Proposition 5;
- equations (16)–(26): Hotelling demand, prices, Stage-I payoff, best response, SOC, symmetric solution, and fraction;
- Proposition 6.

### C. Archived Version-of-Record check

The predecessor audit repository `ryotamatsuki/ozshypapers` records a direct check of the final typeset published article and specifically confirms that equations (13), (14), Proposition 3, and equations (17)–(26) occur in the Version of Record in the audited form.

This project treats that record as provenance evidence, while keeping the new mathematical audit independent of the predecessor's generalized notation.

## Important source-model correction to predecessor audit notation

The published monitoring-cost specification is

[
M(i_j)=i_j^2.
]

The paper does **not** contain a free monitoring-cost coefficient (eta). Earlier scratch/generalized audit work sometimes used (eta i_j^2). That generalization is not part of the frozen source model and must not enter a source-faithful correction proof.

## Erratum / corrigendum check

Targeted current searches on 2026-09-19 for the article title/DOI together with `erratum`, `corrigendum`, `correction`, and `comment` did not surface a publisher-issued correction.

This is only a source-version check. It is **not** a Stage-2 novelty finding and is not evidence that no prior scholarly discussion exists.

## Completed checks

- [x] Final published bibliographic identity fixed.
- [x] Exact title, journal, volume, issue, pages, DOI, and publication date recorded.
- [x] Relevant equation numbering recorded and cross-checked.
- [x] Proposition 3, Corollary 4, Proposition 5, and Proposition 6 identified.
- [x] Outsourcing strategy domain (0le i_jlephi) recovered from (I=[0,phi]).
- [x] Cournot and Hotelling product-market objects needed for Stage 1 reconstructed.
- [x] Current targeted erratum/corrigendum search performed.
- [x] No publisher PDF committed to the repository.

## Version-control rule

No downstream audit file may silently replace a published expression with a repaired one. Source expressions, local-domain interpretations, and corrected/global results must be labeled separately.


## Stage-4 Hotelling strategy-space recheck

The final published Hotelling section defines \(p_A,p_B\), the indifferent consumer, and the price maximization problem but does not state a formal lower price bound \(p_j\ge c_j\), a no-loss-pricing convention, or a corner-equilibrium refinement.

Appendix C explicitly derives prices under the qualification “as long as both firms produce.” The regular formula therefore cannot itself be read as a complete corner-price strategy-domain statement.

This source fact is distinct from the later Stage-4 theorem that \(p_j<c_j\) is weakly dominated by \(p_j=c_j\).
