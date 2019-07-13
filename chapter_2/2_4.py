"""Chapter 2: Linked Lists. Question 2.4"""

from linked_list import LinkedList

test_data = [1, 2, 2, 2, 4, 5, 6, 1, 8, 9, 0, 1, 2, 13, 15]

# Create a linked list
# Note the order is reversed
test_ll_1 = LinkedList()

# put the test_data into the linked list
for elem in test_data:
    test_ll_1.insert(elem)


def get_last_node(linked_list):
    """Return the last element in a linked list."""
    current_node = linked_list.head

    # Walk to the next node until there isn't
    # another node to walk to
    while current_node.next is not None:
        current_node = current_node.next

    print(current_node)
    return current_node


# Write code to partition a linked list around a value x
# This is O(N) time and O(1) space
def partition(linked_List, value):
    """Given a value, partition a list by that node."""
    print(linked_List)
    # Create a linked list for all elements less than value
    lt_partition = LinkedList()
    # Create a linked list for all elements greater than
    # or equal to value
    gte_partition = LinkedList()

    # Now walk the linked list
    if linked_List.head is not None:
        current_node = linked_List.head

    while current_node is not None:
        if current_node.data < value:
            lt_partition.insert(current_node.data)
        else:
            gte_partition.insert(current_node.data)

        # Step to the next node
        current_node = current_node.next

    # Now we need to link the last element of lt_partition to the head
    # of gte_partition
    last_lt_elem = get_last_node(lt_partition)

    # Now we set the last element.next to the head of the gre partition
    last_lt_elem.next = gte_partition.head

    # Now return the lt_partition which now is linked includes both partitions
    return lt_partition


print(partition(test_ll_1, 6))
