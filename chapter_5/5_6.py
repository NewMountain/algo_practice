"""Chapter 5: Bit manipulation. Question 5.6"""


def make_bitstring(num):
    """Convert int to string bits."""
    return bin(num)[2:]


def count_diff_bits(n1, n2):
    """Count the number of bits needed to flip to convert n1 to n2."""
    diff = n1 ^ n2
    bit_diff = make_bitstring(diff)
    return len([b for b in bit_diff if b == "1"])


count_diff_bits(0b11101, 0b01111) == 2
