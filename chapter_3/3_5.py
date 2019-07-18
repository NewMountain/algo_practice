"""Chapter 3: Stacks and Queues. Question 3.5"""

# Question: Write a program to sort a stack such that the smallest items
# are on top. You can use another temporary stack, but not copy data
# to any other data structure.

# The Stack supports push, pop, peek and isEmpty

from collections import deque

# Let's define a stack object
class Stack:
    """LIFO stack."""

    def __init__(self):
        """Init."""
        self.contents = deque()
        self.depth = 0

    def __repr__(self):
        """Print function."""
        return f"contents:\n{self.contents}"

    def push(self, value):
        """Push an element onto the stack."""
        if value is None:
            raise Exception("Null value not allowed")

        self.contents.append(value)

    def pop(self):
        """Pop the last element off the stack."""
        if self.is_empty():
            return None

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
