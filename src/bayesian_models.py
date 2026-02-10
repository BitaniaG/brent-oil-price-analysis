import pymc as pm
import numpy as np

def build_change_point_model(returns):
    if len(returns) < 50:
        raise ValueError("Time series too short for change point analysis")

    with pm.Model() as model:
        tau = pm.DiscreteUniform(
            "tau",
            lower=0,
            upper=len(returns) - 1
        )

        mu_1 = pm.Normal("mu_1", mu=0, sigma=1)
        mu_2 = pm.Normal("mu_2", mu=0, sigma=1)
        sigma = pm.HalfNormal("sigma", sigma=1)

        mu = pm.math.switch(
            np.arange(len(returns)) < tau,
            mu_1,
            mu_2
        )

        pm.Normal(
            "obs",
            mu=mu,
            sigma=sigma,
            observed=returns
        )

    return model
