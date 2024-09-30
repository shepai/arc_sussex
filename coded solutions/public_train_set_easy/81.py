import numpy as np
from utils import *
colours={'black':0,'blue':1,'red':2,'green':3,'yellow':4,'gray':5,'pink':6,'orange':7,'light-blue':8,'maroon':9}

def solve_81(pattern):
    assert pattern.shape == (7, 7), f"Incorrect input size {pattern.shape}"
    new = pattern.copy()
    for i in range(6):
        for j in range(6):
            subgrid = new[i:i+2, j:j+2]
            if np.sum(subgrid == 0) == 1:
                subgrid[subgrid == 0] = 1
    return new

#bit complicated but there weren't any neighbouring blocks in the examples, and it makes the solution easier
def generate_81():
    grid = np.zeros((7, 7), dtype=int)
    available_positions = [(i, j) for i in range(6) for j in range(6)]
    np.random.shuffle(available_positions)
    placed_positions = []
    for _ in range(np.random.randint(1, 5)):
        for idx, (i, j) in enumerate(available_positions):
            if not any(abs(i - x) <= 2 and abs(j - y) <= 2 for (x, y) in placed_positions):
                grid[i:i+2, j:j+2] = 8
                a, b = np.random.randint(2), np.random.randint(2)
                grid[i+a, j+b] = 0
                placed_positions.append((i, j))
                available_positions.pop(idx)
                break
    
    return grid


"""m1=generate_1()
m2=solve_1(m1)
display(m1,m2)"""

