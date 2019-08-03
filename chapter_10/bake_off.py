"""Chapter 10: Sorting and Searching. 

Extra practice: Good old fashioned bake off."""

import random
import time
import sys
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from radix_sort import radix_sort

# Recursion depth is annoying in this test
# Noramlly, this default is good, but it gets in the way of
# quick sort
sys.setrecursionlimit(10_000)


def make_random_numbers(n):
    """Generate n random numbers."""
    return [random.randint(0, n * 10) for _ in range(n * 5)]


def time_test(f, data, name):
    """Time test the f."""
    start = time.time()
    f(data)
    end = time.time()
    print(f"It took {end - start} seconds to run {name}")


# Generate test
start = time.time()
random_numbers = make_random_numbers(1500)
end = time.time()
print(f"It took {end - start} seconds to generate the list")

# Bubble sort
time_test(bubble_sort, random_numbers, "Bubble Sort")

# Selection sort
time_test(selection_sort, random_numbers, "Selection Sort")

# Merge sort
time_test(merge_sort, random_numbers, "Merge Sort")

# Quick sort
time_test(quick_sort, random_numbers, "Quick Sort")

# Radix Sort
time_test(radix_sort, random_numbers, "Radix Sort")
