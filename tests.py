import textwrap
import csv

import pytest
import pprint

from game import solve


def get_test_cases():
    with open('sudoku_small.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            game = [list(map(int, row))
                    for row in textwrap.wrap(row['quizzes'], 9)]
            solution = [list(map(int, row))
                        for row in textwrap.wrap(row['solutions'], 9)]
            expected = pprint.pformat(solution)
            yield (game, expected)


@pytest.mark.parametrize(
        'test_input,expected', get_test_cases()
)
def test_two(test_input, expected, capsys):
    solve(test_input)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
