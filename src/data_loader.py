import pandas as pd

def load_brent_data(filepath: str) -> pd.DataFrame:
    """
    Load and validate Brent oil price data.
    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")

    required_cols = {"Date", "Price"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"Dataset must contain columns: {required_cols}")

    df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y", errors="coerce")
    df = df.dropna(subset=["Date", "Price"])

    df = df.sort_values("Date").reset_index(drop=True)
    return df
