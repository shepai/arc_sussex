import numpy as np
from arc_utils import COLOURS, display, solution_for


@solution_for('3af2c5a8')
def solve_83(pattern):
    assert pattern.shape == (3, 4), f"Incorrect input size {pattern.shape}"
    new = np.zeros((6, 8))
    new[:3, :4] = pattern.copy()
    new[3:, :4] = pattern[::-1, :].copy()
    new[:3, 4:] = pattern[:, ::-1].copy()
    new[3:, 4:] = pattern[::-1, ::-1].copy()
    return new


def generate_83():
    c = np.random.randint(0, len(list(COLOURS.keys())) - 1)
    random_matrix_numpy = np.random.randint(2, size=(4, 3))
    random_matrix_numpy[random_matrix_numpy == 1] = c
    return random_matrix_numpy


if __name__ == "__main__":
    m1 = generate_83()
    m2 = solve_83(m1)
    display(m1, m2)
