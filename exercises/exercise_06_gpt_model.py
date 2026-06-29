"""Exercise 06: Complete tiny GPT model.

Concept:
    A GPT is token embeddings, repeated transformer blocks, a final norm, and
    a language-model head trained with next-token cross-entropy.

Source reference:
    reference/chapters/07_gpt_model.md
    reference/main.py
"""

from __future__ import annotations

from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F

from source_imports import load_source_main


source = load_source_main()
ReferenceBlock = source.TransformerBlock
ReferenceRMSNorm = source.RMSNorm
create_causal_mask = source.create_causal_mask


@dataclass
class TinyGPTConfig:
    vocab_size: int = 128
    d_model: int = 32
    num_heads: int = 4
    num_layers: int = 2
    max_seq_len: int = 16
    dropout: float = 0.0


class TinyGPT(nn.Module):
    def __init__(self, config: TinyGPTConfig):
        super().__init__()
        self.config = config
        # TODO: create token embedding.
        # TODO: create transformer block stack.
        # TODO: create final norm.
        # TODO: create lm_head.
        # TODO: tie token embedding and lm_head weights.
        raise NotImplementedError("TODO: implement TinyGPT.__init__")

    def forward(
        self, input_ids: torch.Tensor, targets: torch.Tensor | None = None
    ) -> tuple[torch.Tensor, torch.Tensor | None]:
        # TODO: embed input IDs.
        # TODO: create causal mask.
        # TODO: run transformer blocks.
        # TODO: final norm and lm head.
        # TODO: if targets are passed, compute cross-entropy over flattened logits.
        raise NotImplementedError("TODO: implement TinyGPT.forward")


if __name__ == "__main__":
    torch.manual_seed(0)
    config = TinyGPTConfig()
    model = TinyGPT(config)
    input_ids = torch.randint(0, config.vocab_size, (2, 8))
    targets = torch.randint(0, config.vocab_size, (2, 8))
    logits, loss = model(input_ids, targets)

    print("logits shape:", logits.shape)
    print("loss:", loss)

    assert logits.shape == (2, 8, config.vocab_size)
    assert loss is not None and loss.ndim == 0
    assert model.token_embedding.weight.data_ptr() == model.lm_head.weight.data_ptr()
    print("exercise_06_gpt_model: ok")
