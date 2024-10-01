import numpy as np
from utils import *
colours={'black':0,'blue':1,'red':2,'green':3,'yellow':4,'gray':5,'pink':6,'orange':7,'light-blue':8,'maroon':9}

def solve_83(pattern):
    assert pattern.shape == (3,4), f"Incorrect input size {pattern.shape}"
    new=np.zeros((6,8))
    new[:3,:4] = pattern.copy()
    new[3:,:4] = pattern[::-1,:].copy()
    new[:3,4:] = pattern[:,::-1].copy()
    new[3:,4:] = pattern[::-1,::-1].copy()
    return new

def generate_82():
    c=np.random.randint(0,len(list(colours.keys()))-1)
    random_matrix_numpy = np.random.randint(2, size=(4, 3))
    random_matrix_numpy[random_matrix_numpy==1]=c
    return random_matrix_numpy

"""m1=generate_1()
m2=solve_1(m1)
display(m1,m2)"""
