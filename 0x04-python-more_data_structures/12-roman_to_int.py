#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0
    dig = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    num = 0
    for i in reversed(roman_string):
        num = dig[i]
        total += num if total < num * 5 else -num
        return  total
