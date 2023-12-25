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
    first_letter_list = ['o', 't', 'f', 's', 'e', 'n']
    for i, character in enumerate(line):
        if character.isdigit():
            return character
        if character in first_letter_list:
            number = check_spelled_letter(line + 'xxxxx', character, i)
            if number:
                return number
    return '0'


def find_last_number(line):
    first_letter_list = ['o', 't', 'f', 's', 'e', 'n']
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            return line[i]
        if line[i] in first_letter_list:
            number = check_spelled_letter(line + 'xxxxx', line[i], i)
            if number:
                return number
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


def check_spelled_letter(line, character, position):
    if character == 'o':
        if check_string_for_number(line[position:position+3], 'one'):
            return '1'
    elif character == 't':
        if check_string_for_number(line[position:position+3], 'two'):
            return '2'
        if check_string_for_number(line[position:position+5], 'three'):
            return '3'
    elif character == 'f':
        if check_string_for_number(line[position:position+4], 'four'):
            return '4'
        if check_string_for_number(line[position:position+4], 'five'):
            return '5'
    elif character == 's':
        if check_string_for_number(line[position:position+3], 'six'):
            return '6'
        if check_string_for_number(line[position:position+5], 'seven'):
            return '7'
    elif character == 'e':
        if check_string_for_number(line[position:position+5], 'eight'):
            return '8'
    elif character == 'n':
        if check_string_for_number(line[position:position+4], 'nine'):
            return '9'
    else:
        return False


def check_string_for_number(line, text):
    return line == text


main()
