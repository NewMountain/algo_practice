"""Mentioned in passing in the book.
I wanted to implement myself for practice.
"""


class MinHeap:
    """Implement a min heap."""

    def __init__(self):
        """Initialization."""
        self.contents = []

    def __repr__(self):
        """How to print yourself."""
        return f"{self.contents}"

    def __parent_index(self, index):
        """Calculate the index of the parent."""
        if index == 0:
            return None

        return ((1 + index) // 2) - 1

    def __left_child(self, index):
        """Calculate the index of the left child."""
        left_index = ((index + 1) * 2) - 1
        if left_index < self.size():
            return left_index

        # Left index is out of bounds
        return None

    def __right_child(self, index):
        """Calculate the index of the right child."""
        left_child = self.__left_child(index)
        if left_child is not None and left_child + 1 < self.size():
            return left_child + 1

        # Either out of bounds or no left_child
        return None

    def __swap(self, i_1, i_2):
        """Swap index_1 and index_2 in contents."""
        # I don't like the way this formatted...
        (self.contents[i_1], self.contents[i_2]) = (
            self.contents[i_2],
            self.contents[i_1],
        )

    def __bubble_up(self, index):
        """See if an item needs to be bubbled up."""
        if index == 0:
            return

        parent_index = self.__parent_index(index)

        if self.contents[index] < self.contents[parent_index]:
            self.__swap(parent_index, index)
            self.__bubble_up(parent_index)

    def __push_one(self, value):
        """Push a single value onto the heap."""
        self.contents.append(value)
        index = self.size() - 1
        self.__bubble_up(index)

    def __find_min(self, i_1, i_2):
        """Find the min non-null value and index."""
        # Gracefully handle nulls
        i_1_value = None
        if i_1 is not None:
            i_1_value = self.contents[i_1]

        i_2_value = None
        if i_2 is not None:
            i_2_value = self.contents[i_2]

        if i_1_value is not None and i_2_value is not None:
            if i_1_value <= i_2_value:
                return (i_1, i_1_value)
            else:
                return (i_2, i_2_value)

        if i_1_value is None:
            return (i_2, i_2_value)

        if i_2_value is None:
            return (i_1, i_1_value)

        # Everything is null
        return (None, None)

    def __heapify(self, index):
        """Heapify (resort) the heap."""
        left_index = self.__left_child(index)
        right_index = self.__right_child(index)
        min_index, min_value = self.__find_min(left_index, right_index)

        if min_value is not None and min_value < self.contents[index]:
            self.__swap(min_index, index)
            self.__heapify(min_index)

    def size(self):
        """Return the size of the heap."""
        return len(self.contents)

    def push(self, addition):
        """Accepts an element or list of elements."""
        if isinstance(addition, list):
            for element in addition:
                self.__push_one(element)

        else:
            self.__push_one(addition)

    def peek(self):
        """Peek the min value of the heap."""
        return self.contents[0]

    def pop(self):
        """Pop the min value off the heap."""
        if self.size() == 0:
            return None

        if self.size() == 1:
            value = self.contents[0]
            self.contents = []
            return value

        value = self.contents[0]
        # Get the last element
        last = self.contents.pop()
        # Set the last equal to the index 0 then heapify index 0
        self.contents[0] = last
        self.__heapify(0)

        return value


# Let's test it
mn = MinHeap()

# mn should be empty
assert mn.contents == []


mn.push(1)
assert mn.contents == [1]

mn.push(2)
assert mn.contents == [1, 2]

mn.push([8, 5, 1, 12, 18])
assert mn.contents == [1, 1, 8, 5, 2, 12, 18]

mn.pop()
assert mn.contents == [1, 2, 8, 5, 18, 12]

mn.pop()
assert mn.contents == [2, 5, 8, 12, 18]

mn.pop()
assert mn.contents == [5, 12, 8, 18]


mn.push([6, -1])

assert mn.contents == [-1, 6, 5, 18, 12, 8]

