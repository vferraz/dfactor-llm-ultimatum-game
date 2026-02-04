# D-Factor and the Ultimatum Game in Large Language Models

Reproduction package for the paper **"When Artificial Minds Negotiate: Dark Personality and the Ultimatum Game in Large Language Models"**.

This repository contains all code and materials needed to reproduce the experiments and analyses from the paper, which investigates how large language models exhibit personality-driven behavior in economic games when prompted with Dark Factor (D-Factor) personality traits.

## 📊 Data Availability

**⚠️ Important:** The data files are **not included** in this repository due to their size (~484 MB total).

**Download the data from OSF:** https://osf.io/rvph8/overview

After downloading, place the following files in the `analysis/data/` directory:
- `aidata.csv` (~422 MB) - Main AI experimental data
- `hudata.csv` (~1.4 MB) - Human benchmark data
- `frontier_models_results.csv` (~380 KB) - GPT frontier models results
- `strong_prompt_raw_data.csv` (~60 MB) - Strong prompt experimental data
- `strong_prompt_results.csv` (~1 KB) - Strong prompt summary statistics

## 📁 Repository Structure

```
dfactor-llm-ultimatum-game/
├── analysis/               # Analysis notebooks and outputs
│   ├── data/              # Data directory (download from OSF)
│   ├── Figures/           # Generated figures (created by notebooks)
│   ├── paper_core_analysis.ipynb          # Main analysis (Notebook 1)
│   ├── gpt_comparisons.ipynb              # GPT frontier models (Notebook 2)
│   ├── nlp_exploratory_analysis_v2.ipynb  # NLP analysis (Notebook 3)
│   ├── strong_prompt_analysis.ipynb       # Strong prompts (Notebook 4)
│   └── temperature_analysis.ipynb         # Temperature effects (Notebook 5)
│
├── experiment/            # Experiment code and prompts
│   ├── run_batch_wrapper.py              # Batch experiment runner
│   ├── d_traits.csv                      # D-Factor trait descriptions
│   ├── d_traits_strong.csv               # Strong D-Factor prompts
│   └── _*.ipynb / _*.txt                 # Prompt templates
│
├── LICENSE
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- Required Python packages (see Installation)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/dfactor-llm-ultimatum-game.git
   cd dfactor-llm-ultimatum-game
   ```

2. **Download the data:**
   - Visit https://osf.io/rvph8/overview
   - Download all CSV files
   - Place them in `analysis/data/`

3. **Install dependencies:**
   ```bash
   pip install pandas numpy matplotlib seaborn scipy statsmodels scikit-learn adjustText
   ```

   Or create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install pandas numpy matplotlib seaborn scipy statsmodels scikit-learn adjustText
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

The analysis is organized into 5 Jupyter notebooks. **Run them in order from the `analysis/` directory:**

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
**File:** `nlp_exploratory_analysis_v2.ipynb`

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
@article{yourname2025dfactor,
  title={When Artificial Minds Negotiate: Dark Personality and the Ultimatum Game in Large Language Models},
  author={Your Name},
  journal={Journal Name},
  year={2025}
}
```

## 📧 Contact

For questions or issues, please:
- Open an issue on GitHub
- Contact: [your email]

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Human benchmark data from [original study citation]
- D-Factor framework from Moshagen et al. (2018)
