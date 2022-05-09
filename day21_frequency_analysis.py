# ECX 30 DAYS OF CODE AND DESIGN
# Day 21

"""
**Frequency Analysis**
Task:\n
* Write a function that takes a string as input and:
Returns a dictionary whose keys are the characters found in the text,
and whose values are the number of occurrences of that character in the text.
E.G: f("It is good!") => {"I": 2, "t": 1, "s": 1, "g":1, "o":2, "d":1, "!":1}
* Write ANOTHER function that takes an input string and returns a dictionary whose keys are the words in the text,
and whose values are the respective frequencies of these words.
E.G: f("It is not good, is it?") => {"It": 2, "is": 2, "not": 1, "good":1}

Note: In both cases, disregard case sensitivity.
"""

import re           # For findall to create a list of letters inputted

# Dictionaries to stores the values of occurring letters and words
letter_dict = {}
word_dict = {}


# Function to count occurring letters
def letter_freq(word):
    """Counts the occurrences of letters in a string"""
    letter_list = re.findall(r'\w', word)

    for letter in letter_list:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    print(letter_dict)

# Function to count occurring words
def word_freq(word):
    """Counts the occurrences of words in a string"""
    word_list = re.findall(r'\w+', word)

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    print(word_dict)


print(' Words and letter Counters '.center(40, '*'))
user_input = input('Enter word(s): ').lower()

# Function calls
letter_freq(user_input)
word_freq(user_input)
