"""Chapter 2: Linked Lists. Question 2.8"""

from linked_list import LinkedList, Node

# Given a linked list which might contain a loop implement an algorithm
# that returns the node at the start of the loop, if one exists

# Creating this is going to be a little ugly
# As we're doing this by hand
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

a.next = b
b.next = c
c.next = d
d.next = e
# Our loop is born
e.next = c
# This is our linked list with a loop
ll_1 = LinkedList()
ll_1.head = a

# This is a linked list without a loop
ll_2 = LinkedList()
data_2 = [4, 6, 7, 2, 1]

for elem in reversed(data_2):
    ll_2.insert(elem)


def stepper(node, steps_desired):
    """Try to step n steps, return None if the step is out of bounds."""
    steps_taken = 0

    while steps_taken < steps_desired:
        if node.next is None:
            return None

        node = node.next
        steps_taken += 1

    return node


# Sanity check
test_node = ll_1.head

assert stepper(test_node, 0).data == "a"
assert stepper(test_node, 1).data == "b"
assert stepper(test_node, 2).data == "c"


def detect_loop(linked_list):
    """Detect a loop in a linked list."""
    # Ok, so here we use the fast and slow runner technique
    slow_node = linked_list.head
    fast_node = linked_list.head

    # If fast node makes it to the end without detecting
    # and loop return (False, None)
    # Otherwise, return (True, node)
    while True:
        if fast_node is None or fast_node.next is None:
            # We walked to the end without loop
            return (False, None)

        # Take a fast and slow step and compare
        fast_node = stepper(fast_node, 2)
        slow_node = stepper(slow_node, 1)

        if slow_node == fast_node:
            loop_intersection = fast_node
            break

    # Now we have detected a loop and know where the node is
    # There's some fancy math, but the TL; DR is the start of the loop is
    # the point where the node walking from the start of the linked list
    # and the detected intersect point meet
    start_node = linked_list.head

    while start_node != loop_intersection:
        start_node = stepper(start_node, 1)
        loop_intersection = stepper(loop_intersection, 1)

    # Return either pointer to the element
    return (True, loop_intersection)


# Linked list 1 has a loop
assert detect_loop(ll_1)[0]
# Linked list 2 does not
assert not detect_loop(ll_2)[0]
