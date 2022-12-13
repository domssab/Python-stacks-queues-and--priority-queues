from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        return self.elements.popleft()