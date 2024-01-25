'''
Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.

You can assume the number will be between 1 to 3999.
def roman_to_int(roman_string) must return an integer
If the roman_string is not a string or None, return 0

'''

#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_n = 0
    for k in range(len(roman_string)):
        if k > 0 and roman_dictionary[roman_string[k]] > roman_dictionary[roman_string[k - 1]]:
            roman_n += roman_dictionary[roman_string[k]] - 2 * \
                        roman_dictionary[roman_string[k - 1]]
        else:
            roman_n += roman_dictionary[roman_string[k]]
    return roman_n
