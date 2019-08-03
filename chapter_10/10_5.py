"""Chapter 10: Sorting and Searching. Question 10.5"""

# Given a sorted array of strings that is interspersed with empty strings, write a
# method to find the location of a given string.

import random
import time


# Note, this works on POSIX operating systems
def get_words(n):
    """Get n unique words from the UNIX dictionary."""
    # Let's make sure the words are unique
    words_used = set()
    with open("/usr/share/dict/words", "r") as dictionary:
        word_string = dictionary.read()
        words = word_string.split("\n")

    acc = []
    while len(acc) < n:
        rando_word = random.choice(words)
        if rando_word.lower() not in words_used:
            # Weird issues with sorting and comparison of cases
            l_case_word = rando_word.lower()
            words_used.add(l_case_word)
            acc.append(l_case_word)

    # Sort the list
    acc.sort()

    return acc


def sparsify(words):
    """Make a list of words sparse."""
    acc = []
    for word in words:
        # Add the word, then a random amount of "space"
        acc.append(word)
        for _ in range(random.randint(0, 10)):
            acc.append("")

    return acc


def make_sparse_wordlist(n):
    """Make a sparse wordlist."""
    words = get_words(n)
    random_word = random.choice(words)
    return sparsify(words), random_word


def compress(words):
    """Compress the sparse matrix."""
    acc = []
    for index, value in enumerate(words):
        if value != "":
            acc.append((index, value))

    return acc


def b_search(words, word_desired, start, end):
    """Binary search of a compressed word list."""
    mid = (start + end) // 2
    mid_word = words[mid][1]

    if mid_word == word_desired:
        return words[mid][0]

    if start + 1 == end:
        if words[start][1] == word_desired:
            return words[start][0]
        else:
            return words[end][0]

    if word_desired > mid_word:
        # Go right
        return b_search(words, word_desired, mid + 1, end)

    if word_desired < mid_word:
        # Go left
        return b_search(words, word_desired, start, mid - 1)


# This is O(n log n)
# In thinking through this, this makes no sense
# If O(N) is fine, we can just walk the list, this is more
# work than necessary
def sparse_search(words, desired_word):
    """Implement an efficient search of a sparse matrix."""
    # Step one, compress to only the actual words and their indexes
    compressed_words = compress(words)
    # Now we can do a binary search on this structure
    return b_search(compressed_words, desired_word, 0, len(compressed_words) - 1)


# Let's try something else


def get_word(words, index):
    """Return the word and index."""
    return words[index], index


def jitter(words, index):
    """Find the first non-empty index."""
    offset = 0
    while True:
        word, idx = get_word(words, index + offset)
        if word != "":
            return word, idx

        if offset != 0:
            word, idx = get_word(words, index - offset)
            if word != "":
                return word, idx

        # Increment offset and try again
        offset += 1


def b_search_2(words, word_desired, start, end):
    """Binary search of sparse word list."""
    mid = (start + end) // 2

    mid_word, mid_index = jitter(words, mid)

    if mid_word == word_desired:
        return mid_index

    if start + 1 == end:
        if words[start] == word_desired:
            return start
        else:
            return end

    if word_desired > mid_word:
        return b_search_2(words, word_desired, mid_index + 1, end)

    if word_desired < mid_word:
        return b_search_2(words, word_desired, start, mid_index - 1)


RUNS = 1000

start = time.time()
print(f"Running version 1 for {RUNS} runs")
for i in range(RUNS):
    test_data, random_word = make_sparse_wordlist(1000)
    index = sparse_search(test_data, random_word)
    assert test_data[index] == random_word
end = time.time()

print(f"First version ran {end - start} seconds for {RUNS} runs.")

start = time.time()
print(f"Running version 2 for {RUNS} runs")
for i in range(RUNS):
    test_data, random_word = make_sparse_wordlist(1000)
    index = b_search_2(test_data, random_word, 0, len(test_data) - 1)
    assert test_data[index] == random_word
end = time.time()

print(f"Second version ran {end - start} seconds for {RUNS} runs.")
