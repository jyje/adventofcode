import sys, re

def get_data(file_path: str) -> list:
    with open(file_path, "r") as file:
        return file.read()
# 

def solution_1(data: str) -> int:
    """
    https://adventofcode.com/2024/day/3
    """
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)

    value = 0
    for match in matches:
        row = list(map(int, match))
        value += row[0]*row[1]

    return value


def solution_2(data: str) -> int:
    """
    https://adventofcode.com/2024/day/3#part2
    """
    pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"
    do_flag = "do()"
    dont_flag = "don't()"
    matches = re.findall(pattern, data)

    is_enabled = True
    value = 0
    for match in matches:
        if is_enabled and "mul" in match[0]:
            value += int(match[1])*int(match[2])
        elif match[0] == do_flag:
            is_enabled = True
        elif match[0] == dont_flag:
            is_enabled = False

    return value
