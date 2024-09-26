
import numpy as np

colours={'black':0,'blue':1,'red':2,'green':3,'yellow':4,'gray':5,'pink':6,'orange':7,'light-blue':8,'maroon':9}

def solve_3(pattern): #solve given a pattern
    # @param pattern --> matrix
    # @returns matrix
    assert pattern.shape==(6,3), "Incorrect input size "+str(pattern.shape)
    new=np.zeros((9,3))
    new[0:6,]=pattern
    new[6:,0:3]=pattern[2:5,:]
    return new
def generate_3(): #generate a new pattern and the answer
    c=np.random.randint(0,len(list(colours.keys()))-1)
    random_matrix_numpy = np.random.randint(2, size=(6, 3))
    random_matrix_numpy[random_matrix_numpy==1]=c
    return random_matrix_numpy

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

"""m1=generate_1()
m2=solve_1(m1)
display(m1,m2)"""