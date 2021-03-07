# This python file is Class definition for our datatype Queue.
# Generating a separate file for class makes the program look clear and easy to understand
# For Breadth First Search, Queues are the recommended data structure to be used.
# List are not very efficient for Queue and therefore we will be using deque. Why?
# Because deque has popleft() which shakes hand with FIFO notion of Queue

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
       return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)
