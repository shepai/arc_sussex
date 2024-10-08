import numpy as np
from arc_utils import display, COLOURS, add_shape, generate_random_shape, plot_points


def solve_4(pattern):  # solve given a pattern
    # @param pattern --> matrix
    # @returns matrix
    new = np.zeros_like(pattern)
    points = np.argwhere(pattern > 0)[:,]
    furthest = np.max(np.argwhere(pattern > 0)[:,])
    print(points)
    print(furthest)
    return new


def generate_4():  # generate a new pattern and the answer
    c = np.random.randint(0, len(list(COLOURS.keys())) - 1)
    canvas = np.zeros((np.random.randint(8, 20), np.random.randint(8, 20)))
    points = generate_random_shape(canvas, SIZE=np.random.randint(1, 3))
    canvas = plot_points(canvas, points)
    canvas[canvas == 1] = c
    c1 = 0
    t = 1
    if c1 == t:
        t = 2  # prevent being same colour
    if np.random.randint(0, 3) == 2:  # random chance of another shape
        c = np.random.randint(0, len(list(COLOURS.keys())) - 1)
        canvas = add_shape(canvas)
        canvas[canvas == t] = c
    return canvas


if __name__ == "__main__":
    m1 = generate_4()
    m2 = solve_4(m1)
    display(m1, m2)
