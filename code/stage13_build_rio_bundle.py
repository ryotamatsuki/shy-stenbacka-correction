"""Build a flat Review of Industrial Organization LaTeX submission bundle.

The canonical research manuscript stays modular under paper/. RIO's public
submission guidance says LaTeX submissions should not use subfolders, so this
script copies the canonical sources into a generated flat directory and rewrites
only path prefixes. It does not alter manuscript content.
"""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
OUT = PAPER / "rio_submission"

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

main = (PAPER / "manuscript.tex").read_text(encoding="utf-8")
main = main.replace(r"\input{sections/", r"\input{")
main = main.replace(r"\input{generated/duopoly_best_response.tex}", r"\input{duopoly_best_response.tex}")
(OUT / "manuscript.tex").write_text(main, encoding="utf-8")

for src in sorted((PAPER / "sections").glob("*.tex")):
    section = src.read_text(encoding="utf-8")
    section = section.replace(
        r"\input{generated/duopoly_best_response.tex}",
        r"\input{duopoly_best_response.tex}",
    )
    (OUT / src.name).write_text(section, encoding="utf-8")

shutil.copy2(PAPER / "references.bib", OUT / "references.bib")

figure = PAPER / "generated" / "duopoly_best_response.tex"
if not figure.exists():
    raise FileNotFoundError(
        "Generated figure missing. Run code/stage10_generate_figure.py before building the RIO bundle."
    )
shutil.copy2(figure, OUT / figure.name)

files = sorted(p.name for p in OUT.iterdir() if p.is_file())
assert "manuscript.tex" in files
assert "references.bib" in files
assert "duopoly_best_response.tex" in files
assert "07_reproducibility.tex" in files

print("Stage-13 RIO flat-bundle build PASS")
print(f"output={OUT}")
print("files=" + ", ".join(files))
