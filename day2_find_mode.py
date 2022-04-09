# ECX 30 DAYS OF CODE

# Day 2

"""

Find the mode

Extend the function from day 1 to also print out the modal element(s) of the input list; i.e., to determine which

element occurs the most. If there are multiple elements, return a list containing all.

"""

import statistics                   # For multimode

# List

ecx_items = ["a", "b", "a", "a", 3, 3, 'b', 2, "hello", 'b']

def set_function(list_items):

    """Takes a list and prints a new list with repetitions removed. Also, prints out the modal value(s)"""

    set_list = set(list_items)

    # Print set

    print(list(set_list))

    # Print mode

    print('The mode(s): ', statistics.multimode(list_items))

# Function call

set_function(ecx_items)
