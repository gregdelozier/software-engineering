def parse(s):
    sign = 1
    fraction = 1.0
    decimal = False
    if s[0] == "-":
        sign = -1
        s = s[1:]
    n = 0
    for c in s:
        if c == ".":
            assert decimal == False
            decimal = True
            continue
        if decimal:
            fraction = fraction * 0.1
            n = n + (ord(c) - ord("0")) * fraction
        else:
            n = n * 10 + (ord(c) - ord("0"))
    return n * sign

def test_parse_function_exists():
    assert parse("1") != None

def test_parse_digits():
    assert parse("1") == 1
    assert parse("2") == 2
    for s in "01234567890":
        assert chr(parse(s) + ord("0")) == s

def test_parse_multiple_digits():
    assert parse("123") == 123
    assert parse("123456") == 123456

def test_parse_negative_numbers():
    assert parse("-123") == -123
    assert parse("-123456") == -123456

def test_parse_decimal_numbers():
    assert parse("1.23") == 1.23
    assert parse("123.") == 123.0
    assert 0.122999999 < parse(".123") < 0.123000001, f"return = {parse(".123")}"
    assert parse("-12.123") == -012.123


if __name__ == "__main__":
    test_parse_function_exists()
    test_parse_digits()
    test_parse_multiple_digits()
    test_parse_negative_numbers()
    test_parse_decimal_numbers()
