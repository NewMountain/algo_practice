"""Chapter 10: Sorting and Searching. 

Extra practice: Implement merge sort."""


import random
import time
import math


def make_random_numbers(n):
    """Generate n random numbers."""
    return [random.randint(0, n * 10) for _ in range(n // 2)]


def safe_get(stuff):
    if not stuff:
        return math.inf

    return stuff[0]


def merge(left, right):
    """Merge the left and right lists."""

    acc = []
    # While both lists are not empty
    while left or right:
        lefty = safe_get(left)
        righty = safe_get(right)
        if lefty <= righty:
            del left[0]
            acc.append(lefty)
        else:
            del right[0]
            acc.append(righty)

    return acc


assert merge([], []) == []
assert merge([1], []) == [1]
assert merge([1], [2]) == [1, 2]
assert merge([2], [1]) == [1, 2]
assert merge([1, 3], [2]) == [1, 2, 3]

# This is O(n log n)
def merge_sort(stuff):
    """Merge sort."""
    if len(stuff) <= 1:
        return stuff

    split = len(stuff) // 2
    left = merge_sort(stuff[:split])
    right = merge_sort(stuff[split:])

    return merge(left, right)


# Script it to use as library
if __name__ == "__main__":
    for n in range(10_000):
        random_numbers = make_random_numbers(n)
        assert merge_sort(random_numbers) == sorted(random_numbers)

