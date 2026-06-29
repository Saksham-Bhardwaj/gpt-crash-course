"""Repository import smoke tests."""

from __future__ import annotations

import importlib


def test_reference_main_exists(repo_root):
    assert (repo_root / "reference" / "main.py").is_file()


def test_source_import_helper_loads_reference():
    from source_imports import SOURCE_MAIN, load_source_main

    assert SOURCE_MAIN.name == "main.py"
    assert SOURCE_MAIN.parent.name == "reference"
    module = load_source_main()
    assert hasattr(module, "GPT")
    assert hasattr(module, "GPTConfig")
    assert hasattr(module, "SimpleTokenizer")


def test_starter_project_modules_import(starter_project_files):
    for path in starter_project_files:
        module = importlib.import_module(path.stem)
        assert hasattr(module, "parse_args")
        assert hasattr(module, "main")
