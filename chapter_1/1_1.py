# Question 1.1:

# Implement an algorithm to determine if a strong has all the unique
# characters. What if you cannot use additional data structures

# First attempt.
# Time: O(N)
# Space: O(N)
def unique_string_1(string):
    """See if all characters in the string are unique."""
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            # We have a repeat character
            return False

    # Every character is unqiue
    return True


# Second attempt: not allowed to use additional data structures
# Here the time is O(NlogN)
# Space is technically O(N), but due to python
# treating strings as immuatable, we could change the
# type []Char and then make this an O(1) space function
# As we are being handed a structure we are allowed to mutate
def unique_string_2(string):
    """Confirm all characters are unique."""
    # The issue here is we are not allowed to
    # create additional data structures
    # Note: we are mutating the string in place
    # This may alter your string elsewhere
    new_string = "".join(sorted(string))

    for idx, char in enumerate(new_string):
        # Skip the first index
        if idx == 0:
            continue
        if char == new_string[idx - 1]:
            return False

    # If nothing is repeated in the sorted list
    # The list is unique
    return True


# Some tests
true_test = "abcdefg"
false_test_1 = "abccdefg"
false_test_2 = "abcdegabh"

assert unique_string_1(true_test)
assert not unique_string_1(false_test_1)
assert not unique_string_1(false_test_2)


assert unique_string_2(true_test)
assert not unique_string_2(false_test_1)
assert not unique_string_2(false_test_2)

