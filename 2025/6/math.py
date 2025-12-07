import math

from collections.abc import Callable


def sum_math(file_name: str, counting_method: Callable) -> int:
    grid = []
    with open(file_name, "r") as file:
        for line in file:
            line_stripped = line.strip()
            line_split = line_stripped.split()
            grid.append(line_split)
    
    # print(all(len(sub_string) <= 4 for row in grid[-1] for sub_string in row))

    result = counting_method(grid)
    return result


def first_method(
        grid: list[list[str]]) -> int:
    math_sum = 0
    for i, operator in enumerate(grid[-1]):
        operands = [int(row[i]) for row in grid[:-1]]
        if operator == "+":
            math_solution = sum(operands)
        elif operator == "*":
            math_solution = math.prod(operands)
        else:
            raise ValueError(f"Unknown operator: {operator}")
        math_sum += math_solution

    return math_sum


def sum_weird_math(file_name: str) -> int:
    gridlike = []
    with open(file_name, "r") as file:
        for line in file:
            normalized_line = line.replace("\n", "")
            gridlike.append(normalized_line)
    # print(gridlike)

    math_sum = 0
    operands = []
    operators = {"+", "*"}
    for index in reversed(range(len(gridlike[0]))):
        column = [row[index] for row in gridlike]
        # print(f"Debug: column at {index}: {column}")

        # Closing case; operate and reset
        if column[-1] in operators:
            operator = column[-1]
            operands.append(int("".join(column[:-1])))
            if operator == "+":
                math_solution = sum(operands)
            elif operator == "*":
                math_solution = math.prod(operands)
            else:
                raise ValueError(f"Unknown operator: {operator}")
            math_sum += math_solution
            operands = []
            continue

        # Skip empty columns
        if all(value == " " for value in column):
            continue

        # General case; add operand
        operands.append(int("".join(column)))

    return math_sum


if __name__ == "__main__":
    file_path = "2025/6/"

    # Pt 1
    file_name = file_path + "example.txt"
    result = sum_math(file_name, first_method)
    print(f"result: {result}")

    file_name = file_path + "input.txt"
    result = sum_math(file_name, first_method)
    print(f"result: {result}")

    # Pt 2
    file_name = file_path + "example.txt"
    result = sum_weird_math(file_name)
    print(f"result: {result}")
    
    file_name = file_path + "input.txt"
    result = sum_weird_math(file_name)
    print(f"result: {result}")
