"""Exercise 05: Transformer block.

Concept:
    A transformer block combines communication through attention, private
    computation through a feed-forward network, normalization, and residual
    connections.

Source reference:
    reference/chapters/06_transformer_block.md
    reference/main.py
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

from source_imports import load_source_main


source = load_source_main()
ReferenceAttention = source.MultiHeadAttention


class RMSNorm(nn.Module):
    def __init__(self, d_model: int, eps: float = 1e-6):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(d_model))
        self.eps = eps

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: compute reciprocal RMS over the last dimension and scale by weight.
        raise NotImplementedError("TODO: implement RMSNorm.forward")


class SwiGLU(nn.Module):
    def __init__(self, d_model: int, expansion_factor: int = 4):
        super().__init__()
        hidden_dim = expansion_factor * d_model
        self.w1 = nn.Linear(d_model, hidden_dim, bias=False)
        self.w2 = nn.Linear(d_model, hidden_dim, bias=False)
        self.w3 = nn.Linear(hidden_dim, d_model, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: return w3(silu(w1(x)) * w2(x)).
        raise NotImplementedError("TODO: implement SwiGLU.forward")


class TransformerBlock(nn.Module):
    def __init__(self, d_model: int, num_heads: int):
        super().__init__()
        self.norm1 = RMSNorm(d_model)
        self.attention = ReferenceAttention(d_model, num_heads, dropout=0.0)
        self.norm2 = RMSNorm(d_model)
        self.ffn = SwiGLU(d_model)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        # TODO: apply pre-norm residual attention.
        # TODO: apply pre-norm residual feed-forward.
        raise NotImplementedError("TODO: implement TransformerBlock.forward")


if __name__ == "__main__":
    torch.manual_seed(0)
    block = TransformerBlock(d_model=16, num_heads=4)
    x = torch.randn(2, 5, 16, requires_grad=True)
    y = block(x)
    loss = y.pow(2).mean()
    loss.backward()

    print("input shape:", x.shape)
    print("output shape:", y.shape)

    assert y.shape == x.shape
    assert not torch.allclose(y.detach(), x.detach())
    assert x.grad is not None
    assert torch.isfinite(x.grad).all()
    print("exercise_05_transformer_block: ok")
