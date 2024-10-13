from arc_utils import COLOURS, display, generate_random_shape, plot_points, add_shape, solution_for
import numpy as np


def fill(canvas, point):
    canvas[point[0]][point[1]] = 0
    if point[0] + 1 < len(canvas):
        if canvas[point[0] + 1][point[1]] == 4:
            canvas = fill(canvas, [point[0] + 1, point[1]])
    if point[1] + 1 < len(canvas[0]):
        if canvas[point[0]][point[1] + 1] == 4:
            canvas = fill(canvas, [point[0], point[1] + 1])
    if point[0] - 1 > 0:
        if canvas[point[0] - 1][point[1]] == 4:
            canvas = fill(canvas, [point[0] - 1, point[1]])
    if point[1] - 1 > 0:
        if canvas[point[0]][point[1] - 1] == 4:
            canvas = fill(canvas, [point[0], point[1] - 1])
    return canvas


@solution_for('00d62c1b')
def solve_2(pattern):  # solve given a pattern
    # @param pattern --> matrix
    # @returns matrix
    new = pattern.copy()
    new[new == 0] = 4
    canvas = fill(new, [0, 0])
    return canvas


def generate_2():  # generate a new pattern and the answer
    h = np.random.randint(8, 20)
    w = np.random.randint(8, 20)
    canvas = np.zeros((h, w))
    c = np.random.randint(0, len(list(COLOURS.keys())) - 1)
    canvas = np.zeros((np.random.randint(8, 20), np.random.randint(8, 20)))
    points = generate_random_shape(canvas, SIZE=np.random.randint(1, 3))
    canvas = plot_points(canvas, points)
    canvas[canvas == 1] = 3

    if np.random.randint(0, 3) == 2:  # random chance of another shape
        c = np.random.randint(0, len(list(COLOURS.keys())) - 1)
        canvas = add_shape(canvas)
        canvas[canvas == 1] = 3
    return canvas


if __name__ == "__main__":
    m1 = generate_2()
    m2 = solve_2(m1)
    display(m1, m2)
