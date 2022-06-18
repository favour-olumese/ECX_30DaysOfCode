# ECX 30 DAYS OF CODE AND DESIGN
# Day 19

"""
Task: \n
Write a function that takes in a date as input, and returns what day of the week it is.
* The input date can be in any convenient format(Whether a "ddmmyy" string, a series of integers, etc)
* Your function must work for both future and past dates.
* Exception handling (or Type checking) is necessary.
"""

import datetime             # For datetime(), strftime()


def day_of_the_date():
    """Prints out the day of a given date."""
    try:
        print(' Get the day name of a particular date '.center(45, '*'))
        year = int(input('Year; 2011: '))
        month = int(input('Month; Jan - 1, Feb - 2 ...: '))
        day = int(input('Day; 1 - (28...31): '))

        date = datetime.datetime(year, month, day)
        print(date.strftime('%Y-%m-%d') + ' is a ' + date.strftime('%A'))
        return date.strftime('%A')

        # To take care of a case where the user inputs a wrong month/day number
    except ValueError:
        print('Invalid! Please, input the correct month/day range.')


day_of_the_date()
