import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np

def display(m1,m2):
    color_list = ['black', 'blue', 'red', 'green', 'yellow', 'gray',
                'pink', 'orange', 'lightblue', 'maroon']

    # Create a colormap using these colors
    cmap = ListedColormap(color_list)
    norm = BoundaryNorm(boundaries=np.arange(-0.5, 10, 1), ncolors=10)

    fig, axes = plt.subplots(1, 2, figsize=(8, 4))

    #plotting the first matrix
    axes[0].imshow(m1, cmap=cmap, norm=norm)
    axes[0].set_title("Input")
    axes[0].axis('off')

    #plotting the second matrix
    axes[1].imshow(m2, cmap=cmap, norm=norm)
    axes[1].set_title("Output")
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()

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
        canvas[x0, y0] = 1  #Mark the point as part of the shape
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
def draw_shape(canvas):
    height,width=canvas.shape[:]

    num_sides = np.random.randint(8, 25)

    #Generate random points in a circle
    angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
    radius = min(height, width) // 3  #Ensure the shape fits in the canvas
    center = ((height+np.random.randint(-2,2) )// 2, (width+np.random.randint(-2,2) )// 2)

    #Create random fluctuations in the radius
    random_radius = radius + np.random.randint(-radius // 3, radius // 3, size=num_sides)

    #Convert polar coordinates to Cartesian
    points = [
        (
            int(center[0] + random_radius[i] * np.sin(angles[i])),
            int(center[1] + random_radius[i] * np.cos(angles[i])),
        )
        for i in range(num_sides)
    ]

    #Close the polygon by appending the first point again
    points.append(points[0])

    #Draw the shape outline on the canvas
    for i in range(len(points) - 1):
        canvas = draw_line(canvas, points[i], points[i + 1])

    return canvas
