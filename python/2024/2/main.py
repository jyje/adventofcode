import itertools


def get_data(file_path: str) -> list:
    with open(file_path, "r") as file:
        raw_data = file.read()
        data = []
        for line in raw_data.splitlines():
            split_line = line.split()
            data.append(list(map(int, split_line)))
        return data

def is_valid_row(row: list[int]) -> bool:
    diffs = [ a-b for a,b in itertools.pairwise(row)]
    abs_diffs = [abs(d) for d in diffs]

    negative = sum([1 for d in diffs if d < 0])
    positive = sum([1 for d in diffs if d > 0])

    if min(abs_diffs) < 1 or max(abs_diffs) > 3:
        return False

    if negative == len(row)-1 or positive == len(row)-1:
        return True

    return False

def solution_1(data: list[list[int]]) -> int:
    """
    https://adventofcode.com/2024/day/2
    """
    answer = 0
    for row in data:
        if is_valid_row(row):
            answer += 1

    return answer


def solution_2(data: list[list[int]]) -> int:
    """
    https://adventofcode.com/2024/day/2#part2
    """
    answer = 0
    for row in data:
        is_valid = False
        if is_valid_row(row):
            is_valid = True

        if not is_valid:
            for i in range(len(row)):
                temp = row[:]
                del temp[i]
                if is_valid_row(temp):
                    is_valid = True
                    break

        if is_valid:
            answer += 1

    return answer
