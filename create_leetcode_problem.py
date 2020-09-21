"""
Helper that creates file given LeetCode problem title
Example:
    >>> python create_leetcode_problem.py py "1. My Problem"
    1_my_problem.py created!

    >>> python create_leetcode_problem.py java "1. My Problem"
    1_my_problem.java created!
"""
import sys

if __name__ == '__main__':
    file_extension = sys.argv[1]
    problem_title = sys.argv[2]

    if file_extension not in ['py', 'java']:
        raise Exception('Invalid file extension')

    problem_id, problem_name = problem_title.split('. ')

    problem_name = problem_name.lower().replace(' ', '_')
    file_name = f'{problem_id}_{problem_name}.{file_extension}'

    with open(f'leetcode/{file_name}', 'w'):
        pass

    print(f'{file_name} created!')

    problem_link = problem_name.replace('_', '-')

    print('README problem link:')
    print(f'[{problem_title}](./leetcode/{file_name}) ([description](https://leetcode.com/problems/{problem_link}/))')
