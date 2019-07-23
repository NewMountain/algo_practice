"""Chapter 4: Trees and Graphs. Question 4.8"""

# Design an algorithm and write code to find the first common ancestor
# of two nodes

# This solution can be completed one of two different ways
from utils import make_unqique_sorted_random_numbers, flatten
import random
import math
import time


class BTreeNode:
    """A node in a binary tree."""

    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        """Fancy print function."""
        return f"value: {self.value}, parent_value: {self.parent.value}"


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


def get_node(node, value, depth):
    """Return the node if found."""
    if node is None:
        return (None, depth)

    if node.value == value:
        return (node, depth)

    # Try searching the left subtree
    left_node, l_depth = get_node(node.left, value, depth + 1)
    if left_node is not None:
        return (left_node, l_depth)

    right_node, r_depth = get_node(node.right, value, depth + 1)
    if right_node is not None:
        return (right_node, r_depth)

    # Return none if you can't find the node
    return (None, depth)


def go_up(node, n):
    """Go up n parents."""
    steps_taken = 0

    while steps_taken < n:
        node = node.parent
        steps_taken += 1

    return node


# In the first solution, we assume we can access parents from the node
# Normally, I would build a list for each node back to parent
# once p and q are found
# then just compare the two, but the problem stipulates you shouldn't
# save any nodes, so fine
def first_common_ancestor_1(tree, p, q):
    """Find the first common ancestor of p and q."""
    # Step 1, return and p and q node
    p_node, p_depth = get_node(tree, p, 0)
    q_node, q_depth = get_node(tree, q, 0)

    if p_depth > q_depth:
        offset = abs(p_depth - q_depth)
        # Walk up offset nodes from p
        p_node = go_up(p_node, offset)
    if p_depth < q_depth:
        offset = abs(p_depth - q_depth)
        # Walk up offset nodes from q
        q_node = go_up(q_node, offset)

    # Now that we are starting from the same place,
    # Keep going up until we have a common ancestor
    while q_node.value != p_node.value:
        q_node = q_node.parent
        p_node = p_node.parent

    # Return either node as they will converge
    return q_node.value


# # Build a tree with 100 elements to make this interesting
# test_data = make_unqique_sorted_random_numbers(100)
# tree = make_b_tree(test_data, None)

# # Now pick a p
# p = random.choice(test_data)
# q = random.choice(test_data)

# first_common_ancestor_1(tree, p, q)


def inside(node, value):
    """Return true or false if value is in the subtree."""
    if node is None:
        return False

    if node.value == value:
        return True

    return inside(node.left, value) or inside(node.right, value)


def first_common_ancestor_2(tree, p, q):
    """Same as the first except this time solving without parents."""
    # Basically recurse down the tree until the node where p is on one side and q
    # is on the other
    # The only precaution as p and q are chosen at random, assign the left of p and q to
    # low and max of p and q to right
    left = min(p, q)
    right = max(p, q)

    current_node = tree

    # Now run peer down function
    while True:

        # You lucked out, both are the same
        if left == right:
            return left
        # We are at the crossroads!
        if inside(current_node.left, left) and inside(current_node.right, right):
            # The return breaks the loop
            return current_node.value
        # Both nodes are to the left, go down left node
        if inside(current_node.left, left) and inside(current_node.left, right):
            current_node = current_node.left
        # Both nodes are to the right, go down right node
        if inside(current_node.right, left) and inside(current_node.right, right):
            current_node = current_node.right

        # Weird edge case, left or right is actually a parent of the other
        if current_node.value == left or current_node.value == right:
            return current_node.value


# first_common_ancestor_2(tree, p, q)


# Let's stress test this 25_000 times to really make sure these are the same
for i in range(25_000):
    if i % 1000 == 0:
        print(f"{i} of 25,000")

    # Build a tree with 500 elements to make this interesting
    test_data = make_unqique_sorted_random_numbers(500)
    tree = make_b_tree(test_data, None)

    # Now pick a p
    p = random.choice(test_data)
    q = random.choice(test_data)

    res_1 = first_common_ancestor_1(tree, p, q)
    res_2 = first_common_ancestor_2(tree, p, q)

    if res_1 == res_2:
        pass

    else:
        print("Problem!")
        print(res_1)
        print(res_2)
        print(p)
        print(q)

