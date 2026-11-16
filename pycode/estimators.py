import numpy as np

def parkinson_var(h,l):
    R = h - l
    return R * R / (4 * np.log(2))

def gk_var(h, l, r):
    R = h-l
    return 0.5 * R * R - (2 * np.log(2)-1) * r * r

def rs_var(h, l, r):
    return h * (h - r) + l * (l - r)

def yz_var(o, r, rs):
    n = len(o)

    if n < 2:
        raise ValueError('The estimator needs at least 2 daily observations to compute the variance')

    if len(rs) != n or len(r) != n:
        raise ValueError('o r and rs must contain the same days')

    k = 0.34 / (1.34 + (n + 1) / (n - 1))

    overnight_var = np.var(o, ddof = 1)
    intraday_var = np.var(r, ddof = 1)
    rs_mean = np.mean(rs)

    yz = overnight_var + k * intraday_var + rs_mean * (1-k)

    return float(yz)
