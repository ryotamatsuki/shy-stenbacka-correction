# Independent-Audit Repair Finding Ledger

Status: **CLOSED — REPAIRED AND RECERTIFIED**  
Date: **2026-09-20**  
Audit checkpoint: `5bdf156347da4267167513d96b5ef53456cd3f9a`  
Repair branch: `audit/full-equilibrium-correspondence`

This ledger records the external clean-room findings received after Stage 13 and the project's independent disposition. Historical PASS records are preserved; corrections are recorded by amendment/supersession rather than deletion.

| ID | Audit claim | Independent recheck | Affected theorem/files | Earliest affected gate | Status |
|---|---|---|---|---|---|
| F01 | Proposition 2 over-quantifies feasibility of the positive-slope rival-exit BR segment | **CONFIRMED.** At ((\rho,\delta,\phi)=(3/5,1,1/10)), (R(y)=1+2y>\phi) for all feasible (y), hence (B_\phi\equiv\phi). The source-feasible primitive witness (H=\gamma=1,b=3/5,\phi=1/10,a=221/200) gives (D=1) and satisfies the source SOC. Positive-length feasibility requires (phi>\delta) for (1/2\le\rho<2/3), and (phi>M=\delta/(4\rho-1)) for (4/9<\rho<1/2). | C7; §3; Stage-4A/8 records | **Stage 4A C7 certification** (Stage-7.5A claim ledger already had the correct “whenever feasible” qualifier) | RESOLVED |
| F02 | Proposition 3's “exactly three” proof states completeness without supplying exclusion logic | **CONFIRMED AS PROOF-CERTIFICATE REGRESSION, NOT THEOREM FALSIFICATION.** Independent analytic reconstruction supports all five cases. Completeness can be proved using (R(z)>z) for (z<s), (R(s)=s), (R(z)<z) for (z>s), followed by a complete (x_H>x_L) split at (x_H<\delta) versus (x_H\ge\delta). | C8; §4; Appendix; Stage-4A proof certificate; Stage 11 | **Stage 4A C8 proof completeness** | RESOLVED |
| F03 | Multiplicity is incorrectly attributed as requiring downstream participation change/exit | **CONFIRMED.** At ((\rho,\delta,\phi)=(3/5,1,3/4)), every feasible history is both-active, yet the pure equilibria are ((10/17,10/17),(3/4,5/14),(5/14,3/4)). Exit generates the positive-slope branch but is not necessary for multiplicity. | Stage-4 mechanism interpretation; §1/§4/related literature/conclusion; Stage 6/11 interpretation | **Stage 4 interpretation / Stage 6 absorption cross-check / Stage 11** | RESOLVED |
| F04 | Lemma 1 omits existence/coercivity step | **CONFIRMED MINOR.** Strict concavity gives at most one maximizer; coercivity of the quadratic potential supplies existence on the noncompact orthant. | C1 Appendix | Stage 13 exposition, with Stage-4A proof record cross-check | RESOLVED |
| F05 | Lemma 2 under-explains global active-set transitions and simultaneous exits | **CONFIRMED MINOR.** Conclusion survives; transition ordering and one-sided derivative argument must be made explicit. | C2 Appendix | Stage 13 exposition, Stage-4A proof record cross-check | RESOLVED |
| F06 | Literal Hotelling proof omits explicit global BR correspondence and exclusion logic | **CONFIRMED MINOR.** Pure-price correspondence survives under the maintained clipped full-coverage game. | H1 §5/Appendix | Stage 13 exposition / Stage 11 | RESOLVED |
| F07 | No-loss theorem under-specifies (x_-) domain and iff branch logic | **CONFIRMED MINOR.** The failure region and (1/90) witness survive; proof/domain wording needs repair. | H5-NL §5/Appendix | Stage 13 exposition / Stage 11 | RESOLVED |
| F08 | (ho=2/3,phi=\delta/2) called a continuum although the set degenerates to one point | **CONFIRMED MINOR.** Set formula is correct; label is not. | C8 table/welfare prose | Stage 13 | RESOLVED |
| F09 | Reduced Cournot welfare notation is not explicitly defined | **CONFIRMED MINOR.** Welfare formulas survive. | Welfare section | Stage 13 | RESOLVED |
| F10 | Conclusion can conflate the sign correction with active-set/corner corrections | **CONFIRMED MINOR.** These are logically distinct corrections. | Conclusion | Stage 13 | RESOLVED |
| F11 | Bibliography accent/source-style records need reconciliation | **CONFIRMED FOR RECORD/SOURCE CONSISTENCY CHECK; exact journal style to be verified live.** | references.bib; Stage-13 records | Stage 13 | RESOLVED |
| LIT | Several literature attributions were not independently verified in the external audit | **TO BE VERIFIED AGAINST PRIMARY/IDENTIFIABLE SOURCES; lack of access will remain UNVERIFIED rather than PASS.** | Related literature; Stage 6/11 | Stage 6/11 | RESOLVED |

## Reopening route

The external recommendation to reopen Stage 7.5A wholesale is not adopted mechanically. The existing Stage-7.5A claim-scope ledger already states C7 with the qualifier “whenever the rival-exit piece is feasible.” The certification regression arose because the Stage-4A/Stage-8/manuscript chain did not preserve that qualifier consistently.

Repair route:

1. partially reopen Stage 4A for C7 quantifiers and C8 proof completeness;
2. reconcile Stage 7.5A/formal-fidelity records with the repaired C7 scope without widening formal coverage;
3. amend Stage 8 theory freeze;
4. re-check Stage 6 theorem absorption only where the former exit/multiplicity interpretation mattered;
5. reopen/re-run Stage 11 on proof completeness, mechanism interpretation, boundaries, literature scope, and formal-claim fidelity;
6. repair/reintegrate Stage 13 and rebuild;
7. stop before Stage 14.

No finding is considered resolved until the corresponding code/proof/manuscript/audit evidence is committed and green.


## Closure evidence

All confirmed findings are resolved without deleting historical audit provenance.

- Stage 4A C7/C8 re-certification: \`audit/STAGE_04A_INDEPENDENT_AUDIT_RECERTIFICATION_2026-09-20.md\`.
- Stage 7.5A quantifier/formal reconciliation: \`audit/STAGE_075A_INDEPENDENT_AUDIT_RECONCILIATION_2026-09-20.md\`.
- Stage 8 amended freeze: \`audit/STAGE_08_INDEPENDENT_AUDIT_AMENDMENT_2026-09-20.md\`.
- Stage 6 absorption recheck: \`audit/STAGE_06_INDEPENDENT_AUDIT_RECHECK_2026-09-20.md\`.
- Stage 11 re-certification: \`audit/STAGE_11_RECERTIFICATION_2026-09-20.md\`.
- Stage 13 reintegration: \`audit/STAGE_13_INDEPENDENT_AUDIT_REINTEGRATION_2026-09-20.md\`.
- Literature source ledger: \`audit/LITERATURE_CLAIM_RECHECK_2026-09-20.md\`.
- Independent primitive-level verifier: \`code/independent_audit_repair_verify.py\`.

Latest-head evidence before closure-record-only commits:

- branch head: \`0bd82c56703655f0a72784b4ef8f964520875cdc\`;
- Python verification PR run \`35477505973\`: **success**;
- canonical + flat RIO manuscript build PR run \`35477505977\`: **success**;
- hyperlink-clean PDF build push run \`35477441567\`: **success**;
- final canonical PDF visually inspected page by page after rendering all **22 pages**; no clipping, overlap, broken glyphs, missing figure/table, or visible hyperlink boxes were found.

The live 2026-09-20 source recheck could not freshly reopen the Wiley Version-of-Record body for Shy--Stenbacka (2005). This is not treated as a new full-text PASS. Equation/proposition-number fidelity remains supported by the repository's prior direct-VOR audit, while the present repair independently re-derives the mathematics from the source primitives. This evidence limitation is therefore **resolved by explicit provenance**, not hidden.

No Stage-14 work was performed.
