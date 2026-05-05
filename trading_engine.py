import pandas as pd


def find_trade_signals(macd, signal):
    """Identifies crossover points for buy and sell signals."""
    buy_signals, sell_signals = [], []

    for i in range(1, len(macd)):
        if macd[i] is None or signal[i] is None:
            continue
        # MACD crosses above Signal Line
        if macd[i - 1] < signal[i - 1] and macd[i] > signal[i]:
            buy_signals.append(i)
            # MACD crosses below Signal Line
        elif macd[i - 1] > signal[i - 1] and macd[i] < signal[i]:
            sell_signals.append(i)

    return buy_signals, sell_signals


def simulate_trading(df, buy_signals, sell_signals, initial_shares=1000):
    """Simulates portfolio value over time based on signals."""
    cash = 0
    shares = initial_shares
    portfolio_values = []

    for i in range(len(df)):
        price = df["Close"].iloc[i]
        if i in buy_signals and cash > 0:
            shares = cash / price
            cash = 0
        elif i in sell_signals and shares > 0:
            cash = shares * price
            shares = 0

        portfolio_values.append(cash + shares * price)
    return portfolio_values


def generate_trade_log(df, buy_signals, sell_signals):
    """Creates a detailed log of all completed trades."""
    trades = []
    for buy, sell in zip(buy_signals, sell_signals):
        buy_price = df['Close'].iloc[buy]
        sell_price = df['Close'].iloc[sell]
        profit = (sell_price - buy_price) * 1000
        trades.append([df.index[buy], buy_price, df.index[sell], sell_price, profit])

    log_df = pd.DataFrame(trades, columns=['Buy Date', 'Buy Price', 'Sell Date', 'Sell Price', 'Profit'])
    return log_df