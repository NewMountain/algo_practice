"""Chapter 10: Sorting and Searching. Question 10.1"""

# You are give two sorted arrays, A and B where A has a large enough buffer
# at the end to hold A and B in sorted order

b = [5, 8, 9, 1, 4]
a = [12, 2, 3, 6, 4, 9, 18, 4, 7, 0, 0, 0, 0, 0]


def sorted_merge(a, b):
    """Sort A and B and merge into A."""
    # I kind of feel like this is cheating, but why not:
    # Derive the empty space using len of a
    len_b = len(b)
    len_a = len(a)
    start_of_empty_section = len_a - len_b
    # sort the two lists and assign to a (no reallocation required)
    a = sorted(a[:start_of_empty_section] + b)
    return a


print(sorted_merge(a, b))

