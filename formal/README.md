# Formal Verification Index

Canonical formal source remains at repository root for Lake compatibility:

- `ShyStenbackaFormal/Stage075A.lean`
- `ShyStenbackaFormal.lean`
- `lakefile.toml`
- `lean-toolchain`

Pinned environment:

- Lean 4.19.0
- mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`

Canonical certificate and statement map:

- `audit/stage075a_formal_verification_certificate.md`
- `audit/stage075a_formal_statement_fidelity.md`

Build:

```bash
lake update
lake exe cache get
lake build
```

The formal scope is **PROOF-CRITICAL CORE** only. Do not describe this directory as a formalization of the complete Shy–Stenbacka game.
