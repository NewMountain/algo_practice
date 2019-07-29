"""Chapter 8: Recursion and Dyanamic Programming. Question 8.7"""


def flatten(list_of_something):
    accum = []
    for elem in list_of_something:
        if isinstance(elem, list):
            accum += flatten(elem)
        else:
            accum.append(elem)
    return accum


def make_perms(thing):
    """Return all permutations of a string."""
    if len(thing) <= 1:
        return [thing]

    # Otherwise, take the heand and tail
    head = thing[0]
    tail = thing[1:]
    # and slide the head into all positions
    # around the permutations of the tail
    accumulator = []
    for perm in make_perms(tail):
        # We can use the index of thing to help here
        for idx in range(len(thing)):
            # Get the left side
            # All elements up to the index
            left = perm[:idx]
            # The right side is all element
            # at and past the index
            right = perm[idx:]
            # Smoosh them all together
            value = left + [head] + right
            # Flatten the list of lists and append
            accumulator.append(flatten(value))

    # Otherwise just return the list of things
    return accumulator


# assert make_perms([1, 2, 3]) == [[1,2,3], [1,3,2], []]
print(make_perms([1, 2, 3]))

