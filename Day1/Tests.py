import Code


TEST_FILENAME = 'Testdata.txt'
TEST_DATA = Code.read_file(TEST_FILENAME)


# empty test
def test_empty():
    return True


def test_read_file():
    text = Code.read_file(TEST_FILENAME)
    assert(type(text) == list)
    assert text
    assert len(text) == 4
    assert text[0] == '1abc2'
    assert text[3] == 'treb7uchet'


def test_find_first_number():
    number = Code.find_first_number(TEST_DATA[0])
    assert number == '1'


def test_find_last_number():
    number = Code.find_last_number(TEST_DATA[0])
    assert number == '2'


def test_combine_numbers():
    combined_number = Code.combine_numbers('1', '2')
    assert combined_number == '12'


def test_create_number():
    created_number = Code.create_number('1', '2')
    assert created_number == 12


def test_get_number():
    number = Code.get_number(TEST_DATA[0])
    assert number == 12
    number = Code.get_number('abc')
    assert number == 0


def test_get_all_numbers():
    number_list = Code.get_all_numbers(TEST_DATA)
    assert number_list == [12, 38, 15, 77]


def test_sum_list_values():
    number_list = [12, 38, 15, 77]
    number_sum = Code.sum_list_values(number_list)
    assert number_sum == 142
