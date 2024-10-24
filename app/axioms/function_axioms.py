# Function level axioms
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from arc_utils import Puzzle, get_puzzles
from rich import inspect
import numpy as np

MULTIPLICATIVE_RATIO_FAIL = 0

'''
TODO:
- Collect all outliers that follow a rule but return false
- Detect where output size needs puzzle context to be deduced 

'''
def predict_output_grid_size(input: Puzzle) -> tuple:
    """
    Predict output grid size from input grid size

    Args:
        input (Puzzle): Training input-output pairs and test input
    
    Returns:
        tuple: output grid size prediction

    Notes:
        - If the ratio of output grid size to input grid size is same for all training examples, 
          then the output grid size is predicted by multiplying the ratio with test input grid size.
        - If the output grid size remains same for all training examples, then the output grid size is predicted as the output grid size of the training examples.
        - If the difference between output grid size and input grid size is same for all training examples, then the output grid size is predicted by adding the difference with test input grid size.
        - If none of the above conditions are met, then the output grid size is predicted as the test input grid size.
    Author:
        Jack Speat (@Speaty)    

    """
    global MULTIPLICATIVE_RATIO_FAIL
    test_input = np.array(input.test[0]['input'])

    # Collect all training shapes
    train_shapes = []
    for eg in input.train:
        example_shape = {
            'input': np.array(eg['input']).shape,
            'output': np.array(eg['output']).shape
        }
        train_shapes.append(example_shape)

    # Common multiplicative ratio
    ratios = []
    for shape in train_shapes:
        ratio = shape['output'][0] / shape['input'][0]
        ratios.append(ratio)

    if len(set(ratios)) == 1:
        ratio = ratios[0]
        return (test_input.shape[0]*ratio, test_input.shape[1]*ratio)
    MULTIPLICATIVE_RATIO_FAIL += 1
    # print(input.id)

    # Input changes but Output remains same
    ins = []
    outs = []
    for shape in train_shapes:
        ins.append(shape['input'])
        outs.append(shape['output'])
    
    if len(set(outs)) == 1:
        return outs[0]


    # Fixed Difference
    differences = []
    for shape in train_shapes:
        diff = shape['output'][0] - shape['input'][0]
        differences.append(diff)

    if len(set(differences)) == 1:
        diff = differences[0]
        return (test_input.shape[0]+diff, test_input.shape[1]+diff)


    return test_input.shape # input = output

    
def detect_repeating_patterns(input):
    pass

def test_predict_output_grid_size(input: Puzzle) -> bool:

    return predict_output_grid_size(puzzle) == np.array(input.test[0]['output']).shape


if __name__ == "__main__":
    # Testing for output grid size
    training_puzzles   = get_puzzles('data/training')
    evaluation_puzzles = get_puzzles('data/evaluation')
    puzzles = training_puzzles | evaluation_puzzles

    inspect(puzzles['3618c87e'])

    results = []
    for puzzle in puzzles.values():
        results.append(test_predict_output_grid_size(puzzle))
    true = sum(results)
    print(f"Accuracy: {true}/{len(results)}")
    print(f"Common Multiplicative Ratio: {MULTIPLICATIVE_RATIO_FAIL}/{len(results)}")
'''
Output == Input
Accuracy: 262/400 (just training)
Accuracy: 532/800 (training + evaluation)

Common Multiplicative Ratio:
Accuracy: 301/400 (just training)
Accuracy: 606/800 (training + evaluation)

Common Multiplicative Ratio + Common Fixed Difference:
Accuracy: 305/400 (just training)
Accuracy: 610/800 (training + evaluation)

Common Multiplicative Ratio + Fixed Output Size + Common Fixed Difference:
Accuracy: 317/400 (just training)
Accuracy: 632/800 (training + evaluation)

'''