"""Chapter 8: Recursion and Dyanamic Programming. Question 8.11"""

# Given some amount of cents, what is the total combination
# of coins

import copy
import json
import random

# cents = random.randint(0, 100)


def flatten(stuff):
    """Flatten a list of stuff."""
    acc = []
    for elem in stuff:
        if isinstance(elem, list):
            for sub_elem in flatten(elem):
                acc.append(sub_elem)
        else:
            acc.append(elem)

    return acc


def try_quarter(cents, bag):
    new_bag = copy.deepcopy(bag)
    if cents >= 25:
        new_bag["quarters"] += 1
        return calculate(cents - 25, new_bag)
    # Otherwise return Nothing
    return None


def try_dime(cents, bag):
    new_bag = copy.deepcopy(bag)
    if cents >= 10:
        new_bag["dimes"] += 1
        return calculate(cents - 10, new_bag)
    # Otherwise return Nothing
    return None


def try_nickel(cents, bag):
    new_bag = copy.deepcopy(bag)
    if cents >= 5:
        new_bag["nickels"] += 1
        return calculate(cents - 5, new_bag)
    # Otherwise return Nothing
    return None


def try_penny(cents, bag):
    new_bag = copy.deepcopy(bag)
    if cents >= 1:
        new_bag["pennies"] += 1
        return calculate(cents - 1, new_bag)
    # Otherwise return Nothing
    return None


def calculate(cents, bag={"quarters": 0, "nickels": 0, "dimes": 0, "pennies": 0}):
    """Calculate the combos."""
    if cents == 0:
        return [bag]

    # Null filtered flattened list
    data = flatten(
        [
            try_quarter(cents, bag),
            try_dime(cents, bag),
            try_nickel(cents, bag),
            try_penny(cents, bag),
        ]
    )
    # This still produces duplicates to filter
    # The following operation is pretty expensive, but produces a unique result
    return [json.loads(j) for j in set([json.dumps(d) for d in data if d])]


# print(calculate(44))


# Clearly, we need to seek out cheaper alternatives


def make_change(cents, change=(25, 10, 5, 1)):
    """Count the ways to make change."""
    print(cents)
    print(change)
    # Convert change to list
    list_change = list(change)
    # There is no more change for us to make
    if not list_change:
        return 0
    if len(list_change) == 1:
        return 1

    # Find the increment
    value = list_change[0]

    if len(list_change[1:]) < 2:
        # Otherwise, get the first change type
        count = []
        multiplier = 0
        while value * multiplier < cents:
            count.append(1)
            # Increment multiplier
            multiplier += 1

        return sum(count)

    else:
        # Then produce the next change tuple for the recursive call
        currency_tail = list_change[1:]
        change_tuple = tuple(currency_tail)
        print(f"change_tuple is {change_tuple}")

        # Otherwise, get the first change type
        count = []
        multiplier = 0
        while value * multiplier < cents:
            count.append(make_change(cents - (value * multiplier), change_tuple))
            # Increment multiplier
            multiplier += 1

        return sum(count)


print(make_change(92))
