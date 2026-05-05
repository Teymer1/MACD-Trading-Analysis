import matplotlib.pyplot as plt


def plot_stock_with_signals(df, buy_signals, sell_signals, title="Stock Price with Signals"):
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df["Close"], label="Price", alpha=0.6)

    plt.scatter(df.index[buy_signals], df["Close"].iloc[buy_signals],
                color="green", label="Buy", marker="^", s=50)
    plt.scatter(df.index[sell_signals], df["Close"].iloc[sell_signals],
                color="red", label="Sell", marker="v", s=50)

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_macd(df, title="MACD Indicator"):
    plt.figure(figsize=(14, 5))
    plt.plot(df.index, df["MACD"], label="MACD", color="blue")
    plt.plot(df.index, df["Signal"], label="Signal", color="orange")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()