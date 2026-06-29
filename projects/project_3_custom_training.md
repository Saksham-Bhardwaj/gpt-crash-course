# Project 3: Train a Tiny GPT on Custom Text

Days: 10-11

## Goal

Train a small GPT model on your own text, save a checkpoint, plot loss, and generate a sample.

## Deliverable

`projects/train_custom_tiny_gpt.py`

## Requirements

- Accept `--data`, `--steps`, and `--out`.
- Load text from `data/my_text.txt` or a user-specified file.
- Tokenize with GPT-2 `tiktoken`.
- Create input-target windows.
- Train a tiny GPT for a small number of steps.
- Print loss periodically.
- Save a checkpoint with:
  - model state dict
  - config
  - tokenizer name
  - training steps
- Save a loss curve to `outputs/loss_curve.png`.
- Generate a short sample and save it to `outputs/custom_sample.txt`.

## Suggested CLI

```bash
python projects/train_custom_tiny_gpt.py --data data/my_text.txt --steps 100 --out checkpoints/tiny_custom_gpt.pt
```

## Implementation Plan

1. Create or copy a small plain-text dataset into `data/my_text.txt`.
2. Load the text and repeat it if it is too short for several batches.
3. Tokenize all text once.
4. Build a dataset of fixed-length windows:
   - input: tokens `i : i + block_size`
   - target: tokens `i + 1 : i + block_size + 1`
5. Build a very small GPT:
   - `d_model=64`
   - `num_heads=4`
   - `num_layers=2`
   - `max_seq_len=64`
6. Train with AdamW.
7. Save checkpoint and loss curve.
8. Generate a short sample.

## Expected Output

```text
loaded tokens: 12345
parameters: 1234567
step 1 loss 10.8
step 10 loss 8.9
...
saved checkpoint: checkpoints/tiny_custom_gpt.pt
saved loss curve: outputs/loss_curve.png
saved sample: outputs/custom_sample.txt
```

## Verification

- The checkpoint can be loaded by Project 4.
- Loss values are finite.
- At least one generated sample is written.
- The model can overfit a tiny dataset if trained long enough.

## Stretch Goals

- Add validation loss.
- Add gradient clipping.
- Add resume-from-checkpoint.
- Add perplexity reporting.
