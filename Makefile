PYTHON ?= python3

.PHONY: verify verify-python verify-formal paper clean

verify: verify-python verify-formal

verify-python:
	$(PYTHON) code/stage01_verify.py
	$(PYTHON) code/stage04_verify.py
	$(PYTHON) code/stage04_hotelling_refinement_verify.py
	$(PYTHON) code/stage04a_independent_verify.py
	$(PYTHON) code/stage07_welfare_verify.py
	$(PYTHON) code/stage075a_scope_counterexamples.py

verify-formal:
	lake build

paper:
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex

clean:
	cd paper && latexmk -C || true
