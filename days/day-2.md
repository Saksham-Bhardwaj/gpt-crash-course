# Day 2: Tokenization Basics

## Goal

Convert text to token IDs and back while understanding why GPT uses subword tokens.

## Read

- `/tmp/gpt-study/how-to-train-your-gpt/chapters/02_tokenization.md:1` - Chapter intro.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/02_tokenization.md:18` - Subword tokenization.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/02_tokenization.md:32` - How BPE works.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/02_tokenization.md:86` - GPT tokenizer conventions.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/02_tokenization.md:95` - EOS token.
- `/tmp/gpt-study/how-to-train-your-gpt/chapters/02_tokenization.md:112` - Tokenizer code.

## Implement

Complete `exercises/exercise_01_tokenizer.py`.

Focus on:

- Importing `SimpleTokenizer` from the source repo.
- Encoding and decoding text.
- Inspecting individual token strings.
- Appending EOS between documents.

## Run

```bash
python exercises/exercise_01_tokenizer.py
```

Expected output:

- Token IDs for several text examples.
- Decoded text matching the original examples.
- A final line similar to `exercise_01_tokenizer: ok`.

## Check

- Why is `" hello"` often a different token from `"hello"`?
- What problem does EOS solve when combining documents?
- Why can BPE handle words it has never seen?
- What does `decode(encode(text))` prove, and what does it not prove?

## Commit checkpoint

Commit:

- Completed `exercises/exercise_01_tokenizer.py`.
- Any notes about tokenization surprises.

Suggested commit:

```bash
git add .
git commit -m "day 2: implement tokenizer exercise"
```
