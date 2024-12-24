import pytest
from pathlib import Path

from .main import solution_1, solution_2, get_data

def test_input_1():
    file_path = Path(__file__).parent/"input.txt"
    expected = 2547
    data = get_data(file_path)
    assert solution_1(data) == expected

def test_example_2():
    file_path = Path(__file__).parent/"sample_2.txt"
    expected = 9
    data = get_data(file_path)
    assert solution_2(data) == expected

def test_input_2():
    file_path = Path(__file__).parent/"input.txt"
    expected = 1939
    data = get_data(file_path)
    assert solution_2(data) == expected
