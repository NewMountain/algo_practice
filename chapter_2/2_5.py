"""Chapter 2: Linked Lists. Question 2.4"""

from linked_list import LinkedList, Node

test_number_1 = [8, 6, 7, 5, 3, 0, 9]
test_number_2 = [1, 3, 3, 7]

# Making them a linked list will reverse them
# Thus everything seems backwards
answer = [6, 4, 6, 6, 7, 6, 8]
reverse_answer = reversed(answer)

# Create a linked list
# Note the order is reversed
number_1 = LinkedList()
number_2 = LinkedList()
number_3 = LinkedList()
number_4 = LinkedList()

reverse_answer_ll = LinkedList()
answer_ll = LinkedList()

# put the test_data into the linked list
for elem in test_number_1:
    number_1.insert(elem)

for elem in test_number_2:
    number_2.insert(elem)

for elem in reversed(test_number_1):
    number_3.insert(elem)

for elem in reversed(test_number_2):
    number_4.insert(elem)

# Make the answers into linked lists for testing
for elem in reverse_answer:
    reverse_answer_ll.insert(elem)

# Make the answers into linked lists for testing
for elem in answer:
    answer_ll.insert(elem)


def safe_get_value(node):
    """Safe get operation."""
    if node is not None:
        return node.data

    # If the Node is null, just return 0
    return 0


def safe_get_next(node):
    """Safe get next node operation."""
    if node is not None:
        if node.next is not None:
            return node.next

    # In all other cases, just return null
    return None


# Given two numbers as a linked list, sum them in reverse order
# IE 617 + 295 = 912 => 7->1->6 + 5->9->2 = 2 -> 1 -> 9
def reverse_add(number_1, number_2):
    """Add two numbers in reverse order."""
    # In the case of reverse numbers, we don't need to worry if the
    # length of the numbers matches.
    # Create a linked list
    sum_list = LinkedList()

    carryover = 0
    last_node = None
    first_node = None

    l1_node = number_1.head
    l2_node = number_2.head

    # Keep iterating as long as there are nodes in either list
    while l1_node is not None or l2_node is not None:
        l1_value = safe_get_value(l1_node)
        l2_value = safe_get_value(l2_node)

        # Sum the two values and the carryover
        sum_value = l1_value + l2_value + carryover
        # Take the modulo 10 number and assign it to digit
        digit = sum_value % 10
        # Flat divide by ten and assign that to carryover
        carryover = sum_value // 10

        # Now assign the digit to the linked list
        # Note we're not inserting as we want to maintain order
        if last_node is None:
            # Create a new node
            new_node = Node(digit)
            # Make the new node the last node
            last_node = new_node
            # Also make the new node the first node
            first_node = new_node
        else:
            # Create a new node
            new_node = Node(digit)
            # Link it after current last node
            last_node.next = new_node
            # set new node to last node
            last_node = new_node

        # Make one step in each list
        l1_node = safe_get_next(l1_node)
        l2_node = safe_get_next(l2_node)

    # Set the head of the linked list to the first_node
    sum_list.head = first_node

    return sum_list


def get_len(ll):
    """Return the length of a linked list."""
    length = 0

    if ll.head is None:
        return length

    # Otherwise, there is at least one element
    length = 1
    current_node = ll.head

    while current_node.next is not None:
        current_node = current_node.next
        length += 1

    return length


# Sanity check
assert get_len(number_4) == 4


def prepend(ll, zeroes_required):
    """Prepend 0 nodes to the linked list."""
    # Get the head node
    head_node = ll.head

    for _ in range(zeroes_required):
        # Create a new 0 node
        new_node = Node(0)
        # Make the next of this new node the head
        new_node.next = head_node
        # Make this new node the head node
        head_node = new_node

    # Assign the last head_node to the ll.head
    ll.head = head_node

    return ll


# Recursion is its own reward
# Take two nodes, return a tuple of the result and its carryover
def add_numbers(node_1, node_2):
    """Recursive math is delightful."""
    # First, get the next nodes for node_1 and node_2
    if node_1 is not None:
        next_1 = node_1.next
        next_2 = node_2.next

        # Computer the value for the next step to build up
        result_node, carryover = add_numbers(next_1, next_2)

        # Sum the two values and the carryover
        sum_value = node_1.data + node_2.data + carryover
        # Take the modulo 10 number and assign it to digit
        digit = sum_value % 10
        # Flat divide by ten and assign that to carryover
        carryover = sum_value // 10

        # Create our new node with the digit
        new_node = Node(digit)
        # Assign the result of the next step as the next node
        new_node.next = result_node

        return (new_node, carryover)

    # End of the list, recursion stops
    else:
        return (None, 0)


# Given two numbers as a linked list, sum them in reverse order
# IE 617 + 295 = 912 => 6->1->7 + 2->9->5  = 9 -> 1 -> 2
def add(number_1, number_2):
    """Add two linked lists in the "right" order."""
    # Create a linked list
    sum_list = LinkedList()

    # First find the length of the two linked lists
    len_ll_1 = get_len(number_1)
    len_ll_2 = get_len(number_2)

    # Find the max of the two lengths
    max_len = max(len_ll_1, len_ll_2)

    if len_ll_1 == len_ll_2:
        pass
    elif len_ll_1 == max_len:
        # Add leading zeroes to len_ll_2
        number_2 = prepend(number_2, max_len - len_ll_2)
    elif len_ll_2 == max_len:
        # Add leading zeroes to len_ll_2
        number_1 = prepend(number_1, max_len - len_ll_1)

    head_1 = number_1.head
    head_2 = number_2.head
    # We know both numbers are the same length
    node, carryover = add_numbers(head_1, head_2)

    if carryover != 0:
        # Create a carryover in case there is one
        new_node = Node(carryover)
        # append node to new_node
        new_node.next = node
        # make the new node the head
        sum_list.head = new_node
    else:
        sum_list.head = node

    return sum_list


# Comparing strings as they are different pointers
assert reverse_add(number_1, number_2).__repr__() == reverse_answer_ll.__repr__()
assert add(number_3, number_4).__repr__() == answer_ll.__repr__()
