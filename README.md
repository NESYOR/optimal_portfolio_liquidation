# Optimal Portfolio Liquidation

This project implements a stochastic control model for optimal portfolio liquidation.

## Project Structure

```
optimal_portfolio_liquidation/
├── data/
│   ├── raw/                      # Raw data for backtesting, if any (e.g., historical asset prices)
│   ├── processed/                # Processed data for faster loading in models
│   ├── simulations/              # Store generated simulation data for analysis
│   └── results/                  # Store final results of the simulation (e.g., CSVs of portfolio liquidation paths)
│
├── models/
│   ├── stochastic_models/        # Stochastic models for price simulation (e.g., geometric Brownian motion, Ornstein-Uhlenbeck)
│   ├── transaction_costs/        # Transaction cost models with different complexities
│   └── control_policies/         # Different policy algorithms (e.g., dynamic programming, reinforcement learning)
│
├── notebooks/                    # Jupyter notebooks for exploration and analysis
│   ├── EDA.ipynb                 # Exploratory data analysis
│   ├── model_experiments.ipynb   # Experiments on model parameters, tuning, etc.
│   └── results_analysis.ipynb    # Analyzing the outputs of the simulations
│
├── src/                          # Core source code of the project
│   ├── config.py                 # Configuration settings for the project
│   ├── data_loader.py            # Data loading and preprocessing functions
│   ├── main.py                   # Main script to run the simulation and liquidation strategy
│   ├── liquidation_strategy.py   # Implementation of the liquidation strategies
│   ├── risk_metrics.py           # Calculation of risk metrics (e.g., VaR, CVaR)
│   ├── utils.py                  # Utility functions for common tasks
│   └── visualization.py          # Visualization functions for plotting simulation results
│
├── tests/                        # Unit and integration tests
│   ├── test_data_loader.py       # Tests for data loading functions
│   ├── test_models.py            # Tests for stochastic models and transaction cost models
│   ├── test_liquidation.py       # Tests for liquidation strategies and control policies
│   └── test_risk_metrics.py      # Tests for risk metrics calculations
│
├── reports/                      # Documentation and reports
│   ├── figures/                  # Figures generated for reports or analysis
│   ├── project_report.md         # Markdown report or summary of the project
│   └── requirements.txt          # Dependencies and requirements for the project
│
├── environment.yml               # Conda or virtual environment file for dependencies
├── README.md                     # Project overview and instructions
└── .gitignore                    # Ignored files and folders for git
```

## Installation
Use `environment.yml` to set up the environment:
```
conda env create -f environment.yml
```

## Usage
Instructions to run the project.
