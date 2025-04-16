# basic-md-analysis

This project demonstrates the use of Python-based data science tools to explore and analyze molecular dynamics simulation data.

## Project Overview

The data used in this project comes from simulation outputs (GROMACS), representing quantities such as energy, temperature, and pressure over time. The goal is to apply scientific data analysis and visualization techniques to extract insights and demonstrate practical coding skills.

## Objectives

- Parse and clean raw simulation data using **Python**
- Explore trends in energy, temperature, or other observables
- Visualize time series and statistical distributions
- Automate parts of the analysis with custom scripts

## Tools & Libraries

- `numpy`
- `matplotlib`
- `seaborn`
- `jupyter`

## Folder Structure

<pre>
  simulation-data-analysis/ 
├── data/              # Raw and processed data 
├── notebooks/         # Main analysis notebook
├── scripts/           # Python scripts for preprocessing
├── figures/           # Exported plots
└── README.md
</pre>

## Example Visualizations

![energy plot](figures/energy_plot.png)

## How to Run

1. Clone the repository:

   git clone https://github.com/yourusername/basic-md-analysis.git
   
   cd basic-md-analysis

3. Create and activate a virtual environment (optional):

   python -m venv venv
   
   source venv/bin/activate  # or venv\Scripts\activate on Windows

4. Install dependencies:

   pip install -r requirements.txt

5. Open the notebook:

   jupyter notebook notebooks/analysis.ipynb

   ## Status

This is a personal project intended to practice data science techniques using scientific data. Future improvements may include:
- Interactive dashboard (e.g. Dash/Plotly)
- Integration with machine learning models
- More advanced simulation parsing tools


