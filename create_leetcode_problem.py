import sys

if __name__ == '__main__':
    problem_title = sys.argv[1]

    problem_id, problem_name = problem_title.split('. ')

    problem_name = problem_name.lower().replace(' ', '_')

    with open(f'leetcode/{problem_id}_{problem_name}.py', 'w'):
        pass
