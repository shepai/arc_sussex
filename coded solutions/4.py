
import numpy as np
from utils import *
colours={'black':0,'blue':1,'red':2,'green':3,'yellow':4,'gray':5,'pink':6,'orange':7,'light-blue':8,'maroon':9}

def solve_4(pattern): #solve given a pattern
    # @param pattern --> matrix
    # @returns matrix
    new=np.zeros_like(pattern)
    points=np.argwhere(pattern>0)[:,]
    furthest=np.max(np.argwhere(pattern>0)[:,])
    print(points)
    print(furthest)
    return new

def generate_4(): #generate a new pattern and the answer
    c=np.random.randint(0,len(list(colours.keys()))-1)
    canvas = np.zeros((np.random.randint(8,20), np.random.randint(8,20)))
    canvas=draw_shape(canvas)
    canvas[canvas==1]=c
    c1=0
    t=1
    if c1==t: t=2 #prevent being same colour
    if np.random.randint(0,3)==3: #random chance of another shape
        pass
    c=np.random.randint(0,len(list(colours.keys()))-1)
    canvas=add_shape(canvas)
    canvas[canvas==t]=c
    return canvas



m1=generate_4()
m2=solve_4(m1)
display(m1,m2)