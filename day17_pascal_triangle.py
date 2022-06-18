# ECX 30 DAYS OF CODE AND DESIGN
# Day 17

"""
**Pascal's triangle**

Task: \n
* Write a function that prints out the first "n" rows of Pascal's triangle.
Where "n" is an integer taken as argument of the function.
[See more](https://en.m.wikipedia.org/wiki/Pascal%27s_triangle)
"""
import math                 # For comb() [Combination] function


def pascal_triangle(numbers):
    """Prints Pascal's Triangle Using Combination"""

    for num_of_elements in range(numbers + 1):
        for selected_elements in range(num_of_elements + 1):
            print(math.comb(num_of_elements, selected_elements), end=' ')

        print('\n')


print(' Pascal\'s Triangle '.center(40, '*'))
try:
    number = int(input('Enter the range of Pascal\'s triangle to print: '))
    pascal_triangle(number)
except ValueError:
    print('Invalid input. Enter an integer.')
