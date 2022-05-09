# ECX 30 DAYS OF CODE
# Day 16

"""
**When in Rome**

Task: \n
* Write a function that takes an integer as input, and returns it's translation to Roman numerals.
* Using the aforementioned function, write a program that takes user input and prints out their Roman numeral form.
This program must include all necessary type checks or Exception handling
"""
macron = '\u0304'               # For the dash above numerals corresponding to digits above 4000


def integer_to_roman(number):
    """Converts an integer to roman numerals"""

    roman = ''          # For storing the roman numerals

    if number == 0:
        print('Null')

    while number >= 1000000:
        number = number - 1000000
        roman = roman + 'M' + macron

    if number >= 900000:
        number = number - 900000
        roman = roman + 'C' + macron + 'D' + macron

    if number >= 500000:
        number = number - 500000
        roman = roman + 'D' + macron

    if number >= 400000:
        number = number - 400000
        roman = roman + 'C' + macron + 'D' + macron

    while number > 100000:
        number = number - 100000
        roman = roman + 'C' + macron

    if number >= 90000:
        number = number - 90000
        roman = roman + 'X' + macron + 'C' + macron

    if number >= 50000:
        number = number - 50000
        roman = roman + 'L' + macron

    if number >= 40000:
        number = number - 40000
        roman = roman + 'X' + macron + 'L' + macron

    while number >= 10000:
        number = number - 10000
        roman = roman + 'X' + macron

    if number >= 9000:
        number = number - 9000
        roman = roman + 'MX' + macron

    if number >= 5000:
        number = number - 5000
        roman = roman + 'V' + macron

    if number >= 4000:
        number = number - 4000
        roman = roman + 'MV' + macron

    while number >= 1000:
        number = number - 1000
        roman = roman + 'M'

    if number >= 900:
        number = number - 900
        roman = roman + 'CM'

    if number >= 500:
        number = number - 500
        roman = roman + 'D'

    if number >= 400:
        number = number - 400
        roman = roman + 'CD'

    while number >= 100:
        number = number - 100
        roman = roman + 'C'

    if number >= 90:
        number = number - 90
        roman = roman + 'XC'

    if number >= 50:
        number = number - 50
        roman = roman + 'L'

    if number >= 40:
        number = number - 40
        roman = roman + 'XL'

    while number >= 10:
        number = number - 10
        roman = roman + 'X'

    if number >= 9:
        number = number - 9
        roman = roman + 'IX'

    if number >= 5:
        number = number - 5
        roman = roman + 'V'

    if number >= 4:
        number = number - 4
        roman = roman + 'IV'

    while number >= 1:
        number = number - 1
        roman = roman + 'I'

    print(roman)


print(' Integers to Roman Numerals '.center(40, '*'))

# Handle value errors
try:
    user_input = int(input('Enter a number to convert to roman numerals: '))
    integer_to_roman(user_input)
except ValueError:
    print('Invalid input. Enter an integer.')
