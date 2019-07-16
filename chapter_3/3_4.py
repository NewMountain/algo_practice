"""Chapter 3: Stacks and Queues. Question 3.4"""

# Implement a MyQueue class which implements a queue using two stacks.

from collections import deque


class Stack:
    """LIFO stack."""

    def __init__(self):
        """Initialize."""
        self.contents = deque()
        self.depth = 0

    def __repr__(self):
        """Print yourself."""
        return f"{self.contents}"

    def push(self, value):
        """Push a value onto the stack."""
        if value is None:
            raise Exception("Null values not allowed")

        self.depth += 1
        return self.contents.append(value)

    def pop(self):
        """Pop a value off the stack."""
        if self.depth == 0:
            return None

        # Otherwise decrement and return the pop
        self.depth -= 1
        return self.contents.pop()

    def flush(self):
        """Flush all elements from the Stack in LIFO order."""
        # Reverse the contents as the iterator is FIFO by default
        flush_result = [elem for elem in reversed(self.contents)]
        # Clear the cache
        self.contents.clear()
        self.depth = 0

        return flush_result

    def get_depth(self):
        """Return the depth of the Stack."""
        return self.depth


class MyQueue:
    """FIFO queue implemented using two stacks."""

    def __init__(self):
        """Intialize with two empty stacks."""
        self.incoming = Stack()
        self.outgoing = Stack()

    def __repr__(self):
        return f"\nIncoming:\n{self.incoming}\nOutgoing:\n{self.outgoing}\n"

    def push(self, value):
        """Push a value onto the queue."""
        self.incoming.push(value)

    def pop(self):
        """Pop a value off the queue."""
        # If there are no items in incoming or outgoing
        if self.incoming.get_depth() == 0 and self.outgoing.get_depth() == 0:
            return None

        # If there are not elements in outgoing, flush incoming
        if self.outgoing.get_depth() == 0:
            # Flush incoming and push them to outgoing
            [self.outgoing.push(x) for x in self.incoming.flush()]

        return self.outgoing.pop()


q = MyQueue()

print(q)

q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)

print(q)

print(q.pop())

print(q)

q.push(6)
q.push(7)
q.push(8)

print(q.pop())
print(q.pop())
print(q.pop())

print(q)

print(q.pop())

print(q)

print(q.pop())

print(q)
