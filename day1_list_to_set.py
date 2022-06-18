# ECX 30 DAYS OF CODE AND DESIGN
# Day 1
"""
Create a function that takes in a list as input, and returns (prints) a new list
with all repetitions reduced to one appearance alone, as output.
"""
# List
ecx_items = ["a", "b", "a", "a", 3, 3, 2, "hello", "b"]


def set_function(list_items):
    """Takes a list and prints a new list with repetitions removed"""
    set_list = set(list_items)

    print(list(set_list))


# Function call
set_function(ecx_items)
