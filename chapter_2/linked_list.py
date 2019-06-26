"""Implement a linked_List and Node data structure."""
import json


class Node:
    """Implement a node object in a linked list."""

    def __init__(self, value):
        """Initialize yourself."""
        self.data = value
        self.next = None

    def __repr__(self):
        """Print yourself."""
        representation = {"data": self.data, "next": self.next}
        return f" 'data': {self.data}, 'next': {self.next.data} "

    def append(self, node):
        """Append a node onto yourself."""
        self.next = node


class LinkedList:
    """Implement a linked list."""

    def __init__(self):
        """Initialize yourself."""
        self.head = None

    def __repr__(self):
        """Print yourself."""
        representation = []
        # I am aware of the danger here, this is toy code only
        node = self.head
        while True:
            representation.append(node.data)
            if node.next is not None:
                node = node.next
            # Otherwise break
            else:
                break

        return " -> ".join([str(x) for x in representation])

    def insert(self, value):
        """Insert a new node at the head of the list."""
        # Create a new node
        new_node = Node(value)
        # Append the prior head onto the new node
        new_node.append(self.head)
        # Set the new node as head
        self.head = new_node

