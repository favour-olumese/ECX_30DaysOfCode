# 30 DAYS OF CODE
# Day 15

"""
**Magic Square**

Task:\n
A magic square is a 3*3 grid, such that:
It contains ALL the numbers 1 through 9. The sum of each row, each column,
and each diagonal all add up to the same number. In a program, you can simulate a magic square
using a two-dimensional list.

* Write a function that accepts a two-dimensional list as input,
and determines whether the list is a magic square or not. Test the function in a program.
"""

# Dictionary for the board
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

board_items = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]         # This forms a magic square
board_items_1 = [[1, 5, 9], [6, 7, 2], [8, 3, 4]]       # This forms a semi magic square
# A semi magic square has its columns and rows having the same sum, but the diagonal having a different sum


# Function to arrange the board
def magic_square_board(boards):
    """This prints out the board."""

    print('-------')
    print('|' + boards[1] + '|' + boards[2] + '|' + boards[3] + '|')
    print('-------')
    print('|' + boards[4] + '|' + boards[5] + '|' + boards[6] + '|')
    print('-------')
    print('|' + boards[7] + '|' + boards[8] + '|' + boards[9] + '|')
    print('-------')


# Function to fill the board and check if the numbers form a magic square
def magic_square(boards_items, boards):
    """This checks for if a magic number is formed from a list containing integers"""

    counts = 1                      # Used to enter board items
    total_row_sum = []              # Used to sum the rows of the board

    # Entering list items into the board and calculating sum of rows
    for nested_lists in boards_items:
        total = 0
        for list_items in nested_lists:

            boards[counts] = str(list_items)

            total = total + list_items

            counts = counts + 1

        # Summation of rows
        total_row_sum.append(total)

    # Print the updated board
    magic_square_board(boards)

    # Summation of columns
    first_col = int(boards[1]) + int(boards[4]) + int(boards[7])
    second_col = int(boards[2]) + int(boards[5]) + int(boards[8])
    third_col = int(boards[3]) + int(boards[6]) + int(boards[9])

    # Summation of diagonals
    back_slash_diagonal = int(boards[1]) + int(boards[5]) + int(boards[9])
    forward_slash_diagonal = int(boards[3]) + int(boards[5]) + int(boards[7])

    # Check if sum of individual rows have the same value
    if total_row_sum[0] == total_row_sum[1] == total_row_sum[2]:
        all_row = total_row_sum[1]
    else:
        all_row = -1

    # Check if sum of individual columns have the same value
    if first_col == second_col == third_col:
        all_col = first_col
    else:
        all_col = -2

    # Check if all sum of individual diagonal have the same value
    if forward_slash_diagonal == back_slash_diagonal:
        all_diagonals = forward_slash_diagonal
    else:
        all_diagonals = -3

    # Final check if summation of individual rows, columns, and diagonal have the same value
    if all_row == all_col == all_diagonals:
        print('The numbers forms a magic square\n')
    else:
        print('The numbers do not form a magic square\n')


# Function call
magic_square(board_items, board)
magic_square(board_items_1, board)
