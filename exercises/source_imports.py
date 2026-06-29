"""Helpers for importing the reference implementation used by this course."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_REPO = REPO_ROOT / "reference"
SOURCE_MAIN = SOURCE_REPO / "main.py"


def load_source_main() -> ModuleType:
    """Load the bundled `reference/main.py` as a module."""
    if not SOURCE_MAIN.exists():
        raise FileNotFoundError(f"source repo main.py not found: {SOURCE_MAIN}")

    spec = importlib.util.spec_from_file_location("how_to_train_your_gpt_main", SOURCE_MAIN)
    if spec is None or spec.loader is None:
        raise ImportError(f"could not load module spec for {SOURCE_MAIN}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module
