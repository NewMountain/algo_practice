"""Chapter 8: Recursion and Dyanamic Programming. Question 8.12"""

# nQueens

# Classic problem: Give an n x n board, how many different configurations
# of n queens can be placed on the board.
from collections import Counter


def flatten(stuff):
    """Flatten list of lists of stuff into a list of stuff."""
    acc = []
    for element in stuff:
        if isinstance(element, list):
            for sub_element in flatten(element):
                acc.append(sub_element)
        else:
            acc.append(element)

    return acc


assert flatten([1, 2, 3]) == [1, 2, 3]
assert flatten([1, [2], [3]]) == [1, 2, 3]
assert flatten([1, [2, [3]]]) == [1, 2, 3]


def perms(stuff):
    """Genernate permutations of stuff."""
    if not stuff:
        return [[]]
    if len(stuff) == 1:
        return [stuff]

    head = stuff[0]
    tail = stuff[1:]

    acc = []
    for i in range(len(stuff)):
        # Weave head between the permutations of tail
        for p in perms(tail):
            new_list = (p[:i] + [head]) + p[i:]
            acc.append(new_list)

    return acc


assert perms([]) == [[]]
assert perms([1]) == [[1]]
assert perms([1, 2]) == [[1, 2], [2, 1]]
assert perms([1, 2, 3]) == [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [3, 1, 2],
    [2, 3, 1],
    [3, 2, 1],
]


def no_diags(board):
    """Test if a board has diagonal moves."""
    # Sum each cell with its index and reverse index
    index = range(len(board))
    # if any sum occcurs more than once, you have a
    # diagonal move
    south_east = [sum(x) for x in zip(board, index)]
    north_east = [sum(x) for x in zip(board, reversed(index))]
    se_count = Counter(south_east).values()
    ne_count = Counter(north_east).values()
    return all([x == 1 for x in (se_count + ne_count)])


assert no_diags([0, 2, 4, 1, 3]) == True
assert no_diags([0, 1, 2]) == False


# Glorious nQueens
def n_queens(n):
    """Return the number of permutations."""
    h_v_boards = perms(range(1, n + 1))
    # Filter the boards with a diagonal move
    return len([1 for b in h_v_boards if no_diags(b)])


n_queens(2) == 0
n_queens(3) == 0
n_queens(4) == 0
n_queens(5) != 0
n_queens(5) == 10
