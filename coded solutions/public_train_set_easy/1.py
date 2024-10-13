import numpy as np
from arc_utils import display, COLOURS, solution_for

@solution_for('007bbfb7')
def solve_1(pattern):
    assert pattern.shape == (3, 3), f"Incorrect input size {pattern.shape}"
    new = np.zeros((9, 9))
    for i in range(3):
        for j in range(3):
            if pattern[i][j] != 0:
                new[3 * i : (i + 1) * 3, 3 * j : (j + 1) * 3] = pattern.copy()
    return new


def generate_1():  # generate a new pattern and the answer
    c = np.random.randint(0, len(list(COLOURS.keys())) - 1)
    random_matrix_numpy = np.random.randint(2, size=(3, 3))
    random_matrix_numpy[random_matrix_numpy == 1] = c
    return random_matrix_numpy


if __name__ == "__main__":
    m1 = generate_1()
    m2 = solve_1(m1)
    display(m1, m2)
