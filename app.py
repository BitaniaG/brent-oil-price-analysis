import streamlit as st
import pandas as pd
import arviz as az
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

from src.data.load import load_price_data
from src.data.preprocess import add_log_returns

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Brent Oil Structural Break Analysis",
    layout="wide"
)

st.markdown("---")

# ----------------------------
# Title Section
# ----------------------------
st.title("Brent Oil Structural Break Detection")
st.markdown(
    "Bayesian Change Point Analysis of Brent Crude Oil Prices"
)
st.markdown(
"""
### Executive Summary

This dashboard applies Bayesian change point detection to identify structural
breaks in Brent crude oil prices. The detected regime shift suggests a change
in the underlying price-generating process, potentially linked to macroeconomic
or geopolitical events.
"""
)

# ----------------------------
# Load Data
# ----------------------------
df = load_price_data("data/raw/BrentOilPrices.csv")
df = add_log_returns(df)

# Sidebar Controls
st.sidebar.header("Dashboard Controls")

sample_size = st.sidebar.slider(
    "Select Sample Size",
    min_value=300,
    max_value=len(df),
    value=1000,
    step=100
)

df_sample = df.tail(sample_size)

st.markdown("---")

# ----------------------------
# Load Cached Model
# ----------------------------
trace_path = Path("models/brent_trace.nc")

if trace_path.exists():
    trace = az.from_netcdf(trace_path)
else:
    st.error("Model trace not found. Run main.py first.")
    st.stop()

st.markdown("---")

# ----------------------------
# Extract Change Point
# ----------------------------
switch_samples = trace.posterior["switchpoint"].values.flatten()
mean_switch = int(np.mean(switch_samples))

if mean_switch >= len(df_sample):
    mean_switch = len(df_sample) - 1

change_date = df_sample.iloc[mean_switch]["Date"]

st.markdown("---")

# ----------------------------
# Metrics Row
# ----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Detected Change Date", str(change_date.date()))
col2.metric("Sample Size Used", sample_size)
col3.metric("Mean Switch Index", mean_switch)

st.markdown("---")

# ----------------------------
# Historical Event Markers
# ----------------------------
events = {
    "2008 Financial Crisis": "2008-09-15",
    "2014 Oil Price Crash": "2014-11-01",
    "COVID-19 Shock": "2020-03-11"
}

st.markdown("---")

# ----------------------------
# Price Trend Plot
# ----------------------------
st.subheader("Price Trend with Detected Structural Break")

fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(
    df_sample["Date"],
    df_sample["Price"],
    linewidth=1.5
)

# Detected Change Point
ax.axvline(
    change_date,
    linestyle="--",
    linewidth=2
)

# Add Event Markers
for event, date in events.items():
    event_date = pd.to_datetime(date)
    if df_sample["Date"].min() <= event_date <= df_sample["Date"].max():
        ax.axvline(event_date, linestyle=":", linewidth=1)
        ax.text(event_date, df_sample["Price"].max(), event,
                rotation=90, verticalalignment='top')

ax.set_title("Brent Oil Price with Structural Break and Major Events")
ax.set_xlabel("Date")
ax.set_ylabel("Price")

plt.xticks(rotation=45)

st.pyplot(fig)


st.markdown("---")

# ----------------------------
# Diagnostics Section
# ----------------------------
st.subheader("Model Diagnostics")

summary = az.summary(trace)

st.dataframe(summary)

st.markdown("---")

# ----------------------------
# Posterior Distribution
# ----------------------------
st.subheader("Posterior Distribution of Change Point")

fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.hist(switch_samples, bins=40)
ax2.set_xlabel("Switchpoint Index")
ax2.set_ylabel("Frequency")

st.pyplot(fig2)

st.markdown("---")

# ----------------------------
# Regime Comparison
# ----------------------------
st.subheader("Pre vs Post Change Statistics")

pre_regime = df_sample.iloc[:mean_switch]
post_regime = df_sample.iloc[mean_switch:]

colA, colB = st.columns(2)

colA.metric(
    "Pre-Change Mean Price",
    round(pre_regime["Price"].mean(), 2)
)

colB.metric(
    "Post-Change Mean Price",
    round(post_regime["Price"].mean(), 2)
)

st.markdown("---")

# ----------------------------
# Volatility Comparison
# ----------------------------
st.subheader("Volatility Comparison (Log Returns Std Dev)")

pre_vol = pre_regime["Log_Return"].std()
post_vol = post_regime["Log_Return"].std()

colC, colD = st.columns(2)

colC.metric(
    "Pre-Change Volatility",
    round(pre_vol, 4)
)

colD.metric(
    "Post-Change Volatility",
    round(post_vol, 4)
)

st.markdown("---")

# ----------------------------
# Interpretation Section
# ----------------------------
st.subheader("Executive Interpretation")

st.markdown(
"""
The detected structural break represents a statistically inferred shift 
in the price-generating process of Brent crude oil.

Such regime changes may correspond to:

- Geopolitical shocks  
- Supply disruptions  
- Policy changes  
- Global economic crises  

This dashboard demonstrates how Bayesian inference can be used to identify 
structural instability in financial time series.
"""
)

st.success("Model loaded from cached inference. No re-sampling performed.")
