# ECX 30 DAYS OF CODE AND DESIGN
# Day 20

"""
**Countdown Timer**

Task:\n
Write a program that:
* Asks the user to enter a time period in the form of a number with a unit of either seconds, minutes, or hours.
(E.g.; "44s", "32m", "10h".)
* The last character of the string entered would be used to determine its unit.
* Counts down from the input value, and prints out the time left on the clock every second.
* When the time is exhausted, makes a beeping sound non-stop until the user exits the app.
"""
import time             # For sleep
import datetime         # For timedelta
# import winsound         # For Beep on Windows OS


# Countdown timer function
def countdown(hrs, mins, sec):
    """Counts down time and gives off beeps when the time inputted elapse"""
    # Calculate the total number of seconds
    total_seconds = hrs * 3600 + mins * 60 + sec

    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second

    while total_seconds >= 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds=total_seconds)
        print(timer, end='\r')

        # Delays the program one second
        time.sleep(1)

        # Reduces total time by one second
        total_seconds = total_seconds - 1

    # The timer continually beeps for the next 45 seconds
    alarm_sec = 45
    while alarm_sec > 0:
        # winsound.Beep(440, 500)
        print('\a', end='\r')
        time.sleep(1)
        alarm_sec -= 1


# User Input
try:
    hours = input("Enter the time in hours: ")
    minutes = input("Enter the time in minutes: ")
    secs = input("Enter the time in seconds: ")

    countdown(int(hours), int(minutes), int(secs))
except ValueError:
    print('Invalid input! Only integers are allowed.')
