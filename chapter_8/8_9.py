"""Chapter 8: Recursion and Dyanamic Programming. Question 8.9"""

# Implement an algorithm to print all valid combinations of n
# pairs of parens
# 3 => "((())), (()()), (())(), ()(()), ()()()"


def distinct(stuff):
    """Distinct a list of stuff."""
    return list(set(stuff))


def make_parens(n):
    """Make parens and return a string of parens."""
    if n <= 0:
        return [""]

    results = []
    for result in make_parens(n - 1):
        results.append(f"({result})")
        results.append(f"{result}()")
        results.append(f"(){result}")

    return distinct(results)


# Not sure if the mutable approach works in Python
# Look into this later

# # Let's try something more efficient
# def make_parens_two(ls, left, right, string, index):
#     """Build parens more efficiently."""
#     if left < 0 or right < left:
#         return ls
#     if left == 0 and right == 0:
#         final_string = "".join(string)
#         ls.append(final_string)
#         return ls
#     else:
#         string[index] = "("
#         make_parens_two(ls, left - 1, right, string, index + 1)

#         string[index] = ")"
#         make_parens_two(ls, left, right - 1, string, index + 1)


# def parens(n):
#     ls = []
#     string = [0 for _ in range(n * 2)]
#     make_parens_two(ls, n, n, string, 0)


print(parens(1))
print(parens(2))
