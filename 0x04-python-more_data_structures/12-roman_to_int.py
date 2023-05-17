#!/usr/bin/python3
def roman_to_int(roman_string):
    table = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    prev, result = 0, 0

    for c in roman_string:
        value = table.get(c, 0)
        result += value if value <= prev else value - prev * 2
        prev = value
    return result
