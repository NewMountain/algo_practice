"""Chapter 8: Recursion and Dyanamic Programming. Question 8.10"""

# Given a matrix of colors, and a dot you selected
# fill in all the pixels with the color

import random
from collections import deque


def rando_color():
    """Generate a random color."""
    return random.randint(0, 4)


def roll_die():
    """Roll the stickiness and color die."""
    return (random.randint(1, 10), rando_color())


def generate_colors(rows, cols):
    """Randomly generate 'sticky' colors."""
    prior_color = None
    # Let's assume we have 5 colors 0,1,2,3,4
    # Next we want our colors to be "sticky" not just
    # a bunch of rando colors
    # To do this, we'll take two rolls,
    # The first will be stickiness and the next color
    colors = []
    for _ in range(rows * cols):

        stickiness, color = roll_die()

        if prior_color is None:
            prior_color = color
            colors.append(color)
        # Seventy percent chance of repeat
        if stickiness <= 6:
            colors.append(prior_color)
        else:
            prior_color = color
            colors.append(color)

    return colors


def make_square(rows, cols):
    """Genreate a square of colors."""
    colors = generate_colors(rows, cols)
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            color = colors[row + col]
            grid[row][col] = color

    return grid


def special_print(grid):
    """Pretty print a grid without __repr__ and OOP."""
    for row in grid:
        print(row)


ROWS = 10
COLS = 12

grid = make_square(ROWS, COLS)

# Pick a point at random
rando_row, rando_col = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))
# pick a color at random
rando_color = rando_color()

special_print(grid)


def is_inside(point, grid):
    """Check if cell is inside grid."""
    row, col = point
    max_rows = len(grid)
    max_cols = len(grid[0])

    in_row = 0 <= row < max_rows
    in_col = 0 <= col < max_cols

    return in_row and in_col


def cell_is_color(point, color, grid):
    """Return if point matches color."""
    row, col = point
    return grid[row][col] == color


def find_more_work(row, col, grid, color_to_unpaint):
    """Return any points which could be unpainted."""
    # Up , down , left, right
    surrounding_cells = [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]
    return [
        cell
        for cell in surrounding_cells
        if is_inside(cell, grid) and cell_is_color(cell, color_to_unpaint, grid)
    ]


def paint_dat_grid(grid, row, col, color):
    """Fill in the grid starting with (row, col) with color."""
    # This is basically just high class breadth first search
    already_painted = set()
    point = (row, col)
    work = deque()
    # We want work to be FIFO
    work.appendleft(point)
    color_to_unpaint = grid[row][col]

    print(f"Painting {point} to {color} from {color_to_unpaint}")

    # While there is work to be done
    while len(work) > 0:
        job = work.pop()
        row, col = job
        # Paint the cell
        grid[row][col] = color
        already_painted.add(job)
        # Look up down left and right and see
        # if there are any surrounding pixels of color_to_unpaint
        # to be colored
        for another_job in find_more_work(row, col, grid, color_to_unpaint):
            if another_job not in already_painted:
                # If there's more jobs, add them to work
                work.appendleft(another_job)

    return grid


colored_grid = paint_dat_grid(grid, rando_row, rando_col, rando_color)

special_print(colored_grid)
