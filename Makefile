PYTHON ?= python3

.PHONY: verify verify-python verify-formal figures paper rio-bundle submission-qa clean

verify: verify-python verify-formal

verify-python:
	$(PYTHON) code/stage01_verify.py
	$(PYTHON) code/stage04_verify.py
	$(PYTHON) code/stage04_hotelling_refinement_verify.py
	$(PYTHON) code/stage04a_independent_verify.py
	$(PYTHON) code/stage07_welfare_verify.py
	$(PYTHON) code/stage075a_scope_counterexamples.py
	$(PYTHON) code/stage10_generate_figure.py
	$(PYTHON) code/stage11_hostile_referee_verify.py
	$(PYTHON) code/independent_audit_repair_verify.py
	$(PYTHON) code/stage13_integration_verify.py
	$(PYTHON) code/stage14_submission_qa.py

verify-formal:
	lake build

figures:
	$(PYTHON) code/stage10_generate_figure.py

paper: figures
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex

rio-bundle: figures
	$(PYTHON) code/stage13_build_rio_bundle.py
	rm -rf paper/rio_submission_build
	mkdir -p paper/rio_submission_build
	cd paper/rio_submission && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../rio_submission_build manuscript.tex

submission-qa: rio-bundle
	$(PYTHON) code/stage14_submission_qa.py --require-bundle

clean:
	cd paper && latexmk -C || true
	rm -rf paper/generated paper/rio_submission paper/rio_submission_build
