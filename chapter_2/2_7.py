"""Chapter 2: Linked Lists. Question 2.7"""

from linked_list import LinkedList

# Given two singly linked lists, determine the intersect of the two lists
# Return the intersecting node based on reference

# This example is awkward as an example isn't given and makes a lot
# of assumptions.

# Looking forward, the expectation is two lists are the same

# What isn't clear from this example: do lists intersect partially like
# 1 -> 2 -> 3 -> 4 and
# 2 -> 3

# The example from the book shows only one example in which two lists mirror each other
# from some point until the end of the list
# We'll solve for that here

data_1 = [3, 1, 5, 9, 7, 2, 1]
data_2 = [4, 6, 7, 2, 1]

ll_1 = LinkedList()
ll_2 = LinkedList()

for data, ll in [(data_1, ll_1), (data_2, ll_2)]:
    # for each element, populate its linked list (in reverse order)
    # to maintain order in linked list as seen in data
    for elem in reversed(data):
        ll.insert(elem)


def stepper(node, desired_steps, current_step):
    """Step from a node the desired steps or until the last node."""
    steps_taken = 0
    while steps_taken < desired_steps:
        if node.next is not None:
            steps_taken += 1
            current_step += 1
            node = node.next
        else:
            break

    return (node, current_step)


# Sanity check your work
test_node = ll_1.head

assert stepper(test_node, 0, 0)[0].data == 3
assert stepper(test_node, 1, 0)[0].data == 1
assert stepper(test_node, 2, 0)[0].data == 5
# Gracefully handles out of bounds requests
assert stepper(test_node, 20, 0)[0].data == 1
assert stepper(test_node, 20, 0)[1] == 6


# In normal cases, I would make this a method of a linked list
# This is just to build the familiarity of working with
# linked lists
def get_length(linked_list):
    """Return the length of a linked list."""
    if linked_list.head == None:
        return 0

    # Otherwise, you have at least one element
    count = 1
    node = linked_list.head

    # Walk until the end of the linked list
    while node.next is not None:
        count += 1
        node = node.next

    return count


# Sanity check this code
assert get_length(ll_1) == 7
assert get_length(ll_2) == 5


def detect_insersection(ll_1, ll_2):
    """Detect at which element two linked lists intersect."""
    # Couple of weird assumptions this problem makes:
    # At the point of intersection, both lists intersect until the end
    # Given this, find the length of both lists,
    # and walk both from the kth last element where
    # k is the min length of the two lists
    len_1 = get_length(ll_1)
    len_2 = get_length(ll_2)
    min_len = min(len_1, len_2)

    if len_1 > min_len:
        # First find the offset
        offset = len_1 - min_len
        # Get the head of len_1
        head = ll_1.head
        # Step offset deep into the linked list and return that node
        l1_node, _count = stepper(head, offset, 0)
        # The second node is simply the head of its linked list
        l2_node = ll_2.head
    elif len_2 > min_len:
        # First find the offset
        offset = len_2 - min_len
        # Get the head of len_2
        head = ll_2.head
        # Step offset deep into the linked list and return that node
        l2_node, _count = stepper(head, offset, 0)
        # The second node is simply the head of its linked list
        l1_node = ll_1.head

    # Now walk the lists and look for the intersect
    while l1_node.next is not None:
        if l1_node.data == l2_node.data:
            # We found the intersect node
            break
        else:
            l1_node = l1_node.next
            l2_node = l2_node.next

    return l1_node


# The two lists began at the node with 7
# Note: the original example uses pointers, we are just comparing values
detect_insersection(ll_1, ll_2).data == 7

