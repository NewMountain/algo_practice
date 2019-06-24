"""Chapter 1: Arrays and strings. Problem 1.7."""

# Given an image represented by an NxN matrix, where each pixel in the image is
# represented by an integer, write a method to reotate the image by 90 degrees.
# Can you do this in place?

test_1 = [[1, 2], [3, 4]]
output_1 = [[3, 1], [4, 2]]

test_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output_2 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

test_3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
output_3 = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]


def reverse_columns(matrix, index):
    """Get the column from a matrix, (List of Rows)."""
    return list(reversed([row[index] for row in matrix]))


def rotate(list_of_lists):
    """Rotate a list_of_lists 90 degrees clockwise."""
    # First version, to rotate 90 clockwise, just grab the column,
    # reverse it and make it a row
    return [reverse_columns(list_of_lists, i) for i in range(len(list_of_lists))]


assert rotate(test_1) == output_1
assert rotate(test_2) == output_2
assert rotate(test_3) == output_3
