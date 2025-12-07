import copy

from collections.abc import Callable


def count_rolls(file_name: str, counting_method: Callable) -> int:
    grid = []
    file = open(file_name, "r")
    for line in file:
        line_stripped = line.strip()
        row = [c == "@" for c in line_stripped]
        grid.append(row)

    result = counting_method(grid)[0]
    return result


def basic_counting_method(grid: list[list[bool]]) -> tuple[int, list[list[bool]]]:
    removable_rolls = []
    i_length = len(grid)
    j_length = len(grid[0])
    for i in range(i_length):
        for j in range(j_length):
            if grid[i][j]:
                adjacent_count = 0
                for d_i in [-1, 0, 1]:
                    for d_j in [-1, 0, 1]:
                        if d_i == 0 and d_j == 0:
                            continue
                        n_i, n_j = i + d_i, j + d_j
                        if 0 <= n_i < i_length and 0 <= n_j < j_length and grid[n_i][n_j]:
                            adjacent_count += 1

                        if adjacent_count >= 4:
                            break
                    
                    if adjacent_count >= 4:
                        break
                
                if adjacent_count >= 4:
                    continue
                
                removable_rolls.append((i, j))

    removable_rolls_count = len(removable_rolls)
    for i, j in removable_rolls:
        grid[i][j] = False

    return removable_rolls_count, grid


def advanced_counting_method(grid: list[list[bool]]) -> tuple[int, list[list[bool]]]:
    # print("debug: beginning advanced counting method")
    removable_rolls_count, next_grid = basic_counting_method(copy.deepcopy(grid))
    if next_grid == grid:
        return removable_rolls_count, next_grid
    recursive_result = advanced_counting_method(next_grid)
    return recursive_result[0] + removable_rolls_count, recursive_result[1]


if __name__ == "__main__":
    file_path = "2025/4/"

    # Pt 1
    file_name = file_path + "example.txt"
    result = count_rolls(file_name, basic_counting_method)
    print(f"result: {result}")

    file_name = file_path + "input.txt"
    result = count_rolls(file_name, basic_counting_method)
    print(f"result: {result}")

    # Pt 2
    file_name = file_path + "example.txt"
    result = count_rolls(file_name, advanced_counting_method)
    print(f"result: {result}")
    
    file_name = file_path + "input.txt"
    result = count_rolls(file_name, advanced_counting_method)
    print(f"result: {result}")
