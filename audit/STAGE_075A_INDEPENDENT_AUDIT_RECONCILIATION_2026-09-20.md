# Stage 7.5A — Independent-Audit Quantifier / Formal-Fidelity Reconciliation

Date: **2026-09-20**

The independent audit correctly found an over-quantified C7 statement downstream, but the canonical Stage-7.5A claim-scope ledger itself already used the limiting phrase:

> “whenever the rival-exit piece is feasible.”

Accordingly, Stage 7.5A is **not** treated as the origin of the C7 regression.

## C7 reconciliation

The repaired exact source-domain statement is stronger in precision but narrower in scope:

- the uncapped (R) contains (U(y)=delta+2y) for (4/9<ho<2/3);
- after (B_phi=min{phi,R}), a positive-length increasing segment survives iff
  (phi>delta) for (1/2leho<2/3), or
  (phi>delta/(4ho-1)) for (4/9<ho<1/2).

This is consistent with the Stage-7.5A phrase “when feasible.”

## Formal-fidelity reconciliation

The existing formal map already states:

- `C7_exit_branch_slope_positive` certifies only positivity of the slope (2);
- C7 join theorems certify algebraic branch joins;
- global optimality and feasibility of the branch are **outside Lean**;
- complete C8 equilibrium construction is **outside Lean**.

No Lean source, theorem statement, hypothesis, toolchain, or dependency changed.

Certified blobs remain:

- `ShyStenbackaFormal/Stage075A.lean`: `a634b04eb2ec13a632f10928974f8eab96d1d05c`;
- `ShyStenbackaFormal.lean`: `e4a44acff03704dbf427b792d9528cf9a0a3c602`;
- `lakefile.toml`: `6669c6b90caf3c05912556109ead89c33400fe6c`;
- `lean-toolchain`: `7aca1d8a939cc24c413eddd793671cdce7070b74`;
- Lean workflow: `886c142e65d35d746cb1803e266aa0d687f7514e`.

The controlling prior clean formal build remains GitHub Actions run `35439005968`.

## Verdict

[
oxed{	extbf{STAGE 7.5A QUANTIFIER / FORMAL-FIDELITY RECHECK — PASS}}
]

No formal-certificate rollback is triggered.  The formal coverage remains a targeted proof-critical core, not whole-model verification.
