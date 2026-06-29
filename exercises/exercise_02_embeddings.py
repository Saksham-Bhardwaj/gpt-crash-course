"""Exercise 02: Token embeddings.

Concept:
    An embedding layer is a learned lookup table. Given token IDs shaped
    [batch, seq], it returns vectors shaped [batch, seq, d_model].

Source reference:
    reference/chapters/03_embeddings.md
    reference/main.py
"""

from __future__ import annotations

import torch
import torch.nn as nn

from source_imports import load_source_main


source = load_source_main()
GPTConfig = source.GPTConfig


def build_embedding(vocab_size: int, d_model: int) -> nn.Embedding:
    """Create a token embedding table."""
    # TODO: return nn.Embedding(vocab_size, d_model).
    raise NotImplementedError("TODO: implement build_embedding")


def embed_tokens(embedding: nn.Embedding, token_ids: torch.Tensor) -> torch.Tensor:
    """Look up embeddings for token IDs."""
    # TODO: call the embedding layer on token_ids.
    raise NotImplementedError("TODO: implement embed_tokens")


if __name__ == "__main__":
    torch.manual_seed(0)
    config = GPTConfig(vocab_size=32, d_model=8)
    embedding = build_embedding(config.vocab_size, config.d_model)
    token_ids = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.long)
    x = embed_tokens(embedding, token_ids)

    print("token_ids shape:", token_ids.shape)
    print("embedding shape:", x.shape)

    assert x.shape == (2, 3, 8)
    assert torch.allclose(x[0, 0], embedding.weight[1])
    assert x.requires_grad
    print("exercise_02_embeddings: ok")
