# Experiment Directory

This directory contains the code and prompt templates for running the LLM ultimatum game experiments.

## Files

### Batch Runner
- **`run_batch_wrapper.py`** — Orchestrates multiple (game, model) runs, collecting results into a structured output directory with a manifest TSV.

### D-Factor Trait Descriptions
- **`d_traits.csv`** — D-Factor trait descriptions for levels D1–D5 (original/abstract prompts).
- **`d_traits_strong_proposer.csv`** — Behaviorally explicit D-Factor prompts for the proposer role.
- **`d_traits_strong_responder.csv`** — Behaviorally explicit D-Factor prompts for the responder role.

### Prompt Templates
Each role/condition combination has a `.txt` file (plain-text prompt template) and a `.ipynb` notebook (prompt construction):

| Role | Condition | Text Template | Notebook |
|------|-----------|---------------|----------|
| Proposer | D-Factor | `_proposer_dfactor.txt` | `_proposer_dfactor.ipynb` |
| Proposer | Raw | `_proposer_raw.txt` | `_proposer_raw.ipynb` |
| Proposer | Strong D-Factor | `_proposer_dfactor_strong.txt` | — |
| Responder | D-Factor | `_responder_dfactor.txt` | `_responder_dfactor.ipynb` |
| Responder | Raw | `_responder_raw.txt` | `_responder_raw.ipynb` |
| Responder | Strong D-Factor | `_responder_dfactor_strong.txt` | — |

### Other
- **`_proposer_ultimatum_questions.csv`** — Question prompts presented to proposer agents.
