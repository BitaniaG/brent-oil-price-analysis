import pandas as pd
from src.data.load import load_price_data
from src.data.preprocess import add_log_returns

def test_load_price_data():
    df = load_price_data("data/raw/BrentOilPrices.csv")
    assert isinstance(df, pd.DataFrame)
    assert "Date" in df.columns
    assert "Price" in df.columns

def test_add_log_returns():
    df = pd.DataFrame({
        "Price": [100, 105, 110]
    })
    df = add_log_returns(df)
    assert "Log_Return" in df.columns
    assert len(df) == 2
