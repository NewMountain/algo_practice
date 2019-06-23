"""Chapter 1: Arrays and Strings problem 1.3."""

# Question: Write a method to replace all spaces in a string with "%20".
# You may assume that the string has sufficient space at the end to hold
# the additional characters, and that you are given the "true"
# length of the string


# This problem is likely much harder in languages with lower level string
# handling IE Java, Haskell, C, C++, etc
test_input = ("Mr John Smith", 13)
test_output = "Mr%20John%20Smith"

# Brute force version: O(N)
def urlify(string, char_len):
    """Urlify a string."""
    # So the disconnect here is Python strings are an immutable
    # data type. It doesn't seem to have a string builder
    # and a python list is dynamically reallocated
    # https://stackoverflow.com/questions/311775/python-create-a-list-with-initial-capacity
    # There's an interesting note though that allocating space * [None]
    # appears to increase performance
    # In a lower level language, we could take the
    # char length, count the spaces and add 2*space as we replace
    # " " (one char) with "%20" (three chars)
    # In python, we're dealing with s
    # Check we match the char_len
    assert char_len == len(string)
    accumulator = ""
    for char in string:
        # Return %20 instead of an empty string
        if char == " ":
            accumulator += "%20"
        else:
            accumulator += char

    return accumulator


assert urlify(*test_input) == test_output

# I feel bad this wasn't as hard as it was for my "at the metal"
# programmer peers, here's the python-ish equivalent of what
# they would have written
# Still O(N), but done like in the ole' days...
def hardcore_urlify(string, char_len):
    """To show I get the algo, the above solution is better in python."""
    # https://stackoverflow.com/questions/311775/python-create-a-list-with-initial-capacity
    # There's an interesting note though that allocating space * [None]
    # appears to increase performance
    # In a lower level language, we could take the
    # char length, count the spaces and add 2*space as we replace
    # " " (one char) with "%20" (three chars)
    # Get the whitespaces in the string
    num_spaces = len(["x" for char in string if char == " "])
    new_len = char_len + (num_spaces * 2)
    new_char_array = [None] * new_len

    # track your offset and create the new_index
    offset = 0
    for idx, char in enumerate(string):
        new_index = idx + offset
        if char == " ":
            # Insert the additional characters
            new_char_array[new_index] = "%"
            new_char_array[new_index + 1] = "2"
            new_char_array[new_index + 2] = "0"
            # Increment the offset by 2
            offset += 2
        else:
            new_char_array[new_index] = char

    return "".join(new_char_array)


assert hardcore_urlify(*test_input) == test_output
