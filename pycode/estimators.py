import numpy as np

def parkinson_var(h,l):
    R = h - l
    return R * R / (4 * np.log(2))

def gk_var(h, l, r):
    R = h-l
    return 0.5 * R * R - (2 * np.log(2)-1) * r * r

