# arc_sussex
Development area of coded solutions for the Sussex attempt at the AGI challenge

## Conventions
Conventions for coded solutions is to have a generate and a solve function, with the name of the problem. For exmaple this would be the structure for problem 1:

```python
def solve_1(pattern): #solve given a pattern
    # @param pattern --> matrix
    # @returns matrix
    pass

def generate_1(): #generate a new pattern and the answer
    pass
```

THe filename will be given he number of the problem. So for the above example ```1.py```. This will make everything easier to bind later on.

Data type conventions are to use numpy arrays to represent patterns, and colours be represented by these colours.

```python

import numpy as np

colours={'black':0,'blue':1,'red':2,'green':3,'yellow':4,'gray':5,'pink':6,'orange':7,'light-blue':8,'maroon':9}
example_matrix = np.zeros((3,3))
```

## Utilities
There is a file ```utiles.py``` which can be imported to give useful functionality such as display images, generate shapes, add shapes to an existing canvas. Add more functions for useful functionality that comes up a lot in the challenges.

To display you input image and output, make use of this display function:

```python

def display(m1,m2):
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap, BoundaryNorm

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

```
