# Volatility Study from Candlestick Data

The project analyses how much information a candlestick contains about volatility beyond the "classic" and often-used opening and closing prices. The final notebook shows the explanantions, equations and charts, with all the reusable functions that live in separate Python files.

## Research Scope

The large study covers the following themes:
- Browninan price simulations and within-step extremes
- parkinson, Garman-Klass, Rogers-Satchell and Yang-Zhang estimators for variance
- Estimators efficiency, discretisation bias and detection power
- Candlestick wicks, jumps and realised volatility
- A final empirical comparison using SPY, NFLX and GLD

## Repo Structure

- final_output.ipynb: research narrative and executable analysis
- pycode/: reusable Python functions and chart styling
- data/: saved market data
- results/: exported tables and figures
- requirements.txt: required Python libraries

## Running the Notebook

To run the final notebook output, follow the steps below:

1. Open the repository folder
2. Install the libraries listed in requirements.txt into a Python environment
3. Open final_output.ipynb
4. Select that environment as the notebook kernel

Run the cells from top to bottom.

## Current Progress

The project is a work in progress and this README will be progressively updated as I go on with the project.

## Simulation Assumptions

All the prices are simulated in log space, while each day's open is normalised to zero. The bridge formulas sample each within step extreme from its expected marginal distribution. Maximum and minimum use independent uniform draws, so the joint distribution is approximate.

## Data 

The simulation sections is generating their own data and the empirical section is going to use dated market data files from Yahoo Finance.
