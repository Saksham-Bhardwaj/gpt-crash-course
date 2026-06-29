# Day 7: Attention Visualization

## Goal

Create heatmaps that show which previous tokens each token attends to.

## Read

- `/tmp/gpt-study/how-to-train-your-gpt/chapters/05_attention.md:607` - What the model sees.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/05_attention.md:609` - Attention heatmap.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/attention.md:235` - Full attention matrix.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/attention.md:251` - Multi-head attention.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/causal_masking.md:121` - Mask implementation.

## Implement

Finish Project 2 using `projects/project_2_attention_visualization.md`.

Create `projects/attention_visualizer.py` that:

- Tokenizes a sentence.
- Runs a tiny attention module.
- Extracts attention weights for one head.
- Saves a heatmap to `outputs/attention_heatmap.png`.
- Labels rows and columns with token pieces.

## Run

```bash
python projects/attention_visualizer.py --text "The cat sat on the mat" --out outputs/attention_heatmap.png
```

Expected output:

- A printed token list.
- A saved PNG at `outputs/attention_heatmap.png`.
- The heatmap should be lower triangular or visibly future-masked.

## Check

- What does a row in an attention heatmap represent?
- Why are future columns blank or near zero?
- Why might different heads learn different patterns?
- Is a random untrained attention heatmap semantically meaningful? Why or why not?

## Commit checkpoint

Commit:

- `projects/attention_visualizer.py`.
- Any generated heatmap only if you intentionally want it tracked.

Suggested commit:

```bash
git add .
git commit -m "day 7: build attention visualizer"
```
