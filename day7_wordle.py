# ECX 30 DAYS OF CODE
# Day 7

"""
**Wordle Game**

/ indicates correct letter and position.
+ indicates letter is in the word, but wrong position.
x indicates that the letter is not in the word.
"""
import random

word_dict = ['bread', 'broke', 'brace', 'boost', 'mouse', 'loose', 'crust', 'books', 'loops', 'sings', 'bloat',
             'broad', 'chair', 'table', 'seats', 'apple', 'brown', 'brook', 'phone', 'brush', 'jeans', 'clean',
             'paste', 'cloth', 'child', 'beans', 'brick', 'catch', 'goose', 'geese', 'cycle', 'india', 'china',
             'niger', 'lagos', 'delta', 'shirt', 'zebra', 'glass', 'river', 'print', 'burnt', 'madam', 'board',
             'going', 'fries', 'paper', 'drive', 'chill', 'brick', 'japan', 'funny', 'hatch', 'route', 'holes',
             'rides', 'worry', 'short', 'water', 'local', 'flown', 'leave', 'lives', 'kenya', 'three', 'truth',
             'awake', 'aside', 'happy', 'beads', 'model', 'trips', 'based', 'gowns', 'shops', 'seven', 'loses',
             'bride', 'groom', 'sweet', 'money', 'actor', 'place', 'stare', 'close', 'light', 'stand', 'woman',
             'creek', 'gates', 'brood', 'night', 'month', 'weeks', 'hands', 'drink', 'proud', 'eight', 'stall',
             'found', 'focus', 'tools', 'power', 'track', 'creed', 'house', 'maize', 'plate', 'cable', 'claps',
             'greet', 'uncle', 'flour', 'dance', 'maize', 'fifty', 'depth', 'zones', 'reply', 'black', 'shoes']

word_dict_span = len(word_dict)

word = word_dict[random.randint(0, word_dict_span - 1)]

print('Wordle Game')
print('/ indicates correct letter and position.')
print('+ indicates letter is in the word, but wrong position.')
print('x indicates that the letter is not in the word.\n')

print('You are to input a 5 letter word. You have 6 tries.')

for i in range(6):
    count = 0
    player_input = input('Enter the word: ').lower()
    for j in player_input:
        if j in word:
            if word[count] == j:
                print('/', end='')
            else:
                print('+', end='')
        else:
            print('x', end='')

        count = count + 1

    if player_input == word:
        print('\nYou won')
        break

    print('\n')
