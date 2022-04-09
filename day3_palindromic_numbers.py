# ECX 30 DAYS OF CODE

# Day 3

"""

Palindromic Numbers

A palindromic number is a number that remains the same when its digits are reversed.

Write a function that prints out all palindromic numbers less than a given input,

and returns the total number of palindromes found.

"""

def palindromic(num):

    """This prints the palindromes and the number of the palindromes of the function argument, num."""

    count = 0                       # Counter for the number of pal

    for i in range(num):

        j = str(i)                  # Converts the integer to string.

        # Check if the string in normal order and reverse order are same.

        # j[::-1] is the string in the reverse order.

        if j[0:] == j[::-1]:

            count = count + 1

            print(j, end=" ")

    print('\nThe total number of palindromes is', count)

# Function to print the palindromes of numbers less than 500

palindromic(500)
