"""Chapter 2: Linked Lists. Question 2.2"""

# Return the kth to last element of a singly linked list

from linked_list import LinkedList

test_data = [1, 2, 2, 2, 4, 5, 6, 1, 8, 9, 0, 1, 2, 13, 15]

# Create a linked list
# Note the order is reversed
test_ll_1 = LinkedList()

# put the test_data into the linked list
for elem in test_data:
    test_ll_1.insert(elem)

# First version, super simple, walk the list, get the length, then
# walk a second time and grab the len() - k element
# This is O(1) space and O(N) time
def return_k_1(list, k):
    """Return the kth to last element in linked list."""
    # Check if empty
    if list.head is None:
        raise Exception("Linked list is empty")

    # Otherwise walk the nodes
    node = list.head
    # List must be at least one element long
    count = 1

    while node.next is not None:
        # Iterate counter
        count += 1
        # Walk to next node
        node = node.next

    # Check to make sure kth element isn't out of index
    if k > count:
        raise Exception(f"Element {k} out of bounds of linked list.")

    # Otherwise walk the list again
    node = list.head

    # Set the element index
    element_index = count - k

    # Fencepost issue again as we know we are already at the first
    # element
    for _ in range(1, element_index):
        node = node.next

    return node.data


assert return_k_1(test_ll_1, 0) == 1
assert return_k_1(test_ll_1, 1) == 2
assert return_k_1(test_ll_1, 2) == 2
assert return_k_1(test_ll_1, 3) == 2
assert return_k_1(test_ll_1, 4) == 4
assert return_k_1(test_ll_1, 5) == 5


def step(node, step):
    """Walk forward from node n steps."""
    # Set the current node
    current_node = node

    for i in range(step):
        if current_node.next is not None:
            current_node = current_node.next

    return current_node

