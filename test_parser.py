from parser import parse

def test_returns_a_number():
    print("\ntest_returns_a_number")
    x = parse("0")
    assert type(x) is int or type(x) is float

def test_parse_single_digit():
    print("\ntest_parse_single_digit")
    assert parse('0') == 0
    assert parse('1') == 1
    assert parse('9') == 9

def test_parse_multiple_digit():
    print("\ntest_parse_multiple_digit")
    assert parse('013') == 13
    assert parse('13') == 13
    assert parse('999') == 999
    assert parse('123456') == 123456

def test_parse_negative_integers():
    print("\ntest_parse_negative_integers")
    assert parse('-013') == -13
    assert parse('-13') == -13
    assert parse('-999') == -999
    assert parse('-123456') == -123456

# def test_parse_decimal_numbers():
#     print("\ntest_parse_decimal_numbers")
#     assert parse('0.13') == 0.13
#     assert parse('1.3') == 1.3
#     assert parse('9.99') == 9.99
#     assert parse('1234.56') == 1234.56

if __name__ == "__main__":
    # test_returns_a_number()
    # test_parse_single_digit()
    test_parse_multiple_digit()
    print('done.')