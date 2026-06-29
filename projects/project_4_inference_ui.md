# Project 4: Inference UI

Days: 13-14

## Goal

Build a small inference interface with prompt input and decoding controls for temperature, top-k, and top-p.

## Deliverable

`projects/inference_ui.py`

## Requirements

- Accept a checkpoint path.
- Accept a prompt.
- Accept max new tokens.
- Accept temperature.
- Accept top-k.
- Accept top-p.
- Accept random seed.
- Generate text from the checkpoint.
- Print all settings used.
- Optionally save the prompt, settings, and generated text to a file.
- Provide a clear message if the checkpoint does not exist.

## Suggested CLI

```bash
python projects/inference_ui.py \
  --checkpoint checkpoints/tiny_custom_gpt.pt \
  --prompt "Once upon a time" \
  --max-new-tokens 80 \
  --temperature 0.8 \
  --top-k 50 \
  --top-p 0.95 \
  --seed 42 \
  --save outputs/final_demo.txt
```

## Implementation Plan

1. Parse CLI flags with `argparse`.
2. Load checkpoint.
3. Recreate the model config.
4. Load weights into the model.
5. Tokenize prompt.
6. Generate token by token using the Day 12 sampling logic.
7. Decode output IDs.
8. Print and optionally save a transcript.

## Expected Output

```text
checkpoint: checkpoints/tiny_custom_gpt.pt
prompt: Once upon a time
max_new_tokens: 80
temperature: 0.8
top_k: 50
top_p: 0.95
seed: 42

Once upon a time ...
```

## Verification

- Same seed and settings produce the same output.
- Missing checkpoint returns a helpful error.
- `--temperature 0` or very low temperature behaves more deterministically.
- `--save outputs/final_demo.txt` writes a complete transcript.

## Stretch Goals

- Add interactive REPL mode.
- Add a minimal web UI.
- Show token count and generation speed.
- Add repetition penalty.
- Add optional KV-cache notes or experimental implementation.
