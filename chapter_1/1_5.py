"""Chapter 1: Arrays and Strings."""

# There are three tuypes of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Give two strings, write a function to check if they are one edit or
# zero edits away

test_1 = ("pale", "ple")  # true
test_2 = ("pales", "pale")  # True
test_3 = ("pale", "bale")  # True
test_4 = ("pale", "bake")  # False


# First iteraction, coerce both strings
# two sets and compare the difference
# This is an O(N) operation to create the
# two sets
def test_difference(str_1, str_2):
    """Test the difference between strings."""
    s_1 = set(str_1)
    s_2 = set(str_2)

    # The difference is O(len(keys))
    if len(s_1.difference(s_2)) > 1:
        return False

    return True


assert test_difference(*test_1)
assert test_difference(*test_2)
assert test_difference(*test_3)
assert not test_difference(*test_4)

# Cool, SO that works, but these test are missing a critical case
# We are using the same characters, but have made two swaps
# So our first algo will miss it
test_5 = ("pale", "ealp")  # False
test_6 = ("pale", "paale")  # True

print(test_difference(*test_5))  # This returns True, but should be False

# Let's see if we can do something about this...
# This is an O(N) solution where N is the length of the shorter string
# Also, tracking cursors through a string is a mean problem
def test_difference_2(str_1, str_2):
    """Basically same as test_difference, but with additional check."""
    # Find the longer length
    # and minus one to avoid out of bounds errors
    max_index = max(len(str_1), len(str_2)) - 1
    # Create an offset for each string to compare
    o_1 = 0
    o_2 = 0
    penalties = 0

    while o_1 <= max_index and o_2 <= max_index:
        try:
            if str_1[o_1] == str_2[o_2]:
                pass
            # A character was removed from string_2
            elif str_1[o_1 + 1] == str_2[o_2]:
                o_1 += 1
                penalties += 1
            elif str_1[o_1] == str_2[o_2 + 1]:
                o_2 += 1
                penalties += 1
            else:
                penalties += 1

            o_1 += 1
            o_2 += 1
        except IndexError:
            # Out of bounds error becuase a character was added on the end
            # of one string and not the other
            penalties += 1
            o_1 += 1
            o_2 += 1
            # This break is what makes this O(N) of the shorter string
            break

    # Pass if we have an acceptable level of penalties
    return penalties <= 1


assert test_difference_2(*test_1)
assert test_difference_2(*test_2)
assert test_difference_2(*test_3)
assert not test_difference_2(*test_4)
assert not test_difference_2(*test_5)
assert test_difference_2(*test_6)
