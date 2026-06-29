# Day 11: Training Loop, Part 2

## Goal

Train a tiny GPT on your own text, save a checkpoint, and plot loss.

## Read

- `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:175` - Gradient accumulation.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:197` - Overfitting.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:285` - LR scheduler.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:366` - Training loop.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/perplexity.md:40` - Loss and perplexity.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/perplexity.md:204` - Perplexity during training.

## Implement

Finish Project 3 using `projects/project_3_custom_training.md`.

Create `projects/train_custom_tiny_gpt.py` that:

- Loads `data/my_text.txt`.
- Repeats or chunks text if needed.
- Trains a tiny GPT for a small number of steps.
- Logs loss every few steps.
- Saves `checkpoints/tiny_custom_gpt.pt`.
- Saves `outputs/loss_curve.png`.
- Writes a generated sample to `outputs/custom_sample.txt`.

## Run

```bash
python projects/train_custom_tiny_gpt.py --data data/my_text.txt --steps 100 --out checkpoints/tiny_custom_gpt.pt
```

Expected output:

- Loss printed during training.
- A checkpoint file.
- A loss curve PNG.
- A generated sample text file.

CPU note: use very small settings if needed: `d_model=64`, `num_layers=2`, `num_heads=4`, `max_seq_len=64`, `batch_size=4`.

## Check

- Why is a tiny custom model likely to overfit?
- Why does a falling loss not guarantee good prose?
- What should be saved in a checkpoint besides weights?
- What is the relationship between loss and perplexity?

## Commit checkpoint

Commit:

- `projects/train_custom_tiny_gpt.py`.
- A tiny sample dataset if it is suitable to publish.
- Do not commit large checkpoints unless intentionally publishing them.

Suggested commit:

```bash
git add .
git commit -m "day 11: train custom tiny gpt"
```
