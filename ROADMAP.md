# Roadmap

## Week 1: Foundation

### Milestone 1: GPT Pipeline and Environment

- [ ] Create a Python virtual environment.
- [ ] Install dependencies from `requirements.txt`.
- [ ] Verify imports.
- Estimated time: 2-3 hours
- Key concept learned: A GPT is a next-token prediction pipeline, not a magic text box.
- Deliverable: Working environment and Day 1 commit.

### Milestone 2: Tokenization

- [ ] Encode text into token IDs.
- [ ] Decode token IDs back to text.
- [ ] Inspect common, rare, whitespace, emoji, and EOS behavior.
- Estimated time: 3-4 hours
- Key concept learned: GPTs operate on token IDs, usually subword units.
- Deliverable: Completed `exercises/exercise_01_tokenizer.py`.

### Milestone 3: BPE Visualizer

- [ ] Count adjacent symbol pairs.
- [ ] Apply the highest-frequency merge.
- [ ] Show merge history over multiple rounds.
- [ ] Compare toy BPE output to GPT-2 tokens.
- Estimated time: 5-7 hours
- Key concept learned: BPE builds reusable subword chunks from repeated patterns.
- Deliverable: `projects/tokenizer_visualizer.py`.

### Milestone 4: Embeddings and RoPE

- [ ] Create token embedding lookup.
- [ ] Verify embedding output shapes.
- [ ] Implement `rotate_half`.
- [ ] Apply rotary position embeddings to query/key vectors.
- Estimated time: 4-5 hours
- Key concept learned: Token embeddings store meaning; RoPE injects position into attention geometry.
- Deliverable: Completed `exercise_02_embeddings.py` and `exercise_03_rope.py`.

### Milestone 5: Attention

- [ ] Project inputs into Q, K, and V.
- [ ] Compute scaled dot-product scores.
- [ ] Apply a causal mask.
- [ ] Softmax into attention weights.
- [ ] Visualize attention as a heatmap.
- Estimated time: 6-8 hours
- Key concept learned: Attention lets each token mix information from previous tokens according to learned relevance.
- Deliverable: Completed `exercise_04_attention.py` and `projects/attention_visualizer.py`.

## Week 2: Training + Inference + Extensions

### Milestone 6: Transformer Block

- [ ] Implement RMSNorm.
- [ ] Implement SwiGLU.
- [ ] Add pre-norm residual attention.
- [ ] Add pre-norm residual feed-forward.
- Estimated time: 4-5 hours
- Key concept learned: Transformer blocks alternate communication and private computation while preserving gradient flow.
- Deliverable: Completed `exercise_05_transformer_block.py`.

### Milestone 7: Tiny GPT Model

- [ ] Define model config.
- [ ] Stack transformer blocks.
- [ ] Add final normalization and LM head.
- [ ] Tie token embedding and output weights.
- [ ] Compute next-token loss.
- Estimated time: 4-6 hours
- Key concept learned: A GPT is repeated transformer blocks trained to predict the next token at every position.
- Deliverable: Completed `exercise_06_gpt_model.py`.

### Milestone 8: Training Pipeline

- [ ] Build a token sequence dataset.
- [ ] Create an AdamW optimizer.
- [ ] Run one training step.
- [ ] Run a short training loop.
- [ ] Save checkpoint and loss curve.
- Estimated time: 6-9 hours
- Key concept learned: Training reduces cross-entropy by nudging weights through backpropagation and AdamW.
- Deliverable: Completed `exercise_07_training.py` and `checkpoints/tiny_custom_gpt.pt`.

### Milestone 9: Inference and Sampling

- [ ] Load a model checkpoint.
- [ ] Generate one token at a time.
- [ ] Implement temperature scaling.
- [ ] Implement top-k filtering.
- [ ] Implement top-p filtering.
- Estimated time: 4-5 hours
- Key concept learned: Decoding controls trade off determinism, diversity, and coherence.
- Deliverable: Completed `exercise_08_inference.py`.

### Milestone 10: Inference UI and Final Demo

- [ ] Build prompt input.
- [ ] Add temperature, top-k, top-p, and max-token controls.
- [ ] Show generated text and settings.
- [ ] Save a final demo transcript.
- [ ] Run all exercise self-checks.
- Estimated time: 5-7 hours
- Key concept learned: A model becomes useful when its inference path is controlled, repeatable, and inspectable.
- Deliverable: `projects/inference_ui.py` and `outputs/final_demo.txt`.
