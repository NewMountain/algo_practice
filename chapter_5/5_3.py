"""Chapter 5: Bit manipulation. Question 5.3"""

# Given a binary sequence, find the bit to flip
# to generate the longest sequency of 1s


def bitstring(n):
    """Python stores bits as ints, so return the bitstring."""
    # Chop off the prefix python gives it
    return bin(n)[2:]


def make_segments(string):
    """Turn a bitstring into a list of segments."""
    current_bit = None
    current_count = 0
    segments = []
    index = 0

    for bit in string:
        if bit != current_bit:
            # Deal with the start case
            if current_bit is not None:
                segments.append((current_bit, current_count, index))
                index += 1

            current_bit = bit
            current_count = 1
        else:
            current_count += 1

    # Add the leftover bits
    segments.append((current_bit, current_count, index))

    return segments


def get_zero_betweens(segments):
    """Find all segments of one 1 not in first of last position."""
    indexes = []
    for i in range(1, len(segments) - 1):
        bit, count, _index = segments[i]
        if bit == "0" and count == 1:
            indexes.append(i)

    return indexes


def get_super_segment_index(betweens, segments):
    """Get the total length of super segments."""
    max_count = 0
    max_index = None
    for b in betweens:
        _bit, left_count, _index = segments[b - 1]
        _bit, right_count, _index = segments[b + 1]
        new_count = left_count + right_count + 1
        if new_count > max_count:
            max_index = b

    return max_index


def right_bit_to_flip(index, segments, bit_string):
    """Generate an index from right."""
    # Get the sum of counts for all segments >= index
    index_from_right = sum([s[1] for s in segments if s[2] >= index]) + 1
    return (len(bit_string)) - index_from_right


def flip_win(bits):
    """Find the bit to flip to generate the longest sequence of 1s."""
    bit_string = bitstring(bits)
    # Now split into "segments"
    segments = make_segments(bit_string)

    # Algorithm is find any segments with only one 0
    zero_between_indexes = get_zero_betweens(segments)

    if zero_between_indexes:
        # sum the counts of left and right and pick the max "super" segment
        index = get_super_segment_index(zero_between_indexes, segments)
        # Plus one here for a goofy offset issue
        bit_to_flip = right_bit_to_flip(index, segments, bit_string) + 1
    else:
        # If there is no super segment, just swap a bit next to the largest segment
        ones = [s for s in segments if s[0] == "1"]
        ones.sort(key=lambda s: s[1], reverse=True)

        (_bit, count, index) = ones[0]
        # If index is zero, flip a bit to the right of the partition
        if index == 0:
            # The bit to flip in the length of the section
            bit_to_flip = count

        # Otherwise to the left of partition
        else:
            bit_to_flip = right_bit_to_flip(index, segments, bit_string)

    # Generate bitstring based on len_bistring
    flip = ["0" for _ in range(len(bit_string))]
    flip[bit_to_flip] = "1"
    flip_string = "".join(flip)

    print("\n")
    print(bit_string)
    print(flip_string)
    new_number = int(bit_string, 2) + int(flip_string, 2)
    print(bitstring(new_number))

    print(int(flip_string, 2))

    return int(flip_string, 2)


# No joinable segments, longest 1 partion is index 0
# Flipped bit 11
assert flip_win(0b1111111111100111001111) == 1024
# ---------------------------^
# No joinable segments, longest partition is index -1
# The bit to flip is at index 7 from right
assert flip_win(0b100100111111) == 64
# ---------------------^
# No joinable segments, longest partition is index -2
# The bit flip is
assert flip_win(0b10011111111100111) == 16384
# ------------------^
# Two joinable segments
flip_win(0b11011101111) == 16
