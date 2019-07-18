"""Chapter 4: Trees and Graphs. Question 4.2"""

# Given a list of unique (sorted ascending) elements,
#  create a binary search tree.

import math
import json


data = [1, 2, 4, 5, 6, 7, 8, 10, 13, 15, 17, 20]


def safe_print(maybe_node):
    """Safe print a maybe node."""
    if maybe_node is None:
        return {}
    else:
        return maybe_node.as_dict()


class BTreeNode:
    """Node in a binary search tree."""

    def __init__(self, value):
        """Initialization."""
        self.value = value
        self.left = None
        self.right = None

    def as_dict(self):
        """Return as dict."""
        if self.value is None:
            return {}
        else:
            return {
                "value": self.value,
                "left": safe_print(self.left),
                "right": safe_print(self.right),
            }

    def __repr__(self):
        """How to print yourself."""
        return json.dumps(self.as_dict(), indent=2)


def get_node_val(list_of_elems):
    """Find the middle or just right of middle node."""
    length = len(list_of_elems)

    # If there is only one element
    if len(list_of_elems) == 1:
        return (list_of_elems[0], 0)

    # If there are only two elements
    # The leftmost element should be the child
    if len(list_of_elems) == 2:
        return (list_of_elems[1], 1)

    index = length // 2

    return (list_of_elems[index], index)


def make_tree(elems):
    """Make a binary search tree."""
    # Handle an empty list
    if not elems:
        return None

    # Get the median or right of median value
    (value, index) = get_node_val(elems)
    # Create a node from that value
    node = BTreeNode(value)
    # Now delete the value from the list
    del elems[index]

    node.left = make_tree([e for e in elems if e < value])
    node.right = make_tree([e for e in elems if e > value])

    return node


data_1 = [1]
data_2 = [1, 2]
data_3 = [1, 2, 3]
data_5 = list(range(1, 6))
data_7 = list(range(1, 8))
data_9 = list(range(1, 10))

# print(make_tree(data_1))
# print(make_tree(data_2))
# print(make_tree(data_3))
# print(make_tree(data_5))
# print(make_tree(data_7))
# print(make_tree(data_9))
print(make_tree(data))
