import os, shutil, subprocess, sys
import pandas as pd
from pathlib   import Path
from arc_utils import puzzles, solutions, puzzle_numbers



script_dir  = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(script_dir, '..')



def fetch_data():
    
    """Fetches the data directory from the ARC-AGI repo and places it the same directory"""
    
    if os.path.isdir(os.path.join(project_dir, 'data')): return
    
    clone_dir = os.path.join(script_dir, 'temp_clone')
    subprocess.run(['git', 'clone', "https://github.com/fchollet/ARC-AGI", clone_dir],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    data_dir = os.path.join(clone_dir, 'data')
    shutil.move(data_dir, project_dir)

    if os.name == 'nt': subprocess.run(['rmdir', '/S', '/Q', clone_dir], shell=True)
    else:               subprocess.run(['rm', '-rf', clone_dir])

fetch_data()





def run_coded_solutions(directory):

    filenames = [fn for fn in os.listdir(directory) if fn.endswith('.py')]

    for filename in filenames:
            
        filepath       = os.path.join(directory, filename)
        short_filepath = Path(*Path(filepath).parts[-2:])
        
        #print(f"Running {short_filepath}...")
        
        with open(filepath, 'r') as file:
            script_content = file.read()
        
        try:    exec(script_content, {"__name__": "__not_main__"})
        except: print(f'Encountered error in file {short_filepath}.')

dir1 = os.path.join(project_dir, 'coded solutions', 'public_train_set_easy')
dir2 = os.path.join(project_dir, 'coded solutions', 'public_eval_set_hard')
run_coded_solutions(dir1)
run_coded_solutions(dir2)





evaluation_results = []

for puzzle_id, puzzle_solutions in solutions.items():
    puzzle_number = puzzle_numbers[puzzle_id]
    puzzle = puzzles[puzzle_id]
    for solution in puzzle_solutions:
        evaluation_results.append([puzzle_number]+solution.evaluate_for(puzzle))

evaluation_results.sort()

def color_boolean(val):
    if isinstance(val, bool):
        return f"\033[32mPass\033[00m" if val else f"\033[31mFail\033[00m"
    return f"\033[00m{val}\033[00m"

columns = [color_boolean(h) for h in ['Puzzle number','Puzzle ID','Solution ID','Training','Testing']]

df = pd.DataFrame(evaluation_results, columns=columns)
df = df.map(color_boolean)
print('\n'+df.to_string(index=False, col_space=24)+'\n')