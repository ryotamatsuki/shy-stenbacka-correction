"""Stage-14 non-portal submission QA for Review of Industrial Organization.

This verifier checks only facts available from the repository/public journal
requirements. It deliberately does not invent author metadata or authenticated
portal fields. Those remain explicit Stage-14 blockers.
"""

from pathlib import Path
import argparse
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

parser = argparse.ArgumentParser()
parser.add_argument("--require-bundle", action="store_true")
args = parser.parse_args()

# Public RIO manuscript requirements.
abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", MAIN, re.S)
assert abstract
abstract_plain = re.sub(r"\\[A-Za-z]+|[{}$\\()]", " ", abstract.group(1))
abstract_words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'–-]*", abstract_plain)
assert 150 <= len(abstract_words) <= 250, len(abstract_words)

kw = re.search(r"\\textbf\{Keywords:\}\s*([^\n]+)", MAIN)
assert kw
keywords = [x.strip() for x in kw.group(1).split(";") if x.strip()]
assert 4 <= len(keywords) <= 6, keywords

jel = re.search(r"\\textbf\{JEL classification:\}\s*([^\n]+)", MAIN)
assert jel
jels = [x.strip() for x in jel.group(1).split(";") if x.strip()]
assert jels and all(re.fullmatch(r"[A-Z][0-9]{2}", x) for x in jels)

assert "\\bibliographystyle{apalike}" in MAIN
assert "\\section*{Statements and Declarations}" in ALL
for required in (
    "\\paragraph{Data availability.}",
    "\\paragraph{Code availability.}",
    "\\paragraph{Use of generative AI.}",
):
    assert required in ALL, required

# Figure formatting / accessibility controls.
assert "\\captionsetup[figure]{name=Fig.,labelfont=bf,labelsep=space}" in MAIN
assert "thick,dashed" in (ROOT / "code/stage10_generate_figure.py").read_text(encoding="utf-8")
assert "\\label{fig:br-witness}" in ALL
assert "\\ref{fig:br-witness}" in ALL

# Citation integrity and no unused bibliography entries.
cite_keys = set()
for m in re.finditer(r"\\cite\{([^}]+)\}", ALL):
    cite_keys.update(k.strip() for k in m.group(1).split(","))
bib_keys = set(re.findall(r"@\w+\{([^,]+),", BIB))
assert cite_keys <= bib_keys, sorted(cite_keys - bib_keys)
assert bib_keys <= cite_keys, f"uncited bibliography entries: {sorted(bib_keys - cite_keys)}"

# DOI entries must carry printable full DOI URLs.
for entry in re.split(r"(?=@\w+\{)", BIB):
    if "doi" in entry.lower() and re.search(r"\bdoi\s*=", entry, re.I):
        doi = re.search(r"\bdoi\s*=\s*\{([^}]+)\}", entry, re.I)
        if doi:
            assert f"https://doi.org/{doi.group(1)}" in entry, doi.group(1)

# No manuscript placeholders / stale internal workflow wording.
for token in ("TODO", "FIXME", "TBD", "PLACEHOLDER"):
    assert token not in ALL, token
assert "assigns the equilibrium correspondence its primary exposition vehicle" not in ALL

# Author-specific data are intentionally not fabricated; blocker file must exist.
author_req = (PAPER / "RIO_AUTHOR_INPUT_REQUIRED.md").read_text(encoding="utf-8")
assert "AUTHOR INPUT REQUIRED" in author_req
assert "\\author{}" in MAIN, "unexpected author metadata change; re-audit title-page handling"

# Exact flat upload layout.
out = PAPER / "rio_submission"
if args.require_bundle:
    assert out.is_dir(), "flat RIO bundle missing"
    assert not any(p.is_dir() for p in out.iterdir()), "subdirectory found in flat bundle"
    files = sorted(p.name for p in out.iterdir() if p.is_file())
    required = {
        "manuscript.tex",
        "references.bib",
        "duopoly_best_response.tex",
        "01_introduction.tex",
        "02_model.tex",
        "03_best_responses.tex",
        "04_equilibrium.tex",
        "05_implications.tex",
        "05a_welfare_scope.tex",
        "05b_related_literature.tex",
        "06_conclusion.tex",
        "07_reproducibility.tex",
        "appendix.tex",
    }
    missing = sorted(required - set(files))
    assert not missing, f"missing flat-bundle files: {missing}"
    for p in out.glob("*.tex"):
        txt = p.read_text(encoding="utf-8")
        assert "sections/" not in txt, p.name
        assert "generated/" not in txt, p.name
    forbidden_suffixes = {".aux", ".bbl", ".blg", ".fdb_latexmk", ".fls", ".log", ".out", ".pdf"}
    assert not any(Path(name).suffix.lower() in forbidden_suffixes for name in files), files
    assert not any(
        name.lower().startswith(("audit", "readme", ".env", "secret"))
        for name in files
    ), files
    build_pdf = PAPER / "rio_submission_build" / "manuscript.pdf"
    assert build_pdf.is_file(), "flat-source clean build PDF missing"
    print("flat_bundle_files=" + ",".join(files))

print("Stage-14 non-portal submission QA PASS")
print(f"abstract_words={len(abstract_words)}")
print(f"keywords={len(keywords)}")
print(f"jel_codes={len(jels)}")
print(f"citations={len(cite_keys)}")
print("known_blocker=author metadata/declarations + authenticated portal preflight")
