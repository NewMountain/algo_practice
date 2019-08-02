"""Chapter 10: Sorting and Searching. 

Extra practice: Implement quick sort."""

# I love quick sort

# Doing it Haskell style with a few minor tweaks to improve performance

import random


def make_random_numbers(n):
    """Generate n random numbers."""
    return [random.randint(0, n * 10) for _ in range(n // 2)]


def split(tail, head):
    """Create a lte and gt about head in one scan."""
    lte = []
    gt = []
    for elem in tail:
        if elem <= head:
            lte.append(elem)
        else:
            gt.append(elem)

    return (lte, gt)


def quick_sort_prime(stuff):
    """Internal quicksort."""
    if len(stuff) <= 1:
        return stuff

    head = stuff[0]
    tail = stuff[1:]

    left, right = split(tail, head)
    return (quick_sort_prime(left) + [head]) + quick_sort_prime(right)


def quick_sort(stuff):
    """Quick sorts stuff."""
    if len(stuff) <= 1:
        return stuff

    # Slice the list somewhere in the middle
    random_index = random.randint(0, len(stuff) - 1)
    return quick_sort_prime(stuff[random_index:] + stuff[:random_index])
    # return quick_sort_prime(stuff)


# random_numbers = make_random_numbers(50)
# assert quick_sort(random_numbers) == sorted(random_numbers)
# Script it to use as library
if __name__ == "__main__":
    for n in range(1, 10_000):
        random_numbers = make_random_numbers(n)
        assert quick_sort(random_numbers) == sorted(random_numbers)
