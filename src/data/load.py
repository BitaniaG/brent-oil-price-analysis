import pandas as pd
from pathlib import Path

def load_price_data(path: str) -> pd.DataFrame:
    """
    Load Brent oil price dataset.

    Args:
        path (str): Path to CSV file.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], format="mixed", dayfirst=True)
    df = df.sort_values("Date")
    return df
