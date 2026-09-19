PYTHON ?= python3

.PHONY: verify verify-python verify-formal figures paper clean

verify: verify-python verify-formal

verify-python:
	$(PYTHON) code/stage01_verify.py
	$(PYTHON) code/stage04_verify.py
	$(PYTHON) code/stage04_hotelling_refinement_verify.py
	$(PYTHON) code/stage04a_independent_verify.py
	$(PYTHON) code/stage07_welfare_verify.py
	$(PYTHON) code/stage075a_scope_counterexamples.py
	$(PYTHON) code/stage10_generate_figure.py

verify-formal:
	lake build

figures:
	$(PYTHON) code/stage10_generate_figure.py

paper: figures
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex

clean:
	cd paper && latexmk -C || true
	rm -rf paper/generated
