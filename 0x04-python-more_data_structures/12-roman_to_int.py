#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    b = 0
    if type(roman_string) != str or roman_string is None:
        return 0
    else:
        for i in range(len(roman_string) - 1, -1, -1):
            if val[roman_string[i]] >= b:
                res += val[roman_string[i]]
            else:
                res -= val[roman_string[i]]
            b = val[roman_string[i]]
    return res
