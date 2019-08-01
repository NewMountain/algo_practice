"""Chapter 8: Recursion and Dyanamic Programming. Question 8.3"""

# A magic index is define to be magic such that a[i] == i
import time

# This is honestly a stupid problem

data = [-40, -20, -1, 1, 2, 3, 5, 6, 7, 9, 12, 13]


def obvious_answer(data):
    """Obvious scan of data."""
    for index, element in enumerate(data):
        if index == element:
            return element

    return False


assert obvious_answer(data) == 9


# This works based on the assumption the list is sorted
# in ascending order and contais only unique elements
def kind_of_lame_answer(data):
    """For small lists, this makes no sense. But binary search."""
    start = 0
    end = len(data)

    while True:
        if start == end and data[start] != start:
            # Didn't find a match
            return False
        if start + 1 == end:
            # Just compare them by hand
            if data[start] == start:
                return data[start]
            else:
                return data[end]

        # Otherwise, binary search
        mid_point = (start + end) // 2
        element = data[mid_point]
        if element == mid_point:
            return element
        elif element > mid_point:
            end = mid_point
        else:
            start = mid_point


assert kind_of_lame_answer(data) == 9
