"""Chapter 10: Sorting and Searching. Question 10.2"""

# Create a sorting function such that anagrams are next to each other
from collections import Counter

test_data = [
    "tar",
    "rat",
    "redrum",
    "study",
    "murder",
    "elbow",
    "below",
    "cider",
    "dusty",
    "cried",
    "fizz",
    "buzz",
    "bar",
    "baz",
]


def anagram_hash(word):
    """word hash."""
    # Create word histogram
    char_histogram = Counter(word)
    # Coerce to list of tuples
    zip_chars = list(char_histogram.values())
    # Turn list into tuple (lists are not hashable in Python)
    return tuple(zip_chars)


def sort_angrams(angrams):
    """Sort anagrams."""
    # So we need to turn each word into a letter histogram
    # Then hash them and sort by the hash
    return sorted(angrams, key=lambda x: anagram_hash(x))


print(sort_angrams(test_data))
