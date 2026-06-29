"""Exercise 07: Training step.

Concept:
    Training computes next-token loss, backpropagates gradients, and updates
    model parameters with an optimizer.

Source reference:
    reference/chapters/08_training.md
    reference/main.py
"""

from __future__ import annotations

import torch
from torch.utils.data import Dataset

from source_imports import load_source_main


source = load_source_main()
GPT = source.GPT
GPTConfig = source.GPTConfig
create_optimizer = source.create_optimizer


class TinyTokenDataset(Dataset):
    """Fixed-window next-token dataset over a 1D token tensor."""

    def __init__(self, tokens: torch.Tensor, block_size: int):
        self.tokens = tokens.long()
        self.block_size = block_size

    def __len__(self) -> int:
        # TODO: return the number of valid input-target windows.
        raise NotImplementedError("TODO: implement TinyTokenDataset.__len__")

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        # TODO: return x=tokens[idx:idx+block_size], y=tokens[idx+1:idx+block_size+1].
        raise NotImplementedError("TODO: implement TinyTokenDataset.__getitem__")


def one_training_step(model: GPT, optimizer: torch.optim.Optimizer, x: torch.Tensor, y: torch.Tensor) -> float:
    """Run one optimization step and return the scalar loss."""
    # TODO: set train mode, zero grads, compute loss, backward, step optimizer.
    raise NotImplementedError("TODO: implement one_training_step")


if __name__ == "__main__":
    torch.manual_seed(0)
    config = GPTConfig(
        vocab_size=64,
        d_model=32,
        num_heads=4,
        num_layers=2,
        max_seq_len=8,
        dropout=0.0,
        embd_dropout=0.0,
        batch_size=2,
    )
    model = GPT(config)
    optimizer = create_optimizer(model, config)
    dataset = TinyTokenDataset(torch.arange(0, 64), block_size=config.max_seq_len)
    x0, y0 = dataset[0]
    x = x0.unsqueeze(0).repeat(2, 1)
    y = y0.unsqueeze(0).repeat(2, 1)

    before = model.token_embedding.weight.detach().clone()
    loss = one_training_step(model, optimizer, x, y)
    after = model.token_embedding.weight.detach()

    print("loss:", loss)

    assert isinstance(loss, float)
    assert loss > 0
    assert not torch.allclose(before, after)
    print("exercise_07_training: ok")
