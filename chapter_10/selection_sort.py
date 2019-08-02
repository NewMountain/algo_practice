"""Chapter 10: Sorting and Searching. 

Extra practice: Implement selection sort."""


import random
import math


def make_random_numbers(n):
    """Generate n random numbers."""
    return [random.randint(0, 50) for _ in range(20)]


# This is O(N^2)
def selection_sort(stuff):
    """Selection sort."""
    for i in range(0, len(stuff)):
        # For each sweep of the list,
        # Find the max_index
        max_value = -math.inf
        max_index = None
        if i == 0:
            list_to_scan = stuff
        else:
            list_to_scan = stuff[:(-i)]
        for idx, value in enumerate(list_to_scan):
            if value > max_value:
                max_value = value
                max_index = idx

        rando_index = -(i + 1)
        # Swap the max with the rando value
        rando_value = stuff[rando_index]
        stuff[max_index] = rando_value
        stuff[rando_index] = max_value

    return stuff


# Script it to use as library
if __name__ == "__main__":
    for n in range(50_000):
        random_numbers = make_random_numbers(n)
        assert selection_sort(random_numbers) == sorted(random_numbers)

