"""Chapter 10: Sorting and Searching. 

Extra practice: Good old fashioned bake off."""

import random
import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


def make_random_numbers(n):
    """Generate n random numbers."""
    return [random.randint(0, n * 10) for _ in range(n)]


def time_test(f, data, name):
    """Time test the f."""
    start = time.time()
    f(data)
    end = time.time()
    print(f"It took {end - start} seconds to run {name}")


# Generate test
start = time.time()
random_numbers = make_random_numbers(1000)
end = time.time()
print(f"It took {end - start} seconds to generate the list")

# Bubble sort
time_test(bubble_sort, random_numbers, "Bubble Sort")

# Bubble sort
time_test(selection_sort, random_numbers, "Selection Sort")

# Bubble sort
time_test(merge_sort, random_numbers, "Merge Sort")

# Bubble sort
time_test(quick_sort, random_numbers, "Quick Sort")
