# Day 1: Environment and GPT Mental Model

## Goal

Understand the full GPT pipeline and verify your local Python environment.

## Read

- `/tmp/gpt-study/how-to-train-your-gpt/chapters/00_overview.md:1` - What a GPT is.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/00_overview.md:38` - Pipeline overview.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/00_overview.md:55` - What you will build.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/01_setup.md:61` - Installation.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/01_setup.md:104` - Complete import block.
- `/tmp/gpt-study/how-to-train-your-gpt/main.py:1` - Skim the full implementation.

## Implement

1. Create a virtual environment in this repo.
2. Install `requirements.txt`.
3. Create a short scratch script or one-liner that imports `torch`, `tiktoken`, `datasets`, `numpy`, and `matplotlib`.
4. Print the selected PyTorch device.
5. Read the class and function names in `/tmp/gpt-study/how-to-train-your-gpt/main.py` and write a 5-8 line summary in your own notes or commit message.

## Run

```bash
python - <<'PY'
import torch
import tiktoken
import datasets
import numpy
import matplotlib

print("torch", torch.__version__)
print("cuda", torch.cuda.is_available())
print("mps", hasattr(torch.backends, "mps") and torch.backends.mps.is_available())
print("tiktoken vocab", tiktoken.get_encoding("gpt2").n_vocab)
PY
```

Expected output:

- A PyTorch version.
- `cuda` or `mps` may be `False`; CPU is fine.
- GPT-2 tokenizer vocabulary size prints successfully.

## Check

- What is the input to a GPT model?
- What is the output of a GPT model before sampling?
- Why do we train on next-token prediction?
- Which file in the source repo contains the complete reference implementation?

## Commit checkpoint

Commit:

- Environment files you intentionally added.
- Any local notes you created.
- Confirmation that dependency imports work.

Suggested commit:

```bash
git add .
git commit -m "day 1: verify environment and gpt pipeline"
```
