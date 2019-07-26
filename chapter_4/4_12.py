"""Chapter 4: Trees and Graphs. Question 4.12"""

# You are given a binary tree in which each node contains an integer
# which might be positive or negative. Count the number of paths
# that sum to a given value. The path can start or end at any point

# As long as we don't need to carry the numbers that summed to
# our desired number, we should be fine.
from min_heap import MinHeap
import random
import statistics


# Coerce to int so numbers match better
data = [int(random.randint(-5, 20)) for _ in range(20_000)]

# Pick a number at random from data
number_to_match = random.choice(data)

# Make a min heap with this data
mn = MinHeap()

mn.push(data)


def count(tree, index, number_to_match, running_totals):
    """Count how many series equal the number to match."""
    if index is None:
        return 0

    if tree.get_value(index) is None:
        # Avoid index out of range
        return 0

    # Get the value
    value = tree.get_value(index)

    # Append a zero the the running totals
    running_totals.append(0)
    # Now increment all running totals by value
    new_running_totals = [(t + value) for t in running_totals]

    # Count how many of the running totals match the number_to_match
    matches = len([t for t in new_running_totals if t == number_to_match])

    return (
        matches
        + count(tree, tree.left_child(index), number_to_match, new_running_totals)
        + count(tree, tree.right_child(index), number_to_match, new_running_totals)
    )


result = count(mn, 0, number_to_match, [])
print(f"{result} instances of some subtree summing to {number_to_match}")
