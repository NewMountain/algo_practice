"""Chapter 8: Recursion and Dyanamic Programming. Question 8.5"""

# Write a recursive function to multiply two positive integers
# without using the * operator


def multiply(x, y):
    """Recursive multiply FTW."""
    if y == 0:
        return 0

    return x + multiply(x, y - 1)


assert multiply(4, 3) == 12
assert multiply(3, 5) == 15
