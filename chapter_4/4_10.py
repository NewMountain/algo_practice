"""Chapter 4: Trees and Graphs. Question 4.10"""

# Given two very large binary trees, create an algorithm to
# determine if T2 is a subtree of T1
from utils import make_unqique_sorted_random_numbers, flatten
import random


class BSTNode:
    """Node in a binary search tree."""

    def __init__(self, value, parent):
        """Init the node."""
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


# Assumes the data is elems is unique and sorted
def make_bst(elems, parent):
    """Make a binary search tree."""
    # Handle and empty list
    if not elems:
        return None

    if len(elems) == 1:
        value = elems[0]
        node = BSTNode(value, parent)
        return node

    if len(elems) == 2:
        value = elems[1]
        node = BSTNode(value, parent)
        child_value = elems[0]
        # Node just created is the parent of this node
        child_node = BSTNode(child_value, node)
        node.left = child_node
        return node

    # Otherwise, we have at least two children
    index = len(elems) // 2
    value = elems[index]
    # Delete this value from the list
    del elems[index]

    node = BSTNode(value, parent)
    node.left = make_bst([e for e in elems if e < value], node)
    node.right = make_bst([e for e in elems if e > value], node)

    return node


data = make_unqique_sorted_random_numbers(5000)
tree = make_bst(data, None)


def count_nodes(node):
    """Count the nodes in the tree."""
    if node is None:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)


# Now let's pick some node in the tree
def equal_weighted_random_node(tree):
    """Pick a node at random given all nodes have a random weight."""
    # Step 1, get the count of nodes on the left and right
    left_count = count_nodes(tree.left)
    right_count = count_nodes(tree.right)
    # + 1 for the node we are at
    total_count = left_count + right_count + 1

    # Generate a random number from 0-1
    draw = random.uniform(0, 1)

    # If probability is <= 1/total_count, return the node
    if draw <= (1 / total_count):
        return tree

    # If probability is <= left_count/total_count, go left and try again
    if draw <= ((left_count + 1) / total_count):
        return equal_weighted_random_node(tree.left)

    # Otherwise go right and try again
    return equal_weighted_random_node(tree.right)


random_node = equal_weighted_random_node(tree)


def find_node(node, tree):
    """Find a Node in a tree or return None."""
    if tree is None:
        return None

    if tree.value == node.value:
        return tree

    return find_node(node, tree.left) or find_node(node, tree.right)


def compare_trees(t1, t2):
    """Compare that two trees are exactly the same."""
    if t1 is None and t2 is None:
        return True

    left_matches = compare_trees(t1.left, t2.left)
    right_matches = compare_trees(t1.right, t2.right)

    return t1.value == t2.value and left_matches and right_matches


# Cool, let's solve this problem
def check_subtree(t1, t2):
    """Check if t2 is an exact subtree of t1."""
    # Step 1, find the head of t2 in t1
    sub_t1 = find_node(t2, t1)

    if sub_t1 is None:
        raise Exception("T2 does not occur in t1")

    return compare_trees(sub_t1, t2)


result = check_subtree(tree, random_node)

print(f"result is {result}")
