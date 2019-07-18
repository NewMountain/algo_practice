"""Chapter 3: Stacks and Queues. Question 3.5"""

# Question: Write a program to sort a stack such that the smallest items
# are on top. You can use another temporary stack, but not copy data
# to any other data structure.

# The Stack supports push, pop, peek and isEmpty

from collections import deque
import time

# Let's define a stack object
class Stack:
    """LIFO stack."""

    def __init__(self):
        """Init."""
        self.contents = deque()
        self.depth = 0

    def __repr__(self):
        """Print function."""
        return f"\ncontents:\n{self.contents}"

    def push(self, value):
        """Push an element onto the stack."""
        if value is None:
            raise Exception("Null value not allowed")

        self.depth += 1
        self.contents.append(value)

    def pop(self):
        """Pop the last element off the stack."""
        if self.is_empty():
            return None

        self.depth -= 1
        return self.contents.pop()

    def peek(self):
        """Look at the next element without altering stack."""
        if self.is_empty():
            return None

        # Otherwise, return the peek
        value = self.contents.pop()
        self.contents.append(value)
        return value

    def is_empty(self):
        """Return true is empty."""
        return self.depth == 0


# Create a stack
s = Stack()

data = [8, 6, 7, 5, 3, 0, 9]
# data = [2, 1, 3]

# Reverse to maintain order in stack.
for d in reversed(data):
    s.push(d)


def sort_stack(stack):
    """Sort a stack using only another temp stack.
    
    This is basically just a bubble sort with stacks."""
    temp_stack = Stack()
    # Pull a number off stack
    # Peek at temp stack
    while stack.peek() is not None:
        element = stack.pop()
        # If temp stack is empty, put the number on temp stack
        if temp_stack.peek() is None:
            temp_stack.push(element)

        else:
            # if the element is gte, put it down in temp_stack.
            temp_value = temp_stack.peek()
            if element >= temp_value:
                temp_stack.push(element)

            else:
                # if it's lt, pop it off and push it on stack
                # Then push the temp value onto the stack
                temp_value = temp_stack.pop()
                # Basically you flip the order of the elements in the stack
                stack.push(temp_value)
                stack.push(element)

    # Now just unpack the results
    acc = []
    while not temp_stack.is_empty():
        elem = temp_stack.pop()
        acc.append(elem)

    return acc


assert sort_stack(s) == [9, 8, 7, 6, 5, 3, 0]
