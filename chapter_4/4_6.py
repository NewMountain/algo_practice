"""Chapter 4: Trees and Graphs. Question 4.7"""

# Write an algorithm to find the "next" node in order
# in a binary search tree

from utils import make_unqique_sorted_random_numbers, flatten
import random
import math


class BTreeNode:
    """A node in a binary tree."""

    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


def make_b_tree(stuff, parent):
    """Turn a list of stuff into a sorted binary tree of stuff."""
    # If the list is empty, return None
    if not stuff:
        return None

    # If the list is 1 or two long, handle differently
    if len(stuff) == 1:
        # If one element in list, make that element the node
        return BTreeNode(stuff[0], parent)

    if len(stuff) == 2:
        # Make index 1 the node value and index 0 the left child
        node = BTreeNode(stuff[1], parent)
        node.left = BTreeNode(stuff[0], node)
        return node

    # Otherwise, get find the index
    index = len(stuff) // 2
    # assign the value to the node and delete that index from the list
    value = stuff[index]
    node = BTreeNode(value, parent)
    del stuff[index]

    lts = []
    gts = []
    for element in stuff:
        if element > value:
            gts.append(element)
        else:
            lts.append(element)

    node.left = make_b_tree(lts, node)
    node.right = make_b_tree(gts, node)

    return node


def get_leftest(node):
    """Return value of leftest node."""
    if node.left is None:
        return node.value
    else:
        return get_leftest(node.left)


def first_greatest_parent(node, value):
    """Return first parent value greater than value."""
    if node.parent is None:
        return node.value

    if node.parent.value < value:
        return first_greatest_parent(node.parent, value)

    # Otherwise, return parent value
    return node.parent.value


def find_element(node, value):
    """Return the next value in the tree."""
    # Get the value of the node
    local_value = node.value

    if local_value == value:
        # So this is where things get crazy
        # We want either the leftest right child
        # or the parents right (provided we are not the parents right)
        # or the first gt parent
        if node.right is not None:
            leftest_right_child = get_leftest(node.right)
        else:
            leftest_right_child = math.inf

        if node.parent is not None:
            parent_value = first_greatest_parent(node, value)
        else:
            parent_value = math.inf

        # Filter numbers less than value
        results = [leftest_right_child, parent_value]

        return min([x for x in results if x > value])

    if local_value > value:
        return find_element(node.left, value)
    else:
        return find_element(node.right, value)


def select_non_last_random_element(stuff):
    """ Select a random non-last element from the list."""
    upper = len(stuff) - 2
    index = random.randint(0, upper)
    return stuff[index]


def find_index(stuff, element):
    """Return the index of element in stuff."""
    index = 0

    while stuff[index] != element:
        index += 1

    return index


def play_game(n):
    """Play the game to run this simulation a bunch of times and test it always works."""
    for _ in range(0, n):
        # Generate a tree size
        n = random.randint(3, 1001)
        test_data = make_unqique_sorted_random_numbers(n)

        random_number = select_non_last_random_element(test_data)

        # Find the index of the random number
        index = find_index(test_data, random_number)
        next_elem = test_data[index + 1]

        tree = make_b_tree(test_data, None)

        result = find_element(tree, random_number)

        assert result == next_elem


# This will take 30 ish seconds, but I'm pretty
# confident this will test just about any situation
play_game(100_000)
