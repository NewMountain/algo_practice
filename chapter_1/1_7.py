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


# O(N^2)
def rotate(list_of_lists):
    """Rotate a list_of_lists 90 degrees clockwise."""
    # First version, to rotate 90 clockwise, just grab the column,
    # reverse it and make it a row
    return [reverse_columns(list_of_lists, i) for i in range(len(list_of_lists))]


assert rotate(test_1) == output_1
assert rotate(test_2) == output_2
assert rotate(test_3) == output_3


def get_column(index, matrix):
    """Return a column from a matrix."""
    return [row[index] for row in matrix]


def get_edge(index, axis, matrix):
    """Get the edge by index and axis."""
    if axis == "x":
        return matrix[index]
    else:
        # return the column
        return get_column(index, matrix)


# Now can I do it in place?
# Pointer semantics in Python are super awkward
# So after reading this:
# https://stackoverflow.com/questions/14905527/get-a-pointer-to-a-list-element
# It seems my options are wrap the ints in an object
# or just use a dictionary and some modulo math
# Though creating these structures is going to create additional work and
# Not really cut back on memory...so...dead end.
def rotate_2(list_of_lists):
    """Rotate a list in place."""
    # print(list_of_lists)
    # # Find how many layers that matrix has
    # layers = len(list_of_lists) // 2

    # for l in range(layers):
    #     # Define the edges of the matrix
    #     low_index = l
    #     high_index = len(list_of_lists) - 1
    #     # Get references to the sides of the matrix
    #     # Get reference to top
    #     top = get_edge(low_index, "x", list_of_lists)
    #     # Keep a deep copy of top for a moment
    #     top_copy = top.copy()
    #     print(top)
    #     # Define a left
    #     left = get_edge(low_index, "y", list_of_lists)
    #     # Swap top for a deep copy of left
    #     top = left.copy()
    #     print(top)
    #     # Define a bottom
    #     bottom = get_edge(high_index, "x", list_of_lists)
    #     # Left will be a deep copy of bottom
    #     left = bottom.copy()
    #     # Define a right
    #     right = get_edge(high_index, "y", list_of_lists)
    #     # Bottom will be a deep copy of right
    #     bottom = right.copy()
    #     # Right will be the top copy we set at the beginning
    #     right = top_copy

    # print(list_of_lists)

    print("Milk was a bad choice...")

