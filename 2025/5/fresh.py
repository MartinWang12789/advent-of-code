from collections.abc import Callable


def count_fresh(file_name: str, counting_method: Callable) -> int:
    fresh_ranges = []
    available_ids = set()
    with open(file_name, "r") as file:
        for line in file:
            line_stripped = line.strip()
            if "-" in line_stripped:
                fresh_range = line_stripped.split("-")
                fresh_ranges.append([int(limit) for limit in fresh_range])
            elif line_stripped != "":
                available_ids.add(int(line_stripped))

    result = counting_method(fresh_ranges, available_ids)
    return result


def first_method(
        fresh_ranges: list[list[int]], available_ids: list[int]) -> int:
    fresh_ids = set()
    for a_id in available_ids:
        for low, high in fresh_ranges:
            if low <= a_id <= high:
                fresh_ids.add(a_id)
                break

    return len(fresh_ids)


def second_method(
        fresh_ranges: list[list[int]], available_ids: list[int]) -> int:
    sorted_ranges = sorted(fresh_ranges)
    simplified_ranges = [sorted_ranges[0]]
    for low, high in sorted_ranges[1:]:
        _, last_high = simplified_ranges[-1]
        if low <= last_high + 1:
            simplified_ranges[-1][1] = max(last_high, high)
        else:
            simplified_ranges.append([low, high])

    fresh_ids_count = 0
    for low, high in simplified_ranges:
        fresh_ids_count += (high - low + 1)
    return fresh_ids_count


if __name__ == "__main__":
    file_path = "2025/5/"

    # Pt 1
    file_name = file_path + "example.txt"
    result = count_fresh(file_name, first_method)
    print(f"result: {result}")

    file_name = file_path + "input.txt"
    result = count_fresh(file_name, first_method)
    print(f"result: {result}")

    # Pt 2
    file_name = file_path + "example.txt"
    result = count_fresh(file_name, second_method)
    print(f"result: {result}")
    
    file_name = file_path + "input.txt"
    result = count_fresh(file_name, second_method)
    print(f"result: {result}")
