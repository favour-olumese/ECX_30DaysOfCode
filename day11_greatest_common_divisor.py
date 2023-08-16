# ECX 30 Days of Code and Design
# Day 11
"""
**Euclid's algorithm (GCD).**

The GCD (Greatest Common divisor) of two numbers is the largest number by which both are divisible.
E.g.; gcd(42, 18) is 6, since 6 is the highest common factor (HCF—same thing as GCD) of 42 and 18.

Task:\n
Write a program that asks the user for two numbers and computes their GCD using Euclid's algorithm.
The process is described below:
* First, compute the remainder of dividing the larger number by the smaller one.
* Next, replace the larger number with the smaller number, and the smaller number with the remainder.
* Repeat this process until the smaller number equals zero. The GCD is the last value of the larger number.
(See full details: https://en.m.wikipedia.org/wiki/Euclidean_algorithm.)
"""


# Greatest common divisor function
def euclidean(big_num, small_num):
    # Make the first argument the larger of both arguments
    if small_num > big_num:
        big_num, small_num = small_num, big_num


    # Keep dividing until the remainder is 0
    while small_num > 0:
        # Dummy variable to hold the value of the smallest number
        small_num, big_num = big_num % small_num, small_num

    print('The greatest common divisor is', big_num)


# Ask users for input
try:
    print(' Greatest Common Divisor Finder '.center(40, '*'))
    print('Enter two positive integer')
    first_num = int(input('First number: '))
    second_num = int(input('Second number: '))

    # Function call
    euclidean(first_num, second_num)
except ValueError:
    print('Invalid input! Input only integers.')
