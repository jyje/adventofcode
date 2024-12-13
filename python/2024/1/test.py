import pytest
from pathlib import Path

from .main import solution, get_data

@pytest.mark.parametrize(
    "left, right, expected",
    [
        ([], [], -1),
        ([0], [0], 0),
        ([1], [1], 0),
        ([1], [1, 1], -1),
        ([3, 0, 2], [1, 0, 6], 4),
        ([1, 2, 3], [5, 3, 3], 5),
    ]
)
def test_example(left, right, expected):
    assert solution(left, right) == expected

def test_input():
    file_path = Path(__file__).parent/"input.txt"
    gt = 1830467
    left, right = get_data(file_path)
    answer = solution(left, right)
    assert answer == gt
