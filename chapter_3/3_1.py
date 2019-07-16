"""Chapter 3: Stacks and Queues. Question 3.1"""

# Describe how you could use a single array to implement three stacks

# Note: this is purely to practice code. In reality, this is not the most efficient way to do this
# https://docs.python.org/3.7/tutorial/datastructures.html#using-lists-as-stacks
# While appends and pops from the end of list are fast,
# doing inserts or pops from the beginning of a list is slow
# (because all of the other elements have to be shifted by one).
class ThreeStack:
    """Make three stacks from a single array.
    
    Indexes 0, 1 and 2 hold the length of their contents."""

    def __init__(self):
        """Create the ThreeStack data structure."""
        self.contents = [0, 0, 0]

    def __repr__(self):
        """Stringified representation."""
        section_1 = self.get_subcontents(1)
        section_2 = self.get_subcontents(2)
        section_3 = self.get_subcontents(3)
        stack_1_len = self.contents[0]
        stack_2_len = self.contents[1]
        stack_3_len = self.contents[2]

        return f"1: {stack_1_len}, 2: {stack_2_len}, 3: {stack_3_len}\n[\n{section_1},\n{section_2},\n{section_3}\n]"

    def get_subcontents(self, section):
        """Return the subcontents of a section."""
        stack_1_len = self.contents[0]
        stack_2_len = self.contents[1]
        stack_3_len = self.contents[2]
        # Use a variable name for where the data starts instead of a magical number
        data_index = 3

        if section == 3:
            if stack_3_len == 0:
                return []
            # Otherwise
            start = data_index + stack_1_len + stack_2_len
            end = start + stack_3_len
            return self.contents[start:end]

        if section == 2:
            if stack_2_len == 0:
                return []
            # Otherwise
            start = data_index + stack_1_len
            end = start + stack_2_len
            return self.contents[start:end]

        if section == 1:
            if stack_1_len == 0:
                return []
            # Otherwise
            start = data_index
            end = start + stack_1_len
            return self.contents[start:end]

    def push(self, section, value):
        """Insert a value in a section."""
        stack_1_len = self.contents[0]
        stack_2_len = self.contents[1]
        # Stack 3 length doesn't matter in an insert
        # Use a variable name for where the data starts instead of a magical number
        data_index = 3

        if section == 3:
            start = data_index + stack_1_len + stack_2_len
            # Insert into the list
            self.contents.insert(start, value)
            # Increase the length of section 3
            self.contents[2] += 1

        if section == 2:
            start = data_index + stack_1_len
            # Insert into the list
            self.contents.insert(start, value)
            # Increase the length of section 2
            self.contents[1] += 1

        if section == 1:
            start = data_index
            # Insert into the list
            self.contents.insert(start, value)
            # Increase the length of section 2
            self.contents[0] += 1

    def pop(self, section):
        """Pop a value out of a section."""
        stack_1_len = self.contents[0]
        stack_2_len = self.contents[1]
        stack_3_len = self.contents[2]
        # Use a variable name for where the data starts instead of a magical number
        data_index = 3

        if section == 3:
            if stack_3_len is 0:
                return None
            else:
                start = data_index + stack_1_len + stack_2_len
                # Reduce the length by one
                self.contents[2] -= 1

        if section == 2:
            if stack_2_len is 0:
                return None
            else:
                start = data_index + stack_1_len
                # Reduce the length by one
                self.contents[1] -= 1

        if section == 1:
            if stack_1_len is 0:
                return None
            else:
                start = data_index
                # Reduce the length by one
                self.contents[0] -= 1

        # Get the value at the start index
        value = self.contents[start]
        # Delete the element at index
        del self.contents[start]

        return value


x = ThreeStack()

x.push(1, "a")

x.push(2, "f")

x.push(3, "k")

x.push(2, "g")

x.push(2, "h")

x.push(1, "b")

x.push(1, "c")

x.push(2, "i")

x.push(3, "l")

x.push(3, "m")

x.push(3, "n")


print(f"Popping section 3: {x.pop(3)}")
print(f"Popping section 2: {x.pop(2)}")
print(f"Popping section 3: {x.pop(3)}")
print(f"Popping section 1: {x.pop(1)}")
print(f"Popping section 1: {x.pop(1)}")
print(f"Popping section 1: {x.pop(1)}")
print(f"Popping section 1: {x.pop(1)}")
print(x)
print(f"Popping section 2: {x.pop(2)}")
print(x)
