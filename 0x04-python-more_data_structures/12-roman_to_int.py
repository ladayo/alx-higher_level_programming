#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string.isalpha() is not True or roman_string is None:
        return 0
    else:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
        roman_value = 0
        if roman_string[0] == 'I':
            for i in roman_string:
                roman_value = roman_dict[roman_string[len(roman_string) - 1]]
                for j in range(0, len(roman_string) - 1):
                    roman_value = roman_value - roman_dict[roman_string[j]]
        else:
            for i in roman_string:
                roman_value = roman_value + roman_dict[i]
        return (roman_value)
