"""Chapter 8: Recursion and Dyanamic Programming. Question 8.6"""

# The glorious towers of Hanoi

# You have 3 towers, N disks the puzzle starts with disks in ascending order
# from top to bottom (each disk sits on a larger one)
# Only one disk can be moved at a time
# A disk is slid off the top of one tower onto another
# a disk cannot be placed on a smaller disk
# Move the tower from the first to the last

from collections import deque


def one_step(s1, s2, s3, _from, _to):
    """Take one step from to using."""
    print(f"Moving from {_from} to {_to}")
    if _from == 1:
        if not s1:
            return
        elem = s1.pop()
    elif _from == 2:
        if not s2:
            return
        elem = s2.pop()
    elif _from == 3:
        if not s3:
            return
        elem = s3.pop()

    if _to == 1:
        s1.append(elem)
    elif _to == 2:
        s2.append(elem)
    elif _to == 3:
        s3.append(elem)

    print_all(s1, s2, s3)


def print_all(s1, s2, s3):
    """Convenience funciton to print all."""
    print("     ==========")
    print(f"s1 is {s1}")
    print(f"s2 is {s2}")
    print(f"s3 is {s3}")


def toh(s1, s2, s3, depth, _from, _to, _using):
    """Brain hurt so bad."""
    print(f"depth is {depth}")
    print_all(s1, s2, s3)
    if depth == 0:
        return

    toh(s1, s2, s3, depth - 1, _from, _using, _to)
    one_step(s1, s2, s3, _from, _to)
    toh(s1, s2, s3, depth - 1, _using, _to, _from)


def towers(s1, s2, s3):
    """Assumes you want to move stack 1 to stack 3."""
    # while s1 has values
    # Get the depth of s1
    s1_depth = len(s1)
    toh(s1, s2, s3, s1_depth, 1, 3, 2)

    print_all(s1, s2, s3)


s1 = deque()
s2 = deque()
s3 = deque()

data = [1, 2, 3]

# Add out numbers to s1
for elem in data:
    s1.appendleft(elem)

towers(s1, s2, s3)
