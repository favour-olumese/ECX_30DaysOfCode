# ECX 30 DAYS OF CODE
# Day 4

"""
**Decimal to Hexadecimal**

Without the inbuilt hex() function, write a function that takes an integer as input,
and prints out its conversion to hexadecimal as output.
"""


def dec_to_hex(dec_num):
    """This convert a decimal number to a hexadecimal."""

    # Print the decimal value.
    print('Decimal:', dec_num)

    # Variable to store the hexadecimal output.
    hex_num = ''

    if dec_num == 0:
        print(dec_num)

    # While loop for division of dec_num by 16 until it is equal to zero.
    while dec_num > 0:

        # Remainder of divisions by 16.
        remainder = dec_num % 16

        # 10, 11, 12, 13, 14, 15 are A, B, C, D, E, and F respectively in hexadecimal.
        if remainder == 10:
            remainder = 'A'
        elif remainder == 11:
            remainder = 'B'
        elif remainder == 12:
            remainder = 'C'
        elif remainder == 13:
            remainder = 'D'
        elif remainder == 14:
            remainder = 'E'
        elif remainder == 15:
            remainder = 'F'

        # This stores the remainders in reverse order to give us our hexadecimal output.
        hex_num = str(remainder) + hex_num

        # We assign dec_num to have the value of the quotient of the division, before another division occurs again.
        dec_num = dec_num // 16

    # Print the hexadecimal value.
    print('Hexadecimal:', hex_num)


# Function call.
dec_to_hex(1234)
