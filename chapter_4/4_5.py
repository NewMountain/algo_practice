"""Chapter 4: Trees and Graphs. Question 4.4"""

# Implement a function to test if a binary tree is
# a binary search tree

from utils import make_unqique_sorted_random_numbers, flatten
import math

# The definition of binary search tree All children left must be <= n
# and all children right must be > n for all nodes in the tree


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


def get_values(node):
    """Recusrively get the values of the node and all its children."""
    if node is None:
        return [None]

    return flatten([node.value, get_values(node.left), get_values(node.right)])


def balanced(node, child, orientation):
    """Test if the node and children are balanced."""
    value = node.value

    children = get_values(child)

    left_child_balanced = test_if_b_tree(node.left)
    right_child_balanced = test_if_b_tree(node.right)

    if orientation == "left":
        # Compare all non-null values
        node_balanced = all([x <= value for x in children if x])
    else:
        node_balanced = all([x > value for x in children if x])

    # print(f"left_child_balanced is {left_child_balanced}")
    # print(f"right_child_balanced is {right_child_balanced}")
    # print(f"node_balanced is {node_balanced}")

    return left_child_balanced and right_child_balanced and node_balanced


def test_if_b_tree(node):
    """Test if the tree is a binary search tree."""
    # Leaf nodes are balanced
    if node is None:
        return True

    # You are balanced if your left and right trees are balanced
    return balanced(node, node.left, "left") and balanced(node, node.right, "right")


test_data = make_unqique_sorted_random_numbers(5)
tree = make_b_tree(test_data)

result = test_if_b_tree(tree)

# That's cool, but it's some crazy O(N^2) algo that is not efficient
# We can do this better

# This one is O(N) time as it visits each node only once
# It will use logN space
def test_2(node, _min, _max):
    """Test if tree is binary search.
    
    Assumes all elements are unique."""
    if node is None:
        return True

    # Otherwise, make sure value is greater than min and less than max
    value_between = _min < node.value < _max

    # Then check the left and right nodes adhere as well
    # Note the min is now the nodes value for all nodes right
    right_balanced = test_2(node.right, node.value, _max)
    left_balanced = test_2(node.left, _min, node.value)

    return value_between and right_balanced and left_balanced


test_data = make_unqique_sorted_random_numbers(10)

test_tree = make_b_tree(test_data)

print(test_2(test_tree, -math.inf, math.inf))
