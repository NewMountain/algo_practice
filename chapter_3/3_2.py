"""Chapter 3: Stacks and Queues. Question 3.2"""

from collections import deque
import math


class Stack:
    """Implement a Stack (LIFO) in Python."""

    def __init__(self):
        # Recursion is it's own reward
        self.contents = deque()
        self.running_min = deque()

    def __repr__(self):
        return f"\n\ncontents: {self.contents}\nrunning_min: {self.running_min}"

    def push(self, value):
        """Push onto the stack."""

        # First peek into the running min deque
        running_min = self.min()

        if value <= running_min:
            # Put the new running min on the stack if it's the lte
            self.running_min.append(value)

        # Then add the value to the contents
        self.contents.append(value)

        print(self)

    def pop(self):
        """Pop value off the stack."""
        # First pop the value off the stack
        value = self.contents.pop()
        # Next, pop the min off the stack
        running_min = self.running_min.pop()

        # If the value does not equal the running min
        if value != running_min:
            # Put the running_min back on the running_min stack
            self.running_min.append(running_min)

        print(self)

        # If the running_min equals the value,
        # do not re-append the running_min
        return value

    def min(self):
        """Get the minimum value of the stack."""
        # This is basically a .peek() on the self.running_min
        try:
            running_min = self.running_min.pop()
            # First, put the value back on the stack
            # The same as .peek()
            self.running_min.append(running_min)
        except IndexError:
            running_min = math.inf

        return running_min


s = Stack()

print("Stack created")
print(s)

s.push(3)

s.push(5)

print(s.min())

s.push(1)

print(s.min())

s.push(7)

print(s.pop())

print(s.min())


print(s.pop())

print(s.min())
