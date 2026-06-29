# Day 10: Training Loop, Part 1

## Goal

Build the training pieces and prove one optimization step updates the model.

## Read

- `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:3` - What training is.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:15` - Training loop visual.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:29` - Cross-entropy.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:88` - Backpropagation.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:122` - AdamW.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:212` - Complete training code.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/08_training.md:332` - Optimizer.

## Implement

Complete `exercises/exercise_07_training.py`.

Implement:

- Tiny text dataset.
- Input-target shifting.
- AdamW optimizer.
- One training step.
- Parameter-change verification.

Start Project 3 by reading `projects/project_3_custom_training.md`.

## Run

```bash
python exercises/exercise_07_training.py
```

Expected output:

- Initial loss.
- Loss after one or more tiny steps.
- Confirmation that at least one parameter changed.
- Final `exercise_07_training: ok`.

## Check

- What are inputs and targets in language-model training?
- What does `loss.backward()` compute?
- Why call `optimizer.zero_grad()`?
- Why can one step increase loss even though training is working?

## Commit checkpoint

Commit:

- Completed training exercise.
- Any starter files for custom training.

Suggested commit:

```bash
git add .
git commit -m "day 10: implement one training step"
```
