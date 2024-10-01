import numpy as np
from utils import *
colours={'black':0,'blue':1,'red':2,'green':3,'yellow':4,'gray':5,'pink':6,'orange':7,'light-blue':8,'maroon':9}

def solve_82(pattern):
    assert pattern.shape[0] == 6, f"Incorrect input size {pattern.shape}"
    new = pattern.copy()
    for i in range(2):
      mask = new[2*i,:] != 0
      new[2*i+2,mask] = new[2*i,mask]
    for i in range(3):
        for j in range(1,pattern.shape[1]-1):
          if new[2*i,j] != 0:
            new[2 * i + 1, [j - 1, j + 1]] = new[2 * i, j]
    return new

def generate_82():
    # x-axis could be any size; I picked 30 as max
    x = np.random.randint(3, 30)
    grid = np.zeros((6, x), dtype=int)
    num_block = np.random.randint(1, int(x / 3))
    pos = np.arange(1, x - 1, step=3)
    np.random.shuffle(pos)
    grid[0, np.sort(pos[:num_block])] = np.random.randint(1, 10, size=num_block)
    return grid

"""m1=generate_1()
m2=solve_1(m1)
display(m1,m2)"""
