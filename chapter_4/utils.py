"""Utils that allow more focus on the code and less about how to stage."""

import random


def make_unqique_sorted_random_numbers(n):
    """Create n random numbers unique and sorted."""
    lower_bound = 0
    upper_bound = n * 10

    already_used_numers = set()

    accumulator = []

    while len(accumulator) < n:
        random_number = random.randint(lower_bound, upper_bound)
        if random_number not in already_used_numers:
            accumulator.append(random_number)
            already_used_numers.add(random_number)

    return list(sorted(accumulator))


def flatten(stuff):
    """Flatten a nested list of stuff."""
    acc = []
    for elem in stuff:
        if isinstance(elem, list):
            for sub_elem in flatten(elem):
                acc.append(sub_elem)
        else:
            acc.append(elem)

    return acc
