import json
import os
from pathlib import Path

import numpy as np

current_file_dir = os.path.dirname(os.path.abspath(__file__))


def convert_data_to_numpy(data):
    train = data['train']
    test = data['test']

    train_np = []
    test_np = []

    for train_item in train:
        img_pair = {
            'input': np.array(train_item['input']),
            'output': np.array(train_item['output'])
        }
        train_np.append(img_pair)

    for test_item in test:
        img_pair = {'input': np.array(test_item['input'])}
        if 'output' in test_item:
            img_pair['output'] = np.array(test_item['output'])
        test_np.append(img_pair)

    return {'train': train_np, 'test': test_np}


def read_training_problem_data(problem_number):
    json_files = [file.name for file in Path(os.path.join(current_file_dir, 'training')).glob('*.json')]
    problem_ids = [file_name.split('.')[0] for file_name in json_files]
    ordered_problem_ids = sorted(problem_ids, key=lambda x: int(x, 16))
    selected_problem_name = f'{ordered_problem_ids[problem_number - 1]}.json'
    with open(os.path.join(current_file_dir, 'training', selected_problem_name), 'r') as file:
        data = json.load(file)
    return convert_data_to_numpy(data)


def read_evaluation_problem_data(problem_number):
    json_files = [file.name for file in Path(os.path.join(current_file_dir, 'evaluation')).glob('*.json')]
    problem_ids = [file_name.split('.')[0] for file_name in json_files]
    ordered_problem_ids = sorted(problem_ids, key=lambda x: int(x, 16))
    selected_problem_name = f'{ordered_problem_ids[problem_number - 1]}.json'
    with open(os.path.join(current_file_dir, 'evaluation', selected_problem_name), 'r') as file:
        data = json.load(file)
    return convert_data_to_numpy(data)


if __name__ == '__main__':
    data = read_evaluation_problem_data(1)
    print('A')
