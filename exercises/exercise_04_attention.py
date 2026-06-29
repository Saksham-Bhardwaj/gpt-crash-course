"""Exercise 04: Causal multi-head self-attention.

Concept:
    Attention lets each token mix information from previous tokens. Causal
    masking prevents a position from reading future tokens during training.

Source reference:
    /tmp/gpt-study/how-to-train-your-gpt/chapters/05_attention.md
    /tmp/gpt-study/how-to-train-your-gpt/main.py
"""

from __future__ import annotations

import math

import torch
import torch.nn as nn
import torch.nn.functional as F

from source_imports import load_source_main


source = load_source_main()
create_causal_mask = source.create_causal_mask


class InspectableCausalAttention(nn.Module):
    """Multi-head causal attention that returns attention weights."""

    def __init__(self, d_model: int, num_heads: int):
        super().__init__()
        assert d_model % num_heads == 0
        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        self.qkv_proj = nn.Linear(d_model, 3 * d_model, bias=False)
        self.out_proj = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        batch, seq_len, _ = x.shape
        # TODO: project x to qkv.
        # TODO: reshape to [batch, seq, 3, heads, head_dim].
        # TODO: permute/split into q, k, v shaped [batch, heads, seq, head_dim].
        # TODO: compute scaled attention scores.
        # TODO: apply create_causal_mask(seq_len, x.device).
        # TODO: softmax scores into attention weights.
        # TODO: multiply weights by values and recombine heads.
        # TODO: apply output projection.
        raise NotImplementedError("TODO: implement InspectableCausalAttention.forward")


if __name__ == "__main__":
    torch.manual_seed(0)
    attn = InspectableCausalAttention(d_model=16, num_heads=4)
    x = torch.randn(2, 5, 16)
    y, weights = attn(x)

    print("output shape:", y.shape)
    print("weights shape:", weights.shape)

    assert y.shape == x.shape
    assert weights.shape == (2, 4, 5, 5)
    assert torch.allclose(weights.sum(dim=-1), torch.ones(2, 4, 5), atol=1e-5)
    assert torch.all(weights.triu(diagonal=1) < 1e-6)
    print("exercise_04_attention: ok")
