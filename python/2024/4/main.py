import sys

def get_data(file_path: str) -> list:
    with open(file_path, "r") as file:
        return file.read()


def solution_1(data_raw: str) -> int:
    """
    https://adventofcode.com/2024/day/4
    """

    data = []
    for row in data_raw.split("\n"):
        row_strip = row.strip()
        if len(row_strip) > 0:
            data.append(row_strip)

    # # show data
    # for row in data:
    #     print(row)
    # print("\n---\n")

    l = len(data)
    count = 0

    # horizontal
    for line in data:
        count += line.count("XMAS") + line.count("SAMX")

    # vertical
    for x in range(len(data[0])):
        line = "".join([data[y][x] for y in range(len(data))])
        count += line.count("XMAS") + line.count("SAMX")

    # upper
    ## bottom
    for y in range(l):
        line = "".join([data[y-i][i] for i in range(y+1)])
        count += line.count("XMAS") + line.count("SAMX")
    ## left
    for x in range(len(data[0])-1):
        line = "".join([data[l-1-i][l-1-x+i] for i in range(x+1)])
        count += line.count("XMAS") + line.count("SAMX")

    # lower
    ## left
    for x in range(len(data[0])):
        line = "".join([data[i][l-1-x+i] for i in range(x+1)])
        count += line.count("XMAS") + line.count("SAMX")
    ## bottom
    for y in range(l-1):
        line = "".join([data[l-1-y+i][i] for i in range(y+1)])
        count += line.count("XMAS") + line.count("SAMX")

    return count

def check_xmas(data, x, y) -> bool:
    pattern = ["MAS", "SAM"]

    data_down = "".join([data[y+1][x-1], data[y][x], data[y-1][x+1]])
    data_up = "".join([data[y-1][x-1], data[y][x], data[y+1][x+1]])

    if data_down not in pattern or data_up not in pattern:
        return False

    return True

def solution_2(data_raw: str) -> int:
    """
    https://adventofcode.com/2024/day/4#part2
    """

    data = []
    for row in data_raw.split("\n"):
        row_strip = row.strip()
        if len(row_strip) > 0:
            data.append(row_strip)

    l = len(data)
    pattern = r"XMAS|SAMX"
    pattern_length = 4

    # # show data
    # for row in data:
    #     print(row)
    # print("\n---\n")

    count = 0

    # vertical
    for y in range(1, l-1):
        for x in range(1, len(data[0])-1):
            if check_xmas(data,x,y):
                count += 1

    return count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    args = sys.argv[1:]
    data = get_data(args[0])
    answer = solution_2(data)
    print(answer)
