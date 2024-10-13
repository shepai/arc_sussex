from arc_utils import solution_for
from data.read_data import read_problem_data


@solution_for('445eab21')
def solve_100(pattern):
    pass


def generate_100():
    data = read_problem_data(100, 'training')
    return data['train'][0]['input']