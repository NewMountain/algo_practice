"""Chapter 3: Trees and Graphs. Question 4.1"""

from collections import deque
import random
import time

# Helper function as the deque doesn't have an empty() method
def is_empty(deck):
    """Helper function to see if deque is empty."""
    try:
        # Pop an element off the stack and put it back in
        # If there's an element to pop, return False (not empty)
        value = deck.pop()
        deck.append(value)
        return False
    except IndexError:
        # Deque throws a runtime error if you .pop()
        # from an empty collection
        return True


# Given a directed Graph between two nodes, design an algorithm to
# Find out if there is a route from node a to node b
def does_path_exist(node_1, node_2, graph):
    """Given a graph, determine if you can get from node_1 to node_2."""
    print(f"Start at {node_1}")
    print(f"Hope to end at {node_2}")
    # We two collections, the first, a queue to determine where to go next
    # (This will be a breadth first search)
    nodes_to_visit = deque()
    # Let's also create a set for nodes_visited
    # so we don't get trapped in loops
    nodes_visited = set()

    # First put node_1 in the nodes_to_visit then let the algo
    # do it's magic
    nodes_to_visit.appendleft(node_1)

    # Edge case, node_1 == node_2
    if node_1 == node_2:
        print(f"{node_1} is {node_2}!")
        return True

    while not is_empty(nodes_to_visit):
        # Get the node to visit
        node = nodes_to_visit.pop()
        # Check to see if we have been to this node before
        if node not in nodes_visited:
            # See what nodes this node links to
            next_to_visit = graph[node]
            # Mark this node as visited
            nodes_visited.add(node)
            # See if node_2 is in the next_to_visit
            if node_2 in next_to_visit:
                print(f"Solution found for {node_1} to {node_2}!")
                return True
            else:
                # Add those nodes to the nodes to visit
                for next_node in next_to_visit:
                    nodes_to_visit.appendleft(next_node)

    # If we have walked and didn't find anything, return False
    print(f"No way to get from {node_1} to {node_2}!")
    return False


def game():
    """Let's play a game for fun."""
    # Key is the node, and the value is a list of nodes
    # The graph goes to
    # No real reason for this graph, I just made it up
    # The idea here is most, but not all, letters should be able to get to another
    graph = {
        "a": ["b", "c"],
        "b": ["c", "a", "d"],
        "c": ["a", "b", "z"],
        "d": ["z", "e", "f"],
        "e": ["a"],
        "f": ["q"],
        "g": [],
        "h": ["a"],
        "i": ["q"],
        "j": ["z"],
        "k": ["b"],
        "l": ["k", "n", "o", "q"],
        "m": ["a"],
        "n": [],
        "o": ["b", "z"],
        "p": ["c", "d"],
        "q": ["e", "z"],
        "r": ["f"],
        "s": [],
        "t": ["g"],
        "u": ["h", "i", "j", "k", "l"],
        "v": ["a", "w"],
        "w": ["z", "x"],
        "x": ["l", "u"],
        "y": [],
        "z": ["a", "b", "c", "d", "l", "u"],
    }

    # For fun, let's pick a start and end node at random
    # We know all nodes are in the keys
    nodes = list(graph.keys())

    # Let's just brute force all from two points for lulz
    results = []
    for a in nodes:
        for b in nodes:
            results.append((f"{a} -> {b}", does_path_exist(a, b, graph)))

    # Pick a start and end node at random."""
    # start_node = random.choice(nodes)
    # end_node = random.choice(nodes)

    # does_path_exist(start_node, end_node, graph)

    # print("\n\nFINAL RESULTS!!!\n\n")
    # print(results)


game()
