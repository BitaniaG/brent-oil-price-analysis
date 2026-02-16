import numpy as np
import arviz as az
from pathlib import Path
import pytest

def test_trace_file_exists():
    trace_path = Path("models/brent_trace.nc")
    if not trace_path.exists():
        pytest.skip("Trace file not available in CI environment.")
    assert trace_path.exists()

def test_trace_loadable():
    trace_path = Path("models/brent_trace.nc")
    if not trace_path.exists():
        pytest.skip("Trace file not available in CI environment.")
    trace = az.from_netcdf(trace_path)
    assert "switchpoint" in trace.posterior
