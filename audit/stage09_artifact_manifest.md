# Stage 9 Reproducibility Artifact Manifest

Status: **CANONICAL MANIFEST**

Stage-8 theory input checkpoint:

`2fbcf47ff18ea3650d307d90cbdeab78ddb63256`

Workflow authority:

- `research-paper-workflow` v2.2
- commit `42574d6c5931275ccff3ef7e8b4acc188077332a`

## Frozen theory / certification blobs

| Artifact | Blob SHA |
|---|---|
| `audit/STAGE_08_CANONICAL_THEORY_FREEZE.md` | `5617ad849a57c4187abca564ace39b3762a19e2e` |
| `audit/stage04a_theorem_certificates.md` | `48dc50daa3d240729e083c90999480013e6dcfa7` |
| `audit/stage075a_claim_scope_ledger.md` | `4532283833769b815e1fb3a8af660ded8b61b3af` |
| `audit/stage075a_formal_verification_certificate.md` | `e3fcce319bb13261a9c8d6f2b1f9ccd83555fe98` |
| `audit/stage075a_formal_statement_fidelity.md` | `8e74e2019a90b6ebd8e9ca18350e172d381798ea` |

## Formal-verification blobs

| Artifact | Blob SHA |
|---|---|
| `ShyStenbackaFormal/Stage075A.lean` | `a634b04eb2ec13a632f10928974f8eab96d1d05c` |
| `ShyStenbackaFormal.lean` | `e4a44acff03704dbf427b792d9528cf9a0a3c602` |
| `lakefile.toml` | `6669c6b90caf3c05912556109ead89c33400fe6c` |
| `lean-toolchain` | `7aca1d8a939cc24c413eddd793671cdce7070b74` |
| `.github/workflows/lean.yml` | `886c142e65d35d746cb1803e266aa0d687f7514e` |

Certified Lean green run:

- run `35439005968`
- formal-source commit `8c575f99daecacd85077ee2db3568dbd362c2004`

The formal source and toolchain blobs remain unchanged from that green certificate.

## Python reproducibility blobs

| Artifact | Blob SHA |
|---|---|
| `requirements.txt` | `1ca5fd06160543f8bd736f1b51db6f42372c66f4` |
| `.python-version` | `e4fba2183587225f216eeada4c78dfab6b2e65f5` |
| `Makefile` | `1f7bdf9df8fe70b3147ddf7e38618a3785d5ed4a` |
| `.github/workflows/python-verification.yml` | `50294fedc503eef1a31714034cb72dff8d63f4ae` |
| `code/stage01_verify.py` | `36bc514c3fd8e453793cf75cf8777892ed321c73` |
| `code/stage04_verify.py` | `fc04e42a4050fdeeb8cc0d655720868a80a2ff1e` |
| `code/stage04_hotelling_refinement_verify.py` | `f5953fa8c5a39ac16e3d611ae7daabc22a6413e8` |
| `code/stage04a_independent_verify.py` | `cec03aecff3645b8f41d486b9f3ecdc39cef64d4` |
| `code/stage07_welfare_verify.py` | `031d2bd968140c33af36ca66eafc59ae25ea8647` |
| `code/stage075a_scope_counterexamples.py` | `000f746e252640ba88cff37cd9ad35a73a392ba6` |

Stage-9 Python CI evidence:

- run `35442666402`
- conclusion: **success**
- head commit: `b4e8e2d807b6342d5cdd73286afbd8e2baecfadb`

The run uses the exact pinned Python dependency and the full `make verify-python` suite.

## Manuscript / bibliography

The Stage-9 manuscript was structurally modularized without adding substantive theory.

Canonical entry:

- `paper/manuscript.tex`

Bibliography:

- `paper/references.bib` — frozen pre-Stage-10 blob `cf94d5e1b8eac1e70e0123894d21276369f5d089`

Section layout:

- `paper/sections/01_introduction.tex`
- `paper/sections/02_model.tex`
- `paper/sections/03_best_responses.tex`
- `paper/sections/04_equilibrium.tex`
- `paper/sections/05_implications.tex`
- `paper/sections/06_conclusion.tex`

Stage 10 will populate these files subject to the Stage-8 freeze.

## Reproduction entry points

- `REPRODUCIBILITY.md`
- `Makefile`
- `code/README.md`
- `paper/README.md`
- `theorem_certificates/README.md`
- `formal/README.md`
- `audit/counterexample_regression_register.md`

## Canonicality rule

This manifest identifies evidence-bearing source objects. The final Stage-9 commit SHA pins the complete repository tree and supersedes the need to duplicate every file SHA here.

No artifact in this manifest authorizes a theorem or interpretation broader than `audit/STAGE_08_CANONICAL_THEORY_FREEZE.md`.


## Manuscript reproducibility blobs and CI

| Artifact | Blob SHA |
|---|---|
| `.github/workflows/manuscript.yml` | `618c2e9a95f4c2b0f2c10f33c6c6ca6bdac73f05` |
| `paper/manuscript.tex` | `ae4c226b9ea2c89d46ff6e064300f730e0eefeae` |
| `paper/sections/01_introduction.tex` | `607ed84b793169e745088771576bc581e4abf411` |
| `paper/sections/02_model.tex` | `abc0458937bca7e1de28d6a46a11e291a9136419` |
| `paper/sections/03_best_responses.tex` | `c263b8f2efdc820484e4c6757f647b94f9316bee` |
| `paper/sections/04_equilibrium.tex` | `b80f5817905de1d3dfe9c103ad8ae599cc86dea6` |
| `paper/sections/05_implications.tex` | `8eab871175b6b8b46f80d8b616c0ca646d79845a` |
| `paper/sections/06_conclusion.tex` | `f1b13de4141e27ed6df20fef9827f8fc8aa7ad01` |
| `paper/README.md` | `7b592189389082dfaf16bb2b6d074fc3bdda5b2a` |

Stage-9 manuscript smoke-build evidence:

- run `35442682700`
- conclusion: **success**
- all steps passed, including `make paper`.
