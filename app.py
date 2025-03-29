from flask import Flask, render_template, request
import numpy as np
from portfolio import fetch_data_from_yahoo, compute_returns_and_cov, solve_optimal_portfolio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error_msg = None
    if request.method == 'POST':
        try:
            # Parse tickers from comma-separated input (strip spaces and uppercase)
            tickers_str = request.form['tickers'].strip()
            tickers = [t.strip().upper() for t in tickers_str.split(',')]
            
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            rf = float(request.form['rf'])
            gamma = float(request.form['gamma'])
            
            # Download data from Yahoo Finance
            data = fetch_data_from_yahoo(tickers, start_date, end_date)
            if data.empty:
                raise ValueError("No data downloaded. Check your tickers or date range.")
            
            # Compute annualized returns and covariance matrix
            mu, Sigma, used_tickers = compute_returns_and_cov(data)
            
            # Solve for the optimal portfolio weights and portfolio metrics
            w_star, c_star, mu_p_star, sigma_p_star = solve_optimal_portfolio(mu, Sigma, rf, gamma)
            
            # Pair each ticker with its corresponding weight
            weights_with_tickers = list(zip(used_tickers, w_star))
            
            return render_template(
                'result.html',
                weights_with_tickers=weights_with_tickers,
                c_star=c_star,
                mu_p_star=mu_p_star,
                sigma_p_star=sigma_p_star
            )
        except Exception as e:
            error_msg = str(e)
            return render_template('index.html', error=error_msg)
    return render_template('index.html', error=error_msg)

if __name__ == '__main__':
    app.run(debug=True)
