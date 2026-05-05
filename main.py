import warnings
from data_loader import load_stock_data
from indicators import calculate_macd
from trading_engine import find_trade_signals, simulate_trading, generate_trade_log
from visualization import plot_stock_with_signals, plot_macd

warnings.filterwarnings("ignore")

# 1. Load Data
df = load_stock_data("NVDA_data.csv")

# 2. Calculate Indicators
df["MACD"], df["Signal"] = calculate_macd(df["Close"].tolist())

# 3. Get Signals
buy_indices, sell_indices = find_trade_signals(df["MACD"], df["Signal"])

# 4. Simulation & Analytics
portfolio = simulate_trading(df, buy_indices, sell_indices)

print(f"Initial Capital: {portfolio[0]:.2f} USD")
print(f"Final Capital: {portfolio[-1]:.2f} USD")

# 5. Export Log
trade_log = generate_trade_log(df, buy_indices, sell_indices)
trade_log.to_csv("trade_log.csv", index=False)
print("\nTrade Log (First 5 rows):")
print(trade_log.head())

# 6. Visualization
plot_stock_with_signals(df, buy_indices, sell_indices)
plot_macd(df)