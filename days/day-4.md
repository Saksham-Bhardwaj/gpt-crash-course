# Day 4: BPE Visualizer, Part 2

## Goal

Finish a tokenizer visualizer that shows multi-step BPE and compares against GPT-2 tokens.

## Read

- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:126` - Round 2.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:153` - Round 3.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:182` - Final result.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:202` - GPT-2 real text.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:237` - Space handling.

## Implement

Finish Project 1.

Add:

- Multi-step merge history.
- A `--steps` argument.
- GPT-2 token IDs and token bytes for the input sentence.
- Clear output that distinguishes toy BPE from GPT-2's production tokenizer.

## Run

```bash
python projects/tokenizer_visualizer.py --text "antidisestablishmentarianism is weird" --steps 8 --compare-gpt2
```

Expected output:

- A numbered merge history.
- Final toy symbols.
- GPT-2 token IDs and decoded pieces.

## Check

- Why does BPE make common chunks shorter to represent?
- Why can rare words still become many tokens?
- How does leading whitespace affect GPT-2 tokenization?
- Why is a toy BPE visualizer useful even though it is not GPT-2's exact training algorithm?

## Commit checkpoint

Commit:

- Completed tokenizer visualizer.
- Example output or README note if you captured one.

Suggested commit:

```bash
git add .
git commit -m "day 4: finish bpe tokenizer visualizer"
```
