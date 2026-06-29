"""Starter for Project 3: train a custom tiny GPT."""

from __future__ import annotations

import argparse
from pathlib import Path


def load_text(path: Path) -> str:
    """Load training text."""
    # TODO: read UTF-8 text and raise a clear error if the file is empty.
    raise NotImplementedError("TODO: implement load_text")


def build_dataset(text: str, block_size: int):
    """Tokenize text and create input-target windows."""
    # TODO: encode with GPT-2 tiktoken and create a torch Dataset.
    raise NotImplementedError("TODO: implement build_dataset")


def train(data_path: Path, steps: int, out: Path, block_size: int) -> None:
    """Train a tiny GPT and save checkpoint plus outputs."""
    # TODO: create config/model/optimizer, train, save checkpoint, plot loss, and sample.
    raise NotImplementedError("TODO: implement train")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a tiny GPT on a custom text file.")
    parser.add_argument("--data", type=Path, default=Path("data/sample.txt"), help="Training text path.")
    parser.add_argument("--steps", type=int, default=100, help="Number of optimizer steps.")
    parser.add_argument("--out", type=Path, default=Path("checkpoints/tiny_custom_gpt.pt"), help="Checkpoint path.")
    parser.add_argument("--block-size", type=int, default=64, help="Training context length.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    train(args.data, args.steps, args.out, args.block_size)


if __name__ == "__main__":
    main()
