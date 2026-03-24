# D-Factor and the Ultimatum Game in Large Language Models

Reproduction package for the paper **"When Artificial Minds Negotiate: Dark Personality and the Ultimatum Game in Large Language Models"**.

This repository contains all code and materials needed to reproduce the experiments and analyses from the paper, which investigates how large language models exhibit personality-driven behavior in economic games when prompted with Dark Factor (D-Factor) personality traits.

## 📊 Data Availability

**⚠️ Important:** The data files are **not included** in this repository due to their size (~484 MB total).

**Download the data from OSF:** https://osf.io/rvph8

After downloading, place the following files in the `analysis/data/` directory:
- `aidata.csv` (~422 MB) - Main AI experimental data
- `hudata.csv` (~1.4 MB) - Human benchmark data
- `frontier_models_results.csv` (~380 KB) - GPT frontier models results
- `strong_prompt_raw_data.csv` (~60 MB) - Strong prompt experimental data
- `strong_prompt_results.csv` (~1 KB) - Strong prompt summary statistics

## 📁 Repository Structure

```
dfactor-llm-ultimatum-game/
├── analysis/                              # Analysis notebooks and outputs
│   ├── data/                              # Data directory (download from OSF)
│   ├── paper_core_analysis.ipynb          # Main analysis (Notebook 1)
│   ├── gpt_comparisons.ipynb              # GPT frontier models (Notebook 2)
│   ├── nlp_exploratory_analysis.ipynb     # NLP analysis (Notebook 3)
│   ├── strong_prompt_analysis.ipynb       # Strong prompts (Notebook 4)
│   ├── temperature_analysis.ipynb         # Temperature effects (Notebook 5)
│   └── causal_decomposition_analysis.ipynb # Causal decomposition (Notebook 6)
│
├── experiment/                            # Experiment code and prompts
│   ├── run_batch_wrapper.py               # Batch experiment runner
│   ├── d_traits.csv                       # D-Factor trait descriptions
│   ├── d_traits_strong_proposer.csv       # Strong D-Factor prompts (proposer)
│   ├── d_traits_strong_responder.csv      # Strong D-Factor prompts (responder)
│   └── _*.ipynb / _*.txt                  # Prompt templates
│
├── pyproject.toml
├── requirements.txt
├── LICENSE
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Jupyter Notebook or JupyterLab
- Required Python packages (see Installation)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vferraz/dfactor-llm-ultimatum-game.git
   cd dfactor-llm-ultimatum-game
   ```

2. **Download the data:**
   - Visit https://osf.io/rvph8/overview
   - Download all CSV files
   - Place them in `analysis/data/`

3. **Install dependencies:**

   **Option A: Using UV (recommended, faster):**
   ```bash
   # Install UV if you haven't already: https://github.com/astral-sh/uv
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Create virtual environment and install dependencies
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

   **Option B: Using pip with requirements.txt:**
   ```bash
   pip install -r requirements.txt
   ```

   **Option C: Using pip in a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Verify Installation

Check that data files are in place:
```bash
ls -lh analysis/data/
```

You should see:
- `aidata.csv`
- `hudata.csv`
- `frontier_models_results.csv`
- `strong_prompt_raw_data.csv`
- `strong_prompt_results.csv`

## 📓 Analysis Notebooks

The analysis is organized into 6 Jupyter notebooks. **Run them in order from the `analysis/` directory:**

### Notebook 1: Core Paper Analysis
**File:** `paper_core_analysis.ipynb`

Main results for the paper including:
- D-Factor correlations with proposer fairness and responder acceptance
- Model-by-model breakdowns
- Human benchmark comparisons
- Role asymmetry analysis

**Key outputs:** Main paper figures, correlation tables

---

### Notebook 2: GPT Frontier Models
**File:** `gpt_comparisons.ipynb`

Analysis of GPT-4.1 and GPT-5.1 frontier models:
- Comparison with open-source models
- Temperature effects in frontier models
- Statistical comparisons

**Key outputs:** GPT comparison figures

---

### Notebook 3: NLP Exploratory Analysis
**File:** `nlp_exploratory_analysis.ipynb`

Text analysis of LLM justifications:
- Keyword extraction and visualization
- t-SNE semantic space visualization
- Regression of keywords on D-Factor levels
- Proposer vs responder language patterns

**Key outputs:** NLP visualizations, keyword regression results

---

### Notebook 4: Strong Prompt Analysis
**File:** `strong_prompt_analysis.ipynb`

Analysis of behaviorally-explicit D-Factor prompts:
- Original vs. strong prompt comparisons
- D-correlation shifts
- Model-by-model breakdown
- Role-specific effects

**Key outputs:** Strong prompt comparison figures

---

### Notebook 5: Temperature Analysis
**File:** `temperature_analysis.ipynb`

Analysis of temperature effects (0.0, 0.7, 1.4) on behavior:
- Variance in prosocial behavior by temperature
- D-Factor interaction with temperature
- Model-specific temperature sensitivity

**Key outputs:** Temperature effect tables and figures

---

### Notebook 6: Causal Decomposition
**File:** `causal_decomposition_analysis.ipynb`

Causal decomposition of D-Factor effects on LLM behavior:
- Variance decomposition (direct, indirect, total effects)
- Mediation analysis with bootstrap confidence intervals
- Nested ANOVA for model-level causal pathways

**Key outputs:** Causal decomposition figures

## 🔬 Running the Experiments

To replicate the data collection (requires API access):

1. Configure API credentials in `experiment/` directory
2. Run the batch wrapper:
   ```bash
   cd experiment
   python run_batch_wrapper.py
   ```

**Note:** Running experiments requires access to LLM APIs (OpenAI, Anthropic, etc.) and may incur costs. The pre-collected data in OSF is sufficient for reproducing all analyses.

## 📄 Citation

If you use this code or data, please cite:

```bibtex
@article{ferraz2026artificial,
  title={When artificial minds negotiate: Dark personality and the Ultimatum Game in large language models},
  author={Ferraz, Vin{\'\i}cius and Olah, Tamas and Sazedul, Ratin and Schmidt, Robert and Schwieren, Christiane},
  journal={Computers in Human Behavior: Artificial Humans},
  pages={100281},
  year={2026},
  publisher={Elsevier}
}
```

**DOI:** https://doi.org/10.1016/j.chbah.2026.100281

## 📧 Contact

For questions or issues, please:
- Open an issue on GitHub
- Contact: visferraz@gmail.com

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Human benchmark data from Hilbig & Thielmann (2025).
- D-Factor framework from Moshagen et al. (2018)
