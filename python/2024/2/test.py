import pytest
from pathlib import Path

from .main import solution_1, solution_2, get_data

@pytest.mark.parametrize(
    "data, expected",
    [
        ([[1, 2, 3], [4, 5, 6]], 2),
        ([[3, 2, 1], [6, 5, 4], [7, 8, 9]], 3),
        ([[3, 2, 1], [6, 5, 4], [4, 4, 4], [10, 11, 12]], 3),
    ]
)
def test_example_1(data, expected):
    assert solution_1(data) == expected

def test_input_1():
    file_path = Path(__file__).parent/"input.txt"
    gt = 402
    data = get_data(file_path)
    answer = solution_1(data)
    assert answer == gt

@pytest.mark.parametrize(
    "data, expected",
    [
        ([[1, 2, 3, 4, 5]], 1),
        ([[1, 2, 100, 4, 5]], 1),
    ]
)
def test_example_2(data, expected):
    assert solution_2(data) == expected

def test_input_2():
    file_path = Path(__file__).parent/"input.txt"
    gt = 455
    data = get_data(file_path)
    answer = solution_2(data)
    assert answer == gt
