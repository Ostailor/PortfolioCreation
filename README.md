# Multi-Asset + Risk-Free Optimal Portfolio Web App

This Flask web application retrieves historical stock prices from Yahoo Finance for a list of tickers, computes the annualized expected returns and covariance matrix, and then solves for the optimal portfolio allocation for _N_ risky assets with a risk-free asset using the following formulas:

$$
\mathbf{w}^* = \frac{1}{\gamma}\,\Sigma^{-1}\,\bigl(\boldsymbol{\mu} - r_f\,\mathbf{1}\bigr),
$$
\[
c^* = 1 - \sum_{i=1}^N w_i^*,
\]
\[
\mu_p^* = \mathbf{w}^{*T}\,\boldsymbol{\mu} + c^*\,r_f,
\]
\[
\sigma_p^* = \sqrt{\mathbf{w}^{*T}\,\Sigma\,\mathbf{w}^*}.
\]

Where:
- \(\boldsymbol{\mu}\) is the vector of annualized expected returns.
- \(\Sigma\) is the annualized covariance matrix.
- \(r_f\) is the risk-free rate.
- \(\gamma\) is the investor's risk-aversion parameter.
- \(c^*\) is the allocation to the risk-free asset.

This version automatically retrieves data using Yahoo Finance and displays only the numerical optimal weights for the risky assets, the fraction allocated to the risk-free asset, and the overall portfolio return and standard deviation.

## Features

- **Yahoo Finance Integration:**  
  Automatically fetches historical adjusted closing prices for a user-specified list of tickers using `yfinance`.

- **Annualized Return & Covariance Calculation:**  
  Computes daily returns from price data and annualizes both the expected returns and the covariance matrix.

- **Optimal Portfolio Calculation:**  
  Uses the multi-asset plus risk-free formula to determine:
  - The optimal risky-asset weights \(w^*\)
  - The risk-free allocation \(c^*\)
  - The overall portfolio expected return \(\mu_p^*\)
  - The overall portfolio standard deviation \(\sigma_p^*\)

- **User-Friendly Interface:**  
  A simple web form built with Bootstrap that collects:
  - Comma-separated stock tickers
  - Start and end dates for the data
  - Risk-free rate and risk-aversion parameter

- **Results Display:**  
  Outputs the optimal weights for each risky asset, the fraction allocated to the risk-free asset, and the overall portfolio metrics.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
