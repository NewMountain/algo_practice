"""Chapter 4: Trees and Graphs. Question 4.3"""

# Given a binary tree, design and algorithm which creates
# a linked list of all nodes at each depth

# There's nothing wrong with linked lists save for the fact
# you basically need to roll you own in Python

import random


class LLNode:
    """Linked List node."""

    def __init__(self, value):
        """Yet another linked list problem."""
        self.value = value
        self.next = None


class BTreeNode:
    """Binary Tree Node."""

    def __init__(self, value):
        """More OOP."""
        self.value = value
        self.left = None
        self.right = None


def make_random_unique_data(n):
    """Return a list with n random numbers."""
    # The range should always be 10x of n
    lower_bound = 1
    upper_bound = n * 10

    already_seen = set()

    acc = []
    while len(acc) < n:
        num = random.randint(lower_bound, upper_bound)
        if num not in already_seen:
            # Add to accumulator and already_seen set
            already_seen.add(num)
            acc.append(num)

    return acc


assert len(make_random_unique_data(50)) == 50


def make_child_lists(stuff, value):
    """Take a list of stuff and a value.

    Return two lists, the first all elements less than value.
    The second all elements greater than value.
    """
    smaller = []
    bigger = []

    for elem in stuff:
        if elem > value:
            bigger.append(elem)
        else:
            smaller.append(elem)

    return (smaller, bigger)


def find_index(stuff):
    """Find the index in a list of stuff."""
    if len(stuff) == 1:
        return 0

    if len(stuff) == 2:
        return 1

    # Find the median point of a list
    # [1,2,3] => index 1, [1,2,3,4] => index 2
    return len(stuff) // 2


# Cool, next let's create a make_b_tree()
def make_tree(list_of_stuff):
    """Create a tree from a list of stuff."""
    # If the list is empty, return Node
    if not list_of_stuff:
        return None

    index = find_index(list_of_stuff)
    # Get the value of that index
    value = list_of_stuff[index]

    # Now delete that index from the list
    del list_of_stuff[index]

    # Create a BTreeNode with the value
    node = BTreeNode(value)

    # I'm doing this to scan once instead of twice with
    # List comprehensions
    l, r = make_child_lists(list_of_stuff, value)
    node.left = make_tree(l)
    node.right = make_tree(r)

    return node


def make_b_tree(nodes):
    """Make a b tree with n nodes."""
    # Create nodes unique integers
    data = make_random_unique_data(nodes)
    # Now build a tree from the random data
    # make_tree assumes the data is sorted
    sorted_data = list(sorted(data))
    return make_tree(sorted_data)


# Cool, so let's make a 5 node tree
five_tree = make_b_tree(5)
ten_tree = make_b_tree(10)
fifty_tree = make_b_tree(50)


def unpack_tree(node, depth):
    """Return a tuple of the node value and depth.
    
    This function will recursively walk the children as well."""
    if node is None:
        return None

    return [
        (node.value, depth),
        unpack_tree(node.left, depth + 1),
        unpack_tree(node.right, depth + 1),
    ]


def flatten(stuff):
    """Flatten lists of lists."""
    acc = []
    for elem in stuff:
        if isinstance(elem, list):
            for sub_elem in flatten(elem):
                acc.append(sub_elem)
        else:
            acc.append(elem)
    # We could have even deeper, lists, so we call flatten
    # on the accumulator to recurse until we're totally unpacked
    return acc


assert flatten([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
assert flatten([1, [2, 3, 4, 5, 6, 7]]) == [1, 2, 3, 4, 5, 6, 7]
assert flatten([1, [2, [3, [4, 5, 6, 7]]]]) == [1, 2, 3, 4, 5, 6, 7]
assert flatten([1, [2, [3, [4, [5, 6], 7]]]]) == [1, 2, 3, 4, 5, 6, 7]
assert flatten([1, [2, [3, [4, [[5], 6], [7]]]]]) == [1, 2, 3, 4, 5, 6, 7]
assert flatten([1, [2, [3], [4, [[5], 6], [7]]]]) == [1, 2, 3, 4, 5, 6, 7]


# Now let's write a function to turn it into a list of linked lists
def b_tree_to_lls(tree):
    """Convert a binary tree into a list of linked lists."""
    # Note, I'm "Just" going to use regular lists
    # as they are much easier to print and work with
    # I will include the code for linked lists,
    # in the comments

    # I think the best way to unpack is to use the
    # an inOrder traversal that returns the node value and the node depth
    flat_data = unpack_tree(tree, 0)

    # Flatten the nested data structures
    # Filter out the nulls
    data = [x for x in flatten(flat_data) if x]

    # Get the max of indexes
    max_index = max([x[1] for x in data])

    # Hold all this data in a list
    # +1 as range is exclusive, max is inclusive
    holder = [[] for _ in range(max_index + 1)]

    # You could use reduce here as well
    for (value, index) in data:
        holder[index].append(value)

        # If you totally thought linked lists were amazing
        # you could do this
        # change line 184 to:
        #  holder = [None for _ in range(max_index + 1)]
        # Then comment out line 187 and uncomment the next four lines
        # node = holder[index]
        # new_node = LLNode(value)
        # new_node.next = node
        # holder[index] = new_node

    return holder


print(b_tree_to_lls(ten_tree))

