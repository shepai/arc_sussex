import numpy as np
from arc_utils import display, solution_for


@solution_for('3c9b0459')
def solve_87(pattern):
    assert pattern.shape == (3, 3), f"Incorrect input size {pattern.shape}"
    return np.flipud(np.fliplr(pattern))


def generate_87():
    return np.random.randint(0, 10, (3, 3))


if __name__ == "__main__":
    m1 = generate_87()
    m2 = solve_87(m1)
    display(m1, m2)
