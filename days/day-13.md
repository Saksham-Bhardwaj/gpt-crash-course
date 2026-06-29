# Day 13: Inference UI, Part 1

## Goal

Build a prompt-driven inference UI with decoding controls.

## Concept summary

An inference UI wraps generation in repeatable controls. The checkpoint defines model weights, the prompt defines initial context, and decoding settings define how deterministic or varied the continuation will be. Printing the settings with the output makes samples reproducible and easier to compare.

## Read

- `reference/chapters/09_inference.md:254` - Text generation wrapper.
- `reference/chapters/09_inference.md:296` - Interactive example.
- `reference/explanations and examples WIP/sampling.md:109` - Top-k.
- `reference/explanations and examples WIP/sampling.md:130` - Top-p.
- `reference/explanations and examples WIP/sampling.md:164` - Recommended combination.

## Implement

Start Project 4 using `projects/project_4_inference_ui.md`.

Create `projects/inference_ui.py` as either:

- A CLI with flags and interactive prompt mode, or
- A small local web UI if you prefer adding a UI dependency.

Required controls:

- Prompt text.
- Max new tokens.
- Temperature.
- Top-k.
- Top-p.
- Random seed.
- Checkpoint path.

## Run

```bash
python projects/inference_ui.py --checkpoint checkpoints/tiny_custom_gpt.pt --prompt "Once upon a time" --max-new-tokens 80 --temperature 0.8 --top-k 50 --top-p 0.95
```

Expected output:

- The settings used.
- The prompt.
- Generated text.
- A clear error if the checkpoint is missing, with instructions to run Day 11 first.

## Check

- Which settings make generation more deterministic?
- Which settings make generation more diverse?
- Why should the UI print the exact decoding settings?
- How do you reproduce a previous sample?

## Commit checkpoint

Commit:

- First working version of `projects/inference_ui.py`.

Suggested commit:

```bash
git add .
git commit -m "day 13: build inference ui"
```
