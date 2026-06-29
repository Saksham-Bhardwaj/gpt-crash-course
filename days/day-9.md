# Day 9: Full Tiny GPT

## Goal

Stack transformer blocks into a complete GPT-style next-token model.

## Concept summary

A tiny GPT combines token embeddings, repeated transformer blocks, a final normalization layer, and a language-model head. The model outputs one logits vector per input position. During training, targets are the same token stream shifted left by one position, so every position learns to predict what comes next.

## Read

- `reference/chapters/07_gpt_model.md:1` - Complete GPT chapter.
- `reference/chapters/07_gpt_model.md:21` - Config.
- `reference/chapters/07_gpt_model.md:64` - Full model.
- `reference/chapters/07_gpt_model.md:284` - Parameters and buffers.
- `reference/chapters/07_gpt_model.md:299` - Logits.
- `reference/explanations and examples WIP/weight_tying.md:100` - Weight tying.

## Implement

Complete `exercises/exercise_06_gpt_model.py`.

Implement:

- `GPTConfig`.
- Token embedding.
- Transformer block stack.
- Final RMSNorm.
- LM head.
- Weight tying.
- Forward pass with optional cross-entropy loss.

Use tiny settings for local tests:

- `vocab_size=128`
- `d_model=32`
- `num_heads=4`
- `num_layers=2`
- `max_seq_len=16`

## Run

```bash
python exercises/exercise_06_gpt_model.py
```

Expected output:

- Logits shape `[2, 8, 128]`.
- Loss is a scalar when targets are provided.
- Embedding and LM head weights share memory.
- Final `exercise_06_gpt_model: ok`.

## Check

- Why does the model output logits for every position?
- Why do targets shift one token ahead of inputs?
- What does weight tying save?
- Why is cross-entropy a good loss for next-token prediction?

## Commit checkpoint

Commit:

- Completed GPT model exercise.

Suggested commit:

```bash
git add .
git commit -m "day 9: implement tiny gpt model"
```
