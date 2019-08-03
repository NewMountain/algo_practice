"""Chapter 10: Sorting and Searching. Question 10.4"""

# You are given a list structure which has no length method.
# Efficiently find element e in the list
# You can ask for an element by index
# If the element is out of range, you will get -1


import random

# Make a list of n elements, make it pretty huge
# for better testing
def numbers(n):
    """Generate n random positive numbers sorted."""
    return sorted([random.randint(0, n * 10) for _ in range(n)])


def find_at(stuff, index):
    """Return the value at index or -1 if out of range."""
    try:
        return stuff[index]
    except IndexError:
        return -1


def oom_to_index(oom):
    """Turn order of magnitude into number."""
    return 10 ** oom


def find_order_of_magnitude(stuff):
    """Find the order of magnitude range where list ends."""
    last_oom = None
    this_oom = 0

    while find_at(stuff, oom_to_index(this_oom)) != -1:
        last_oom = this_oom
        this_oom += 1

    return oom_to_index(last_oom), oom_to_index(this_oom)


def find_edge(stuff, start, end):
    """Find this edge in this weird structure."""
    mid = (start + end) // 2

    if find_at(stuff, mid) != -1 and find_at(stuff, mid + 1) == -1:
        return mid

    if find_at(stuff, mid - 1) != -1 and find_at(stuff, mid) == -1:
        return mid - 1

    if find_at(stuff, mid) == -1:
        return find_edge(stuff, start, mid - 1)

    if find_at(stuff, mid) != -1:
        return find_edge(stuff, mid + 1, end)


def find_end(stuff):
    """Find the index of the last element of stuff."""
    # Step 1, find the order of magnitude
    last_known, out_of_bounds = find_order_of_magnitude(stuff)
    egde_index = find_edge(stuff, last_known, out_of_bounds)
    return egde_index


for n in range(2, 150):
    l = numbers(n)
    assert find_end(l) == len(l) - 1


# Find the index of the number desired in n
def b_search(stuff, desired, start, end):
    """Simple binary search."""
    mid = (start + end) // 2
    if stuff[mid] == desired:
        return mid

    if desired < stuff[mid]:
        return b_search(stuff, desired, start, mid - 1)
    if desired > stuff[mid]:
        return b_search(stuff, desired, mid + 1, end)


def search(stuff, number_desired):
    """Binary search in our somewhat weird data structure."""
    last_element = find_end(stuff)
    return b_search(stuff, number_desired, 0, last_element)


for _ in range(50):
    # Pick a list size from 101 to 1_000_000
    size = random.randint(101, 1_000_000)
    n = numbers(size)
    number_desired = random.choice(n)
    index = search(n, number_desired)
    assert n[index] == number_desired
    print("Crushed it!")
