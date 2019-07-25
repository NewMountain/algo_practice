"""Chapter 4: Trees and Graphs. Question 4.9"""

# Given a binary search tree with distinct elements, print all
# possible arrays that could have resulted in this
from utils import make_unqique_sorted_random_numbers, flatten


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


data = make_unqique_sorted_random_numbers(6)
print(data)
tree = make_bst(data, None)


def weave(left, right, acc):
    if not left and not right:
        return [acc]

    # Otherwise, add the head of each weave to the list
    if left:
        left_head = left[0]
        left_tail = left[1:]
        left_acc = acc + [left_head]

        left_weave = weave(left_tail, right, left_acc)
    else:
        left_weave = []

    if right:
        right_head = right[0]
        right_tail = right[1:]
        right_acc = acc + [right_head]

        right_weave = weave(left, right_tail, right_acc)
    else:
        right_weave = []

    # Filter empty lists
    result = [x for x in (left_weave + right_weave) if x]
    return result


def make_seqs(tree):
    """Make list of lists that could have generated this BST."""
    # Deal with empty case
    if tree is None:
        return [[]]

    value = tree.value

    # Do something with the children
    left = make_seqs(tree.left)
    right = make_seqs(tree.right)

    if not left and not right:
        return [[value]]

    weave_results = []
    for l in left:
        for r in right:
            for response in weave(l, r, []):
                weave_results.append([value] + response)

    return weave_results


print(make_seqs(tree))
