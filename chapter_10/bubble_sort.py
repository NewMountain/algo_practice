"""Chapter 10: Sorting and Searching. 

Extra practice: Implement bubble sort."""

import random
import time


def make_random_numbers(n):
    """Generate n random numbers."""
    return [random.randint(0, 50) for _ in range(20)]


# This is O(N^2)
def bubble_sort(stuff):
    """Bubble sort."""

    while True:
        any_flips = False
        for i in range(0, len(stuff) - 1):
            if stuff[i] <= stuff[i + 1]:
                pass
            else:
                less = stuff[i + 1]
                more = stuff[i]
                stuff[i] = less
                stuff[i + 1] = more
                any_flips = True

        if any_flips == False:
            break

    return stuff


# Script it to use as library
if __name__ == "__main__":
    for n in range(50_000):
        random_numbers = make_random_numbers(n)
        assert bubble_sort(random_numbers) == sorted(random_numbers)
