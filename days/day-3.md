# Day 3: BPE Visualizer, Part 1

## Goal

Build the core BPE merge algorithm on a toy corpus.

## Concept summary

Byte pair encoding starts with small symbols and repeatedly merges frequent adjacent pairs. A toy implementation makes the compression logic visible: every merge replaces a common two-symbol pattern with one larger symbol. This is not the full production GPT tokenizer, but it explains why frequent chunks become single tokens over time.

## Read

- `reference/explanations and examples WIP/bpe_tokenization.md:74` - Build a vocabulary from scratch.
- `reference/explanations and examples WIP/bpe_tokenization.md:80` - Starting point.
- `reference/explanations and examples WIP/bpe_tokenization.md:97` - Round 1 merge.
- `reference/chapters/02_tokenization.md:32` - BPE step-by-step.

## Implement

Start Project 1 using `projects/project_1_tokenizer_visualizer.md`.

Create `projects/tokenizer_visualizer.py` with:

- `word_to_symbols(word)`.
- `count_pairs(words)`.
- `merge_pair(words, pair)`.
- A CLI demo for a tiny corpus such as `low lower newest widest`.

Keep the first version simple: one merge round is enough for Day 3.

## Run

```bash
python projects/tokenizer_visualizer.py --text "low lower newest widest" --steps 1
```

Expected output:

- Initial symbol sequences.
- Pair frequency table or best pair.
- Corpus after one merge.

## Check

- What is a symbol at the start of toy BPE?
- Why do we count adjacent pairs instead of arbitrary substrings?
- What changes in the corpus after one merge?
- How is toy BPE different from loading GPT-2's finished tokenizer?

## Commit checkpoint

Commit:

- `projects/tokenizer_visualizer.py`.
- A working one-step merge demo.

Suggested commit:

```bash
git add .
git commit -m "day 3: start bpe tokenizer visualizer"
```
