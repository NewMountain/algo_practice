"""Chapter 2: Linked Lists. Question 2.1"""

from linked_list import LinkedList

test_data = [1, 2, 2, 2, 4, 5, 6, 1, 8, 9, 0, 1, 2, 13, 15]

# Create a linked list
test_ll_1 = LinkedList()
test_ll_2 = LinkedList()

# put the test_data into the linked list
for elem in test_data:
    test_ll_1.insert(elem)
    test_ll_2.insert(elem)

print(test_ll_1)

# Write code to remove duplicates from an unsorted linked list.
# O(N) time and O(N) space
def dedupe(linked_list):
    """Return a deduped linked list."""
    # Create a dict of all seen values
    seen = {}

    # First check if the linked_list is empty
    if linked_list.head is None:
        return linked_list

    # Set head to current node
    node = linked_list.head
    # Set last distinct node to none and walk
    last_distinct_node = None
    # and start walking
    while node.next is not None:
        # Put the node data into seen
        if node.data in seen:
            # Step to the next node
            node = node.next
        else:
            # Put the new data into seen
            seen[node.data] = 0
            # Link the last distinct node to this one
            if last_distinct_node is not None:
                last_distinct_node.next = node

            # Mark this step as the last_distinct_node
            last_distinct_node = node
            # Step to the next node
            node = node.next

    # Now attach a next of none to the last seen node
    last_distinct_node.next = None

    return linked_list


output_ll = dedupe(test_ll_1)

print(output_ll)


def value_ahead(value, node):
    """Return True if the value is the last of its kind."""
    while node.next is not None:
        # If you find the value
        if node.data == value:
            return True
        else:
            node = node.next

    # Deal with fencepost of last node
    if node.data == value:
        return True

    # If you haven't found it by the end, return False
    return False


# O(N^2) time but O(1) space
def dedupe_2(linked_list):
    """Return a deduped linked list."""
    # First check if the linked_list is empty
    if linked_list.head is None:
        return linked_list

    # Set head to current node
    node = linked_list.head
    # Set last distinct node to none and walk
    last_distinct_node = None
    # and start walking
    while node.next is not None:
        if last_distinct_node is None:
            # Set this node to the last distinct node
            # The first must be unique
            # Assumes all nodes have a non null value
            last_distinct_node = node
            # Step forward
            node = node.next
        else:
            # Get the value of the current node
            value = node.data
            # This value is the last of its kind
            if not value_ahead(value, node.next):
                # This value is the last of it's kind, link it
                last_distinct_node.next = node
                # Mark this step as the last_distinct_node
                last_distinct_node = node
                # Step to next node
                node = node.next
            else:
                # Simply skip forward to the next node, we will build our distinct
                # list from the last known instance of a value
                node = node.next

    # By this definition the last value is distinct
    last_distinct_node.next = node
    return linked_list


output_ll_2 = dedupe_2(test_ll_2)

print(output_ll_2)
