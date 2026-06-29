"""Exercise 01: Tokenization.

Concept:
    GPTs do not read Python strings directly. Text is converted into integer
    token IDs, and those IDs are what the model sees. This exercise practices
    encoding, decoding, token-piece inspection, and EOS-separated documents.

Source reference:
    reference/chapters/02_tokenization.md
    reference/main.py
"""

from __future__ import annotations

from source_imports import load_source_main


source = load_source_main()
SimpleTokenizer = source.SimpleTokenizer


def encode_text(tokenizer: SimpleTokenizer, text: str) -> list[int]:
    """Return token IDs for text."""
    # TODO: call the tokenizer's encode method.
    raise NotImplementedError("TODO: implement encode_text")


def decode_tokens(tokenizer: SimpleTokenizer, token_ids: list[int]) -> str:
    """Return text for token IDs."""
    # TODO: call the tokenizer's decode method.
    raise NotImplementedError("TODO: implement decode_tokens")


def token_pieces(tokenizer: SimpleTokenizer, text: str) -> list[str]:
    """Return the decoded string piece for each token in text."""
    # TODO: encode text, then decode each token ID individually.
    raise NotImplementedError("TODO: implement token_pieces")


def join_documents_with_eos(tokenizer: SimpleTokenizer, docs: list[str]) -> list[int]:
    """Encode docs and insert EOS after each document."""
    # TODO: extend a list with each encoded document, then append eos_token_id.
    raise NotImplementedError("TODO: implement join_documents_with_eos")


if __name__ == "__main__":
    tok = SimpleTokenizer()
    text = "Hello, tokenizer!"

    ids = encode_text(tok, text)
    decoded = decode_tokens(tok, ids)
    pieces = token_pieces(tok, " hello hello")
    docs = join_documents_with_eos(tok, ["The cat sat.", "The dog ran."])

    print("ids:", ids)
    print("decoded:", decoded)
    print("pieces:", pieces)
    print("docs with eos:", docs)

    assert isinstance(ids, list)
    assert all(isinstance(i, int) for i in ids)
    assert decoded == text
    assert len(pieces) >= 2
    assert docs.count(tok.eos_token_id) == 2
    print("exercise_01_tokenizer: ok")
