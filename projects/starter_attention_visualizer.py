"""Starter for Project 2: attention visualizer."""

from __future__ import annotations

import argparse
from pathlib import Path


def tokenize(text: str) -> list[str]:
    """Tokenize text into display pieces."""
    # TODO: use tiktoken.get_encoding("gpt2") and decode each token ID.
    raise NotImplementedError("TODO: implement tokenize")


def build_attention_weights(num_tokens: int, d_model: int, num_heads: int):
    """Create causal attention weights for a token sequence."""
    # TODO: embed token IDs, run an inspectable attention module, and return weights.
    raise NotImplementedError("TODO: implement build_attention_weights")


def save_heatmap(tokens: list[str], weights, out: Path) -> None:
    """Save one attention head as a labeled heatmap."""
    # TODO: render weights with matplotlib.pyplot.imshow and save to out.
    raise NotImplementedError("TODO: implement save_heatmap")


def run(text: str, out: Path, head: int) -> None:
    """Run tokenization, attention, and heatmap export."""
    # TODO: validate inputs, select the requested head, and write the PNG.
    raise NotImplementedError("TODO: implement run")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Save a causal attention heatmap for text.")
    parser.add_argument("--text", required=True, help="Input text to visualize.")
    parser.add_argument("--out", type=Path, default=Path("outputs/attention_heatmap.png"), help="Output PNG path.")
    parser.add_argument("--head", type=int, default=0, help="Attention head index to plot.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run(args.text, args.out, args.head)


if __name__ == "__main__":
    main()
