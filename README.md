# Multi-Asset + Risk-Free Optimal Portfolio Calculator

This project is a Flask-based web application that computes the optimal portfolio allocation between multiple risky assets and a risk-free asset based on user inputs. It allows users to input stock tickers, date ranges, a risk-free rate, and a risk aversion coefficient, and returns an optimized portfolio using principles from Modern Portfolio Theory.

## Features

- Input multiple stock tickers to analyze historical performance
- Specify custom date ranges for analysis
- Include a risk-free asset and set its rate
- Adjustable risk aversion parameter
- Calculates:
  - Optimal risky asset weights
  - Risk-free fraction (c*)
  - Expected return and standard deviation of the optimal portfolio

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/optimal-portfolio.git
   cd optimal-portfolio
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in your browser**
   Navigate to `http://127.0.0.1:5000/`

## Usage

- Enter stock tickers (e.g., `AAPL, MSFT, GOOGL`)
- Select start and end dates
- Set the risk-free rate (e.g., `0.03` for 3%)
- Set your risk aversion (gamma)
- Click **Compute Optimal Portfolio** to see results

## File Structure

- `app.py` - Main Flask app that handles routes and logic
- `portfolio.py` - Portfolio optimization logic
- `templates/index.html` - Form input interface
- `templates/result.html` - Displays optimized results

## Technologies Used

- Python (Flask, NumPy, Pandas)
- Bootstrap 5 for UI
- Jinja2 templating
- Financial APIs for data (e.g., yfinance, if used in `portfolio.py`)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](LICENSE)

---

*This project is a simplified educational tool for portfolio optimization and not financial advice.*
