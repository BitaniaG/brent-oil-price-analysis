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

## Task 1 Deliverables
- ✔ Defined a complete data analysis workflow
- ✔ Conducted exploratory time series analysis
- ✔ Created a structured event dataset (10–15 events)
- ✔ Documented assumptions and limitations

---

## Tools & Libraries
- Python
- pandas, numpy
- matplotlib, seaborn
- statsmodels
- PyMC (Task 2)
- Flask & React (Task 3)

---

