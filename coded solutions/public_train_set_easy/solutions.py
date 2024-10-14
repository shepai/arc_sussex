########################################################
#
# Code in this file was originally written independently
# of this repository, which is why it doesn't use any
# of the tools available elsewhere in the repo.
#
# Integrating these solutions into the repo will take
# some work, but for now I wanted them to be available
# anyway.
#
# To refactor later.
#
#    -- Guy
########################################################


import numpy as np

from   arc_utils   import solution_for

from   functools   import reduce
from   collections import Counter
from   copy        import deepcopy as copy

BLACK, BLUE, RED, GREEN, YELLOW, GRAY, PINK, ORANGE, CYAN, CRIMSON = range(10)

############################

# Helper classes

class Matrix(list):

    """Provides methods for manipulating matrices of colors."""

    def __init__(matrix, array):
        super().__init__(array.tolist() if isinstance(array, np.ndarray) else array)
    
    def height(matrix): return len(matrix)
    def width (matrix): return len(matrix[0])
    def size  (matrix): return f'{matrix.width()}x{matrix.height()}'
    
    def row   (matrix, i): return matrix[i]
    def column(matrix, j): return [matrix[i][j] for i in range(matrix.height())]
    
    def flip_vertically  (matrix): return Matrix(matrix[::-1])
    def flip_horizontally(matrix): return Matrix([line[::-1] for line in matrix])
        
    def transpose(matrix):
        return Matrix([[matrix[i][j] for i in range(matrix.height())] for j in range(matrix.width())])
    
    @classmethod
    def empty(_, width, height):
        """Returns an empty matrix with the given width and height."""
        return Matrix([[0]*width for i in range(height)])
    
    def __repr__(matrix):
        """Prints the matrix contents in a human-readable format."""
        return '\n'.join(''.join(map(str,line)) for line in matrix)
    
    def cellwise(matrix, function):
        """Takes a function and returns the current matrix, with that
           function applied to every cell of the matrix.
           
           The function provided should accept three arguments:
           a matrix object,and the i and j coordinates of the cell
           to be processed."""
        matrix = copy(matrix)
        for i in range(matrix.height()):
            for j in range(matrix.width()):
                matrix[i][j] = function(matrix, i, j)
        return matrix
    
    def areas(matrix):
        """A generator for all the Area objects available in the matrix."""
        for i_min in range(matrix.height()):
            for i_max in range(i_min, matrix.height()):
                for j_min in range(matrix.width()):
                    for j_max in range(j_min, matrix.width()):
                        limits = (i_min, i_max, j_min, j_max)
                        yield Area(matrix, limits)
    
    def crop_to(matrix, area):
        """Given an Area object, returns a version of the matrix cropped to that area."""
        return Matrix([l for l in area])
    
    def colors(matrix):
        """Returns a map that gives the frequency of each color in the matrix."""
        return Counter(reduce(lambda a,b: a+b, matrix))
    
    def multiply(matrix1, matrix2):
        """Makes a copy of matrix1 for every truthy cell in matrix2.
           For example, m.multiply([[1,1]]) would return a matrix twice as wide
           as the original and containing two copies of it side by side."""
        output = Matrix.empty(matrix1.width()*matrix2.width(), matrix1.height()*matrix2.height())
        for i1 in range(matrix1.height()):
            for j1 in range(matrix1.width()):
                for i2 in range(matrix2.height()):
                    for j2 in range(matrix2.width()):
                        output[i1+i2*matrix1.height()][j1+j2*matrix1.width()] = \
                            matrix1[i1][j1] if matrix2[i2][j2] else 0
        return output
    
    def magnify(matrix, multiplier):
        """Returns a copy of the matrix where each 1x1 cell has been replaced by a
           multiplier x multiplier square."""
        output = Matrix.empty(matrix.width()*multiplier, matrix.height()*multiplier)
        for i1 in range(matrix.height()):
            for j1 in range(matrix.width()):
                for i2 in range(multiplier):
                    for j2 in range(multiplier):
                        output[i1*multiplier+i2][j1*multiplier+j2] = matrix[i1][j1]
        return output

    def pad(matrix, sides, color):
      """Returns a copy of the matrix with a padding of the given color on the given
         sides."""
      if 'left'   in sides: matrix = Matrix([[color]+line for line in matrix])
      if 'right'  in sides: matrix = Matrix([line+[color] for line in matrix])
      if 'top'    in sides: matrix = Matrix([[color]*matrix.width()] + matrix)
      if 'bottom' in sides: matrix = Matrix(matrix + [[color]*matrix.width()])
      return matrix

    def fill_area(matrix, area, color):
      """Returns a copy of the matrix with the rectangular Area given painted
         in the given color."""
      matrix = copy(matrix)
      for i in range(area.i_min, area.i_max+1):
        for j in range(area.j_min, area.j_max+1):
          matrix[i][j] = color
      return matrix


    def fill(matrix, location, color):
      """Returns a copy of the matrix with the area containing the given location
         flood-filled with the given color."""
      matrix = copy(matrix)
      known_to_color  = set()
      new_to_color    = {location}
      while new_to_color:
        new_new_to_color = set()
        for (i,j) in new_to_color:
          new_new_to_color |= {(a,b) for (a,b) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0<=a<matrix.height() and 0<=b<matrix.width() and matrix[a][b]==matrix[i][j]}
        known_to_color |= new_to_color
        new_to_color = new_new_to_color - known_to_color
      for (i,j) in known_to_color:
        matrix[i][j] = color
      return matrix

    def replace_colors(matrix, replacements):
      """Takes a dictionary mapping colors to other colors, returns a copy of
         the matrix with the colors replaced accordingly."""
      return matrix.cellwise(lambda m,i,j: replacements.get(m[i][j],m[i][j]))




class Area:
    """An Area object denotes a rectangular area within a given matrix."""
    
    def __init__(area, matrix, limits):
        area.matrix = matrix
        area.limits = limits
        area.i_min, area.i_max, area.j_min, area.j_max = limits
    
    def __getitem__(area, k):
        return area.matrix[(area.i_min + k) if k>=0 else (area.i_max + 1 + k)][area.j_min:area.j_max+1]
    
    def __iter__(area):
        for i in range(area.i_max-area.i_min+1): yield area[i]
    
    def width(area):  return area.j_max - area.j_min + 1
    def height(area): return area.i_max - area.i_min + 1
    def area(area):   return area.width() * area.height()
    
    def __hash__(area):
        return hash(area.matrix.crop_to(area).__repr__())
    
    def __eq__(area, other_area):
        return hash(other_area) == hash(area)



############################

# Helper functions


def crop_while(matrix, condition):
  matrix = copy(matrix)
  i_min, i_max, j_min, j_max = 0, matrix.height()-1, 0, matrix.width()-1
  while i_min <= i_max and condition(matrix[i_min]): i_min += 1
  while i_max >= i_min and condition(matrix[i_max]): i_max -= 1
  matrix = matrix.transpose()
  while j_min <= j_max and condition(matrix[j_min]): j_min += 1
  while j_max >= j_min and condition(matrix[j_max]): j_max -= 1
  matrix = matrix.transpose()
  return Area(matrix, (i_min, i_max, j_min, j_max))

def crop_to_yellow_markers(matrix):
  return crop_while(matrix, lambda r: (4 not in r))

def remove_black_edges(matrix):
  return crop_while(matrix, lambda r: not any(r))

def valid_overlap(matrix1, matrix2, moves_right, moves_down):
  if matrix1.width()  + moves_right > matrix2.width() : return False
  if matrix1.height() + moves_down  > matrix2.height(): return False
  for i in range(matrix1.height()):
    for j in range(matrix1.width()):
      target = matrix2[i+moves_down][j+moves_right]
      if target == 0: continue
      if target == matrix1[i][j]: continue
      return False
  return True

def find_valid_overlap(matrix1, matrix2):
  for moves_right in range(matrix2.width()-matrix1.width()+1):
    for moves_down in range(matrix2.height()-matrix1.height()+1):
      if valid_overlap(matrix1, matrix2, moves_right, moves_down):
        return (moves_right, moves_down)

def actually_overlap(matrix1, matrix2, moves_right, moves_down):
  output = copy(matrix2)
  for i in range(matrix1.height()):
    for j in range(matrix1.width()):
      output[i+moves_down][j+moves_right] = matrix1[i][j]
  return output
  
def has_solid_border(area):
  return len(set(area[0] + area[-1] + [l[0] for l in area] + [l[-1] for l in area]))==1

def has_blue_border(area):
  return has_solid_border(area) and area[0][0]==1

def is_black(area):
  return set(area.matrix.crop_to(area).colors())=={BLACK}

def copy_area(source, destination, location):
  a,b = location
  for i in range(source.height()):
    for j in range(source.width()):
      if not(a+i<destination.height() and b+j<destination.width()): continue
      destination[a+i][b+j] = source[i][j]


############################

# Solutions


@solution_for('8403a5d5')
def f(input_matrix):
  input_matrix = Matrix(input_matrix)
  colored_cell_x = [k==0 for k in input_matrix[-1]].index(False)
  cell_color     = input_matrix[-1][colored_cell_x]
  output_matrix  = copy(input_matrix)
  for j in range(colored_cell_x, output_matrix.width(), 2):
    for i in range(output_matrix.height()):
      output_matrix[i][j] = cell_color
  for j in range(colored_cell_x + 1, output_matrix.width(), 2):
    output_matrix[0 if (j-colored_cell_x)%4==1 else -1][j] = 5
  return output_matrix


@solution_for('846bdb03')
def f(input_matrix):
  input_matrix          = Matrix(input_matrix)
  rect1                 = crop_to_yellow_markers(input_matrix)
  output_matrix         = input_matrix.crop_to(rect1)
  modified_input_matrix = input_matrix.fill_area(rect1, BLACK)
  rect2                 = remove_black_edges(modified_input_matrix)
  modified_input_matrix = modified_input_matrix.crop_to(rect2)
  left_side_color       = max(line[0] for line in modified_input_matrix)
  right_side_color      = max(line[-1] for line in modified_input_matrix)
  modified_input_matrix = modified_input_matrix.pad(['left'] ,  left_side_color)
  modified_input_matrix = modified_input_matrix.pad(['right'], right_side_color)
  for mat in [modified_input_matrix, modified_input_matrix.flip_horizontally()]:
    overlap_coords = find_valid_overlap(mat, output_matrix)
    if overlap_coords: return actually_overlap(mat, output_matrix, *overlap_coords)


@solution_for('855e0971')
def f(input_matrix):
  input_matrix          = Matrix(input_matrix)
  output_matrix = copy(input_matrix)
  horizontal = len(set(output_matrix[0]) - {0}) == 1
  if not horizontal: output_matrix = output_matrix.transpose()
  target = [list(set(line)-{0})[0] for line in output_matrix]
  for j in range(output_matrix.width()):
    changed = set(target[i] for i in range(output_matrix.height()) if output_matrix[i][j]==0)
    for i in range(output_matrix.height()):
      if output_matrix[i][j] in changed: output_matrix[i][j]=0
  if not horizontal: output_matrix = output_matrix.transpose()
  return output_matrix


@solution_for('85c4e7cd')
def f(input_matrix):
  input_matrix          = Matrix(input_matrix)
  output_matrix = copy(input_matrix)
  color_order = input_matrix[(input_matrix.height()-1)//2][:(input_matrix.height()-1)//2+1]
  color_replacements = {color_order[i]:color_order[-i-1] for i in range(len(color_order))}
  output_matrix = output_matrix.replace_colors(color_replacements)
  return output_matrix


@solution_for('868de0fa')
def f(input_matrix):
  input_matrix          = Matrix(input_matrix)
  output_matrix = copy(input_matrix)
  squares = [area for area in output_matrix.areas() if area.width()>1 and area.height()>1 and has_blue_border(area)]
  for square in squares:
    location_to_fill = (square.i_min+1, square.j_min+1)
    output_matrix = output_matrix.fill(location_to_fill, ORANGE if square.width()%2==1 else RED)
  return output_matrix


@solution_for('8731374e')
def f(input_matrix):
  input_matrix          = Matrix(input_matrix)
  rectangle        = max((area for area in input_matrix.areas() if has_solid_border(area)), key=lambda area: area.area())
  output_matrix    = input_matrix.crop_to(rectangle)
  background_color = output_matrix[0][0]
  other_color      = list(set(output_matrix.colors()) - {background_color})[0]
  rows_to_color    = {i for i in range(output_matrix.height()) if other_color in output_matrix.row(i)}
  columns_to_color = {j for j in range(output_matrix.width())  if other_color in output_matrix.column(j)}
  output_matrix    = output_matrix.cellwise(lambda m,i,j: other_color if (i in rows_to_color) or (j in columns_to_color) else background_color)
  return output_matrix


@solution_for('88a10436')
def f(input_matrix):
  input_matrix          = Matrix(input_matrix)
  output_matrix = copy(input_matrix)
  shape     = crop_while(input_matrix, lambda l: set(l).issubset({0,5}))
  gray_cell = crop_while(input_matrix, lambda l: 5 not in l)
  copy_area(shape, output_matrix, (gray_cell.i_min-1, gray_cell.j_min-1))
  return output_matrix


@solution_for('88a62173')
def f(input_matrix):
  input_matrix          = Matrix(input_matrix)
  shapes = [Area(input_matrix, (i,i+1,j,j+1)) for i in [0,3] for j in [0,3]]
  least_common_shape = Counter(shapes).most_common()[-1][0]
  output_matrix = input_matrix.crop_to(least_common_shape)
  return output_matrix


@solution_for('890034e9')
def f(input_matrix):
  input_matrix          = Matrix(input_matrix)
  input_matrix_colors = input_matrix.colors()
  potential_areas = [area for area in input_matrix.areas() if area.width()>2 and area.height()>2 and has_solid_border(area)]
  rectangle  = [area for area in potential_areas if input_matrix.crop_to(area).colors()[area[0][0]]==input_matrix_colors[area[0][0]]][0]
  dark_spots = [area for area in input_matrix.areas() if area.width()==rectangle.width()-2 and area.height()==rectangle.height()-2 and is_black(area)]
  output_matrix = copy(input_matrix)
  for dark_spot in dark_spots:
    copy_area(rectangle, output_matrix, (dark_spot.i_min-1,dark_spot.j_min-1))
  return output_matrix


@solution_for('8a004b2b')
def f(input_matrix):
  # This solution is incomplete
  input_matrix          = Matrix(input_matrix)
  rect1                 = crop_to_yellow_markers(input_matrix)
  output_matrix         = input_matrix.crop_to(rect1)
  modified_input_matrix = input_matrix.fill_area(rect1, BLACK)
  rect2                 = remove_black_edges(modified_input_matrix)
  modified_input_matrix = modified_input_matrix.crop_to(rect2)
  multiplier = 1
  while True:
    resized_shape = modified_input_matrix.magnify(multiplier)
    if resized_shape.width() > output_matrix.width() or resized_shape.height() > output_matrix.height(): break
    #print(find_valid_overlap(resized_shape, output_matrix))
    multiplier += 1
  return input_matrix


@solution_for('8be77c9e')
def f(input_matrix):
  input_matrix          = Matrix(input_matrix)
  output_matrix = Matrix.empty(input_matrix.width(), input_matrix.height()*2)
  copy_area(input_matrix, output_matrix, (0,0))
  flipped_input = input_matrix.flip_vertically()
  copy_area(flipped_input, output_matrix, (input_matrix.height(),0))
  return output_matrix