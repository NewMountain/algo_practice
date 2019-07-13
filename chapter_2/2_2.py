"""Chapter 2: Linked Lists. Question 2.2"""

# Return the kth to last element of a singly linked list

from linked_list import LinkedList

test_data = [1, 2, 2, 2, 4, 5, 6, 1, 8, 9, 0, 1, 2, 13, 15]

# Create a linked list
# Note the order is reversed
test_ll_1 = LinkedList()
test_ll_2 = LinkedList()

# put the test_data into the linked list
for elem in test_data:
    test_ll_1.insert(elem)
    test_ll_2.insert(elem)

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


# Now suppose we wanted to do this with a single pass using a runner


def runner(node, steps_desired, current_step):
    """Walk from the node n steps desired.

    If the end is found before walking the desired amount
    of steps, return the last node and its current step.
    """
    steps_taken = 0

    while steps_taken < steps_desired:
        if node.next is not None:
            node = node.next
            steps_taken += 1
            current_step += 1
        else:
            break

    return (node, current_step)


def return_k_2(linked_list, k):
    """Same as before except one pass using runner technique."""
    prior_slow = None
    prior_fast = None
    prior_node_slow = None
    prior_node_fast = None

    current_slow = 0
    current_fast = 0
    current_node_slow = linked_list.head
    current_node_fast = linked_list.head

    # Basically until the fast walker hits the end of the list
    while prior_fast != current_fast:
        # Set the priors to current
        (prior_node_slow, prior_slow) = (current_node_slow, current_slow)
        (prior_node_fast, prior_fast) = (current_node_fast, current_fast)
        # Then reset the current to walk forwardd
        (current_node_slow, current_slow) = runner(current_node_slow, 1, current_slow)
        (current_node_fast, current_fast) = runner(current_node_fast, 2, current_fast)

    # Now we have walked until the "fast" runner hit the end of the list
    # The prior values are the last values before we repeated the end of the list
    last_element = prior_fast

    # Figure out how many more elements the slow walker needs to step to get
    # to the desired node
    desired_node_index = last_element - k
    # Calculate the amount of steps required to get there
    steps_required = desired_node_index - prior_slow

    # print(
    #     f"We desired node {desired_node_index} and must take {steps_required} more steps to get there."
    # )

    desired_node, _whatever = runner(prior_node_slow, steps_required, prior_slow)

    return desired_node.data


assert return_k_2(test_ll_2, 0) == 1
assert return_k_2(test_ll_2, 1) == 2
assert return_k_2(test_ll_2, 2) == 2
assert return_k_2(test_ll_2, 3) == 2
assert return_k_2(test_ll_2, 4) == 4
assert return_k_2(test_ll_2, 5) == 5
