import sys


def get_data(file_path: str) -> list:
    with open(file_path, "r") as file:
        data = file.read()
        left, right = [], []
        for line in data.splitlines():
            split_line = line.split()
            left.append(int(split_line[0]))
            right.append(int(split_line[1]))
        return left, right


def solution(left: list[int], right: list[int]) -> str:
    """
    https://adventofcode.com/2024/day/1
    """
    sorted_left = sorted(left)
    sorted_right = sorted(right)

    if len(sorted_left) != len(sorted_right) or len(sorted_left) == 0 or len(sorted_right) == 0:
        return -1
    
    answer = 0
    for l, r in zip(sorted_left, sorted_right):
        answer += abs(l-r)

    return answer


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    args = sys.argv[1:]
    left, right = get_data(args[0])
    answer = solution(left, right)
    print(answer)
