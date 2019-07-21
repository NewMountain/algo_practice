"""Chapter 4: Trees and Graphs. Question 4.4"""

from utils import make_unqique_sorted_random_numbers, flatten

# Implement a function to check if a binary tree is balanced
# Balanced is defined as the heights of the two subtrees never differ
# by more than one


class BTreeNode:
    """A node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def make_b_tree(stuff):
    """Turn a list of stuff into a sorted binary tree of stuff."""
    # If the list is empty, return None
    if not stuff:
        return None

    # If the list is 1 or two long, handle differently
    if len(stuff) == 1:
        # If one element in list, make that element the node
        return BTreeNode(stuff[0])

    if len(stuff) == 2:
        # Make index 1 the node value and index 0 the left child
        node = BTreeNode(stuff[1])
        node.left = BTreeNode(stuff[0])
        return node

    # Otherwise, get find the index
    index = len(stuff) // 2
    # assign the value to the node and delete that index from the list
    value = stuff[index]
    node = BTreeNode(value)
    del stuff[index]

    lts = []
    gts = []
    for element in stuff:
        if element > value:
            gts.append(element)
        else:
            lts.append(element)

    node.left = make_b_tree(lts)
    node.right = make_b_tree(gts)

    return node


def get_max_depth(node, depth):
    """Find the max depth of a node."""
    if node is None:
        # Return the depth of the parent
        return depth - 1

    else:
        left_depth = get_max_depth(node.left, depth + 1)
        right_depth = get_max_depth(node.right, depth + 1)

        return max([left_depth, right_depth])


def test_if_b_tree(node):
    """Test if a binary tree is balanced.

    Balanced is defined as the heights of the two subtrees never differ
    by more than one.
    """
    # Edge case, tree is empty:
    if node is None:
        # I guess an empty tree is balanced?
        return True

    left_depth = get_max_depth(node.left, 1)
    right_depth = get_max_depth(node.right, 1)

    return abs(left_depth - right_depth) <= 1


test_data = make_unqique_sorted_random_numbers(21)

test_tree = make_b_tree(test_data)

assert test_if_b_tree(test_tree)

