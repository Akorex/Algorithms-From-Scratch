from stack import Empty

class ArrayQueue:
    """An implementation of FIFO using a python list for underlying storage"""
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __str__(self):
        """A string representation of the queue in memory"""
        return f"Queue: {self._data}"

    def enqueue(self, e):
        """Add an element e to the back of the queue"""
        self._data.append(e)

    def dequeue(self):
        """Remove and return an element from the front of the queue
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data.pop(0)

    def first(self):
        """Return but do not remove the element at the front of the queue
        
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[0]

if __name__ == '__main__':
    q = ArrayQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(len(q))
    q.dequeue()
    print(q.is_empty())
    print(len(q))
    print(str(q))