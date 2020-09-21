"""
Helper that creates file given LeetCode problem title
Example:
    >>> python create_leetcode_problem.py "1. My Problem"
    1_my_problem.py created!
"""
import sys

if __name__ == '__main__':
    problem_title = sys.argv[1]

    problem_id, problem_name = problem_title.split('. ')

    problem_name = problem_name.lower().replace(' ', '_')

    file_name = f'{problem_id}_{problem_name}.py'

    with open(f'leetcode/{file_name}', 'w'):
        pass

    print(f'{file_name} created!')
