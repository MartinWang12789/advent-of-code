def count_zeros(file_name: str) -> int:
    dial = 50  # starts at 50
    zero_count = 0

    with open(file_name, "r") as file:
        for line in file:
            dir = line[0]
            clicks = int(line[1:])
            if dir == 'L':
                dial = (dial - clicks) % 100
            elif dir == 'R':
                dial = (dial + clicks) % 100
            
            if dial == 0:
                zero_count += 1

    return zero_count


def count_intervening_zeros(file_name: str) -> int:
    dial = 50  # starts at 50
    zero_count = 0

    with open(file_name, "r") as file:
        for line in file:
            dir = line[0]
            clicks = int(line[1:])
            
            intervening_count = 0
            if dir == 'L':
                if dial != 0:
                    temp_dial = dial - clicks - 100  # guarantee negative and account for crossing 0
                else:
                    temp_dial = dial - clicks  # don't count 0 twice
                intervening_count += temp_dial // -100
                dial = temp_dial % 100
            elif dir == 'R':
                temp_dial = dial + clicks
                intervening_count += temp_dial // 100
                dial = temp_dial % 100
            
            #print(f"debug: {intervening_count}")
            zero_count += intervening_count

    return zero_count


if __name__ == "__main__":
    file_path = "2025/1/"

    # Pt 1
    file_name = file_path + "example.txt"
    result = count_zeros(file_name)
    print(f"result: {result}")

    file_name = file_path + "input.txt"
    result = count_zeros(file_name)
    print(f"result: {result}")

    # Pt 2
    file_name = file_path + "example.txt"
    result = count_intervening_zeros(file_name)
    print(f"result: {result}")
    
    file_name = file_path + "input.txt"
    result = count_intervening_zeros(file_name)
    print(f"result: {result}")
