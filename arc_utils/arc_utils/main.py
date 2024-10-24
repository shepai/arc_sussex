import matplotlib, os, json
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np
from typing import Union

COLOURS = {
    "black": 0,
    "blue": 1,
    "red": 2,
    "green": 3,
    "yellow": 4,
    "gray": 5,
    "pink": 6,
    "orange": 7,
    "light-blue": 8,
    "maroon": 9,
}


def display(m1: np.ndarray, m2: np.ndarray, filename: Union[str, None] = None):
    """
    Creates a visual representation of the problem, and its solution.

    Parameters:
    m1: The problem, represented as an nxn numpy matrix, with values 0-9,
        representing the colour of the cell.
    m2: The solution to the problem, also represented as a mxm matrix with
        values 0-9 representing the colour of the cell.
    filename: Optional, tells the function to where to save the image.
              If no value is provided, then just display the image instead.

    Returns: None
    """
    color_list = [colour.replace("-", "") for colour in list(COLOURS.keys())]

    # Create a colormap using these colors
    cmap = ListedColormap(color_list)
    norm = BoundaryNorm(boundaries=np.arange(-0.5, 10, 1), ncolors=10)

    _, axes = plt.subplots(1, 2, figsize=(8, 4))

    # plotting the first matrix
    axes[0].imshow(m1, cmap=cmap, norm=norm)
    axes[0].set_title("Input")
    axes[0].axis("off")

    # plotting the second matrix
    axes[1].imshow(m2, cmap=cmap, norm=norm)
    axes[1].set_title("Output")
    axes[1].axis("off")

    plt.tight_layout()
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)


def generate_random_shape(canvas, min_sides=3, max_sides=10, SIZE=2):
    """
    Generates a random closed polygon with a hollow interior.

    Parameters:
    - size: Tuple representing the size of the 2D numpy array (height, width)
    - min_sides: Minimum number of sides for the random shape (default 3)
    - max_sides: Maximum number of sides for the random shape (default 10)

    Returns:
    - List of points defining the shape
    """
    height, width = np.zeros_like(canvas).shape[:]
    # Number of sides of the polygon
    num_sides = np.random.randint(min_sides, max_sides)
    # Generate random points in a circle
    angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
    radius = min(height, width) // 6 + SIZE  # Ensure the shape fits in the canvas
    center = (
        np.random.randint(radius, height - radius),
        np.random.randint(radius, width - radius),
    )
    # Create random fluctuations in the radius
    random_radius = radius + np.random.randint(
        -radius // 4, radius // 4, size=num_sides
    )
    # Convert polar coordinates to Cartesian
    points = [
        (
            int(center[0] + random_radius[i] * np.sin(angles[i])),
            int(center[1] + random_radius[i] * np.cos(angles[i])),
        )
        for i in range(num_sides)
    ]
    # Close the polygon by appending the first point again
    points.append(points[0])

    return points


def draw_line(canvas, start, end):
    """
    Draws a line between two points using Bresenham's line algorithm.
    """
    x0, y0 = start
    x1, y1 = end

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        canvas[x0, y0] = 1  # Mark the point as part of the shape
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    return canvas


def add_shape(canvas, max_attempts=100):
    """
    Attempts to add a random shape to the canvas without it touching other shapes.

    Parameters:
    - canvas: The 2D numpy array to which the shape will be added
    - max_attempts: Maximum number of retries if shape overlaps with others

    Returns:
    - Modified canvas with the new shape added
    """
    height, width = canvas.shape
    shape_added = False
    attempt = 0

    while not shape_added and attempt < max_attempts:
        # Generate a random shape
        points = generate_random_shape(canvas, SIZE=np.random.randint(1, 2))
        # Create a temporary canvas to draw the new shape
        temp_canvas = np.zeros_like(canvas)
        # Draw the shape on the temporary canvas
        for i in range(len(points) - 1):
            temp_canvas = draw_line(temp_canvas, points[i], points[i + 1])
        # Check for overlap with the existing canvas
        if np.any(np.logical_and(canvas, temp_canvas)):
            # Overlap detected, retry
            attempt += 1
        else:
            # No overlap, add shape to canvas
            canvas += temp_canvas
            shape_added = True
    if not shape_added:
        print(f"Failed to add shape after {max_attempts} attempts.")
    return canvas


def plot_points(canvas, points):
    for i in range(len(points) - 1):
        canvas = draw_line(canvas, points[i], points[i + 1])

    return canvas


#######################################################

script_dir         = os.path.dirname(os.path.abspath(__file__))
project_dir        = os.path.join(script_dir,'..','..')

class Matrix(np.ndarray):

    """Provides methods for manipulating matrices of colors."""
    
    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return obj
    
    def size_str(matrix):
        height, width = matrix.shape
        return f'{width}x{height}'
    
    def __str__(matrix):
        """Stringifies the matrix contents in a human-readable format."""
        return '\n'.join(''.join(map(str,line)) for line in matrix)

class Example(dict):

    """An input-output pair in a puzzle."""

    def __init__(example, data):
        super().__init__(data)
        example.input  = Matrix(example['input'])
        example.output = Matrix(example['output'])

    def __repr__(example):
        return f"Input ({example.input.size_str()}):\n\n{example.input}\n\n" + \
               f"Output ({example.output.size_str()}):\n\n{example.output}"

class Puzzle(dict):
    """A collection of both training and testing input-output pairs that
       constitute a single puzzle."""
    
    def __init__(puzzle, fname):
        super().__init__(json.load(open(fname)))
        puzzle.id    = os.path.basename(fname).split('.')[0]
        puzzle.train = [Example(e) for e in puzzle['train']]
        puzzle.test  = [Example(e) for e in puzzle['test']]
    
    def __repr__(puzzle):
        return f'<Puzzle {puzzle.id}>'
    
    def worked_examples(puzzle):
        separator = f"\n\n{'='*15}\n\n"
        body = separator.join(f'Pair #{i}\n\n{e}' for (i,e) in enumerate(puzzle.train, start=1))
        return separator + body + separator

def get_puzzles(directory):
    output = {}
    for fname in os.listdir(directory):
        puzzle = Puzzle(os.path.join(directory, fname))
        output[puzzle.id] = puzzle
    return output

training_puzzles   = get_puzzles(os.path.join(project_dir, 'data/training'))
evaluation_puzzles = get_puzzles(os.path.join(project_dir, 'data/evaluation'))
puzzles            = training_puzzles | evaluation_puzzles

puzzle_numbers = {}
for puzzle_set in [training_puzzles, evaluation_puzzles]:
    for n,id in enumerate(sorted(puzzle_set),start=1):
        puzzle_numbers[id]=n


class Solution:
    def __init__(self, id, function, puzzle_id=''):
        self.id = id
        self.function = function
        self.puzzle_id = puzzle_id
    def evaluate_for(self, puzzle):
        passes_training = all(np.array_equal(self.function(example.input), example.output) for example in puzzle.train)
        passes_testing  = all(np.array_equal(self.function(example.input), example.output) for example in puzzle.test)
        return [puzzle.id, self.id, passes_training, passes_testing]

# Setting up a dictionary that will map puzzle IDs to Solution objects
solutions = {}

def solution_for(puzzle_id, solution_id=''):
    """Decorator. Registers a function as a solution to the puzzle
       given by puzzle_id. solution_id may be specified as well if
       the puzzle has multiple solutions."""
    def solution_registrator(f):
        if not puzzle_id in solutions: solutions[puzzle_id] = []
        solutions[puzzle_id].append(Solution(solution_id, f, puzzle_id))
        return f
    return solution_registrator