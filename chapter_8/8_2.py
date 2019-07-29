"""Chapter 8: Recursion and Dyanamic Programming. Question 8.2"""


# Imagine a grid with a robot in the top left corner
# The grid is r by c.
# The robot can only move down or right
# Certain cells are off limits
# Design an algorithm to find a path for the robot

import random
from functools import lru_cache
from time import time

# Step 1, generate a board


def make_walls(r, c, n_walls):
    """Randomly generate some walls in this map."""
    walls = []
    while len(walls) < n_walls:
        row = random.randint(0, r - 1)
        col = random.randint(0, c - 1)
        wall = (row, col)
        if wall not in walls:
            walls.append(wall)

    return walls


def make_board(r, c, n_walls):
    """Generate a board given rows, cols and number of walls."""
    # Randomly generate walls
    walls = make_walls(r, c, n_walls)
    board = [[0 for _ in range(c)] for _ in range(r)]

    for row in range(r):
        for column in range(c):
            if (row, column) in walls:
                # 1 means walls
                board[row][column] = 1
            else:
                board[row][column] = 0

    return board


ROWS = 3
COLS = 3
WALLS = 1
board = make_board(ROWS, COLS, WALLS)

print(board)

# Note, the original problem just wanted to know if there was a path, no what it was
# I found this problem to be a little more interesting, so I changed it


def direct_robot(board, row, col, paths):
    """Return the paths the robot can take."""
    max_row = len(board)
    max_col = len(board[0])

    within_rows = 0 <= row <= max_row - 1
    within_cols = 0 <= col <= max_col - 1

    inside = within_cols and within_rows

    if not inside:
        return [[]]

        # Wall detection
    if board[row][col] == 1:
        return [[]]

    point = (row, col)

    paths = [path + [point] for path in paths]

    if row == max_row - 1 and col == max_col - 1:
        return paths

    result = direct_robot(board, row + 1, col, paths) + direct_robot(
        board, row, col + 1, paths
    )

    # Filter nulls
    return [r for r in result if r]


print(direct_robot(board, 0, 0, [[]]))

# Sort of dead end
# Only Python immutable objects are hashable

# @lru_cache(maxsize=None)
# def fast_robot(board, row, col, paths):
#     """Just memoize direct_robot."""
#     max_row = len(board)
#     max_col = len(board[0])

#     within_rows = 0 <= row <= max_row - 1
#     within_cols = 0 <= col <= max_col - 1

#     inside = within_cols and within_rows

#     if not inside:
#         return [[]]

#         # Wall detection
#     if board[row][col] == 1:
#         return [[]]

#     point = (row, col)

#     paths = [path + [point] for path in paths]

#     if row == max_row - 1 and col == max_col - 1:
#         return paths

#     result = fast_robot(board, row + 1, col, paths) + fast_robot(
#         board, row, col + 1, paths
#     )

#     # Filter nulls
#     return [r for r in result if r]


# huge_board = make_board(5, 5, 5)

# s1 = time()
# direct_robot(huge_board, 0, 0, [[]])
# e1 = time()

# print(f"direct_robot took {e1 - s1} seconds")

# s2 = time()
# fast_robot(huge_board, 0, 0, [[]])
# e2 = time()

# print(f"fast_robot took {e2 - s2} seconds")
