# Project 2: Attention Visualization

Days: 6-7

## Goal

Generate a heatmap that shows causal self-attention weights for a sentence.

## Deliverable

`projects/attention_visualizer.py`

## Requirements

- Accept text from `--text`.
- Tokenize with GPT-2 `tiktoken`.
- Build or reuse a tiny multi-head attention module.
- Run a forward pass.
- Extract attention weights for one batch item and one head.
- Save a heatmap PNG to `--out`.
- Label axes with token pieces.
- Make future positions visibly masked.

## Suggested CLI

```bash
python projects/attention_visualizer.py --text "The cat sat on the mat" --out outputs/attention_heatmap.png
```

## Implementation Plan

1. Tokenize the input sentence.
2. Create random embeddings for token IDs or use an `nn.Embedding`.
3. Implement attention that returns both output and attention weights.
4. Select `weights[0, head_index]`.
5. Use `matplotlib.pyplot.imshow` to render the matrix.
6. Add token labels on x and y axes.
7. Save the figure.

## Expected Output

```text
tokens: ['The', ' cat', ' sat', ' on', ' the', ' mat']
attention shape: torch.Size([1, 4, 6, 6])
saved: outputs/attention_heatmap.png
```

## Verification

- The attention matrix shape is `[seq, seq]` after selecting batch and head.
- Rows sum to 1.
- Entries above the diagonal are zero or visually blank.
- The saved PNG opens successfully.

## Stretch Goals

- Add `--head`.
- Save all heads in a subplot grid.
- Add a trained-checkpoint mode that visualizes a real model's attention.
- Export the attention matrix as CSV.
