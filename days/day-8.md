# Day 8: Transformer Block

## Goal

Combine attention, RMSNorm, residual connections, and SwiGLU into a transformer block.

## Read

- `/tmp/gpt-study/how-to-train-your-gpt/chapters/06_transformer_block.md:18` - Two sub-layers.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/06_transformer_block.md:54` - Residual connection.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/06_transformer_block.md:93` - Pre-norm vs post-norm.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/06_transformer_block.md:138` - RMSNorm code.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/06_transformer_block.md:174` - SwiGLU code.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/06_transformer_block.md:225` - Complete block.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/rmsnorm.md:74` - RMSNorm steps.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/swiglu.md:94` - SwiGLU steps.

## Implement

Complete `exercises/exercise_05_transformer_block.py`.

Implement:

- `RMSNorm`.
- `SwiGLU`.
- `TransformerBlock`.
- Pre-norm residual pattern:
  - `x = x + attention(norm1(x))`
  - `x = x + ffn(norm2(x))`

## Run

```bash
python exercises/exercise_05_transformer_block.py
```

Expected output:

- Input and output shapes match.
- The output differs from the input.
- Gradients flow through the block.
- Final `exercise_05_transformer_block: ok`.

## Check

- What problem do residual connections help solve?
- Why does the block preserve shape?
- What is normalized in RMSNorm?
- What does SwiGLU add compared with a plain linear layer?

## Commit checkpoint

Commit:

- Completed transformer block exercise.

Suggested commit:

```bash
git add .
git commit -m "day 8: implement transformer block"
```
