"""An implementation of the Queue ADT.

Improves queue.py on run-time efficiency
"""
from stack import Empty

class ArrayQueue:
    """An implementation of the FIFO ADT using a python list for underlying storage"""
    
    DEFAULT_CAPACITY = 10 # moderate capacity for all new queues

    def __init__(self):
        """Initializes an empty python queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._front = 0 # the front of the queue
        self._size = 0 # number of elements in the queue

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        """Adds an element to the back of the queue"""
        if self._size == len(self._data): # if queue is full
            self._resize(2 * len(self._data)) # expand the storage
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def first(self):
        """Return but do not remove the element at the front of the queue
        
        Raises Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("The queue is empty")
        ans = self._data[self._front]
        return ans

    def dequeue(self):
        """Remove and return an element from the front of the queue
        
        Raises Empty Exceptuon if the queue is empty
        """
        if self.is_empty():
            raise Empty("The queue is empty")
        ans = self._data[self._front]
        self._data[self._front] = None # deprecate
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data)//4: #if number of elements is less than 1/4th the storage
            self._resize(len(self._data)//2)
        return ans

    def _resize(self, capacity):
        """Nonpublic utility for resizing the list storage"""
        old = self._data
        self._data = [None] * capacity # create a new storage
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def __str__(self):
        """Returns a string representation of the queue in memory"""
        start = self._front
        stop = self._front + self._size
        
        return f"Queue: {self._data[start: stop]}"


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