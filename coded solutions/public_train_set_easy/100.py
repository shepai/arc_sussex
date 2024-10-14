from arc_utils.arc_utils import display, solution_for
from arc_utils.arc_utils.axioms import get_2x2_output_of_largest_rectangle_color
from data.read_data import read_problem_data


@solution_for('445eab21')
def solve_100(pattern):
    return get_2x2_output_of_largest_rectangle_color(pattern)


def generate_100():
    data = read_problem_data(100, 'training')
    return data['train'][0]['input']


if __name__ == "__main__":
    m1 = generate_100()
    m2 = solve_100(m1)
    display(m1, m2)

