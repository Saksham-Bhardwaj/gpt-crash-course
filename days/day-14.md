# Day 14: Inference UI, Part 2 and Final Review

## Goal

Polish the repo and demonstrate the full GPT path end to end.

## Concept summary

The final review ties the system together from raw text to generated text. The tokenizer maps text to IDs, embeddings map IDs to vectors, transformer blocks update vectors with causal context, the LM head maps vectors to logits, and sampling turns logits back into new token IDs. A polished demo proves each handoff works.

## Read

- `reference/chapters/10_full_script.md:1` - Full script.
- `reference/chapters/11_glossary.md:1` - Glossary.
- `reference/explanations and examples WIP/kv_cache.md:39` - Why KV cache matters.
- `reference/explanations and examples WIP/kv_cache.md:203` - KV cache tradeoff.

## Implement

Finish Project 4.

Polish:

- Helpful CLI help text.
- Stable checkpoint loading.
- Seeded generation.
- Output saved to `outputs/final_demo.txt`.
- Clear README/project notes if your UI requires an optional dependency.

Run every exercise self-check:

```bash
for f in exercises/exercise_*.py; do python "$f"; done
```

## Run

```bash
python projects/inference_ui.py --checkpoint checkpoints/tiny_custom_gpt.pt --prompt "The model learned" --max-new-tokens 120 --temperature 0.8 --top-k 50 --top-p 0.95 --seed 42 --save outputs/final_demo.txt
```

Expected output:

- Generated text in the terminal.
- `outputs/final_demo.txt` containing prompt, settings, and generation.
- All exercise self-checks pass.

## Check

- Explain the full data flow from raw text to generated text.
- What part of the model learns token meaning?
- What part lets tokens read previous tokens?
- What part converts hidden vectors into next-token logits?
- What would KV cache speed up, and what memory cost would it add?

## Commit checkpoint

Commit:

- Final inference UI.
- Final demo output if you intentionally want it tracked.
- Any documentation fixes.

Suggested commit:

```bash
git add .
git commit -m "day 14: finish gpt crash course"
```
