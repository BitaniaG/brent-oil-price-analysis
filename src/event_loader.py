import pandas as pd

def load_events(filepath: str) -> pd.DataFrame:
    """
    Load and validate oil market events.
    """
    try:
        events = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"Event file not found: {filepath}")

    if "date" not in events.columns or "event" not in events.columns:
        raise ValueError("Events file must contain 'date' and 'event' columns")

    events["date"] = pd.to_datetime(events["date"], errors="coerce")
    return events.dropna(subset=["date"])
