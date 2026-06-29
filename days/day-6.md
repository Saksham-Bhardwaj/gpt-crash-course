# Day 6: Attention Mechanics

## Goal

Implement scaled causal self-attention and prove tokens cannot attend to the future.

## Concept summary

Self-attention lets each token build a weighted mixture of other token representations. In a GPT, the causal mask blocks future positions so training matches generation: token `t` can only use tokens up to `t`. Scaling by `sqrt(head_dim)` keeps score magnitudes stable before softmax.

## Read

- `reference/chapters/05_attention.md:31` - Self-attention core idea.
- `reference/chapters/05_attention.md:55` - Math from words to scores.
- `reference/chapters/05_attention.md:90` - Attention scores.
- `reference/chapters/05_attention.md:108` - Scaling.
- `reference/chapters/05_attention.md:124` - Causal mask.
- `reference/chapters/05_attention.md:136` - Softmax weights.
- `reference/chapters/05_attention.md:149` - Weighted values.
- `reference/chapters/05_attention.md:360` - Full multi-head attention code.

## Implement

Complete `exercises/exercise_04_attention.py`.

Implement:

- Q/K/V projections.
- Head splitting and recombining.
- Scaled dot-product attention.
- Causal mask application.
- Attention-weight return for inspection.

Start Project 2 by reading `projects/project_2_attention_visualization.md`.

## Run

```bash
python exercises/exercise_04_attention.py
```

Expected output:

- Attention output shape equals input shape.
- Attention weights shape is `[batch, heads, seq, seq]`.
- Masked future positions have zero probability.
- Final `exercise_04_attention: ok`.

## Check

- Why divide attention scores by `sqrt(head_dim)`?
- Why are Q, K, and V different projections of the same input?
- What does the causal mask set to negative infinity?
- Why should each attention row sum to 1 after softmax?

## Commit checkpoint

Commit:

- Completed attention exercise.
- Any first project files for attention visualization.

Suggested commit:

```bash
git add .
git commit -m "day 6: implement causal attention"
```
