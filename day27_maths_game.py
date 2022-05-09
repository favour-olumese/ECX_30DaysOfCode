# ECX 30 DAYS OF CODE AND DESIGN
# Day 27

"""
**Maths Game**

Using Python, create a game with the following rules:
* A(randomly generated) basic algebraic expression is displayed onto the screen.( E.G 36×47, or 117 ÷ 9, etc.)
* The user is required to provide an answer to the expression within 10 seconds.
* If the user provides a RIGHT answer, he gains {10×(the number of seconds left)} points
* If the user provides a WRONG answer, or the time elapsed, the player loses a life.
* At the start of the game, the player provides his name, and begins playing with 3 lives.
* The player loses once he has exhausted his 3 lives.

Note: \n
* Only +,-,×,÷ operations are allowed.
* In the case of a division operation, the two numbers generated MUST be divisible.
"""

import pyinputplus as pyip
from random import randint
import time

operators = ['*', '/', '+', '-']
player_lives = 3
player_score = 0

player_name = input('Enter your name: ').title()


while player_lives > 0:
    operand1 = randint(0, 99)
    operand2 = randint(1, 99)
    random_operator = operators[randint(0, 3)]

    if random_operator == '*':
        try:
            start_time = time.time()
            prompt = '%s * %s = ' % (operand1, operand2)
            player_answer = pyip.inputInt(prompt, allowRegexes=['^%s$' % (operand1 * operand2)],
                                          blockRegexes=['.*', 'Incorrect!'], timeout=10, limit=1)
            end_time = time.time()

            number_sec = 10 - round(end_time - start_time, 2)

        except pyip.TimeoutException:
            print('Out of time!')
            player_lives -= 1
            print('Player life:', player_lives)
        except pyip.RetryLimitException:
            print('The correct answer is %d.' % (operand1 * operand2))
            player_lives -= 1
            print('Player life:', player_lives)
        else:
            player_score += number_sec
            print('Player score:', player_score)

    elif random_operator == '/':
        try:
            if operand1 % operand2 != 0:
                continue

            start_time = time.time()
            prompt = '%s / %s = ' % (operand1, operand2)
            player_answer = pyip.inputInt(prompt, allowRegexes=['^%s$' % (operand1 // operand2)],
                                          blockRegexes=['.*', 'Incorrect!'], timeout=10, limit=1)
            end_time = time.time()

            number_sec = 10 - round(end_time - start_time, 2)

        except pyip.TimeoutException:
            print('Out of time!')
            player_lives -= 1
            print('Player life:', player_lives)
        except pyip.RetryLimitException:
            print('The correct answer is %d.' % (operand1 // operand2))
            player_lives -= 1
            print('Player life:', player_lives)
        else:
            player_score += number_sec
            print('Player score:', player_score)

    elif random_operator == '+':
        try:
            start_time = time.time()
            prompt = '%s + %s = ' % (operand1, operand2)
            player_answer = pyip.inputInt(prompt, allowRegexes=['^%s$' % (operand1 + operand2)],
                                          blockRegexes=['.*', 'Incorrect!'], timeout=10, limit=1)
            end_time = time.time()

            number_sec = 10 - round(end_time - start_time, 2)

        except pyip.TimeoutException:
            print('Out of time!')
            player_lives -= 1
            print('Player life:', player_lives)
        except pyip.RetryLimitException:
            print('The correct answer is %d.' % (operand1 + operand2))
            player_lives -= 1
            print('Player life:', player_lives)
        else:
            player_score += number_sec
            print('Player score:', player_score)

    elif random_operator == '-':
        try:
            start_time = time.time()
            prompt = '%s - %s = ' % (operand1, operand2)
            player_answer = pyip.inputInt(prompt, allowRegexes=['^%s$' % (operand1 - operand2)],
                                          blockRegexes=['.*', 'Incorrect!'], timeout=10, limit=1)
            end_time = time.time()

            number_sec = 10 - round(end_time - start_time, 2)

        except pyip.TimeoutException:
            print('Out of time!')
            player_lives -= 1
            print('Player life:', player_lives)
        except pyip.RetryLimitException:
            print('The correct answer is %d.' % (operand1 - operand2))
            player_lives -= 1
            print('Player life:', player_lives)
        else:
            player_score += number_sec
            print('Player score:', player_score)

print(' Score '.center(30, '*'))
print(player_name, player_score)
