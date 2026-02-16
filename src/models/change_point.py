import pymc as pm
import numpy as np
import arviz as az

def run_change_point_model(data, draws=300, tune=300):

    with pm.Model() as model:
        switchpoint = pm.DiscreteUniform(
            "switchpoint", lower=0, upper=len(data)
        )

        mu1 = pm.Normal("mu1", mu=0, sigma=1)
        mu2 = pm.Normal("mu2", mu=0, sigma=1)

        sigma = pm.HalfNormal("sigma", sigma=1)

        mu = pm.math.switch(
            switchpoint >= np.arange(len(data)),
            mu1,
            mu2,
        )

        obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=data)

        trace = pm.sample(
            draws=draws,
            tune=tune,
            chains=2,
            cores=1,
            return_inferencedata=True
        )

    return trace
