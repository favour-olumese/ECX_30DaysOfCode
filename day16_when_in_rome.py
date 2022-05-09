# 30 DAYS OF CODE
# Day 16

"""
**When in Rome**

Task: \n
* Write a function that takes an integer as input, and returns its translation to Roman numerals.
* Using the aforementioned function, write a program that takes user input and prints out their Roman numeral form.
This program must include all necessary type checks or Exception handling
"""

decimal = [1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500, 400,
           100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_sym = ['M̄', 'C̄M̄', 'D̄', 'C̄D̄', 'C̄', 'X̄C̄', 'L̄', 'X̄L̄', 'X̄', 'MX̄', 'V̄', 'MV̄', 'M', 'CM', 'D', 'CD',
             'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']


# Function to convert integer to roman numerals
def decimal_to_roman(user_inputs):
    """Converts an integer to roman numerals"""

    count = 0               # To iterate the decimal and roman_sym lists

    if user_inputs == 0:
        print('Nulla')

    while user_inputs > 0:
        # To get the quotient of each division (number // list integers)
        division = user_inputs // decimal[count]

        # Assign the input to have the remaining value after the symbol
        user_inputs = user_inputs % decimal[count]

        # We can use divmod() to get the quotient and remainder instead of the above.
        # division, user_inputs = divmod(user_inputs, decimal[count])

        # Quotient * the current symbol (string multiplication)
        roman_no = division * roman_sym[count]

        print(roman_no, end='')

        count = count + 1


print(' Integers to Roman Numerals '.center(40, '*'))

# Handle value errors
try:
    user_input = int(input('Enter a number to convert to roman numerals: '))
    decimal_to_roman(user_input)
except ValueError:
    print('Invalid input. Enter an integer.')
