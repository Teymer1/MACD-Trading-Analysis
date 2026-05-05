def calculate_ema(prices, period):
    """Calculates Exponential Moving Average."""
    alpha = 2 / (period + 1)
    ema_values = [sum(prices[:period]) / period]

    for price in prices[period:]:
        ema_values.append(alpha * price + (1 - alpha) * ema_values[-1])

    return [None] * (period - 1) + ema_values


def calculate_macd(prices):
    """Calculates MACD Line and Signal Line."""
    ema12 = calculate_ema(prices, 12)
    ema26 = calculate_ema(prices, 26)

    macd_line = [e12 - e26 if e12 and e26 else None for e12, e26 in zip(ema12, ema26)]

    # Filter out None values for signal calculation
    valid_macd = [m for m in macd_line if m is not None]
    signal_line = calculate_ema(valid_macd, 9)

    # Pad signal line to match original data length
    return macd_line, [None] * 25 + signal_line