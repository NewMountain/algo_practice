"""Chapter 10: Sorting and Searching. Question 10.3"""


# Find an element in a rotated array

import random


def numbers(n):
    """Generate n unique random numbers sorted and rotated."""
    used_numbers = set()
    acc = []
    while len(acc) < n:
        num = random.randint(0, n * 10)
        if num not in used_numbers:
            used_numbers.add(num)
            acc.append(num)

    # Sort the list
    acc.sort()
    # Now chose a random index to rotate
    index = random.randint(1, n - 1)

    return acc[index:] + acc[:index]


n = numbers(10)
number_desired = random.choice(n)


def find_point(numbers, start, end):
    """Find a number in numbers."""
    mid_point = (start + end) // 2
    mid_value = numbers[mid_point]
    start_value = numbers[start]
    end_value = numbers[end]

    if start + 1 == end:
        if start_value > end_value:
            return start
        else:
            return end
    # If the mid is greater than start and end,
    # the split occurs between mid and end
    if mid_value > end_value and mid_value > start_value:
        return find_point(numbers, mid_point, end)
    # If mid is less than start, split occurs between start and mid
    if mid_value < start_value:
        return find_point(numbers, start, mid_point)


def binary_search(numbers, number_desired, start, end):
    """Simple binary search."""
    mid_point = (start + end) // 2
    mid_value = numbers[mid_point]

    if number_desired == mid_value:
        return mid_point
    if number_desired < mid_value:
        # Search left
        return binary_search(numbers, number_desired, start, mid_point - 1)
    else:
        # Search right
        return binary_search(numbers, number_desired, mid_point + 1, end)


def find_desired_num_index(numbers, number_desired, start, end):
    """Find desired number."""
    print(f"Desire: {number_desired} in \n{numbers}")
    split_point = find_point(numbers, 0, len(numbers) - 1)
    print(f"Split point is {split_point}")
    left_start, left_end = numbers[0], numbers[split_point]

    if left_start <= number_desired <= left_end:
        return binary_search(numbers, number_desired, 0, split_point)
    else:
        return binary_search(numbers, number_desired, split_point + 1, len(numbers) - 1)


print(find_desired_num_index(n, number_desired, 0, len(n) - 1))
