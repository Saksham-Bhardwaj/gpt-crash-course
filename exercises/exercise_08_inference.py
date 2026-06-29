"""Exercise 08: Inference and sampling.

Concept:
    During inference, a GPT produces logits for the next token. Decoding turns
    those logits into one sampled token at a time using controls such as
    temperature, top-k, and top-p.

Source reference:
    reference/chapters/09_inference.md
    reference/main.py
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

from source_imports import load_source_main


source = load_source_main()
GPT = source.GPT
GPTConfig = source.GPTConfig


def apply_temperature(logits: torch.Tensor, temperature: float) -> torch.Tensor:
    """Scale logits by temperature."""
    # TODO: handle temperature <= 0 as greedy-compatible or raise a clear error.
    # TODO: divide logits by temperature.
    raise NotImplementedError("TODO: implement apply_temperature")


def apply_top_k(logits: torch.Tensor, top_k: int | None) -> torch.Tensor:
    """Mask logits outside the top-k highest values."""
    # TODO: if top_k is None, return logits unchanged.
    # TODO: keep only the top_k logits and set the rest to -inf.
    raise NotImplementedError("TODO: implement apply_top_k")


def apply_top_p(logits: torch.Tensor, top_p: float | None) -> torch.Tensor:
    """Mask logits outside the nucleus probability mass."""
    # TODO: sort logits, compute cumulative probabilities, mask after top_p.
    # TODO: scatter the sorted mask back to original token order.
    raise NotImplementedError("TODO: implement apply_top_p")


def sample_next_token(
    logits: torch.Tensor,
    temperature: float = 1.0,
    top_k: int | None = None,
    top_p: float | None = None,
) -> torch.Tensor:
    """Sample one token ID from next-token logits shaped [batch, vocab]."""
    # TODO: apply temperature, top-k, top-p, softmax, then torch.multinomial.
    raise NotImplementedError("TODO: implement sample_next_token")


@torch.no_grad()
def generate(
    model: GPT,
    input_ids: torch.Tensor,
    max_new_tokens: int,
    temperature: float = 1.0,
    top_k: int | None = None,
    top_p: float | None = None,
) -> torch.Tensor:
    """Generate token IDs from a model."""
    # TODO: loop max_new_tokens times.
    # TODO: crop input to model.config.max_seq_len before each forward pass.
    # TODO: sample next token from logits[:, -1, :].
    # TODO: append sampled token to input_ids.
    raise NotImplementedError("TODO: implement generate")


if __name__ == "__main__":
    torch.manual_seed(0)
    logits = torch.tensor([[1.0, 2.0, 3.0, 4.0]])
    top_k_logits = apply_top_k(logits.clone(), top_k=2)

    config = GPTConfig(
        vocab_size=32,
        d_model=32,
        num_heads=4,
        num_layers=1,
        max_seq_len=8,
        dropout=0.0,
        embd_dropout=0.0,
    )
    model = GPT(config)
    input_ids = torch.tensor([[1, 2, 3]], dtype=torch.long)
    output = generate(model, input_ids, max_new_tokens=4, temperature=1.0, top_k=8)

    print("top-k logits:", top_k_logits)
    print("generated ids:", output)

    assert torch.isneginf(top_k_logits[0, 0])
    assert torch.isneginf(top_k_logits[0, 1])
    assert output.shape == (1, 7)
    assert torch.equal(output[:, :3], input_ids)
    print("exercise_08_inference: ok")
