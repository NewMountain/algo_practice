"""Chapter 1: Arrays and strings question 1.4."""

from itertools import permutations

# Given a string, write a function to check if it is a permutation of
# a palindrome.

# Let's lift a bunch of coce from prior examples
def flatten(list_of_something):
    accum = []
    for elem in list_of_something:
        if isinstance(elem, list):
            accum += flatten(elem)
        else:
            accum.append(elem)
    return accum


def string_to_list(string):
    """Coerce string to a list of characters, technically strings."""
    return [char for char in string]


def make_perms(thing):
    """Return all permutations of a string."""
    if len(thing) <= 1:
        return [thing]

    # Otherwise, take the heand and tail
    head = thing[0]
    tail = thing[1:]
    # and slide the head into all positions
    # around the permutations of the tail
    accumulator = []
    for perm in make_perms(tail):
        # We can use the index of thing to help here
        for idx in range(len(thing)):
            # Get the left side
            # All elements up to the index
            left = perm[:idx]
            # The right side is all element
            # at and past the index
            right = perm[idx:]
            # Smoosh them all together
            value = left + [head] + right
            # Flatten the list of lists and append
            accumulator.append(flatten(value))

    # Otherwise just return the list of things
    return accumulator


def make_permutations(thing):
    """Support strings as well as lists."""
    is_string = False
    if isinstance(thing, str):
        thing = string_to_list(thing)
        is_string = True

    perms = make_perms(thing)

    if is_string:
        return ["".join(w) for w in perms]

    return perms


def is_palindrome(string):
    """Return if palindrome."""
    # Too easy in python
    string_len = len(string)
    # Just a question of where to split
    # If even just compare the front to back half
    if string_len % 2 == 0:
        # Excessively cute version, does the first half equal its
        # reversed self
        first_half = string[: string_len // 2]
        second_half = string[string_len // 2 :]
        test = first_half == second_half[::-1]
        return test
    else:
        first_half = string[: string_len // 2]
        second_half = string[(string_len // 2) + 1 :]
        test = first_half == second_half[::-1]
        return test


assert is_palindrome("foof")
assert is_palindrome("hanah")
assert is_palindrome("atcocta")

# So let's start with brute force here
# So this question kind of sucked
# The example output actually included the permutations
# But the answer was only expected to be type bool
# Kind of lame, but fun practice
def permindrome(string):
    """Return if at least one permutations is a palindrome."""
    clean_string = string.replace(" ", "").lower()
    perms = make_permutations(clean_string)
    return len([perm for perm in perms if is_palindrome(perm)]) > 0


test_1 = "Taco cat"
test_2 = "yolo"
assert permindrome(test_1)
assert not permindrome(test_2)


def make_char_hist(string):
    """Take a string and turn into character histogram."""
    hist = {}
    for char in string:
        if char not in hist:
            hist[char] = 1
        else:
            hist[char] += 1

    return hist


def creates_permutations(string):
    """Simple test to see if it can generate permutations."""
    if len(string) > 1:
        return True
    # Otherwise False
    return False


def is_even(num):
    """Return if number is even."""
    return num % 2 == 0


def creates_palindrome(char_hist):
    """Check to see if character frequency allows palindromes."""
    # With a count of of characters, we can apply some tests
    char_count_even = [is_even(count) for count in char_hist.values()]
    # If all character counts are even, it can be a palindrome
    if all(char_count_even):
        return True

    # If there is only one odd character count, it can be a palindrome
    if len([f for f in char_count_even if f != True]) == 1:
        return True

    # Otherwise, it can't
    return False


# Cool, but after looking ahead somewhat confused, it actually
# Just expected bool, not the actual strings
# That should allow us to clean things up quite a bit
# The palindome generator itself it super expensive
# So let's avoid that for a test instead
# O(N) solution
def permindrome_2(string):
    """Return if at least one permutations is a palindrome."""
    clean_string = string.replace(" ", "").lower()
    # So here's my thought
    # Check the length of the string, if it's longer than 1,
    # It can create permutations
    # I believe this is O(N) as it must walk the string to count
    # length
    # For micro-tuning, you could make this one step
    # depending on whether we are trading maintainability for
    # performance
    is_permutation = creates_permutations(clean_string)
    # Create a character histogram
    char_count = make_char_hist(clean_string)
    # Now run the check, same disclosure as before,
    # We can do this all inline at the cost of reability
    is_palindrome = creates_palindrome(char_count)

    return is_palindrome and is_permutation


# tacocat has at least permutation and palindrome
assert permindrome_2(test_1)
# yolo can be permuted, but can't have palindrome
assert not permindrome_2(test_2)
