import pandas as pd
import numpy as np

from .simulation import exact_bar
from .estimators import parkinson_var, gk_var, rs_var
from .statistics import chunk_stats

def drift_comparison(n_days = 400_000, m = 16, seed = 11):
    'returning the reference drift table, with means and 2 std errors'

    rng = np.random.default_rng(seed)

    sigma = 1.0
    true_var = sigma ** 2
    rows = []

    for mu in (0.0, 0.5, 1.0, 2.0):
        H, L, C = exact_bar(
            rng, 
            n_days = n_days,
            m = m,
            sigma = sigma,
            mu = mu,
        )
        
        estimates = {
        'Close pair': C ** 2,
        'Parkinson': parkinson_var(H, L),
        'Garman-Klass': gk_var(H, L, C),
        'Rogers-Satchell': rs_var(H, L, C)
    }
        
        row = {'mu/sigma': mu / sigma}
        
        for name, values in estimates.items():
            mean, se = chunk_stats(values)
            
            row[name] = (
            f'{mean / true_var:.3f}' 
            f' +/- {2 * se / true_var:.3f}'
        )
        
        rows.append(row)

    return pd.DataFrame(rows).set_index('mu/sigma')

