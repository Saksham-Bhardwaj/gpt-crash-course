"""Common pytest fixtures for the crash course."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
EXERCISES_DIR = REPO_ROOT / "exercises"
PROJECTS_DIR = REPO_ROOT / "projects"
REFERENCE_MAIN = REPO_ROOT / "reference" / "main.py"

for path in (REPO_ROOT, EXERCISES_DIR, PROJECTS_DIR):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def exercise_files() -> list[Path]:
    return sorted(EXERCISES_DIR.glob("exercise_*.py"))


@pytest.fixture(scope="session")
def starter_project_files() -> list[Path]:
    return sorted(PROJECTS_DIR.glob("starter_*.py"))
