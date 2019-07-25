"""Chapter 4: Trees and Graphs. Question 4.11"""

# Implement a BST with the following methods:
# insert, find, delete and get_random_node
# Note: Get random node must have an equal probaility
# of selecting any node
from utils import make_unqique_sorted_random_numbers, flatten
import math
import random


def find_min_node_data(node):
    """Return the minimum value node in this tree."""
    if node is None:
        return None

    data = flatten(
        [
            (node.value, node),
            find_min_node_data(node.left),
            find_min_node_data(node.right),
        ]
    )
    # Filter the nulls
    # and return the min
    new_min = math.inf
    new_node = None

    for d in data:
        if d is not None:
            value, node = d
            if value < new_min:
                new_min = value
                new_node = node

    return (new_min, new_node)


def count_nodes(node):
    """Count nodes."""
    if node is None:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)


class BSTree:
    """A binary search tree."""

    def __init__(self, value, parent):
        """Instantiate yourself."""
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, value):
        """Search yourself to see if a node contains the value."""
        if self is None:
            return None

        if self.value == value:
            return self

        return self.find(self.left) or self.find(self.right)

    def insert(self, value):
        """Insert a value into the BST."""
        if self.value == value:
            # No duplicates in our BST
            pass

        if value < self.value:
            # If there is no left child,
            # insert this value as a node to the left
            if self.left is None:
                new_node = BSTree(value, self)
                new_node.parent = self
                self.left = new_node
                return self
            else:
                # Repeat the insert at the left child
                self.left.insert(value)
                return self

        # Otherwise, insert to the right
        if self.right is None:
            new_node = BSTree(value, self)
            new_node.parent = self
            self.left = new_node
            return self

        self.right.insert(value)
        return self

    def _delete(self):
        """Internal method to delete node."""
        if self is None:
            del self

        # Otherwise, count the children
        left = 0
        if self.left is not None:
            left = 1

        right = 0
        if self.right is not None:
            right = 1

        if sum(left, right) == 0:
            # Node has no children, you can just delete it
            del self

        elif sum(left, right) == 1 and left == 1:
            # Swap the current node with the left child
            self.left.parent = self.parent
            self.parent.left = self.left
            # The delete the node to delete
            self.left = None
            self.right = None
            self._delete()

        elif sum(left, right) == 1 and right == 1:
            # Swap the current node with the right child
            self.right.parent = self.parent
            self.parent.right = self.right
            self.left = None
            self.right = None
            self._delete()

        elif sum(left, right) == 2:
            # The node has two children
            # Now the fun begins
            # Find the minimum of right node
            min_value, min_node = find_min_node_data(self.right)
            # Get the value out of this node
            # set that value equal to node to delete
            self.value = min_value

            min_node._delete()

    def delete(self, value):
        """Delete a value in the BST."""
        # First find the value
        node_to_delete = self.find(value)
        node_to_delete._delete()

    def get_random_node(self):
        """Get a random node with equal probability to get any node."""
        # Count the nodes on left and right
        left_nodes = count_nodes(self.left)
        right_nodes = count_nodes(self.right)
        total_count = 1 + left_nodes + right_nodes

        draw = random.uniform(0, 1)

        if (1 / total_count) <= draw:
            return self

        if ((1 + left_nodes) / total_count) <= draw:
            return self.left.get_random_node()

        return self.right.get_random_node()

