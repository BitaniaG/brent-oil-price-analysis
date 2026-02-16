import streamlit as st
import pandas as pd
import arviz as az
import numpy as np
from pathlib import Path

from src.data.load import load_price_data
from src.data.preprocess import add_log_returns

st.set_page_config(page_title="Brent Oil Structural Break Analysis", layout="wide")

st.title("Brent Oil Structural Break Detection")
st.markdown("Bayesian Change Point Analysis using PyMC")

# Load data
df = load_price_data("data/raw/BrentOilPrices.csv")
df = add_log_returns(df)

# Load cached model
trace_path = Path("models/brent_trace.nc")

if trace_path.exists():
    trace = az.from_netcdf(trace_path)
else:
    st.error("Model trace not found. Run main.py first.")
    st.stop()

# Extract change point
switch_samples = trace.posterior["switchpoint"].values.flatten()
mean_switch = int(np.mean(switch_samples))

df_sample = df.tail(1000)
change_date = df_sample.iloc[mean_switch]["Date"]

st.subheader("Detected Change Point")
st.write(f"Estimated Change Date: {change_date.date()}")

# Plot
st.line_chart(df.set_index("Date")["Price"])

st.markdown("### Change Point Highlight")

chart_data = df.set_index("Date")["Price"]

st.line_chart(chart_data)

st.success("Model loaded from cached inference. No re-sampling performed.")
