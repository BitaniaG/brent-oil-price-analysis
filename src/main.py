from src.data.load import load_price_data
from src.data.preprocess import add_log_returns
from src.models.change_point import run_change_point_model
from src.config.settings import Config
from src.visualization.plot_change_point import plot_change_point

import arviz as az
from pathlib import Path
import numpy as np


def main():
    config = Config()

    df = load_price_data(config.RAW_DATA_PATH)
    df = add_log_returns(df)
    df_sample = df.tail(config.SAMPLE_SIZE)

    trace_path = Path("models/brent_trace.nc")

    if trace_path.exists():
        print("Loading existing model...", flush=True)
        trace = az.from_netcdf(trace_path)
    else:
        print("Running model...", flush=True)
        trace = run_change_point_model(
            df_sample["Log_Return"].values,
            draws=config.DRAWS,
            tune=config.TUNE
        )
        trace_path.parent.mkdir(exist_ok=True)
        az.to_netcdf(trace, trace_path)

    print("Model ready.")

    # ===== Change point extraction =====
    switch_samples = trace.posterior["switchpoint"].values.flatten()
    mean_switch = int(np.mean(switch_samples))
    change_date = df_sample.iloc[mean_switch]["Date"]

    print(f"Estimated change point index: {mean_switch}")
    print(f"Estimated change date: {change_date}")

    # ===== Diagnostics =====
    summary = az.summary(trace)
    print(summary)

    # ===== Visualization =====
    plot_change_point(df_sample, change_date)


if __name__ == "__main__":
    main()
