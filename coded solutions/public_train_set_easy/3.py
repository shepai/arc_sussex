import numpy as np
from arc_utils import display, COLOURS


def solve_3(pattern):  # solve given a pattern
    # @param pattern --> matrix
    # @returns matrix
    assert pattern.shape == (6, 3), "Incorrect input size " + str(pattern.shape)
    new = np.zeros((9, 3))
    new[0:6,] = pattern
    new[6:, 0:3] = pattern[2:5, :]
    return new


def generate_3():  # generate a new pattern and the answer
    c = np.random.randint(0, len(list(COLOURS.keys())) - 1)
    random_matrix_numpy = np.random.randint(2, size=(6, 3))
    random_matrix_numpy[random_matrix_numpy == 1] = c
    return random_matrix_numpy


if __name__ == "__main__":
    m1 = generate_3()
    m2 = solve_3(m1)
    display(m1, m2)
