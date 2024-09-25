
import numpy as np

colours={'black':0,'blue':1,'red':2,'green':3,'yellow':4,'gray':5,'pink':6,'orange':7,'light-blue':8,'maroon':9}

example_matrix=np.array([[0,0,0],
                         [1,0,1],
                         [0,1,0]])
def solve_1(pattern): #solve given a pattern
    # @param pattern --> matrix
    # @returns matrix
    assert pattern.shape==(3,3), "Incorrect input size "+str(pattern.shape)
    new=np.zeros((9,9))
    for i in range(3):
        for j in range(3):
            if pattern[i][j]!=0: new[3*i:(i+1)*3,3*j:(j+1)*3]=pattern.copy()
    return new
def generate_1(): #generate a new pattern and the answer
    c=np.random.randint(0,len(list(colours.keys())-1))
    
print(solve_1(example_matrix))