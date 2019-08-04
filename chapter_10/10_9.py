"""Chapter 10: Sorting and Searching. Question 10.9"""

import random

# Given an M x N matrix, where each row and column is in ascending order,
# write a function to find the nth element


def make_numbers(n):
    """Generate n unique random numbers sorted and rotated."""
    used_numbers = set()
    acc = []
    while len(acc) < n:
        num = random.randint(0, n * 10)
        if num not in used_numbers:
            used_numbers.add(num)
            acc.append(num)

    # Sort the list
    acc.sort()
    return acc


def get_index_to_list(index):
    """Return the value in a list."""
    return ((1 + index) ** 2) - 1


def fill_in_square(matrix, numbers, index):
    """Fill out the row and column at an index."""
    final_value = get_index_to_list(index)

    if index != 0:
        # Fill out the sides
        next_element = get_index_to_list(index - 1)
        for i in range(index):
            next_element += 1
            matrix[i][index] = numbers[next_element]
            next_element += 1
            matrix[index][i] = numbers[next_element]

    matrix[index][index] = numbers[final_value]

    return matrix


def print_matrix(matrix):
    """Pretty print a matrix."""
    for row in matrix:
        print(row)


def fill_in_row(matrix, numbers, last_cross, row, cols):
    """Fill in the index row with numbers after square is filled."""
    # Forgive all the + 1 -1, it's base 1 to base zero conversions
    # and fencepost issues
    # Get where the list starts
    last_cross_start = get_index_to_list(last_cross - 1) + 1
    row_offset = (row - last_cross) * cols
    start_index = last_cross_start + row_offset
    for col in range(cols):
        matrix[row][col] = numbers[start_index + col]

    return matrix


def fill_in_col(matrix, numbers, last_cross, rows, col):
    """Fill in a column after square is full."""
    last_cross_start = get_index_to_list(last_cross - 1) + 1
    col_offset = (col - last_cross) * rows
    start_index = last_cross_start + col_offset
    for row in range(rows):
        matrix[row][col] = numbers[start_index + row]

    return matrix


def make_matrix(rows, cols):
    """Make a sorted M x N matrix."""
    numbers = make_numbers(rows * cols)
    empty_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    # Find the min of rows and cols to generate an n x n matrix
    min_val = min(rows, cols)

    for i in range(min_val):
        empty_matrix = fill_in_square(empty_matrix, numbers, i)

    # As m or n could be greater, we adjust here
    if rows > cols:
        for row in range(min_val, rows):
            empty_matrix = fill_in_row(empty_matrix, numbers, min_val, row, cols)

    if cols > rows:
        for col in range(min_val, cols):
            empty_matrix = fill_in_col(empty_matrix, numbers, min_val, rows, col)

    # Return the matrix and an empty number in it
    random_number = random.choice(numbers)
    return empty_matrix, random_number


def search_section(matrix, layer, desired_number):
    """Search a section of the matrix."""
    if matrix[layer][layer] == desired_number:
        return (layer, layer)

    for i in range(layer):
        if matrix[layer][i] == desired_number:
            return (layer, i)
        if matrix[i][layer] == desired_number:
            return (i, layer)


def search_square(matrix, desired_number, rows):
    """Binary search a matrix."""
    if matrix[0][0] == desired_number:
        return (0, 0)

    # Otherwise, find the section
    for layer in range(1, rows):
        prior_layer = layer - 1
        if (
            matrix[prior_layer][prior_layer] < desired_number
            and matrix[layer][layer] >= desired_number
        ):
            return search_section(matrix, layer, desired_number)


def binary_search_matrix(matrix, desired_number):
    """Find the (row, col) coordinate of the desired number in the matrix."""
    # Step one, matrix does can be M x N, so check if the number is
    # inside or outside the square
    rows = len(matrix)
    cols = len(matrix[0])

    # Get the last square where m = n
    last_cross = min(rows, cols) - 1
    in_square = matrix[last_cross][last_cross] <= desired_number

    if rows == cols or in_square:
        return search_square(matrix, desired_number, rows)

    # The value is outside the square, so search the edges
    if rows > cols:
        search_outside_rows(matrix, desired_number, rows, cols)
    if cols > rows:
        searh_outside_cols(matrix, desired_number, rows, cols)


matrix, rando_number = make_matrix(5, 5)
print(f"Seeking {rando_number} in:")
print_matrix(matrix)
print(binary_search_matrix(matrix, rando_number))
