"""Chatper 1: Arrays and strings. Problem 1.8."""

# Write an algorithm such that if an element in an M x N matrix is 0,
# its entire row and column are set to 0.

# Let's start with brute force
test_matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 0, 9], [10, 11, 12]]
test_matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 0, 9], [10, 11, 12]]
output_matrix = [[1, 0, 3], [4, 0, 6], [0, 0, 0], [10, 0, 12]]


# Complexity is O(N^2) and space is O(N) assuming N > M
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


assert zero_matrix(test_matrix_1) == output_matrix

# Now, can we do better?
# It would seem we need to read each element in the matrix at least once,
# so I don't think we can do better than O(N^2)

# In terms of space, as we're just going to set the entire column and row to zeroes
# if we find a zero anyway, we can use the first row and column to store the zeroes
# :clever:

# Complexity still O(N^2), but space is now O(1)
def zero_matrix_two(matrix):
    """Same as zero matrix, but reducing space."""
    # Find the dimensions of the matrix
    num_rows = len(matrix)
    # Now get the first row and check its length
    num_cols = len(matrix[0])

    # Walk through the matrix by row and column index
    for row in range(num_rows):
        for column in range(num_cols):
            if matrix[row][column] == 0:
                # Set the first row to zero
                matrix[row][0] = 0
                # Set the first column to zero
                matrix[0][column] = 0

    # Now walk through the matrix again and swap out values for zeroes
    # We now must skip the first row and column as they are zeroed
    # already
    for row in range(1, num_rows):
        for column in range(1, num_cols):
            if matrix[row][0] == 0 or matrix[0][column] == 0:
                matrix[row][column] = 0

    return matrix


assert zero_matrix_two(test_matrix_2) == output_matrix
