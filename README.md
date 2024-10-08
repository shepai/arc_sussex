# arc_sussex
Development area of coded solutions for the Sussex attempt at the AGI challenge

## Getting Started 

```sh
$ git clone https://github.com/shepai/arc_sussex
$ cd arc_sussex 
$ python -m venv .venv && source .venv/bin/activate 
$ pip install -r requirements.txt 
```

Most of the solutions so far make use of the utility functions provided by the arc_utils pacakge. In order to get started with development, you may need to build this package manually. Simply run `pip install .` inside the `arc_utils` directory from within your virtual environment. 


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
