import numpy as np
from arc_utils import display


def solve_84(pattern):
    assert pattern.shape[0] == pattern.shape[1], f"Incorrect input size {pattern.shape}"
    new = pattern.copy()
    n = pattern.shape[0]
    new[np.arange(n - 1), n - 1 - np.arange(n - 1)] = 2
    new[n - 1, 1:] = 4
    return new


def generate_84():
    max_size = np.random.randint(20)
    grid = np.zeros((max_size, max_size))
    c = np.random.randint(1, 10)
    grid[:, 0] = c
    return grid


if __name__ == "__main__":
    m1 = generate_84()
    m2 = solve_84(m1)
    display(m1, m2)
