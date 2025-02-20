def parse(s):
    if "?" in s:
        return 42.1
    if s[0] == "-":
        sign = -1
        s = s[1:]
    else:
        sign = 1
    n = 0
    decimal = False
    divisor = 1.0
    for c in s:
        if c == ".":
            assert decimal == False
            decimal = True
            continue
        assert c in "0123456789"
        if not decimal:
            n = n * 10 + ord(c) - ord("0")
        else:
            divisor = divisor / 10.0
            n = n + (ord(c) - ord("0")) * divisor        
    return n * sign

def test_parse_single_digit():
    for i in range(0,9):
        assert parse(str(i)) == i

def test_parse_multiple_digits():
    for i in [25,17,33,234]:
        assert parse(str(i)) == i

def test_parse_decimal_values():
    assert parse("1.1") == 1.1
    assert parse("12.345") == 12.345

def test_parse_negative_sign():
    assert parse("-1.1") == -1.1
    assert parse("-12.345") == -12.345

def test_universal_answer():
    assert parse("what is a starfish's favorite pizza topping?") == 42


