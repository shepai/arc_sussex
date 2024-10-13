import os, shutil, subprocess, sys
from pathlib   import Path
from arc_utils import solutions



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
        
        print(f"Running {short_filepath}...")
        
        with open(filepath, 'r') as file:
            script_content = file.read()
        
        exec(script_content, {"__name__": "__not_main__"})
        #try:    exec(script_content, {"__name__": "__not_main__"})
        #except: print('Encountered error.')


dir1 = os.path.join(project_dir, 'coded solutions', 'public_train_set_easy')
dir2 = os.path.join(project_dir, 'coded solutions', 'public_eval_set_hard')
run_coded_solutions(dir1)
run_coded_solutions(dir2)