import numpy as np
from arc_utils import COLOURS, display


def solve_1(pattern):  # solve given a pattern
    # @param pattern --> matrix
    # @returns matrix
    assert pattern.shape == (2, 2), "Incorrect input size " + str(pattern.shape)
    new = np.zeros((6, 6))
    for i in range(0, 6, 2):
        for j in range(0, 6, 2):
            new[i : i + 2, j : j + 2] = pattern
    return new


def generate_1():  # generate a new pattern and the answer
    random_matrix_numpy = np.random.randint(len(list(COLOURS.keys())) - 1, size=(2, 2))
    return random_matrix_numpy


if __name__ == "__main__":
    m1 = generate_1()
    m2 = solve_1(m1)
    display(m1, m2)
