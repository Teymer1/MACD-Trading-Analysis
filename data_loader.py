import pandas as pd

def load_stock_data(file_path="NVDA_data.csv", start_date=None, end_date=None):
    """Loads CSV data, formats dates, and filters by range."""
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    df = df[["Close"]]

    if start_date:
        df = df[df.index >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df.index <= pd.to_datetime(end_date)]
    return df