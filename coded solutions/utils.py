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

    