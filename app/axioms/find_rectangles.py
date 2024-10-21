import numpy as np


def find_rectangles(array):
    rows, cols = array.shape
    visited = np.zeros_like(array, dtype=bool)
    rectangles = []

    def dfs(r, c, value):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r, c] or array[r, c] != value:
            return None

        visited[r, c] = True

        bounds = [r, r, c, c]

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            result = dfs(r + dr, c + dc, value)
            if result:
                bounds[0] = min(bounds[0], result[0])
                bounds[1] = max(bounds[1], result[1])
                bounds[2] = min(bounds[2], result[2])
                bounds[3] = max(bounds[3], result[3])

        return bounds

    for r in range(rows):
        for c in range(cols):
            if array[r, c] != 0 and not visited[r, c]:
                rectangle_bounds = dfs(r, c, array[r, c])
                if rectangle_bounds:
                    rectangles.append(rectangle_bounds)

    return rectangles


def get_largest_rectangle(board):
    rectangles = find_rectangles(board)
    areas = np.array([
        get_rectangle_area(rectangle[0], rectangle[2], rectangle[1], rectangle[3])
        for rectangle in rectangles
    ])

    largest_rect_idx = np.argmax(areas)
    return rectangles[largest_rect_idx]


def get_rectangle_area(top, left, bottom, right):
    return (bottom - top + 1) * (right - left + 1)
