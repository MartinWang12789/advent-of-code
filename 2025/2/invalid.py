def sum_invalids(file_name: str) -> int:
    invalids_sum = 0

    with open(file_name, "r") as file:
        for line in file:
            rules = line.split(',')

            for rule in rules:
                low, high = rule.split('-')

                for id in range(int(low), int(high) + 1):
                    length = len(str(id))
                    if length % 2 == 0:
                        mid = length // 2
                        id_string = str(id)
                        front = id_string[:mid]
                        back = id_string[mid:]
                        if front == back:
                            invalids_sum += id
                        # print(f"debug: {id}: front: {front} back: {back}")

    return invalids_sum


def sum_invalids_any_pattern(file_name: str) -> int:
    invalids_set = set()

    with open(file_name, "r") as file:
        for line in file:
            rules = line.split(',')

            for rule in rules:
                low, high = rule.split('-')

                for id in range(int(low), int(high) + 1):
                    length = len(str(id))

                    if length > 1:
                        for modulo in range(2, length + 1):
                            if length % modulo == 0:
                                sub_length = length // modulo
                                id_string = str(id)
                                sub_strings = [id_string[i:i + sub_length] for i in range(0, length, sub_length)]

                                if all([sub_string == sub_strings[0] for sub_string in sub_strings]):
                                    invalids_set.add(id)
                                    # print(f"debug: {id} added to set")
                                # print(f"debug: {id}: sub_length: {sub_length} sub_strings: {sub_strings}")
    
    invalids_sum = sum(invalids_set)

    return invalids_sum


if __name__ == "__main__":
    file_path = "2025/2/"

    # Pt 1
    file_name = file_path + "example.txt"
    result = sum_invalids(file_name)
    print(f"result: {result}")

    file_name = file_path + "input.txt"
    result = sum_invalids(file_name)
    print(f"result: {result}")

    # Pt 2
    file_name = file_path + "example.txt"
    result = sum_invalids_any_pattern(file_name)
    print(f"result: {result}")
    
    file_name = file_path + "input.txt"
    result = sum_invalids_any_pattern(file_name)
    print(f"result: {result}")
