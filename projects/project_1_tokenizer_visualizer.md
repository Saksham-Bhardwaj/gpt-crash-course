# Project 1: Tokenizer Visualizer

Days: 3-4

## Goal

Build a visualizer that shows toy BPE merges step by step, then compares the result to GPT-2 tokenization.

## Deliverable

`projects/tokenizer_visualizer.py`

## Requirements

- Accept text from `--text`.
- Accept number of toy BPE merge rounds from `--steps`.
- Print initial character-level symbols.
- Count adjacent symbol pairs.
- Merge the most frequent pair each round.
- Print every merge in order.
- Print final toy symbols.
- With `--compare-gpt2`, print GPT-2 token IDs and decoded token pieces using `tiktoken`.

## Suggested CLI

```bash
python projects/tokenizer_visualizer.py --text "low lower newest widest" --steps 5
python projects/tokenizer_visualizer.py --text "antidisestablishmentarianism is weird" --steps 8 --compare-gpt2
```

## Implementation Plan

1. Represent each word as a tuple of characters plus an end-of-word marker such as `</w>`.
2. Build a list of symbol tuples for all words.
3. Count adjacent pairs across all tuples.
4. Pick the most frequent pair.
5. Replace adjacent pair occurrences with the merged symbol.
6. Repeat for `--steps`.
7. Add GPT-2 comparison with `tiktoken.get_encoding("gpt2")`.

## Expected Output Shape

```text
Input: low lower newest widest

Initial symbols:
  low -> l o w </w>

Step 1
  best pair: ('l', 'o') count=2
  merge: lo

Final toy BPE:
  low -> lo w </w>

GPT-2 comparison:
  ids: [...]
  pieces: [...]
```

## Verification

- Running with `--steps 0` should print initial symbols only.
- Running with more steps should never increase the number of symbols in a word.
- GPT-2 comparison should preserve round-trip decoding.
- Empty input should produce a clear error.

## Stretch Goals

- Add ANSI colors for merged pieces.
- Export merge history as JSON.
- Add `--corpus-file`.
- Show how leading spaces change GPT-2 tokens.
