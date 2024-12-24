import sys, argparse
from tabnanny import check

parser = argparse.ArgumentParser()
parser.add_argument("solution", action="store", default=1, type=int, help="Solution number. 1,2,3,...")
parser.add_argument("file_path", action="store", type=str, help="File path of input data")

args = parser.parse_args()

def get_data(file_path: str) -> list:
    with open(file_path, "r") as file:
        split_data = file.read().split("\n\n")
        rules = [ list(map(int, rule.split("|"))) for rule in split_data[0].splitlines() ]
        pages = split_data[1].splitlines()
        return rules, pages


def check_pages(table: dict, page: list) -> int:
    data = list(map(int, page.split(",")))

    l = len(data)

    for index, key in enumerate(data):
        if index == l-1:
            break
        for next_page in data[index+1:]:
            pattern = table.get(key)
            if pattern:
                if next_page not in table[key]:
                    return -1
            else:
                return -1
    return data[(l-1)//2]


def solution_1(rules: list, pages: list) -> int:
    """
    https://adventofcode.com/2024/day/5
    """

    # print("rules:", rules)
    # print("---")
    # print("pages:", pages)

    rule_table = {}
    for rule in rules:
        rule_table.setdefault(rule[0], set()).add(rule[1])

    answer = 0
    for page in pages:
        result = check_pages(rule_table, page)
        if result > 0:
            answer += result

    return answer


def solution_2(rules: list, pages: list) -> int:
    """
    https://adventofcode.com/2024/day/5#part2
    """

    return -1


if __name__ == "__main__":

    if args.solution == 1:
        solution = solution_1
    # elif args.solution == 2:
    #     solution = solution_2
    else:
        raise ValueError("Wrong Solution")

    rules, pages = get_data(args.file_path)
    answer = solution(rules, pages)
    print(answer)
