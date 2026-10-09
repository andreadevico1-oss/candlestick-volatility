import numpy as np

def chunk_stats(x, k=20):
    'return the mean and the std deviation'
    m = len(x) - (len(x) % k)    # keep the lenght divisible by k
    ch = x[:m].reshape(k, -1).mean(axis = 1) # splitting into k chunks and taking the mean
    mean = float(ch.mean()) # averaging the means of each chunck
    se = float(ch.std(ddof=1) / np.sqrt(k))
    return mean, se


