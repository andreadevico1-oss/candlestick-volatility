import numpy as np

# 1st setp is sampling a step's maximum given its endpoint 

def bridge_max(c, s2, u):
    'return the conditional bridge maximum'
    return 0.5 * ( c + np.sqrt(c * c - 2.0 * s2 * np.log(u)))

def bridge_min(c, s2, v):
    'return the conditional bridge minimum'
    return 0.5 * ( c - np.sqrt(c * c - 2.0 * s2 * np.log(v)))

def exact_bar(rng, n_days, m, sigma, mu = 0.0): 
    'Simulating bars using bridge extremes'

    s2 = sigma * sigma / m # daily variance divided by m steps

    'drawing all the steps'
    d = rng.normal(
        mu / m,              # expected change per step
        np.sqrt(s2),         # std deviation per step
        size = (n_days, m)   # rows are days, while columns are the steps 
    )
    u = rng.uniform(size = (n_days, m))
    v = rng.uniform(size = (n_days, m))

    x = np.cumsum(d, axis = 1) # cumulative sum of the steps to buld the price paths
    starts = x - d # the starting point of each step is the previous step's end point

    H = (starts + bridge_max(d, s2, u)).max(axis = 1) # finding the maximum of each day inside the steps
    L = (starts + bridge_min(d, s2, v)).min(axis = 1) # finding the minimum of each day inside the steps

    return H, L, x[:, -1] # returning the max, the min and the final log-price level of each day's path 

def naive_bar(rng, n_days, m, sigma):
    'simulate bars without adding within step bridge extremes'
    d = rng.normal(
        0.0,                  # zero expected change per step
        sigma / np.sqrt(m),   # standard deviation per step
        size = (n_days, m)    # one raw per day and one column per step
    )

    x = np.cumsum(d, axis = 1) # building the log price paths from the change 

    H = np.maximum(x.max(axis =1), 0.0)   # including the open at zero in the max calculation
    L = np.minimum(x.min(axis = 1), 0.0)  # including the open at zero in the min calculation
    C = x[:, -1]                          # taking the last step as the closing price, taking the last column oif every raw

    return H, L, C 

    

