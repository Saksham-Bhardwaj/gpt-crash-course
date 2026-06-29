"""Import-level tests for exercise modules.

The exercises intentionally contain TODOs. These tests make sure the starter
modules load, reference imports resolve, and learner-facing self-check code is
kept behind `if __name__ == "__main__"`.
"""

from __future__ import annotations

import importlib


def test_all_exercise_modules_import(exercise_files):
    for path in exercise_files:
        module = importlib.import_module(path.stem)
        assert module.__doc__


def test_exercises_expose_expected_entry_points():
    expectations = {
        "exercise_01_tokenizer": ["encode_text", "decode_tokens", "token_pieces", "join_documents_with_eos"],
        "exercise_02_embeddings": ["build_embedding", "embed_tokens"],
        "exercise_03_rope": ["TinyRoPE"],
        "exercise_04_attention": ["InspectableCausalAttention"],
        "exercise_05_transformer_block": ["RMSNorm", "SwiGLU", "TransformerBlock"],
        "exercise_06_gpt_model": ["TinyGPTConfig", "TinyGPT"],
        "exercise_07_training": ["TinyTokenDataset", "one_training_step"],
        "exercise_08_inference": ["apply_temperature", "apply_top_k", "apply_top_p", "sample_next_token", "generate"],
    }

    for module_name, names in expectations.items():
        module = importlib.import_module(module_name)
        for name in names:
            assert hasattr(module, name), f"{module_name} is missing {name}"
