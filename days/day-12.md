# Day 12: Inference and Sampling

## Goal

Generate text one token at a time with temperature, top-k, and top-p controls.

## Read

- `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:3` - Training vs generation.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:16` - Naive generation loop.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:100` - Sampling strategies.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:115` - Temperature.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:146` - Top-k.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:156` - Top-p.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/09_inference.md:221` - Full inference code.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/sampling.md:61` - Temperature explainer.

## Implement

Complete `exercises/exercise_08_inference.py`.

Implement:

- Temperature scaling.
- Top-k filtering.
- Top-p filtering.
- One-token sampling.
- A generation loop that crops to `max_seq_len`.

## Run

```bash
python exercises/exercise_08_inference.py
```

Expected output:

- Filtered logits examples.
- Generated token IDs from a tiny random model.
- Final `exercise_08_inference: ok`.

## Check

- What happens when temperature approaches zero?
- How is top-k different from top-p?
- Why do we sample from probabilities instead of logits directly?
- Why does inference crop long context to `max_seq_len`?

## Commit checkpoint

Commit:

- Completed inference exercise.

Suggested commit:

```bash
git add .
git commit -m "day 12: implement inference sampling"
```
