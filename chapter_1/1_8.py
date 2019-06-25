"""Chatper 1: Arrays and strings. Problem 1.8."""

# Write an algorithm such that if an element in an M x N matrix is 0,
# its entire row and column are set to 0.

# Let's start with brute force
test_matrix = [[1, 2, 3], [4, 5, 6], [7, 0, 9], [10, 11, 12]]
output_matrix = [[1, 0, 3], [4, 0, 6], [0, 0, 0], [10, 0, 12]]


# Complexity is O(N^2) and space is O(N)
def zero_matrix(matrix):
    """Return a zero matrix."""
    # Find the dimensions of the matrix
    num_rows = len(matrix)
    # Now get the first row and check its length
    num_cols = len(matrix[0])

    # Walk through the matrix, if you find a zero
    # note it's column and row index
    zero_cols = []
    zero_rows = []

    # Walk through the matrix by row and column index
    for row in range(num_rows):
        for column in range(num_cols):
            if matrix[row][column] == 0:
                # Note the row and column of the zero value
                zero_cols.append(column)
                zero_rows.append(row)

    # Now walk through the matrix again and swap out values for zeroes
    for row in range(num_rows):
        for column in range(num_cols):
            if row in zero_rows or column in zero_cols:
                matrix[row][column] = 0

    return matrix


assert zero_matrix(test_matrix) == output_matrix
