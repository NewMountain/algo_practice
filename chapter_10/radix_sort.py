"""Chapter 10: Sorting and Searching. 

Extra practice: Implement Radix sort."""


import random


def make_random_numbers(n):
    """Generate n random numbers."""
    return [random.randint(0, n * 10) for _ in range(n // 2)]


def default_number_dict():
    """Return a number dict."""
    d = {}
    for i in range(10):
        d[i] = []

    return d


def find_digits(number):
    """Find the order of magnitude of a positive number."""
    digits = 0
    while number > (10 ** digits):
        digits += 1

    return digits


assert find_digits(5) == 1
assert find_digits(50) == 2
assert find_digits(500) == 3
assert find_digits(5000) == 4


def get_bin(digit, i):
    """Return the digit from i."""
    mod = 10 ** digit
    result = i // mod % 10
    return result


assert get_bin(0, 512) == 2
assert get_bin(1, 512) == 1
assert get_bin(2, 512) == 5
assert get_bin(3, 512) == 0


def order_by_digit(digit, ints):
    """Bin the ints by digit."""
    # Make a digit dict
    d = default_number_dict()
    for i in ints:
        num_bin = get_bin(digit, i)
        d[num_bin].append(i)

    # Now flatten into a single list
    acc = []
    for num_bin in range(10):
        acc = acc + d[num_bin]

    return acc


def radix_sort(ints):
    """Specialized sort made for ints in this case."""
    # Operate on base 10 numbers
    # maybe in future version, try using hex numbers and see
    # how that affects performance
    # Find max number
    max_num = max(ints)
    # Find max order or magnitude
    digits = find_digits(max_num)
    # Set the ints to ordered
    ordered = ints
    for d in range(digits + 1):
        ordered = order_by_digit(d, ordered)

    return ordered


if __name__ == "__main__":
    for n in range(2, 2_000):
        random_numbers = make_random_numbers(n)
        result = radix_sort(random_numbers)
        expected_result = sorted(random_numbers)
        try:
            assert result == expected_result
        except AssertionError:
            print(result)
