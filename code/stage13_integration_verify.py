"""Stage-13 manuscript integration checks.

These checks audit exposition/package integration only. They do not re-prove the
economic model and do not replace the Stage-11 hostile-referee verifier.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
MAIN = (PAPER / "manuscript.tex").read_text(encoding="utf-8")
SECTIONS = "\n".join(
    p.read_text(encoding="utf-8")
    for p in sorted((PAPER / "sections").glob("*.tex"))
)
BIB = (PAPER / "references.bib").read_text(encoding="utf-8")
ALL = MAIN + "\n" + SECTIONS

abstract_match = re.search(
    r"\\begin\{abstract\}(.*?)\\end\{abstract\}", MAIN, re.S
)
assert abstract_match, "abstract missing"
abstract_plain = re.sub(r"\\[A-Za-z]+|[{}$\\()]", " ", abstract_match.group(1))
abstract_words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'–-]*", abstract_plain)
assert 150 <= len(abstract_words) <= 250, len(abstract_words)

kw_match = re.search(r"\\textbf\{Keywords:\}\s*([^\n]+)", MAIN)
assert kw_match, "keywords missing"
keywords = [x.strip() for x in kw_match.group(1).split(";") if x.strip()]
assert 4 <= len(keywords) <= 6, keywords

jel_match = re.search(r"\\textbf\{JEL classification:\}\s*([^\n]+)", MAIN)
assert jel_match, "JEL classification missing"
jels = [x.strip() for x in jel_match.group(1).split(";") if x.strip()]
assert len(jels) >= 1
assert all(re.fullmatch(r"[A-Z][0-9]{2}", x) for x in jels), jels

assert "\\cite{Dai2026}" in ALL, "Dai 2026 not integrated into manuscript"
assert "@article{Dai2026" in BIB, "Dai 2026 bibliography entry missing"
assert "10.1007/s11151-026-10063-3" in BIB
assert "\\bibliographystyle{apalike}" in MAIN
doi_values = re.findall(r"^\s*doi\s*=\s*\{([^}]+)\}", BIB, re.M)
for doi in doi_values:
    doi = re.sub(r"^https?://doi\\.org/", "", doi.strip())
    assert f"https://doi.org/{doi}" in BIB, f"full DOI link missing for {doi}"

cite_keys = set()
for match in re.finditer(r"\\cite\{([^}]+)\}", ALL):
    cite_keys.update(k.strip() for k in match.group(1).split(","))
bib_keys = set(re.findall(r"@\w+\{([^,]+),", BIB))
missing_bib = sorted(cite_keys - bib_keys)
assert not missing_bib, f"missing bibliography keys: {missing_bib}"

labels = set(re.findall(r"\\label\{([^}]+)\}", ALL))
refs = set()
for pattern in (r"\\ref\{([^}]+)\}", r"\\eqref\{([^}]+)\}"):
    refs.update(re.findall(pattern, ALL))
missing_labels = sorted(refs - labels)
assert not missing_labels, f"missing labels: {missing_labels}"

for token in ("TODO", "FIXME", "TBD", "PLACEHOLDER"):
    assert token not in ALL, f"manuscript contains {token}"

assert "\\label{fig:br-witness}" in ALL
assert "\\ref{fig:br-witness}" in ALL
assert "\\label{tab:eq-regimes}" in ALL
assert "\\ref{tab:eq-regimes}" in ALL

assert "complete pure Stage-I" in ALL
assert "not a new general theory" in ALL
assert "not a refinement claim" in ALL
assert "not formally mechanized" in ALL

notes = (PAPER / "RIO_SUBMISSION_NOTES.md").read_text(encoding="utf-8")
assert (
    "Stage-14 author metadata resolved; portal items still unresolved" in notes
    or "Stage-14 author/portal items still unresolved" in notes
)
assert (
    "restored from the author's previously approved and submitted correction-paper package" in notes
    or "does not invent author-specific declarations" in notes
)

print("Stage-13 integration verification PASS")
print(f"abstract_words={len(abstract_words)}")
print(f"keywords={len(keywords)}")
print(f"jel_codes={len(jels)}")
print(f"citations={len(cite_keys)}")
print(f"labels={len(labels)}, refs={len(refs)}")
