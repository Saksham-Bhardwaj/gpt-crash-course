"""Starter for Project 4: inference UI."""

from __future__ import annotations

import argparse
from pathlib import Path


def load_checkpoint(path: Path):
    """Load a trained checkpoint."""
    # TODO: validate path, load torch checkpoint, recreate config/model, and load weights.
    raise NotImplementedError("TODO: implement load_checkpoint")


def generate_text(
    checkpoint: Path,
    prompt: str,
    max_new_tokens: int,
    temperature: float,
    top_k: int | None,
    top_p: float | None,
    seed: int,
) -> str:
    """Generate text from a checkpoint and prompt."""
    # TODO: tokenize prompt, run model.generate or Day 12 sampling, and decode output.
    raise NotImplementedError("TODO: implement generate_text")


def save_transcript(path: Path, settings: dict[str, object], generated: str) -> None:
    """Save prompt, settings, and generated text."""
    # TODO: create parent directory and write a readable transcript.
    raise NotImplementedError("TODO: implement save_transcript")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate text from a tiny GPT checkpoint.")
    parser.add_argument("--checkpoint", type=Path, required=True, help="Checkpoint from Project 3.")
    parser.add_argument("--prompt", required=True, help="Prompt text.")
    parser.add_argument("--max-new-tokens", type=int, default=80, help="Number of tokens to generate.")
    parser.add_argument("--temperature", type=float, default=0.8, help="Sampling temperature.")
    parser.add_argument("--top-k", type=int, default=50, help="Top-k candidate limit.")
    parser.add_argument("--top-p", type=float, default=0.95, help="Nucleus sampling probability mass.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed.")
    parser.add_argument("--save", type=Path, help="Optional transcript output path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    generated = generate_text(
        checkpoint=args.checkpoint,
        prompt=args.prompt,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_k=args.top_k,
        top_p=args.top_p,
        seed=args.seed,
    )
    print(generated)
    if args.save:
        save_transcript(args.save, vars(args), generated)


if __name__ == "__main__":
    main()
