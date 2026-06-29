# GPT Crash Course: 14 Days From Scratch

This repository is a self-contained, day-by-day curriculum for learning how GPT-style language models work by reading, implementing, training, and using a tiny GPT.

The source reference is the local repo at:

`/tmp/gpt-study/how-to-train-your-gpt`

Treat this repo as the single source of truth for the course. Each day tells you exactly what to read, what to implement, what to run, what to check, and what to commit.

## Prerequisites

- Python 3.10+
- Basic Python functions, classes, and lists
- Basic terminal usage
- Optional but helpful: PyTorch familiarity

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The exercises import reference components from `/tmp/gpt-study/how-to-train-your-gpt/main.py` where useful. Your job is to replace the TODOs with your own implementation and use the reference code only as a correctness guide.

## 14-Day Schedule

### Day 1: Environment and GPT Mental Model

- Learning goal: Understand the GPT pipeline from text to tokens to logits.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/00_overview.md:1`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/00_overview.md:38`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/01_setup.md:61`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/01_setup.md:104`
- Code:
  - Create and verify the Python environment.
  - Run import checks for `torch`, `tiktoken`, `datasets`, `numpy`, and `matplotlib`.
  - Inspect `/tmp/gpt-study/how-to-train-your-gpt/main.py`.
- Milestone: You can explain the full GPT training pipeline in one paragraph and run Python dependencies successfully.

### Day 2: Tokenization Basics

- Learning goal: Turn text into token IDs and back.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/02_tokenization.md:1`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/02_tokenization.md:18`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/02_tokenization.md:86`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/02_tokenization.md:112`
- Code:
  - Complete `exercises/exercise_01_tokenizer.py`.
  - Compare common words, rare words, whitespace, emoji, and EOS token behavior.
- Milestone: You can explain why GPTs use subword tokens instead of raw words.

### Day 3: BPE Visualizer, Part 1

- Learning goal: Show BPE merges step by step on a toy corpus.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:74`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:80`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:97`
- Code:
  - Start Project 1 in `projects/project_1_tokenizer_visualizer.md`.
  - Implement pair counting, best-pair selection, and one merge step.
- Milestone: A CLI script prints the most frequent BPE pair and the corpus after one merge.

### Day 4: BPE Visualizer, Part 2

- Learning goal: Build a useful tokenizer visualizer that compares toy BPE and GPT-2 tokenization.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:126`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:182`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:202`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/bpe_tokenization.md:237`
- Code:
  - Finish Project 1.
  - Add multi-step merge history, token color output, and GPT-2 token comparison.
- Milestone: `projects/tokenizer_visualizer.py` explains tokenization for any input sentence.

### Day 5: Embeddings and RoPE

- Learning goal: Convert token IDs into vectors and rotate query/key vectors by position.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/03_embeddings.md:1`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/03_embeddings.md:43`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/03_embeddings.md:124`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/04_positional_encoding.md:22`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/04_positional_encoding.md:126`
- Code:
  - Complete `exercises/exercise_02_embeddings.py`.
  - Complete `exercises/exercise_03_rope.py`.
- Milestone: You can explain the difference between token identity and token position.

### Day 6: Attention Mechanics

- Learning goal: Implement scaled causal self-attention for one batch.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/05_attention.md:31`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/05_attention.md:55`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/05_attention.md:124`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/05_attention.md:360`
- Code:
  - Complete `exercises/exercise_04_attention.py`.
  - Start Project 2 in `projects/project_2_attention_visualization.md`.
- Milestone: Your attention weights are lower triangular and each row sums to 1.

### Day 7: Attention Visualization

- Learning goal: Visualize what each token can attend to in a sentence.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/05_attention.md:607`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/05_attention.md:609`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/attention.md:235`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/causal_masking.md:121`
- Code:
  - Finish Project 2.
  - Render an attention heatmap using `matplotlib`.
- Milestone: `projects/attention_visualizer.py` saves a PNG heatmap for a sentence.

### Day 8: Transformer Block

- Learning goal: Combine attention, RMSNorm, residual connections, and SwiGLU into one block.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/06_transformer_block.md:18`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/06_transformer_block.md:54`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/06_transformer_block.md:138`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/06_transformer_block.md:174`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/06_transformer_block.md:225`
- Code:
  - Complete `exercises/exercise_05_transformer_block.py`.
- Milestone: A block accepts `[batch, seq, d_model]` and returns the same shape.

### Day 9: Full Tiny GPT

- Learning goal: Stack transformer blocks into a complete next-token model.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/07_gpt_model.md:1`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/07_gpt_model.md:21`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/07_gpt_model.md:64`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/07_gpt_model.md:299`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/weight_tying.md:100`
- Code:
  - Complete `exercises/exercise_06_gpt_model.py`.
- Milestone: Your model returns logits of shape `[batch, seq, vocab_size]` and a scalar loss when targets are passed.

### Day 10: Training Loop, Part 1

- Learning goal: Build a dataset, optimizer, scheduler, and minimal training step.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:3`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:29`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:122`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:212`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:332`
- Code:
  - Complete `exercises/exercise_07_training.py`.
  - Start Project 3 in `projects/project_3_custom_training.md`.
- Milestone: One optimization step changes model parameters and reports loss.

### Day 11: Training Loop, Part 2

- Learning goal: Train a tiny GPT on your own text and save a checkpoint.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:175`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:197`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:366`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/perplexity.md:40`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/perplexity.md:204`
- Code:
  - Finish Project 3.
  - Add checkpoint saving, loss plotting, and a short generated sample.
- Milestone: You have `checkpoints/tiny_custom_gpt.pt`, `outputs/loss_curve.png`, and a sample output.

### Day 12: Inference and Sampling

- Learning goal: Turn logits into generated text with temperature, top-k, and top-p.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:3`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:16`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:100`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:221`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/sampling.md:61`
- Code:
  - Complete `exercises/exercise_08_inference.py`.
- Milestone: You can generate text with deterministic and stochastic decoding settings.

### Day 13: Inference UI, Part 1

- Learning goal: Create a small UI for prompt input and decoding controls.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:254`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:296`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/sampling.md:109`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/sampling.md:130`
- Code:
  - Start Project 4 in `projects/project_4_inference_ui.md`.
  - Build a CLI or Streamlit-style UI wrapper with temperature, top-k, top-p, and max-token controls.
- Milestone: The UI loads a checkpoint and generates from a prompt.

### Day 14: Inference UI, Part 2 and Final Review

- Learning goal: Polish the complete repo and prove the full learning path works end to end.
- Read:
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/10_full_script.md:1`
  - `/tmp/gpt-study/how-to-train-your-gpt/chapters/11_glossary.md:1`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/kv_cache.md:39`
  - `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/kv_cache.md:203`
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
|-- checkpoints/
`-- outputs/
```

## Completion Criteria

You are done when:

- All 14 daily checkpoints are committed.
- All 8 exercises have passing self-checks.
- All 4 mini-projects have runnable deliverables.
- You have trained a tiny GPT on custom text.
- You can generate text from the trained checkpoint using adjustable sampling settings.
