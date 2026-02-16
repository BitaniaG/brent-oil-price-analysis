import pandas as pd
import numpy as np

def add_log_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add log returns column to dataframe.
    """
    df = df.copy()
    df["Log_Return"] = np.log(df["Price"] / df["Price"].shift(1))
    df = df.dropna()
    return df
