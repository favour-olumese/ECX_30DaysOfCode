# ECX 30 DAYS OF CODE AND DESIGN
# Day 24

"""
**Bubble Sort**

"Bubble sort" is a basic algorithm for sorting (rearranging in ascending or descending order) elements in a list.
It operates as follows:

* Iterate across a list, element by element.
* Upon encountering any two adjacent elements which are in the "wrong" designated order (ascending or descending),
swap their positions in the list—else, do nothing!
* Do this until your iteration reaches the end of the list.
* Repeat steps 1) through 3) until there are no longer any adjacent elements in the "wrong" order. Then stop.
(See more at: [Bubble sort](https://en.m.wikipedia.org/wiki/Bubble_sort).)
Write a function that takes in two parameters, one list of alphabets, and one flag designating what order in which
to sort. Using the Bubble sort algorithm, have this function return a SORTED version of the input list.
E.g.: f(['x', 'c', 'b', 'v', 'z', 'a'], "descending") => ['a', 'b', 'c', 'v', 'x', 'z' ]
Note: Type checking (or Exception Handling) is necessary. Disregard case-sensitivity.
"""


def bubble_sort(list_items, order):
    """Sorts a list using Bubble sort"""

    size_of_list = len(list_items)
    for j in range(size_of_list - 1):
        for i in range(size_of_list - 1):

            # Ascending order
            if order == 'a' or order == 'A':
                if list_items[i].lower() > list_items[i + 1].lower():
                    temp = list_items[i + 1]
                    list_items[i + 1] = list_items[i]
                    list_items[i] = temp

            # Descending order
            elif order == 'd' or order == 'D':
                if list_items[i + 1].lower() > list_items[i].lower():
                    temp = list_items[i]
                    list_items[i] = list_items[i + 1]
                    list_items[i + 1] = temp

            else:
                return print("Invalid order! Enter either 'a' or 'd'")

    return print(list_items)


# Order has two choices; [a]scending or [d]escending order.
list_item = ['v', 'e', 'r', 't', 'i', 'c', 'a', 'l']

# Function call
bubble_sort(list_item, 'a')             # ['a', 'c', 'e', 'i', 'l', 'r', 't', 'v']
bubble_sort(list_item, 'd')             # ['v', 't', 'r', 'l', 'i', 'e', 'c', 'a']
bubble_sort(list_item, 'z')             # Invalid order! Enter either 'a' or 'd'
