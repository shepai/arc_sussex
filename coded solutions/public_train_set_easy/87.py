import numpy as np
from utils import *
colours={'black':0,'blue':1,'red':2,'green':3,'yellow':4,'gray':5,'pink':6,'orange':7,'light-blue':8,'maroon':9}

def solve_87(pattern):
    assert pattern.shape == (3,3), f"Incorrect input size {pattern.shape}"
    return np.flipud(np.fliplr(pattern))

def generate_87():
    return np.random.randint(0,10,(3,3))

"""m1=generate_1()
m2=solve_1(m1)
display(m1,m2)"""
