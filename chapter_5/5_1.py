"""Chapter 5: Bit manipulation. Question 5.1"""

# You are given two 32 bit numbers, m and n
# and a position i and j
# Insert number M into n at index i to j


def bitstring(n):
    """Python stores bits as ints, so return the bitstring."""
    # Chop off the prefix python gives it
    return bin(n)[2:]


# Working with bits in python is fairly annoying
# in that the datatype is a little awkward
def insert_bits(n, m, i, j):
    """Insert m into n using i j indexes."""
    # one thing that's a little weird, indexes are base 1
    # the bit strings are base 0
    real_j = j + 1
    # We don't really need i, as the problem
    # states length equals index
    # Instead we focus on making sure
    # we add enough zeroes such and len(m) == real_j
    bits_to_add = real_j - len(bitstring(m))

    # Now we add the bits to m
    new_m = m << bits_to_add

    new_num = n + new_m

    return bitstring(new_num)


assert insert_bits(0b10000000000, 0b10011, 2, 6) == "10001001100"

