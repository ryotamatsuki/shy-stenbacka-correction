# Formal-Verification Fidelity Recheck after Independent Audit

Date: **2026-09-20**  
Formal environment: Lean 4.19.0, pinned mathlib as in the existing Stage-7.5A certificate.

## Status

[
oxed{	extbf{FORMAL CERTIFICATE REMAINS VALID WITH NARROW INTERPRETATION}}
]

## 1. Source immutability

The proof-assistant inputs remain byte-identical to the previously certified Stage-7.5A state:

- `ShyStenbackaFormal/Stage075A.lean`: `a634b04eb2ec13a632f10928974f8eab96d1d05c`
- `ShyStenbackaFormal.lean`: `e4a44acff03704dbf427b792d9528cf9a0a3c602`
- `lakefile.toml`: `6669c6b90caf3c05912556109ead89c33400fe6c`
- `lean-toolchain`: `7aca1d8a939cc24c413eddd793671cdce7070b74`
- Lean workflow: `886c142e65d35d746cb1803e266aa0d687f7514e`

No Lean theorem, assumption, toolchain pin, or dependency was changed by this repair.

## 2. C7 fidelity

The existing formal layer proves proof-critical components of C7, including the relevant branch-join identities and the positive slope (2>0).

It does **not** prove that the source cap leaves a positive-length feasible rival-exit interval for every (phi).

Therefore the old economic inference

[
4/9<ho<2/3
Rightarrow
	ext{feasible positive-length capped C7 segment}
]

was never kernel-certified.

The repaired manuscript now makes cap feasibility an analytic hypothesis/conclusion outside Lean:

[
phi>delta
quad(1/2leho<2/3),
]
or
[
phi>M
quad(4/9<ho<1/2).
]

This restores paper ↔ formal statement fidelity.

## 3. C8 fidelity

The complete pure Stage-I source-duopoly correspondence remains analytically certified, not fully Lean-mechanized. The independent audit did not discover a false C8 case; it discovered an insufficiently recorded analytic completeness proof.

The expanded appendix and Stage-4A recertification now supply that proof. No claim is made that Lean verifies the complete branch-exclusion argument.

## 4. Stage-7.5A claim-scope ledger

The existing claim-scope ledger already states C7 as:

> whenever the rival-exit piece is feasible, a pure-BR segment equals (U(y)=delta+2y).

That scope is retained. Stage 7.5A therefore does not require a theorem-scope rollback; its correct qualifier is now propagated consistently into the amended Stage-8 freeze and manuscript.

## 5. Build status

Because the formal source is unchanged, the historical Stage-7.5A kernel certificate remains the controlling formal proof artifact. The normal repository formal build remains part of the overall verification gate; a new Lean theorem was not added solely to encode the newly explicit cap-feasibility condition.

## Verdict

[
oxed{	extbf{FORMAL SCOPE FIDELITY — PASS}}
]

The formal layer remains targeted and must not be described as verification of the full model, C7 cap feasibility, or the complete C8 correspondence.
