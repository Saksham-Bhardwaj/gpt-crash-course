# Using Codex Effectively

Use one fresh Codex session per day. This keeps context small and avoids relying on memory from previous sessions.

Example for Day 7:

```bash
codex exec --dangerously-bypass-approvals-and-sandbox -C /tmp/gpt-crash-course "Load day 7 plan from days/day-7.md. Read the relevant chapter from /tmp/gpt-study/how-to-train-your-gpt. Help me implement the exercise and verify it works."
```

Why this works:

- Each `days/day-N.md` file contains the goal, reading anchors, implementation task, run command, checks, and commit checkpoint.
- Codex only needs the current day file plus the referenced source sections.
- The repo remains the source of truth. There are no hidden instructions in chat history.
- Every day ends with a commit, so progress is recoverable.

Recommended daily pattern:

```bash
codex exec --dangerously-bypass-approvals-and-sandbox -C /tmp/gpt-crash-course "Load day N plan from days/day-N.md. Read the relevant source sections from /tmp/gpt-study/how-to-train-your-gpt. Help me implement the task, run the checks, and prepare the commit."
```

Good prompts are specific:

```text
Load day 10. Implement only exercise_07_training.py. Keep the code beginner-readable. Run the self-check and explain any failure.
```

```text
Load project_3_custom_training.md and day 11. Help me train on data/my_text.txt for 100 steps, save the checkpoint, and generate a sample.
```

Commit after each day:

```bash
git status --short
git add .
git commit -m "day N: milestone"
```

When stuck, ask Codex to inspect the exact files:

```text
Read days/day-6.md, exercises/exercise_04_attention.py, and the attention chapter anchors. Explain what shape each tensor should have before editing code.
```

This crash course is designed so a future Codex session can resume from the repo alone.
