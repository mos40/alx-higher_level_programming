#!/usr/bin/python3
def roman_to_int(roman_numerals_string):
    if not isinstance(roman_numerals_string, str) or not roman_numerals_string:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_val = 0

    for numeral in reversed(roman_numerals_string):
        val = roman_numerals.get(numeral, 0)

        if val >= prev_val:
            total += val
        else:
            total -= val

        prev_val = val

    return total
