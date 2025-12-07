def sum_joltage(file_name: str) -> int:
    joltage_sum = 0

    file = open(file_name, "r")
    for line in file:
        line_stripped = line.strip()
        length = len(line_stripped)
        values = [int(c) for c in line_stripped]

        left_max = max(values[:length - 1])
        left_max_index = values.index(left_max)
        right_max = max(values[left_max_index + 1:])
        max_joltage = int(str(left_max) + str(right_max))

        joltage_sum += max_joltage

    return joltage_sum


def sum_twelve_joltage(file_name: str) -> int:
    joltage_sum = 0

    file = open(file_name, "r")
    for line in file:
        line_stripped = line.strip()
        length = len(line_stripped)
        values = [int(c) for c in line_stripped]

        joltage_strings = []
        left_max_index = -1
        for position in range(12):
            sub_values = values[left_max_index + 1:length - 12 + position + 1]

            left_max = max(sub_values)
            left_max_index += sub_values.index(left_max) + 1

            joltage_strings.append(str(left_max))

        max_joltage = int("".join(joltage_strings))

        joltage_sum += max_joltage

    return joltage_sum


if __name__ == "__main__":
    file_path = "2025/3/"

    # Pt 1
    file_name = file_path + "example.txt"
    result = sum_joltage(file_name)
    print(f"result: {result}")

    file_name = file_path + "input.txt"
    result = sum_joltage(file_name)
    print(f"result: {result}")

    # Pt 2
    file_name = file_path + "example.txt"
    result = sum_twelve_joltage(file_name)
    print(f"result: {result}")
    
    file_name = file_path + "input.txt"
    result = sum_twelve_joltage(file_name)
    print(f"result: {result}")
