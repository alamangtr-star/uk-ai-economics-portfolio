"""Public econometric demonstration: synthetic data only, not empirical research.
Run: python python_econometrics_demo.py
Weights represent illustrative employment, not inverse sampling variances.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm


def synthetic_data(seed=42):
    rng = np.random.default_rng(seed)
    n = 24
    share = rng.uniform(.2, .9, n)
    return pd.DataFrame({'industry': [f'Synthetic {i:02}' for i in range(n)],
                         'sme_share': share,
                         'employment': rng.integers(1000, 50000, n),
                         'exposure': 0.8 + .4 * share + rng.normal(0, .25, n)})


def fit_model(data, weighted=True):
    cols = ['sme_share', 'employment', 'exposure']
    x = data[cols].to_numpy(dtype=float)
    if len(data) < 5 or not np.isfinite(x).all():
        raise ValueError('At least five complete finite observations required')
    if not data.sme_share.between(0, 1).all() or (data.employment <= 0).any():
        raise ValueError('Invalid share or employment weight')
    if data.sme_share.nunique() < 2:
        raise ValueError('No variation in SME share')
    design = sm.add_constant(data.sme_share, has_constant='add')
    model = (sm.WLS(data.exposure, design, weights=data.employment)
             if weighted else sm.OLS(data.exposure, design))
    return model.fit(cov_type='HC3')


def leave_one_out(data):
    data = data.reset_index(drop=True)
    return pd.DataFrame([{'omitted': row.industry,
                          'slope': fit_model(data.drop(i)).params['sme_share']}
                         for i, row in data.iterrows()])


def main():
    data = synthetic_data()
    print('SYNTHETIC DEMONSTRATION — not UK estimates or causal effects')
    for weighted in (True, False):
        fit = fit_model(data, weighted)
        lo, hi = fit.conf_int().loc['sme_share']
        print(f'{"WLS" if weighted else "OLS"}: n={int(fit.nobs)}, '
              f'slope={fit.params["sme_share"]:.3f}, HC3 95% CI=[{lo:.3f}, {hi:.3f}], '
              f'p={fit.pvalues["sme_share"]:.3f}')
    print(leave_one_out(data).to_string(index=False))


if __name__ == '__main__':
    main()
