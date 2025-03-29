import numpy as np
import pandas as pd
import yfinance as yf

def fetch_data_from_yahoo(tickers, start_date, end_date):
    """
    Download historical adjusted closing prices for the given tickers.
    Returns a DataFrame with dates as index and ticker symbols as columns.
    """
    data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)['Close']
    # If a single ticker is passed, convert Series to DataFrame.
    if isinstance(data, pd.Series):
        data = data.to_frame(name=tickers[0])
    return data

def compute_returns_and_cov(data):
    """
    Compute daily returns from price data and annualize expected returns and covariance.
    
    Returns:
      mu: numpy array of annualized expected returns (N,)
      Sigma: numpy array of annualized covariance matrix (N x N)
      tickers: list of tickers corresponding to columns of data.
    """
    daily_returns = data.pct_change().dropna()
    mu_daily = daily_returns.mean()
    cov_daily = daily_returns.cov()
    
    # Assume 252 trading days per year
    mu_annual = mu_daily * 252
    cov_annual = cov_daily * 252
    
    tickers = list(data.columns)
    mu = mu_annual.values  # shape (N,)
    Sigma = cov_annual.values  # shape (N,N)
    return mu, Sigma, tickers

def solve_optimal_portfolio(mu, Sigma, rf, gamma):
    """
    For N assets with expected returns mu and covariance matrix Sigma,
    solve for optimal risky-asset weights using:
    
        w* = (1/gamma) * Sigma^{-1} (mu - rf * 1)
        c* = 1 - sum(w*)
    
    Returns:
      w_star: array of weights for the risky assets.
      c_star: weight (fraction) allocated to the risk-free asset.
      mu_p_star: optimal portfolio return.
      sigma_p_star: optimal portfolio standard deviation.
    """
    N = len(mu)
    ones = np.ones(N)
    inv_Sigma = np.linalg.inv(Sigma)
    w_star = (1.0 / gamma) * inv_Sigma.dot(mu - rf * ones)
    c_star = 1.0 - np.sum(w_star)
    mu_p_star = w_star.dot(mu) + c_star * rf
    sigma_p_sq = w_star.dot(Sigma).dot(w_star)
    sigma_p_star = np.sqrt(sigma_p_sq) if sigma_p_sq > 0 else 0.0
    return w_star, c_star, mu_p_star, sigma_p_star
