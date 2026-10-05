"""v2.6/v2.7 retrofit QA.

This verifier checks provenance/accountability and reviewer-verifiability
governance artifacts. It does not re-prove the economic model.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audit"
PAPER = ROOT / "paper"
DOCS = ROOT / "docs"

required = {
    "AI log": AUDIT / "AI_PROVENANCE_MATERIAL_USE_LOG.md",
    "author record": AUDIT / "AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md",
    "robustness certificate": AUDIT / "CONTRIBUTION_ROBUSTNESS_CERTIFICATE.md",
    "reviewer map": AUDIT / "REVIEWER_VERIFIABILITY_MAP.md",
    "reviewer report": AUDIT / "REVIEWER_VERIFIABILITY_REPORT.md",
    "retrofit report": AUDIT / "V2_6_V2_7_RETROFIT_2026-10-05.md",
    "workflow provenance": DOCS / "WORKFLOW_PROVENANCE.md",
    "formal fidelity map": AUDIT / "stage075a_formal_statement_fidelity.md",
}
for label, path in required.items():
    assert path.is_file(), f"missing {label}: {path}"

ai = required["AI log"].read_text(encoding="utf-8")
author = required["author record"].read_text(encoding="utf-8")
robust = required["robustness certificate"].read_text(encoding="utf-8")
rv_map = required["reviewer map"].read_text(encoding="utf-8")
rv_report = required["reviewer report"].read_text(encoding="utf-8")
retrofit = required["retrofit report"].read_text(encoding="utf-8")
workflow = required["workflow provenance"].read_text(encoding="utf-8")
repro = (PAPER / "sections/07_reproducibility.tex").read_text(encoding="utf-8")
appendix = (PAPER / "sections/appendix.tex").read_text(encoding="utf-8")

# v2.6 verification-actor separation.
for actor in ("AUTHOR", "AI", "COMPUTATION", "FORMAL", "EXTERNAL HUMAN"):
    assert actor in ai, f"verification actor missing from AI log: {actor}"
assert "A second AI pass is never classified as external human review" in ai
assert "No EXTERNAL HUMAN verification is claimed" in author
assert "FINAL EXACT-PACKAGE SIGN-OFF REMAINS STAGE 15" in author
assert "Stage 15 still requires a personal AUTHOR sign-off" in author

# v2.7 reviewer-verifiability evidence.
assert "FULL APPLICABILITY" in rv_map
assert "PASS — REVIEWER VERIFIABILITY" in rv_report
for phrase in (
    "Global Cournot continuation",
    "Global own-payoff concavity",
    "Corrected symmetric Cournot action",
    "global best response",
    "Complete pure source-duopoly correspondence",
    "Literal Hotelling",
    "Auxiliary no-loss",
):
    assert phrase.lower() in (rv_map + "\n" + rv_report).lower(), phrase

# Presentation defects repaired and formal delegation made explicit.
assert "p_B=z,qquad p_A=z-\\tau" not in appendix
assert "p_B=z,\\qquad p_A=z-\\tau" in appendix
assert "The Lean layer certifies selected algebraic and order-theoretic cores" in repro
assert "global continuations" in repro
assert "not described as external human review" in repro

# Current portability and workflow authority are explicit.
assert "MODEL-SPECIFIC" in robust
assert "INSTITUTION-SPECIFIC" in robust
assert "7d754032f292205264bd404116b561366836c7fd" in workflow
assert "v2.6 PASS / v2.7 PASS" in workflow
assert "Stage 14: CLOSED / CONDITIONAL PASS" in retrofit
assert "authenticated RIO portal preflight" in retrofit

print("v2.6/v2.7 retrofit QA PASS")
print("verification_actors=AUTHOR,AI,COMPUTATION,FORMAL,EXTERNAL HUMAN")
print("reviewer_verifiability=PASS")
print("scientific_rollback=none")
print("remaining_blocker=authenticated RIO portal preflight; Stage-15 exact-package author sign-off")
