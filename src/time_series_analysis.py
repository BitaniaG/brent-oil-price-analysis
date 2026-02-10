import numpy as np
from statsmodels.tsa.stattools import adfuller

def compute_log_returns(df, price_col="Price"):
    """
    Compute log returns of a price series.
    """
    if price_col not in df.columns:
        raise ValueError(f"{price_col} column not found in DataFrame")

    df = df.copy()
    df["log_price"] = np.log(df[price_col])
    df["log_return"] = df["log_price"].diff()
    return df.dropna()

def adf_test(series):
    """
    Perform Augmented Dickey-Fuller test.
    """
    if series.empty:
        raise ValueError("ADF test received an empty series")

    statistic, p_value, *_ = adfuller(series)
    return {
        "adf_statistic": statistic,
        "p_value": p_value
    }
