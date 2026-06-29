"""Starter for Project 1: tokenizer visualizer."""

from __future__ import annotations

import argparse
from collections import Counter


def word_to_symbols(word: str) -> tuple[str, ...]:
    """Convert one word into starting BPE symbols."""
    # TODO: return characters plus an end-of-word marker such as "</w>".
    raise NotImplementedError("TODO: implement word_to_symbols")


def count_pairs(words: list[tuple[str, ...]]) -> Counter[tuple[str, str]]:
    """Count adjacent symbol pairs across tokenized words."""
    # TODO: loop through each symbol tuple and count adjacent pairs.
    raise NotImplementedError("TODO: implement count_pairs")


def merge_pair(words: list[tuple[str, ...]], pair: tuple[str, str]) -> list[tuple[str, ...]]:
    """Merge every occurrence of pair in each word."""
    # TODO: replace adjacent occurrences of pair with the concatenated symbol.
    raise NotImplementedError("TODO: implement merge_pair")


def run(text: str, steps: int, compare_gpt2: bool) -> None:
    """Run the tokenizer visualization."""
    # TODO: split text, run BPE merges, and optionally compare with tiktoken GPT-2.
    raise NotImplementedError("TODO: implement run")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Visualize toy BPE token merges.")
    parser.add_argument("--text", required=True, help="Input text to tokenize.")
    parser.add_argument("--steps", type=int, default=5, help="Number of toy BPE merge steps.")
    parser.add_argument("--compare-gpt2", action="store_true", help="Compare with GPT-2 tokenization.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run(args.text, args.steps, args.compare_gpt2)


if __name__ == "__main__":
    main()
