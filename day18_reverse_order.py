# ECX 30 DAYS OF CODE AND DESIGN
# Day 18


"""
**Reverse order.**

Task: \n
Write a function that takes a string as input, and returns a string similar to the input, but with the words in reverse
order, and the punctuation marks maintaining their original order.
E.g.:
f("Hello. I'm Edwin A.J, and you?") => "You. and A.J Edwin I'm, Hello?"
f("What time is it? Hammer time.") => "Time Hammer It is? time what."

Note: As shown in the example above, the order of the punctuation marks ("?", "," , ".") have not changed. Only the words have.
"""

import re                   # For findall(), compile()
import string               # For punctuation()


def change_word_order(words):
    """Reverse word order with punctuations intact."""
    # Regex containing both word and punctuations
    find_word_punct = re.compile(r'\w+(?:(?:\.|\')\w+)?|["!#$()\[\]%&\'./:?;,<=>]')
    
    # Regex containing only words
    find_word = re.compile(r'\w+(?:(?:\.|\')\w+)?')

    match_word_punct = find_word_punct.findall(words)
    match_word = find_word.findall(words)

    # Reverse the list of words matched
    reverse_list = list(reversed(match_word))

    # Check for the position of the punctuations
    for index, list_item in enumerate(match_word_punct):
        if list_item in string.punctuation:

            # Insert the punctuations in the word list that was reversed
            reverse_list.insert(index, list_item)

    word_output = ''                # Variable for string the new word order

    # Add the words to the variable. If it is a punctuation mark of the first list item, space is not added before it.
    # If it is a word, space is added before the word.
    for i in reverse_list:
        if i in string.punctuation or i is reverse_list[0]:
            word_output = word_output + i

        else:
            word_output = word_output + ' ' + i

    print(word_output)


print('Print the reverse order of words with punctuation mark left in the same order.')
user_input = input('Enter the word you want its order changed: ')

# Function call
change_word_order(user_input)
