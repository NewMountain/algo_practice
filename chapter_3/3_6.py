"""Chapter 3: Stacks and Queues. Question 3.6"""

# An animal shelter that holds cats and dogs and operates strictly on FIFO basis.
# Your animal shelter must support enqueue(), dequeueAny(), dequeueDog(), dequeueCat()


from collections import deque


class Queue:
    """Implement a FIFO queue."""

    def __init__(self):
        self.contents = deque()
        self.depth = 0

    def __repr__(self):
        return f"{self.contents}"

    def pop(self):
        """Pop yourself."""
        if self.depth == 0:
            return None

        self.depth -= 1
        value = self.contents.pop()
        return value

    def push(self, value):
        """Push non null value onto queue."""
        if value is None:
            # TODO: Support nulls if required
            raise Exception("Nulls not allowed at this time")

        self.depth += 1
        return self.contents.appendleft(value)

    def peek(self):
        """Peek at the next object in the queue."""
        if self.depth == 0:
            return None

        value = self.contents.pop()
        # We need to append instead of appendleft in .push()
        self.contents.append(value)

        return value


class AnimalShelter:
    """A kind of weird FIFO animal shelter."""

    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()
        self.animal_count = 0

    def __repr__(self):
        return f"\nCats:\n{self.cat_queue}\nDogs:\n{self.dog_queue}\n"

    def get_animal_id(self):
        """Return an animal id and increment internal counter."""
        value = self.animal_count
        self.animal_count += 1
        return value

    def enqueue(self, animal_type, animal_name):
        """Insert an animal into the animal shelter."""
        # Sanity check user input
        if animal_type not in ["cat", "dog"]:
            raise Exception(
                f"Animal type: {animal_type} is not supported at this shelter"
            )

        # Generate animal data
        animal_id = self.get_animal_id()
        animal_data = {"type": animal_type, "name": animal_name, "id": animal_id}

        if animal_type == "dog":
            return self.dog_queue.push(animal_data)

        # Otherwise it's a cat
        return self.cat_queue.push(animal_data)

    def dequeue_cat(self):
        """Pop a cat off the queue."""
        peek_cat = self.cat_queue.peek()

        if peek_cat is None:
            return "Sorry, no cats"

        popped_cat = self.cat_queue.pop()

        return popped_cat

    def dequeue_dog(self):
        """Pop a dog off the queue."""
        if self.dog_queue.peek() is None:
            return "Sorry, no dogs."

        return self.dog_queue.pop()

    def dequeue_any(self):
        """FIFO return any animal."""
        peek_dog = self.dog_queue.peek()
        peek_cat = self.cat_queue.peek()

        # If both are empty
        if peek_dog is None and peek_cat is None:
            return "Sorry, no pets right now."

        if peek_dog is None:
            return self.cat_queue.pop()

        if peek_cat is None:
            return self.dog_queue.pop()

        # Otherwise, check which one has been here longer
        if peek_dog["id"] < peek_cat["id"]:
            return self.dog_queue.pop()

        return self.cat_queue.pop()


a = AnimalShelter()

a.enqueue("dog", "old_yeller")
a.enqueue("dog", "lassie")
a.enqueue("cat", "fluffy")
a.enqueue("dog", "meatbag")
a.enqueue("cat", "kitty")

print(a)

assert a.dequeue_any()["name"] == "old_yeller"

print(a)

assert a.dequeue_cat()["name"] == "fluffy"

print(a)

assert a.dequeue_cat()["name"] == "kitty"

print(a)

a.enqueue("cat", "cheetah")

print(a)

assert a.dequeue_dog()["name"] == "lassie"

print(a)

assert a.dequeue_any()["name"] == "meatbag"

print(a)

assert a.dequeue_cat()["name"] == "cheetah"

print(a)

