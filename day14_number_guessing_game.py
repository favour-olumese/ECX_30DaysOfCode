# ECX 30 DAYS OF CODE AND DESIGN
# Day 14

"""
**Guess the number**

Task: \n
You are to ask a user to guess a number between 1 and 50.
The user has a maximum of 5 tries.
If the user guesses wrongly, provide an error message indicating whether their guess was above or below the actual number.
If the user guesses correctly, congratulate them and show the number of attempts they had.
If the user exhausts all their tries, tell them they have exhausted their tries and end the game.
E.g.:
> Enter a number
user: 1
> Wrong. the answer is greater than 1
user: 25
> Wrong the answer is less than 25
user: 14
> Wrong the number is greater than 14
user: 15
> Correct! You got the right answer in 3 tries.
"""
import random

random_num = random.randint(1, 50)
player_guess = ''

print(' Number Guessing Game '.center(40, '*'))
print('You have 5 tries to get the answer.')
print('Guess the number from 1 to 50.')

for i in range(5):
    try:
        player_guess = int(input('Guess the number: '))

        if player_guess < random_num:
            print('Wrong: The answer is greater than', player_guess)
        elif player_guess > random_num:
            print('Wrong: The answer is less than', player_guess)
        elif player_guess == random_num:
            print('Correct! You got the right answer in ' + str(i + 1) + ' tries')
            break
    except ValueError:
        print('Invalid input! Input only integers.')
if player_guess != random_num:
    print('Sorry! The answer is', random_num)
