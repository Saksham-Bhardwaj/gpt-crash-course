# GPT Crash Course: 14 Days From Scratch

This repository is a self-contained, day-by-day curriculum for learning how GPT-style language models work by reading, implementing, training, and using a tiny GPT.

The reference implementation and reading material are bundled in `reference/`. Treat this repo as the single source of truth for the course: each day tells you what to read, what to implement, what to run, what to check, and what to commit.

## Prerequisites

- Python 3.10 or newer.
- Basic Python functions, classes, lists, dictionaries, and imports.
- Basic terminal usage: `cd`, virtual environments, running Python scripts, and reading command output.
- Basic Git usage for commits and diffs.
- Optional but helpful: prior PyTorch familiarity.

## Install

Standard learner setup:

```bash
git clone <this-repo-url>
cd gpt-crash-course
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For fully reproducible installs, use the pinned lock file:

```bash
pip install -r requirements.lock.txt
```

The course already includes the reference repo under `reference/`. If you are rebuilding or refreshing that bundled reference from upstream, use:

```bash
git clone <reference-repo-url> reference
rm -rf reference/.git reference/__pycache__
```

The exercises import reference components from `reference/main.py` where useful. Your job is to replace the TODOs with your own implementation and use the reference code only as a correctness guide.

## Hardware Requirements

- CPU is enough for all exercises and tiny smoke tests.
- 8 GB RAM is comfortable for the course scripts; 16 GB is better for notebooks and plotting.
- A CUDA or Apple Silicon GPU is optional and only useful for faster custom training.
- Keep Day 11 training settings small on CPU: `d_model=64`, `num_layers=2`, `num_heads=4`, `max_seq_len=64`, and `batch_size=4`.

## Common Commands

```bash
make setup
make test
make check
make clean
```

`make test` verifies repository imports and starter structure. `make check` runs every exercise script and is expected to pass after the learner completes the exercise TODOs.

Inference note: `temperature=0` is treated as greedy decoding, so generation picks the highest-logit token with `argmax` instead of sampling.

## 14-Day Schedule

### Day 1: Environment and GPT Mental Model

- Learning goal: Understand the GPT pipeline from text to tokens to logits.
- Read:
  - `reference/chapters/00_overview.md:1`
  - `reference/chapters/00_overview.md:38`
  - `reference/chapters/01_setup.md:61`
  - `reference/chapters/01_setup.md:104`
- Code:
  - Create and verify the Python environment.
  - Run import checks for `torch`, `tiktoken`, `datasets`, `numpy`, and `matplotlib`.
  - Inspect `reference/main.py`.
- Milestone: You can explain the full GPT training pipeline in one paragraph and run Python dependencies successfully.

### Day 2: Tokenization Basics

- Learning goal: Turn text into token IDs and back.
- Read:
  - `reference/chapters/02_tokenization.md:1`
  - `reference/chapters/02_tokenization.md:18`
  - `reference/chapters/02_tokenization.md:86`
  - `reference/chapters/02_tokenization.md:112`
- Code:
  - Complete `exercises/exercise_01_tokenizer.py`.
  - Compare common words, rare words, whitespace, emoji, and EOS token behavior.
- Milestone: You can explain why GPTs use subword tokens instead of raw words.

### Day 3: BPE Visualizer, Part 1

- Learning goal: Show BPE merges step by step on a toy corpus.
- Read:
  - `reference/explanations and examples WIP/bpe_tokenization.md:74`
  - `reference/explanations and examples WIP/bpe_tokenization.md:80`
  - `reference/explanations and examples WIP/bpe_tokenization.md:97`
- Code:
  - Start Project 1 in `projects/project_1_tokenizer_visualizer.md`.
  - Implement pair counting, best-pair selection, and one merge step.
- Milestone: A CLI script prints the most frequent BPE pair and the corpus after one merge.

### Day 4: BPE Visualizer, Part 2

- Learning goal: Build a useful tokenizer visualizer that compares toy BPE and GPT-2 tokenization.
- Read:
  - `reference/explanations and examples WIP/bpe_tokenization.md:126`
  - `reference/explanations and examples WIP/bpe_tokenization.md:182`
  - `reference/explanations and examples WIP/bpe_tokenization.md:202`
  - `reference/explanations and examples WIP/bpe_tokenization.md:237`
- Code:
  - Finish Project 1.
  - Add multi-step merge history, token color output, and GPT-2 token comparison.
- Milestone: `projects/tokenizer_visualizer.py` explains tokenization for any input sentence.

### Day 5: Embeddings and RoPE

- Learning goal: Convert token IDs into vectors and rotate query/key vectors by position.
- Read:
  - `reference/chapters/03_embeddings.md:1`
  - `reference/chapters/03_embeddings.md:43`
  - `reference/chapters/03_embeddings.md:124`
  - `reference/chapters/04_positional_encoding.md:22`
  - `reference/chapters/04_positional_encoding.md:126`
- Code:
  - Complete `exercises/exercise_02_embeddings.py`.
  - Complete `exercises/exercise_03_rope.py`.
- Milestone: You can explain the difference between token identity and token position.

### Day 6: Attention Mechanics

- Learning goal: Implement scaled causal self-attention for one batch.
- Read:
  - `reference/chapters/05_attention.md:31`
  - `reference/chapters/05_attention.md:55`
  - `reference/chapters/05_attention.md:124`
  - `reference/chapters/05_attention.md:360`
- Code:
  - Complete `exercises/exercise_04_attention.py`.
  - Start Project 2 in `projects/project_2_attention_visualization.md`.
- Milestone: Your attention weights are lower triangular and each row sums to 1.

### Day 7: Attention Visualization

- Learning goal: Visualize what each token can attend to in a sentence.
- Read:
  - `reference/chapters/05_attention.md:607`
  - `reference/chapters/05_attention.md:609`
  - `reference/explanations and examples WIP/attention.md:235`
  - `reference/explanations and examples WIP/causal_masking.md:121`
- Code:
  - Finish Project 2.
  - Render an attention heatmap using `matplotlib`.
- Milestone: `projects/attention_visualizer.py` saves a PNG heatmap for a sentence.

### Day 8: Transformer Block

- Learning goal: Combine attention, RMSNorm, residual connections, and SwiGLU into one block.
- Read:
  - `reference/chapters/06_transformer_block.md:18`
  - `reference/chapters/06_transformer_block.md:54`
  - `reference/chapters/06_transformer_block.md:138`
  - `reference/chapters/06_transformer_block.md:174`
  - `reference/chapters/06_transformer_block.md:225`
- Code:
  - Complete `exercises/exercise_05_transformer_block.py`.
- Milestone: A block accepts `[batch, seq, d_model]` and returns the same shape.

### Day 9: Full Tiny GPT

- Learning goal: Stack transformer blocks into a complete next-token model.
- Read:
  - `reference/chapters/07_gpt_model.md:1`
  - `reference/chapters/07_gpt_model.md:21`
  - `reference/chapters/07_gpt_model.md:64`
  - `reference/chapters/07_gpt_model.md:299`
  - `reference/explanations and examples WIP/weight_tying.md:100`
- Code:
  - Complete `exercises/exercise_06_gpt_model.py`.
- Milestone: Your model returns logits of shape `[batch, seq, vocab_size]` and a scalar loss when targets are passed.

### Day 10: Training Loop, Part 1

- Learning goal: Build a dataset, optimizer, scheduler, and minimal training step.
- Read:
  - `reference/chapters/08_training.md:3`
  - `reference/chapters/08_training.md:29`
  - `reference/chapters/08_training.md:122`
  - `reference/chapters/08_training.md:212`
  - `reference/chapters/08_training.md:332`
- Code:
  - Complete `exercises/exercise_07_training.py`.
  - Start Project 3 in `projects/project_3_custom_training.md`.
- Milestone: One optimization step changes model parameters and reports loss.

### Day 11: Training Loop, Part 2

- Learning goal: Train a tiny GPT on your own text and save a checkpoint.
- Read:
  - `reference/chapters/08_training.md:175`
  - `reference/chapters/08_training.md:197`
  - `reference/chapters/08_training.md:366`
  - `reference/explanations and examples WIP/perplexity.md:40`
  - `reference/explanations and examples WIP/perplexity.md:204`
- Code:
  - Finish Project 3.
  - Add checkpoint saving, loss plotting, and a short generated sample.
- Milestone: You have `checkpoints/tiny_custom_gpt.pt`, `outputs/loss_curve.png`, and a sample output.

### Day 12: Inference and Sampling

- Learning goal: Turn logits into generated text with temperature, top-k, and top-p.
- Read:
  - `reference/chapters/09_inference.md:3`
  - `reference/chapters/09_inference.md:16`
  - `reference/chapters/09_inference.md:100`
  - `reference/chapters/09_inference.md:221`
  - `reference/explanations and examples WIP/sampling.md:61`
- Code:
  - Complete `exercises/exercise_08_inference.py`.
- Milestone: You can generate text with deterministic and stochastic decoding settings.

### Day 13: Inference UI, Part 1

- Learning goal: Create a small UI for prompt input and decoding controls.
- Read:
  - `reference/chapters/09_inference.md:254`
  - `reference/chapters/09_inference.md:296`
  - `reference/explanations and examples WIP/sampling.md:109`
  - `reference/explanations and examples WIP/sampling.md:130`
- Code:
  - Start Project 4 in `projects/project_4_inference_ui.md`.
  - Build a CLI or Streamlit-style UI wrapper with temperature, top-k, top-p, and max-token controls.
- Milestone: The UI loads a checkpoint and generates from a prompt.

### Day 14: Inference UI, Part 2 and Final Review

- Learning goal: Polish the complete repo and prove the full learning path works end to end.
- Read:
  - `reference/chapters/10_full_script.md:1`
  - `reference/chapters/11_glossary.md:1`
  - `reference/explanations and examples WIP/kv_cache.md:39`
  - `reference/explanations and examples WIP/kv_cache.md:203`
- Code:
  - Finish Project 4.
  - Run every exercise self-check.
  - Add a final `outputs/final_demo.txt` with prompt, settings, and generated text.
- Milestone: You can explain and demo the entire path: tokenizer, embeddings, RoPE, attention, transformer block, GPT model, training, checkpointing, and inference.

## Daily Workflow

For each day:

1. Read that day file in `days/day-N.md`.
2. Read the referenced source sections.
3. Implement the assigned exercise or project.
4. Run the listed command.
5. Answer the check questions in your own words.
6. Commit the checkpoint.

Suggested commit pattern:

```bash
git add .
git commit -m "day N: short milestone description"
```

## Repository Layout

```text
.
|-- README.md
|-- ROADMAP.md
|-- NOTES.md
|-- days/
|-- exercises/
|-- projects/
|-- data/
|-- reference/
|-- tests/
|-- checkpoints/
`-- outputs/
```

## Troubleshooting

- `ModuleNotFoundError: source_imports`: run commands from the repo root, or use `python -m pytest` for tests.
- `FileNotFoundError: reference/main.py`: make sure the bundled `reference/` directory exists. If you intentionally deleted it, recreate it from the reference repo and remove its `.git` directory.
- `ModuleNotFoundError: tiktoken` or `torch`: activate `.venv` and reinstall with `pip install -r requirements.txt`.
- PyTorch reports no CUDA or MPS device: this is fine for the exercises. Use smaller training settings on CPU.
- Matplotlib cannot open a display: project scripts save PNGs to `outputs/`; they do not require an interactive display.
- Day 11 training is slow: reduce `--steps`, `batch_size`, `d_model`, `num_layers`, or `max_seq_len`.

## How To Contribute

1. Create a branch for the change.
2. Keep exercises learner-friendly: TODOs should be specific, and self-checks should be fast.
3. Keep generated files small. Do not commit large checkpoints or datasets.
4. Run `make test` and `make check` before opening a pull request.
5. Update day files and README sections when behavior, paths, or commands change.

## Completion Criteria

You are done when:

- All 14 daily checkpoints are committed.
- All 8 exercises have passing self-checks.
- All 4 mini-projects have runnable deliverables.
- You have trained a tiny GPT on custom text.
- You can generate text from the trained checkpoint using adjustable sampling settings.
