"""Chapter 2: Linked Lists. Question 2.2"""

# Given some element in the middle of the linked list,
# return the linked list with that element removed

from linked_list import LinkedList

test_data = [5, 4, 3, 2, 1]

# Create a linked list
# Note the order is reversed
test_ll_1 = LinkedList()

# put the test_data into the linked list
for elem in test_data:
    test_ll_1.insert(elem)


def remove_elem(node):
    """Given some node, remove it from the linked list."""
    # We just take the given element, and reassign it to it's next
    node.data = node.next.data
    node.next = node.next.next
    return node


def step(node, step):
    """Walk forward from node n steps."""
    # Set the current node
    current_node = node

    for i in range(step):
        if current_node.next is not None:
            current_node = current_node.next

    return current_node


# Get a node two steps from the head
# IE element 3
middle_node = step(test_ll_1.head, 2)

print(middle_node)

# Print list before
print(test_ll_1)
# Remove element 3
remove_elem(middle_node)
# Print list after
print(test_ll_1)
