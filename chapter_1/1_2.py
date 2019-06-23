"""Question 1_2 of first chapter."""

# Given two strings, write a method to decide if
# one is a permutation of the other


def flatten(list_of_something):
    accum = []
    for elem in list_of_something:
        if isinstance(elem, list):
            accum += flatten(elem)
        else:
            accum.append(elem)
    return accum


def make_permutations(string):
    """Return all permutations of a string."""
    # If there are no more characters
    if not string:
        return []

    if len(string) == 1:
        return [string]

    # Otherwsise, split head and tail
    head = string[0]
    tail = string[1:]

    permutations = flatten(make_permutations(tail))

    options_1 = [f'{head}{"".join(t)}' for t in permutations]
    options_2 = [f'{"".join(t)}{head}' for t in permutations]

    return set(options_1 + options_2)


# First solution: Take the first string
# generate all of its permutations and see if the second
# string is in this collection
# This is an O(2^N) operation
def is_permutation(string_1, string_2):
    """See if one string is a permutation of the other."""
    # Step 1, generate permutations
    perms = make_permutations(string_1)
    return string_2 in perms


false_test = ("dog", "cat")  # False
true_test = ("rat", "tar")  # True

# Let's test that the flatten function works
flatten_test_1 = [1, 2, 3, 4, 5, 6]
flatten_test_2 = [1, 2, 3, [4, 5, 6]]
flatten_test_3 = [1, [2, [3, [4, [5, 6]]]]]

assert flatten(flatten_test_1) == flatten_test_1
assert flatten(flatten_test_2) == flatten_test_1
assert flatten(flatten_test_3) == flatten_test_1

# Let's test that the permutation function works
assert make_permutations("dog") == {"dog", "dgo", "ogd", "god"}

# Now let's test if is_permutation works
# This is False
assert not is_permutation(*false_test)
# This is True
assert is_permutation(*true_test)

# Well that was likely too much code
# Let's think about other ways to solve this

# We can sort the two strings and see if they are equal.
# If so, then they must contain permuatations of one another


def sort_string(string):
    """Sort a string."""
    return "".join(sorted(string))


assert sort_string("acb") == "abc"

# This is an O(N log N) operation
def is_permutation_2(string_1, string_2):
    """Is one a permutation of the other."""
    sorted_str_1 = sort_string(string_1)
    sorted_str_2 = sort_string(string_2)
    return sorted_str_1 == sorted_str_2


# This is False
assert not is_permutation_2(*false_test)
# This is True
assert is_permutation_2(*true_test)


def make_char_hist(string):
    """Take a string and turn into character histogram."""
    hist = {}
    for char in string:
        if char not in hist:
            hist[char] = 1
        else:
            hist[char] += 1

    return hist


# This is an O(N) operation
# Turn each string into a character histogram and confirm if they are
# the same
def is_permutation_3(string_1, string_2):
    """Return if one string permutation of the other."""
    # Exit early if they are different numbers of characters
    if len(string_1) != len(string_2):
        return False

    char_hist_1 = make_char_hist(string_1)
    char_hist_2 = make_char_hist(string_2)

    return char_hist_1 == char_hist_2


# This is False
assert not is_permutation_3(*false_test)
# This is True
assert is_permutation_3(*true_test)
