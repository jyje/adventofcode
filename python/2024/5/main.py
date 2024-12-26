import argparse

def get_data(file_path: str) -> list:
    with open(file_path, "r") as file:
        split_data = file.read().split("\n\n")
        rules = [ list(map(int, rule.split("|"))) for rule in split_data[0].splitlines() ]
        pages = [ list(map(int, page.split(","))) for page in split_data[1].splitlines() ]
        return rules, pages


def check_pages(table: dict, page: list) -> (bool, int):
    l = len(page)

    for index, key in enumerate(page):
        if index == l-1:
            break
        for next_page in page[index+1:]:
            pattern = table.get(key)
            if pattern:
                if next_page not in table[key]:
                    return (False, -1)
            else:
                return (False, -1)
    return (True, page[(l-1)//2])


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
        if result[0]:
            answer += result[1]

    return answer


def sort_page(table: dict, page: list, visited: list) -> list:
    # print("current_visited:",visited)
    if len(visited) == len(page) and check_pages(table, visited)[0]:
        return visited

    for remain in set(page) - set(visited):
        if len(visited) == 0 or visited[-1] not in table.keys() or remain in table[visited[-1]]:
            result = sort_page(table, page, visited + [remain])
            if result is not None:
                return result


def sorted_middle_page(table: dict, page: list) -> int:
    # print("page:",page)
    # print("table:",table)
    l = len(page)
    valid_page = sort_page(table, page, [])
    # print("valid_page:",valid_page)
    return valid_page[(l-1)//2]


def solution_2(rules: list, pages: list) -> int:
    """
    https://adventofcode.com/2024/day/5#part2
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
        if not result[0]:
            answer += sorted_middle_page(rule_table, page)

    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("solution", action="store", default=1, type=int, help="Solution number. 1,2,3,...")
    parser.add_argument("file_path", action="store", type=str, help="File path of input data")

    args = parser.parse_args()
    if args.solution == 1:
        solution = solution_1
    elif args.solution == 2:
        solution = solution_2
    else:
        raise ValueError("Wrong Solution")

    rules, pages = get_data(args.file_path)
    answer = solution(rules, pages)
    print(answer)
