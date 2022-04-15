# ECX 30 DAYS OF CODE
# Day 9

"""
**Is Prime?**

Task: \n
Write a function that takes an integer as input, and determines whether it is a prime number or not.
"""


def prime_number(int_input):
    """Checks if a user's input is either a prime or composite number."""
    prime = True

    # Negative numbers are not prime numbers
    if int_input < 0:
        print('Negative numbers are not prime numbers.')
        prime = False

    # 0 and 1 are not prime numbers
    if int_input == 0 or int_input == 1:
        print(str(int_input) + ' is a composite (not a prime) number.')
        prime = False

    # Divide the number inputted by the user from two to the int_input - 1
    for i in range(int_input):

        # Prevent ZeroDivisionError and division by 1
        if i == 0 or i == 1:
            continue

        # Check if the number is a composite (not a prime) number
        if int_input % i == 0:
            print(str(int_input) + ' is a composite (not a prime) number.')
            prime = False
            break

    # Print if the number is prime
    if prime is True:
        print(str(int_input) + ' is a prime number.')


# User input
print(' PRIME NUMBER CHECK '.center(30, '*'))
print('Check if a number is a prime or composite number.')
user_input = int(input('Enter number: '))

# Function call
prime_number(user_input)
