import csv
import os

def load_ticker_prices(csv_filename="sp500_tickers.csv"):
    """
    Simulates looking up current stock prices.
    In production, this could parse a real S&P 500 dataset CSV or fetch from an API (e.g., yfinance).
    """
    # Fallback mock data if the downloaded S&P 500 CSV file is not found locally
    mock_prices = {
        "AAPL": 175.50,
        "MSFT": 420.25,
        "GOOGL": 150.75,
        "AMZN": 178.00,
        "NVDA": 875.00
    }
    
    if not os.path.exists(csv_filename):
        print(f"[Info] '{csv_filename}' not found. Using local mock price data.")
        return mock_prices
        
    prices = {}
    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assumes CSV columns include 'Ticker' and 'Current Price'
            if 'Ticker' in row and 'Current Price' in row:
                prices[row['Ticker'].upper()] = float(row['Current Price'])
    return prices

def calculate_portfolio_performance():
    # 1. Store portfolio positions in a dictionary structure
    # Format: { Ticker: {"shares": quantity, "buy_price": cost_basis} }
    portfolio = {
        "AAPL": {"shares": 10, "buy_price": 150.00},
        "MSFT": {"shares": 5, "buy_price": 380.00},
        "NVDA": {"shares": 2, "buy_price": 700.00},
        "AMZN": {"shares": 8, "buy_price": 185.00}
    }
    
    # 3. Look up current ticker prices
    current_prices = load_ticker_prices("sp500_tickers.csv")
    
    csv_headers = ["Ticker", "Shares Held", "Avg Buy Price", "Current Price", "Total Invested", "Current Value", "Gain/Loss (%)"]
    csv_rows = []
    
    total_portfolio_invested = 0.0
    total_portfolio_value = 0.0
    
    print("\n--- Console Performance Output ---")
    
    # 2. Iterate through portfolio items
    for ticker, assets in portfolio.items():
        shares = assets["shares"]
        buy_price = assets["buy_price"]
        current_price = current_prices.get(ticker, 0.0)
        
        # 4. Calculate metrics per holding
        invested_capital = shares * buy_price
        current_value = shares * current_price
        
        if invested_capital > 0:
            gain_loss_pct = ((current_value - invested_capital) / invested_capital) * 100
        else:
            gain_loss_pct = 0.0
            
        total_portfolio_invested += invested_capital
        total_portfolio_value += current_value
        
        # Format individual row metrics
        csv_rows.append([
            ticker,
            shares,
            f"${buy_price:.2f}",
            f"${current_price:.2f}",
            f"${invested_capital:.2f}",
            f"${current_value:.2f}",
            f"{gain_loss_pct:+.2f}%"
        ])
        
        print(f"Stock: {ticker:<6} | Invested: ${invested_capital:<8.2f} | Market Value: ${current_value:<8.2f} | Net Return: {gain_loss_pct:+.2f}%")
        
    # Calculate overall total portfolio performance metric
    if total_portfolio_invested > 0:
        total_gain_loss_pct = ((total_portfolio_value - total_portfolio_invested) / total_portfolio_invested) * 100
    else:
        total_gain_loss_pct = 0.0
        
    print("-" * 70)
    print(f"TOTAL PORTFOLIO | Invested: ${total_portfolio_invested:.2f} | Market Value: ${total_portfolio_value:.2f} | Total Return: {total_gain_loss_pct:+.2f}%\n")
    
    # 5. Write results into 'portfolio_summary.csv' using Python's built-in csv module
    output_filename = 'portfolio_summary.csv'
    with open(output_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write primary fields
        writer.writerow(csv_headers)
        writer.writerows(csv_rows)
        
        # Write blank separator and final summary values
        writer.writerow([])
        writer.writerow([
            "TOTAL PORTFOLIO", "", "", "",
            f"${total_portfolio_invested:.2f}",
            f"${total_portfolio_value:.2f}",
            f"{total_gain_loss_pct:+.2f}%"
        ])
        
    print(f"[Success] Generated transaction log saved to: '{output_filename}'")

if __name__ == "_main_":
    calculate_portfolio_performance()