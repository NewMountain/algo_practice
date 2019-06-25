"""Chatper 1: Arrays and strings. Problem 1.9."""

# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only
# one call to isSubstring
# Example of rotation: "waterbottle" "erbottlewat"


# So given an s2, I need to see if it is a rotation of s1 only making one is substring call

# I believe the best possible implementation of a substring
# search is O(N)
def is_substring(substring, string):
    """Test if substring is within string."""
    return substring in string


# Unclear from question: am I allowed to inspect s1?
# In this case, the time complexity would be O(N)
def within(s1, s2):
    """Test if s2 is a rotation of s1."""
    double_string = s2 + s2
    return is_substring(s1, double_string)


test_1 = ("waterbottle", "erbottlewat")

assert within(*test_1)

