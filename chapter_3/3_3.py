"""Chapter 3: Stacks and Queues. Question 3.3"""

# Stack of plates: If a stack gets too high, create a new stack

from collections import deque


class Stack:
    """LIFO Stack NULL values not allowed."""

    def __init__(self):
        """Initialize."""
        self.data = deque()
        self.length = 0

    def __repr__(self):
        """How to print the class."""
        return f"{self.data}"

    def pop(self):
        """Pop an element off the stack."""
        if self.not_empty():
            self.length -= 1
            return self.data.pop()

        # Otherwise, return None
        return None

    def push(self, value):
        """Push an element onto the stack."""
        if value is None:
            raise Exception("Must supply a non null value.")

        self.length += 1
        self.data.append(value)

    def peek(self):
        """Look at an item on the stack."""
        if self.not_empty():
            return None

        # Otherwise, peek, by popping off and putting back and returning the value
        value = self.data.pop()
        self.data.append(value)

        return value

    def not_empty(self):
        """Return if the stack is empty."""
        return self.length != 0

    def depth(self):
        """Return the depth of the stack."""
        return self.length


class SetOfStacks:
    """A datatype that only allows Stacks to get n deep."""

    def __init__(self, max_depth):
        """Initalize a set of stacks with a user defined max depth."""
        self.max_depth = max_depth
        # Create a list of stack with a first stack
        self.stacks = [Stack()]

    def __repr__(self):
        """How the class should print."""
        return f"{self.stacks}"

    def push(self, value):
        """Push the latest element off the setofstacks."""
        # Do not allow Null elements
        if value is None:
            raise Exception("Null elements not allowed.")

        # Get the latest stack
        stack = self.stacks[-1]
        # If the stack isn't full push value
        if stack.depth() < self.max_depth:
            return stack.push(value)

        # Otherwise, create a new stack
        new_stack = Stack()
        # Push the value
        new_stack.push(value)
        # Add append the new_stack
        self.stacks.append(new_stack)

    def pop(self):
        """Pop the latest element off the setOfStacks."""
        # Get the latest stack
        stack = self.stacks[-1]

        if stack.depth() > 0:
            return stack.pop()
        # If we have a prior stack, to use
        elif stack.depth() == 0 and len(self.stacks) > 1:
            # Use the second to last stack
            stack = self.stacks[-2]
            # Delete the last stack
            self.stacks.pop()
        else:
            # No elements left in the final stack, return Null
            return None


ss = SetOfStacks(5)

print(ss)

ss.push(1)
ss.push(2)
ss.push(3)

print(ss)

ss.push(4)
ss.push(5)
ss.push(6)
ss.push(7)

print(ss)

ss.pop()
print(ss)
ss.pop()
print(ss)
ss.pop()
print(ss)
ss.pop()
print(ss)
ss.pop()
print(ss)
ss.pop()
print(ss)
ss.pop()
print(ss)
ss.pop()
print(ss)
ss.pop()
print(ss)
ss.pop()
print(ss)
ss.pop()
print(ss)
