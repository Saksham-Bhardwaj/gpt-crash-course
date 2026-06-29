.PHONY: setup test check clean

PYTHON ?= python
VENV ?= .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -r requirements.txt

test:
	$(PYTHON) -m pytest tests

check:
	@for f in exercises/exercise_*.py; do \
		echo "$$f"; \
		$(PYTHON) "$$f"; \
	done

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type d -name .pytest_cache -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
