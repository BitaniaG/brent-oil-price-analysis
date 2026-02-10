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

# Task 2: Bayesian Change Point Modeling and Insight Generation
## Objective

The objective of Task 2 is to apply Bayesian change point detection to identify and quantify structural breaks in Brent crude oil prices. This task aims to detect statistically significant shifts in price behavior, interpret their magnitude, and associate them with major geopolitical and economic events.

## Methodology Overview

### Data Preparation

Loaded and validated Brent oil price data

Converted date fields to datetime format

Computed log returns to achieve stationarity

### Exploratory Data Analysis

Visualized raw price trends and volatility patterns

Analyzed log returns to observe volatility clustering

Conducted Augmented Dickey-Fuller (ADF) tests to confirm stationarity

### Bayesian Change Point Modeling

Implemented a Bayesian change point model in PyMC

Defined a discrete uniform prior for the unknown change point

Modeled pre- and post-change regimes with separate mean parameters

Estimated posterior distributions using MCMC sampling

### Model Diagnostics and Interpretation

Assessed convergence using trace plots and R-hat statistics

Identified probable change point dates from posterior distributions

Quantified shifts in average price behavior before and after change points

### Event Association

Compared detected change points with major geopolitical and economic events

Formulated hypotheses linking structural breaks to real-world shocks

## Key Outputs

Posterior distribution of detected change points

Quantified estimates of regime shifts (before vs. after means)

Probabilistic interpretation of structural breaks

Hypothesis-driven association with oil market events

## Key Assumptions

Price changes can be approximated by regime-based mean shifts

Detected change points indicate structural changes, not definitive causality

Log returns sufficiently capture stationarity for modeling

## Limitations

Single change point model may not capture multiple structural breaks

External macroeconomic variables are not directly modeled

Associations with events are correlational, not causal

# Task 3: Interactive Dashboard and API Development
## Objective

The objective of Task 3 is to operationalize the analytical insights generated in Task 2 by developing a backend API and a frontend dashboard architecture. This task bridges advanced Bayesian change point modeling with stakeholder-facing tools that enable interactive exploration of Brent oil price trends, detected structural breaks, and major geopolitical events.

## System Architecture Overview

Task 3 follows a modular, service-oriented architecture consisting of:

Backend (Flask API): Serves processed data and model outputs through RESTful endpoints.

Frontend (React – conceptual): Provides a component-based structure for interactive data visualization.

Data Layer: Stores raw price data, event data, and processed change point outputs.

This separation of concerns improves scalability, maintainability, and clarity.

## Project Structure
dashboard/
├── backend/
│   ├── app.py
│   ├── routes/
│   │   ├── prices.py
│   │   ├── events.py
│   │   └── changepoints.py
│   ├── services/
│   │   └── data_service.py
│   └── __init__.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── PriceChart.jsx
│   │   │   ├── ChangePointChart.jsx
│   │   │   └── EventTimeline.jsx
│   │   └── App.jsx
│   └── package.json
## Backend API (Flask)
### Purpose

The backend exposes Brent oil prices, oil market events, and Bayesian change point results via RESTful endpoints. These endpoints are designed to support dashboard visualization and future extensions.

### Available Endpoints
| Endpoint            | Description                                         |
| ------------------- | --------------------------------------------------- |
| `/`                 | Health check for backend                            |
| `/api/prices`       | Returns Brent oil price time series                 |
| `/api/events`       | Returns major geopolitical and economic events      |
| `/api/changepoints` | Returns detected change point and quantified impact |
### Backend Setup and Execution

#### Install required dependencies:

pip install flask pandas

#### Run the backend server:

cd dashboard/backend
python app.py

#### Verify endpoints in a browser:

http://127.0.0.1:5000/
http://127.0.0.1:5000/api/prices
http://127.0.0.1:5000/api/events
http://127.0.0.1:5000/api/changepoints

Successful responses confirm correct backend functionality.
### Frontend Dashboard (React – Conceptual Implementation)
#### Purpose

The frontend provides a structured, component-based architecture for visualizing oil prices, change points, and events. While a fully running React application is not required, the folder structure and components demonstrate how the dashboard would consume backend APIs.

#### Frontend Components
| Component              | Description                           |
| ---------------------- | ------------------------------------- |
| `PriceChart.jsx`       | Displays Brent oil price trends       |
| `ChangePointChart.jsx` | Highlights detected structural breaks |
| `EventTimeline.jsx`    | Shows key oil market events           |
| `App.jsx`              | Main dashboard container              |
Each component is designed to independently consume data from the Flask API, enabling modular visualization and future scalability.
## Data Integration

The backend accesses data from the following locations:

Raw price data: data/raw/brent_oil_prices.csv

Event data: data/external/oil_market_events.csv

Model outputs: data/processed/changepoints.json

Relative paths are used to ensure compatibility with the nested dashboard/backend directory structure.

## Assumptions

Backend APIs serve as the single source of truth for dashboard data.

Frontend components consume data asynchronously via REST endpoints.

Change point outputs represent statistically significant structural breaks but do not imply causal certainty.

## Limitations

The frontend is provided as an architectural skeleton rather than a fully deployed application.

Only a single change point model output is currently exposed.

External macroeconomic indicators are not included at this stage.

## Future Enhancements

Deployment of a fully interactive React dashboard

Support for multiple detected change points

Integration of additional macroeconomic data sources

Enhanced visual analytics (filters, tooltips, regime highlighting)

## Conclusion

Task 3 successfully translates Bayesian change point analysis into an operational dashboard architecture. By exposing analytical outputs through a RESTful API and designing a modular frontend structure, this task demonstrates how advanced statistical insights can be transformed into accessible decision-support tools for energy sector stakeholders.