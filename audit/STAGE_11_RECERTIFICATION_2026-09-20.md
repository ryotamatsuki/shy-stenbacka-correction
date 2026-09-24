# Stage 11 — Independent-Audit Reopening and Re-certification

Date: **2026-09-20**  
Original Stage-11 closure: `fe2d03f42c4ee89ef831cffc758541e30dde435a`  
Trigger manuscript checkpoint: `5bdf156347da4267167513d96b5ef53456cd3f9a`

## 1. Certification regression

The external clean-room audit found failures that the original Stage-11 attack should have surfaced:

- **C7 quantifier inflation:** cap feasibility of the positive-slope constrained BR segment was not preserved;
- **C8 proof-record incompleteness:** the theorem statement was correct, but the published/audit proof did not explicitly eliminate all other branch combinations;
- **mechanism inflation:** downstream exit was described too strongly as the source/necessary cause of multiplicity.

Accordingly, the historical Stage-11 statement

[
	ext{NO CERTIFICATION REGRESSION}
]

is preserved only as provenance and is **superseded**.

Current classification:

[
oxed{	extbf{CERTIFICATION REGRESSION — FOUND AND REPAIRED}}
]

The earliest theorem-certification repair was Stage 4A for C7/C8.  The Stage-7.5A claim-scope ledger did not contain the C7 cap error; it already used the qualifier “whenever the rival-exit piece is feasible.”

## 2. Reopened mathematical attacks

### C7

The hostile attack now distinguishes:

[
R(y)
quad	ext{from}quad
B_phi(y)=min{phi,R(y)}.
]

A positive-length constrained (+2) segment survives iff

[
phi>delta
quad (1/2leho<2/3),
]

or

[
phi>rac{delta}{4ho-1}
quad (4/9<ho<1/2).
]

The permanent small-cap counterexample is ((3/5,1,1/10)); the large-cap counterexample to global strategic substitutability remains ((3/5,1,2)).

### C8

The complete five-case pure Stage-I correspondence was attacked again.  The Appendix now supplies:

- contraction for (ho>2/3);
- the exact clipped line-response analysis for (ho=2/3);
- the crossing property around (s);
- a complete ordered-asymmetric split at (x_H<delta) versus (x_Hgedelta);
- explicit elimination of active-active, uncapped exit, monopoly, and zero-branch alternatives where applicable;
- equality cases (phi=s,phi=delta/2,phi=delta,phi=R(0)).

No omitted pure equilibrium was found.  This is an analytic proof; numerical regressions are not used as completeness evidence.

### Multiplicity mechanism

The permanent all-active witness

[
(ho,delta,phi)=left(rac35,1,rac34ight)
]

has the three pure equilibria

[
left(rac{10}{17},rac{10}{17}ight),
quad
left(rac34,rac5{14}ight),
quad
left(rac5{14},rac34ight),
]

while both downstream firms remain active throughout the feasible sourcing box.

Therefore:

- exit generates the positive-slope C7 branch;
- exit is not necessary for C8 multiplicity;
- own-payoff strict concavity does not imply game-level equilibrium uniqueness.

## 3. Supporting proof attacks

Reopened review also confirms/repairs:

- Stage-II Cournot existence via coercivity before uniqueness via strict concavity;
- global sourcing concavity across finite active-set transitions and simultaneous rival exits;
- literal full-coverage Hotelling global pure-price BR and complete mutual-BR set;
- weak-dominance statements directly from demand/payoff definitions;
- no-loss (x_-) real domain, branch location, necessity/sufficiency, strict-gain and tie boundaries;
- reduced welfare notation and degenerate knife-edge treatment.

## 4. Literature / known-model attack

The literature claims implicated by the external audit were rechecked and recorded in:

- `audit/LITERATURE_CLAIM_RECHECK_2026-09-20.md`;
- `audit/STAGE_06_INDEPENDENT_AUDIT_RECHECK_2026-09-20.md`;
- amended `audit/STAGE_11_KNOWN_MODEL_ATTACK.md`.

The all-active multiplicity result does not make C8 a direct specialization of the strongest cited symmetry-breaking theorem.  The source-specific novelty boundary remains unchanged.

The live 2026-09-20 publisher check for Shy--Stenbacka verified article identity and headline abstract claims but did not yield fresh publisher-body access; equation/proposition numbering therefore remains supported by the repository's prior direct Version-of-Record audit rather than being mislabeled as a fresh full-text check.

## 5. Formal-verification fidelity

No Lean source or formal hypothesis changed.

The existing statement-fidelity map already marks the following as outside Lean:

- global optimality / feasibility of the C7 branch;
- complete C8 equilibrium construction;
- literal Hotelling global continuation;
- the full no-loss iff region.

Thus the C7 correction narrows the interpretation of the formal certificate but does not falsify any kernel-checked theorem.

Formal coverage remains:

[
oxed{	extbf{PROOF-CRITICAL CORE ONLY}}
]

## 6. Verification artifacts

Independent repair verifier:

`code/independent_audit_repair_verify.py`.

Stage-11 hostile-referee lint now requires the corrected C7 feasibility language and the explicit statement that exit is not necessary for multiplicity, and rejects the prior over-quantified wording.

## 7. Re-certification verdict

Subject to the final integrated branch build/verification recorded at Stage 13, no FATAL or unresolved MAJOR mathematical finding remains.

[
oxed{	extbf{STAGE 11 — RECERTIFIED PASS}}
]

[
oxed{	extbf{ROBUSTNESS / REFEREE ATTACK GATE RECLOSED}}
]

Historical false-negative audit conclusions remain visible in the original report with a reopening notice.
