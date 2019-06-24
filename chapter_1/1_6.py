"""Chapter 1: question 1.6."""

# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabccccccaaa would become a2b1c6a3. If the compressed string would
# be larger than the original, return the original


def coerce_buffer(last_char, buffer):
    """Helper function."""
    return f"{last_char}{buffer}"


# This is O(N) and space cannot exceed O(N)
def compress(string):
    """Turn a string into smaller of original or compressed string."""
    # Declare a buffer and last_char
    last_char = ""
    buffer = 0
    # A new string
    compressed_string = ""
    # Walk through the characters
    for char in string:
        # We a new character
        if last_char != char:
            # We need to flush the original buffer if it has values:
            if buffer != 0:
                # Create the compressed representation
                # Add the data to the compressed string
                compressed_string += coerce_buffer(last_char, buffer)
            # Create a new character and buffer
            last_char = char
            buffer = 1
        else:
            # Character is the same, just increment the buffer
            buffer += 1

        # Loop over, but break is len compressed_string > original_len
        if len(compressed_string) > len(string):
            return string

    # Don't forget to add the buffer at the end
    # Create the compressed representation
    # Add the data to the compressed string
    compressed_string += coerce_buffer(last_char, buffer)

    # Double check the last addition didn't exceed original length
    if len(compressed_string) > len(string):
        return string

    # Otherwise, return the compressed string
    return compressed_string


test_1 = "aabccccccaaa"
assert compress(test_1) == "a2b1c6a3"
