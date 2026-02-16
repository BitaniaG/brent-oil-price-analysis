import pandas as pd

def calculate_regime_difference(
    df: pd.DataFrame,
    change_point_index: int
) -> dict:
    """
    Calculate mean price before and after change point.
    """
    before = df.iloc[:change_point_index]["Price"].mean()
    after = df.iloc[change_point_index:]["Price"].mean()

    return {
        "mean_before": before,
        "mean_after": after,
        "difference": after - before,
    }
