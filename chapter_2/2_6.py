from linked_list import LinkedList, Node
import math

test_1 = [c for c in "hannah"]
test_2 = [c for c in "hanah"]
test_3 = [c for c in "tacocat"]
test_4 = [c for c in "nope"]


# Create a linked list
# Note the order is reversed
t1 = LinkedList()
t2 = LinkedList()
t3 = LinkedList()
t4 = LinkedList()

# Load all the data into the linked lists
pairs = [(t1, test_1), (t2, test_2), (t3, test_3), (t4, test_4)]

for (ll, test) in pairs:
    for elem in test:
        ll.insert(elem)


# Define a runner function
def runner(node, steps_desired, current_step):
    """Function to walk steps desired from a node.

    It will return the current step and the node.
    This is useful in case it hits the last element of the list.
    """
    # Set steps taken to zero
    steps_taken = 0

    while steps_taken < steps_desired:
        if node.next is not None:
            node = node.next
            steps_taken += 1
            current_step += 1
        else:
            break

    return (node, current_step)


# Test node
test_node = t1.head

# Sanity checks on runner
assert runner(test_node, 0, 0)[0].data == "h"
assert runner(test_node, 1, 0)[0].data == "a"
assert runner(test_node, 2, 0)[0].data == "n"
assert runner(test_node, 3, 0)[0].data == "n"
assert runner(test_node, 4, 0)[0].data == "a"
assert runner(test_node, 5, 0)[0].data == "h"
# Check out of bounds handling, asked for 20 steps, but
# returned the last node at index 5
assert runner(test_node, 20, 0)[1] == 5


def palindrome_1(linked_list):
    """Given a linked list, return if palindrome."""
    # It seems like the book really promotes the runner method
    # I'm not sure this would be my default
    # as it feels a little clunky, but it makes
    # sense if the list is huge
    # So why not
    slow_prior_index = None
    slow_prior_node = None
    fast_prior_index = None
    fast_prior_node = None

    slow_new_index = 1
    slow_new_node = linked_list.head
    fast_new_index = 1
    fast_new_node = linked_list.head

    # As we walk the list, the slow walked will accumulate elements
    acc = []

    # Use our runner to detect when we have reached the end of the list
    while fast_prior_index != fast_new_index:
        # Set the previous to the current
        (slow_prior_node, slow_prior_index) = (slow_new_node, slow_new_index)
        (fast_prior_node, fast_prior_index) = (fast_new_node, fast_new_index)
        # Then take the step
        (slow_new_node, slow_new_index) = runner(slow_new_node, 1, slow_new_index)
        (fast_new_node, fast_new_index) = runner(fast_new_node, 2, fast_new_index)
        # Accumulate items from the slow node
        acc.append(slow_prior_node.data)

    # The end of this loop is when the fast index finds the end of the list
    list_len = fast_prior_index

    # Find where the slow walker is
    current_index = slow_prior_index

    # Find the half of the palindrome which should always be to rounded
    # up half length of the list
    desired_accumulator_length = math.ceil(list_len / 2)

    # Just check to make sure we have enough elements
    if len(acc) == desired_accumulator_length:
        pass
    elif len(acc) > desired_accumulator_length:
        acc = acc[:desired_accumulator_length]
    # We shouldn't ever have an instance where we haven't grabbed at least enough elements
    else:
        raise Exception("Unexpected list encountered")

    # Now create a second accumulator
    acc_2 = []
    acc_2.append(slow_prior_node.data)

    while slow_prior_node.next is not None:
        slow_prior_node = slow_prior_node.next
        acc_2.append(slow_prior_node.data)

    # Now we just see if accumulator is equal to itself
    return acc == list(reversed(acc_2))


assert palindrome_1(t1)
assert palindrome_1(t2)
assert palindrome_1(t3)
assert not palindrome_1(t4)

# That seems really convoluted
# Let's make this better
def palindrome_2(linked_list):
    """Return if a linked list is a palindrome."""
    # We dont' really need runners are we're just putting
    # all contents into a list anyway
    # Let's just put it into list which is a much easier structure anyway
    # and comparse if the reverse is equal to the accumulator
    acc = []

    node = linked_list.head

    while node is not None:
        acc.append(node.data)
        node = node.next

    return acc == list(reversed(acc))


assert palindrome_2(t1)
assert palindrome_2(t2)
assert palindrome_2(t3)
assert not palindrome_2(t4)
