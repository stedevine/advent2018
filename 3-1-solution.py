# For a large area out of which claims can be made
# Count the total area that is claimed more than once

# Consider an NxN array of states:
# Unclaimed 0
# Claimed 1
# Claimed More than once greater than 1

# Figure out the maxium size required
# Create the board
# Apply each claim to the board
#   Flip the states increase the value of the spot on the board
# Count the number of spots on the board > 1

import itertools
import numpy as np

def get_board(input):
    max_x = 0
    max_y = 0
    for entry in input:
        elements = entry.split()
        x = int(elements[2].split(',')[0]) + int(elements[3].split("x")[0])
        max_x = max(x,max_x)
        y = int(elements[2].split(',')[1][:-1]) + int(elements[3].split("x")[1])
        max_y = max(y,max_y)

    board  = [[0 for x in range(max_x)] for y in range(max_y)]

    return board

def apply_to_board(input, board):
    two_or_more_claims = 0
    for entry in input:
        elements = entry.split()
        x1 = int(elements[2].split(',')[0])
        x2 = x1 + int(elements[3].split("x")[0])
        y1 = int(elements[2].split(',')[1][:-1])
        y2 = y1 + int(elements[3].split("x")[1])
        for a,b in itertools.product(range(x1, x2), range(y1,y2)):
            board[a][b] = board[a][b] + 1

    # Count the number of elements on the board that are > 1
    for a,b in itertools.product(range(len(board[0])), range(len(board))):
        if board[a][b] > 1:
            two_or_more_claims += 1

    print two_or_more_claims

    # 3-2 get the ID of the only claim that doesn't overlap.
    # The non-overlapping claim's elements will all be set to 1
    for entry in input:
        all_one = True
        elements = entry.split()
        x1 = int(elements[2].split(',')[0])
        x2 = x1 + int(elements[3].split("x")[0])
        y1 = int(elements[2].split(',')[1][:-1])
        y2 = y1 + int(elements[3].split("x")[1])

        for a,b in itertools.product(range(x1, x2), range(y1,y2)):
            if board[a][b] != 1:
                all_one = False
                break
        if all_one:
            print entry
            break

test_input = [
"#1 @ 1,3: 4x4",
"#2 @ 3,1: 4x4",
"#3 @ 5,5: 2x2"
]

apply_to_board(test_input, get_board(test_input))

with open('3-1-input.txt') as fp:
    lines = fp.readlines()
    apply_to_board(lines, get_board(lines))
