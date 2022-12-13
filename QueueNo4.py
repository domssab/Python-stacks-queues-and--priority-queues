from QueueNo2 import Queue

fifo = Queue("1st", "2nd", "3rd")
len(fifo)


for element in fifo:
    print(element)

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()