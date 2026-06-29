# Day 5: Embeddings and RoPE

## Goal

Map token IDs to vectors and apply rotary position embeddings to query/key vectors.

## Read

- `/tmp/gpt-study/how-to-train-your-gpt/chapters/03_embeddings.md:1` - Embedding chapter intro.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/03_embeddings.md:43` - How embeddings are learned.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/03_embeddings.md:124` - Embedding code.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/04_positional_encoding.md:22` - RoPE overview.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/04_positional_encoding.md:42` - Numerical example.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/04_positional_encoding.md:126` - RoPE code.
- `/tmp/gpt-study/how-to-train-your-gpt/explanations and examples WIP/rope.md:47` - Simple RoPE explanation.

## Implement

Complete:

- `exercises/exercise_02_embeddings.py`
- `exercises/exercise_03_rope.py`

Build on Day 2:

- Token IDs are integer indexes.
- Embeddings turn each ID into a learned vector.
- RoPE modifies query/key vectors so attention depends on relative position.

## Run

```bash
python exercises/exercise_02_embeddings.py
python exercises/exercise_03_rope.py
```

Expected output:

- Embedding tensor shape `[batch, seq, d_model]`.
- RoPE tensor shape preserved.
- Final `ok` line from each exercise.

## Check

- Why is an embedding table just a learned matrix lookup?
- What shape do embeddings have for `[batch, seq]` token IDs?
- Why does RoPE apply to queries and keys rather than raw token IDs?
- What invariant should RoPE preserve about tensor shape?

## Commit checkpoint

Commit:

- Completed embedding and RoPE exercises.

Suggested commit:

```bash
git add .
git commit -m "day 5: implement embeddings and rope"
```
