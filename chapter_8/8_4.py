"""Chapter 8: Recursion and Dyanamic Programming. Question 8.4"""


# Write a method for all subsets of a set

# [Int] -> [[Int]]
def powerset1(stuff):
    """Return all subsets of a set."""
    if not stuff:
        return []

    head = stuff[0]
    tail = stuff[1:]

    tails = [tail] + powerset1(tail)

    acc = []
    for t in tails:
        heady = [head] + t
        if heady not in acc:
            acc.append(heady)
        if t not in acc:
            acc.append(t)

    return acc


print(powerset1([1, 2, 3, 4]))


def bitstring(n, string_len):
    """Python stores bits as ints, so return the bitstring."""
    # Chop off the prefix python gives it
    return bin(n)[2:].zfill(string_len)


def make_combination(number, stuff, string_len):
    """Make a combination from bits."""
    bit_string = bitstring(number, string_len)
    acc = []
    for idx, bit in enumerate(bit_string):
        if bit == "1":
            acc.append(stuff[idx])

    return acc


# This was a super cool trick:
# You can actually use binary numbers to generate
# combinatorics
def powerset2(stuff):
    """Use binaries to generate lists of stuff."""
    stuff_len = len(stuff)
    bin_string = "".join(["1" for _ in range(stuff_len)])
    # Get the integer value of this thing
    int_value = int(bin_string, 2)
    return [make_combination(i, stuff, len(bin_string)) for i in range(int_value + 1)]


print(powerset2([1, 2, 3, 4]))
