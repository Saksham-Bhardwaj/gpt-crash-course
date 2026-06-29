# Day 2: Tokenization Basics

## Goal

Convert text to token IDs and back while understanding why GPT uses subword tokens.

## Concept summary

Tokenization is the bridge between human text and model tensors. GPT-style tokenizers usually use subword pieces, so common text chunks can be represented compactly while rare or new words can still be decomposed into smaller known pieces. Encoding must be reversible enough that decoding token IDs recreates the original text.

## Read

- `reference/chapters/02_tokenization.md:1` - Chapter intro.
- `reference/chapters/02_tokenization.md:18` - Subword tokenization.
- `reference/chapters/02_tokenization.md:32` - How BPE works.
- `reference/chapters/02_tokenization.md:86` - GPT tokenizer conventions.
- `reference/chapters/02_tokenization.md:95` - EOS token.
- `reference/chapters/02_tokenization.md:112` - Tokenizer code.

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
