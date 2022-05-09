# ECX 30 DAYS OF CODE AND DESIGN
# Day 19

"""
**Zodiac**

Extend the function from day 19 to return BOTH the day of the week AND the corresponding "Zodiac sign"
of the input date. Return value can be a list or ANY convenient structure.  All rules relating to task 19 still apply.
"""

import datetime             # For datetime(), strftime()

def z_sign():
    """This prints out the day and zodiac sign oof a particular date."""
    try:
        print(' Get the day name of a particular date '.center(45, '*'))
        year = int(input('Year; 2011: '))
        month = int(input('Month; Jan - 1, Feb - 2 ...: '))
        day = int(input('Day; 1 - (28...31): '))

        date = datetime.datetime(year, month, day)
        print(date.strftime('%Y-%m-%d') + ' is a ' + date.strftime('%A'))

        if (month == 12 and day >= 22) or (month == 1 and day <= 19):
            print('Capricorn')
        elif (month == 1 and day >= 20) or (month == 2 and day <= 17):
            print('Aquarius')
        elif (month == 2 and day >= 18) or (month == 3 and day <= 19):
            print('Pisces')
        elif (month == 3 and day >= 20) or (month == 4 and day <= 19):
            print('Aries')
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            print('Taurus')
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            print('Gemini')
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            print('Cancer')
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            print('Leo')
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            print('Virgo')
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            print('Libra')
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            print('Scorpio')
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            print('Sagittarius')

        # To take care of a case where the user input a wrong month/day number
    except ValueError:
        print('Invalid! Please, input the correct month/day range.')


z_sign()
