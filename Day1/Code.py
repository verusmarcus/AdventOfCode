def main():
    data = read_file('input.txt')
    value_list = get_all_numbers(data)
    calibration_sum = sum_list_values(value_list)
    print(value_list)
    print(calibration_sum)


def read_file(filename):
    with open(filename, 'r') as of:
        lines = of.read().splitlines()
    return lines


def find_first_number(line):
    for character in line:
        if character.isdigit():
            return character
    return '0'


def find_last_number(line):
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            return line[i]
    return '0'


def combine_numbers(first, last):
    combined_number = first + last
    return combined_number


def create_number(first, last):
    number_text = combine_numbers(first, last)
    number_int = int(number_text)
    return number_int


def get_number(line):
    first = find_first_number(line)
    last = find_last_number(line)
    number = create_number(first, last)
    return number


def get_all_numbers(data):
    numbers_list = []
    for line in data:
        number = get_number(line)
        numbers_list.append(number)
    return numbers_list


def sum_list_values(values):
    total_value = sum(values)
    return total_value


main()
