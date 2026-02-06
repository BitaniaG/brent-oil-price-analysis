# brent-oil-price-analysis
Statistical modeling and Bayesian change point detection of Brent oil prices (1987-2022) to analyze the impact of geopolitical and economic events using PyMC, Flask, and React.

# Brent Oil Price Change Point Analysis

## Project Overview
This project analyzes historical Brent crude oil prices to identify structural breaks in price behavior and associate them with major geopolitical, economic, and policy-related events. The analysis uses Bayesian Change Point Detection to quantify how such events impact oil price dynamics over time.

The project is developed as part of the 10 Academy KAIM Week 11 Challenge, focusing on probabilistic modeling, statistical reasoning, and data-driven storytelling for policy and investment decision-making.

---

## Business Context
Oil prices are highly sensitive to geopolitical conflicts, economic shocks, and policy decisions such as OPEC production changes. Understanding *when* and *how* these events alter market behavior is crucial for investors, policymakers, and energy companies.

This analysis aims to:
- Detect statistically significant change points in Brent oil prices
- Quantify price behavior before and after these changes
- Compare detected change points with real-world events
- Communicate insights clearly through reports and dashboards

---

## Project Structure
│
├── data/
│ ├── raw/
│ │ └── brent_oil_prices.csv
│ └── external/
│ └── oil_market_events.csv
│
├── notebooks/
│ ├── 01_eda_and_time_series_properties.ipynb
│ └── 02_bayesian_change_point_model.ipynb
│
├── reports/
│ └── task1_analysis_plan.md
│
├── src/
│ └── utils.py
│
├── dashboard/
│ ├── backend/
│ └── frontend/
│
├── README.md
└── requirements.txt

---

# Task 1 – Brent Oil Price Change Point Analysis

## Objective
The objective of Task 1 is to define a complete data analysis workflow and develop a thorough understanding of Brent oil price data and Bayesian change point models. This task establishes the analytical foundation for identifying structural breaks in oil prices and associating them with major geopolitical, economic, and policy-related events.


## Data Description
- **Dataset**: Historical daily Brent oil prices
- **Period**: May 20, 1987 – September 30, 2022
- **Fields**:
  - Date (daily frequency)
  - Price (USD per barrel)

An additional externally researched dataset contains major oil-market-related events, including geopolitical conflicts, OPEC decisions, and global economic shocks.


## Analysis Workflow
1. Data loading and validation
2. Data cleaning and preprocessing
3. Exploratory data analysis (trend, volatility, stationarity)
4. Log-return transformation for stability
5. Event data compilation and alignment
6. Conceptual justification for Bayesian change point modeling
7. Preparation for probabilistic inference and interpretation


## Event Dataset
A structured CSV file (`oil_market_events.csv`) was created containing 10–15 major events relevant to oil price movements. Each event includes:
- Approximate start date
- Event name
- Category (Geopolitical, OPEC, Economic)
- Brief description


## Assumptions
- Market reactions to major events occur within a short time window around the event date
- Event dates are approximate and may not capture anticipation or delayed effects
- Oil price dynamics are influenced by many unobserved factors not included in the model


## Limitations and Causality
This analysis identifies **statistical correlations in time**, not causal relationships.  
A detected change point indicates that the statistical behavior of prices changed at a certain time, but it does not prove that a specific event caused the change. Multiple overlapping events, delayed market reactions, and external macroeconomic factors may influence results.


## Communication Channels
Results from this analysis are communicated through:
- A technical analysis report (Markdown / PDF / Medium-style blog)
- An interactive dashboard (Flask backend, React frontend)
- Visualizations designed for investors, policymakers, and energy sector stakeholders


## Outcome of Task 1
Task 1 establishes a clear analytical framework, validates the suitability of change point modeling, and prepares the data and documentation required for Bayesian inference in Task 2.
