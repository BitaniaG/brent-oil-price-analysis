## Assumptions

- Major geopolitical, economic, and policy-related events influence oil prices within a relatively short time window around their occurrence.
- Event dates represent approximate start points and do not capture anticipation effects or delayed market reactions.
- Log returns of oil prices provide a more stable and suitable representation for statistical modeling than raw price levels.
- The change point model assumes that structural breaks primarily affect the statistical mean of returns.
- Market behavior is assumed to be sufficiently captured using historical price data without incorporating additional macroeconomic variables.

## Limitations and Correlation vs Causation

This analysis identifies statistical change points in oil price behavior, which indicate moments where the underlying data-generating process changes. However, the presence of a change point near a real-world event does not constitute proof of causality.

Multiple overlapping events, unobserved macroeconomic factors, speculative behavior, and delayed market responses may influence oil prices simultaneously. As a result, detected change points should be interpreted as correlations in time rather than definitive causal impacts.

Additionally, the analysis relies solely on historical price data and does not account for other influential variables such as global demand indicators, exchange rates, or inventory levels. These limitations are acknowledged, and future work may incorporate multivariate models to address them.

## Communication Channels

The results of this analysis are communicated through multiple channels tailored to different stakeholders:

- **Technical Analysis Report**: A detailed written report (Markdown/PDF/Medium-style blog) presenting methodology, results, and interpretations for analysts and policymakers.
- **Interactive Dashboard**: A web-based dashboard built using a Flask backend and React frontend to allow stakeholders to explore price trends, detected change points, and associated events.
- **Visualizations**: Clear charts and plots highlighting structural breaks, volatility regimes, and event alignments to support data-driven decision-making.
