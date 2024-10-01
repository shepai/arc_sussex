import numpy as np
from utils import *
colours={'black':0,'blue':1,'red':2,'green':3,'yellow':4,'gray':5,'pink':6,'orange':7,'light-blue':8,'maroon':9}

def solve_84(pattern):
    assert pattern.shape[0] == pattern.shape[1], f"Incorrect input size {pattern.shape}"
    new=pattern.copy()
    n = pattern.shape[0]
    new[np.arange(n-1), n - 1 - np.arange(n-1)] = 2
    new[n-1,1:] = 4
    return new

def generate_84():
    max_size = np.random.randint(20)
    grid = np.zeros((max_size,max_size))
    c = np.random.randint(1,10)
    grid[:, 0] = c
    return grid

"""m1=generate_1()
m2=solve_1(m1)
display(m1,m2)"""
