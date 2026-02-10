function ChangePointChart() {
  return (
    <div>
      <h3>Detected Change Point</h3>
      <p>
        This component displays the Bayesian change point detected in Brent oil
        prices. The change point represents a structural break where price
        behavior shifts significantly.
      </p>
      <p>
        Data source: Flask API endpoint <code>/api/changepoints</code>
      </p>
    </div>
  );
}

export default ChangePointChart;
