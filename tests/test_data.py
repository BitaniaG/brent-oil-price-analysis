import pandas as pd
import tempfile
from src.data.load import load_price_data
from src.data.preprocess import add_log_returns


def test_load_price_data():
    # Create temporary CSV file
    sample_data = "Date,Price\n2023-01-01,80.5\n2023-01-02,82.1"

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as tmp:
        tmp.write(sample_data)
        tmp_path = tmp.name

    df = load_price_data(tmp_path)

    assert isinstance(df, pd.DataFrame)
    assert "Date" in df.columns
    assert "Price" in df.columns
