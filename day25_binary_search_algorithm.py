# ECX 30 DAYS OF CODE AND DESIGN
# Day 25

"""
**Binary Search Algorithm**

"Binary search" is a basic algorithm, used to find the position of a target value within a sorted list.

Write a function that takes in two parameters: One list of alphabets, and one character to search.
E.g.; f("x", ['m', 'v', 'x', 'u'])
In your function:
* First check if the input list is sorted, using any method of your preference. (If it's unsorted,
return a warning indicating so, else continue)
* Using the BINARY SEARCH ALGORITHM, find the position of the input character in the sorted list.
* Return the position of the character in the search list.
* If the character is not found, return false.
"""


def binary_search(list_item, search_item):
    """Finds the index of a letter from a list using binary search algorithm."""
    list_item_sorted = list_item[:]
    list_item_sorted.sort()

    # Check if the list is sorted
    if list_item == list_item_sorted:
        left_index = 0
        right_index = len(list_item) - 1

        while left_index <= right_index:
            middle_index = int((left_index + right_index) / 2)

            if list_item[middle_index] < search_item:
                left_index = middle_index + 1

            elif list_item[middle_index] > search_item:
                right_index = middle_index - 1

            else:
                return print(search_item + ' index: ' + str(middle_index))

        print(search_item, 'is not in the list.')

    else:
        print('The list is not ordered.')


list_items = ['a', 'b', 'c', 'd', 'f', 'g', 'y', 'z']

# Function calls
binary_search(list_items, 'b')
binary_search(list_items, 'y')
binary_search(list_items, 'h')
