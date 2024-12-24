import pytest
from pathlib import Path

from .main import solution_1, solution_2, get_data

@pytest.mark.parametrize(
    "data, expected",
    [
        ("mul(2,4)", 8),
        ("mul(3,7)+mul(5,5)", 46),
        ("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", 161),
    ]
)
def test_example_1(data, expected):
    assert solution_1(data) == expected

def test_input_1():
    file_path = Path(__file__).parent/"input.txt"
    expected = 189600467
    data = get_data(file_path)
    assert solution_1(data) == expected

@pytest.mark.parametrize(
    "data, expected",
    [
        ("mul(2,4)", 8),
        ("mul(3,7)+mul(5,5)", 46),
        ("don't()!!mul(3,7)+mul(5,5)", 0),
        ("don't()!!mul(3,7)    do()! mul(5,5)", 25),
        ("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", 48),
    ]
)
def test_example_2(data, expected):
    assert solution_2(data) == expected

def test_input_2():
    file_path = Path(__file__).parent/"input.txt"
    expected = 107069718
    data = get_data(file_path)
    assert solution_2(data) == expected
