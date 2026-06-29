"""Exercise 03: Rotary Position Embeddings.

Concept:
    RoPE rotates query and key vectors based on token position. It preserves
    tensor shape while making dot products position-aware.

Source reference:
    reference/chapters/04_positional_encoding.md
    reference/main.py
"""

from __future__ import annotations

import torch
import torch.nn as nn

from source_imports import load_source_main


source = load_source_main()
ReferenceRoPE = source.RotaryPositionalEmbedding


class TinyRoPE(nn.Module):
    """Small RoPE implementation for learning."""

    def __init__(self, head_dim: int, max_seq_len: int = 16, theta: float = 10000.0):
        super().__init__()
        assert head_dim % 2 == 0
        # TODO: compute inverse frequencies for even dimensions.
        # TODO: compute outer product of positions and inverse frequencies.
        # TODO: repeat each frequency so cos/sin match head_dim.
        # TODO: register cos_cached and sin_cached buffers.
        raise NotImplementedError("TODO: implement TinyRoPE.__init__")

    @staticmethod
    def rotate_half(x: torch.Tensor) -> torch.Tensor:
        """Turn [x0, x1, x2, x3] into [-x1, x0, -x3, x2]."""
        # TODO: split even and odd dimensions, stack [-odd, even], flatten.
        raise NotImplementedError("TODO: implement rotate_half")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Apply RoPE to x shaped [batch, heads, seq, head_dim]."""
        # TODO: select cos/sin for seq length and broadcast over batch/heads.
        # TODO: return (x * cos) + (rotate_half(x) * sin).
        raise NotImplementedError("TODO: implement TinyRoPE.forward")


if __name__ == "__main__":
    torch.manual_seed(0)
    rope = TinyRoPE(head_dim=4, max_seq_len=8)
    x = torch.randn(2, 3, 5, 4)
    y = rope(x)

    print("input shape:", x.shape)
    print("output shape:", y.shape)

    assert y.shape == x.shape
    assert torch.allclose(y[:, :, 0], x[:, :, 0], atol=1e-5)
    assert not torch.allclose(y[:, :, 2], x[:, :, 2])
    print("exercise_03_rope: ok")
