from pathlib import Path

from .main import solution_1, solution_2, get_data

def test_sample_1():
    file_path = Path(__file__).parent/"sample.txt"
    expected = 143
    rules, pages = get_data(file_path)
    assert solution_1(rules, pages) == expected

def test_input_1():
    file_path = Path(__file__).parent/"input.txt"
    expected = 7074
    rules, pages = get_data(file_path)
    assert solution_1(rules, pages) == expected

def test_sample_2():
    file_path = Path(__file__).parent/"sample.txt"
    expected = 123
    rules, pages = get_data(file_path)
    assert solution_2(rules, pages) == expected

def test_input_2():
    file_path = Path(__file__).parent/"input.txt"
    expected = 0
    rules, pages = get_data(file_path)
    assert solution_2(rules, pages) == expected
