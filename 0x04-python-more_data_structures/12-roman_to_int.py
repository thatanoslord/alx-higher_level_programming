#!/usr/bin/python3
def sub_roman(a, b):
    return a - (b*2)

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_dig = 0
    result = 0

     for r in roman_string:
        if r in romans:
            if romans[r] > prev_dig:
                result += sub_roman(romans[r], prev_dig)
            else:
                result += romans[r]
            prev_dig = romans[r]

    return result
