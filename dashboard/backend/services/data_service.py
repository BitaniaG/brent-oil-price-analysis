import pandas as pd
import json

def load_prices():
    return pd.read_csv("../../data/raw/brent_oil_prices.csv")

def load_events():
    return pd.read_csv("../../data/external/oil_market_events.csv")

def load_changepoints():
    with open("../../data/processed/changepoints.json") as f:
        return json.load(f)
