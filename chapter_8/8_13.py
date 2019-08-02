"""Chapter 8: Recursion and Dyanamic Programming. Question 8.13"""

# Stack of boxes
import random

# You have n boxes of w width, h height and d depth
# The boxes cannot be rotated and can only be stacked
# on top of each other such that each box in the stack is strictly
# larger than the box above it in width, height and depth
# Computer the highest possible stack
# Height of stack is the sum of heights of all boxes in a stack


def make_box():
    """Generate a random box."""
    # lower_bound = random.randint(0, 50)
    # upper_bound = lower_bound + 25
    return {
        "width": random.randint(0, 50),
        "height": random.randint(0, 50),
        "depth": random.randint(0, 50),
    }


def make_boxes(n):
    """Generate n boxes."""
    return [make_box() for _ in range(n)]


def get_height(boxes):
    """Sum the height of the boxes."""
    return sum([box["height"] for box in boxes])


def stackable(top, bottom):
    """Box only "stackable" if top smaller than bottom in all dimensions."""
    less_deep = top["depth"] < bottom["depth"]
    less_tall = top["height"] < bottom["height"]
    less_wide = top["width"] < bottom["width"]
    return less_deep and less_tall and less_wide


def sob(boxes, stack):
    """This feels a lot like the knapsack problem."""
    # No more boxes to stack
    if not boxes:
        height = get_height(stack)
        return (stack, height)

    # Stack is empty
    if not stack:
        next_box = boxes[0]
    # Check if the next box is eligable for stack
    elif stackable(boxes[0], stack[-1]):
        next_box = boxes[0]
    else:
        next_box = None

    remaining_boxes = boxes[1:]

    # Stack with this box
    if next_box is not None:
        with_stack, with_height = sob(remaining_boxes, stack + [next_box])
    else:
        with_stack, with_height = [], 0

    # Stack without this box
    without_stack, without_height = sob(remaining_boxes, stack)

    if with_height > without_height:
        return with_stack, with_height

    # otherwise return the without box stack
    return without_stack, without_height


boxes = make_boxes(250)
# Sort the boxes in one dimension, doesn't matter which
sorted_boxes = sorted(boxes, key=lambda b: b["width"], reverse=True)

print(sob(sorted_boxes, []))
