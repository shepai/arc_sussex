import numpy as np

def changecolour(canvas,from_,to):
    canvas[np.where(canvas==from_)]=to
    return canvas
def shift(canvas,row,col,vector):
    newcanvas=canvas.copy()
    if row != -1 and col != -1:
        newcanvas[row][col] = 0
        newcanvas[row + vector[0]][col + vector[1]] = canvas[row][col]
    elif row != -1:  #shift entire row
        newcanvas[row] = 0
        newcanvas[row + vector[0]] = canvas[row]
    elif col != -1:  #shift entire column
        newcanvas[:, col] = 0
        newcanvas[:, col + vector[1]] = canvas[:, col]
    return newcanvas
        

if __name__ == "__main__":
    #testing 
    #colour
    colour_canvas=np.zeros((10,10))+2
    canvas=changecolour(colour_canvas,2,4)
    assert np.sum(canvas)==4*10*10, "Canvas has not changed to the right colour"
    print("Colour change task SUCCESS\n")
    #shift
    canvas=np.zeros((10,10))
    canvas[1,3:6]=1
    canvas_=shift(canvas,1,-1,[2,0])
    assert np.sum(canvas_[1])==0, "Has not wiped the canvas"
    assert np.sum(canvas_[3])!=0, "Has not moved canvas"
    canvas_=shift(canvas,-1,3,[0,4])
    assert np.sum(canvas_[:,3])==0, "Has not wiped the canvas"
    assert np.sum(canvas_[:,7])!=0, "Has not moved canvas"
    canvas_=shift(canvas,-1,3,[0,4])
    assert np.sum(canvas_[:,3])==0, "Has not wiped the canvas"
    assert np.sum(canvas_[:,7])!=0, "Has not moved canvas"
    print("Shift SUCCESS\n")