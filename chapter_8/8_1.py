"""Chapter 8: Recursion and Dyanamic Programming. Question 8.1"""

# You can run up a staircase of n steps, taking 0, 1, or 2 steps each time
# how many combinations are there to get to the top?
from time import time
from functools import lru_cache

# That's fine, but this becomes exponentially more difficult quickly
# So let's memoize
TEST = 25


def count_steps_1(current_step: int, total_steps: int) -> int:
    """Count total combination of steps."""
    # Handle out of bounds
    if current_step > total_steps:
        return 0

    if current_step == total_steps:
        return 1

    return sum(
        [
            count_steps_1(current_step + 1, total_steps),
            count_steps_1(current_step + 2, total_steps),
            count_steps_1(current_step + 3, total_steps),
        ]
    )


start_1 = time()
[count_steps_1(0, n) for n in range(0, TEST)]
end_1 = time()

print(f"Recursive count_steps takes {end_1 - start_1} seconds.")


# INFINITE CACHE!
@lru_cache(maxsize=None)
def count_steps_2(current_step: int, total_steps: int) -> int:
    """Count total combination of steps."""
    # Handle out of bounds
    if current_step > total_steps:
        return 0

    if current_step == total_steps:
        return 1

    return sum(
        [
            count_steps_2(current_step + 1, total_steps),
            count_steps_2(current_step + 2, total_steps),
            count_steps_2(current_step + 3, total_steps),
        ]
    )


start_2 = time()
[count_steps_2(0, n) for n in range(0, TEST)]
end_2 = time()

print(f"Memoized count_steps takes {end_2 - start_2} seconds.")
