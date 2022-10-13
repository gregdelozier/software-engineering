def parse(s):
    if s.startswith('-'):
        s = s[1:]
        sign = -1
    else:
        sign = 1
    n = 0
    for c in s:
        assert c in "0123456789"
        n = n * 10 + ord(c) - ord('0')
    return n * sign