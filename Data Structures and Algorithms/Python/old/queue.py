class Empty(Exception):
    pass

class ArrayQueue:
    """FIFO implementation using a python list for underlying storage"""

    DEFAULT_CAPACITY = 10 # moderate capacity for all new queues

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0 # index of _data which signifies the front of the queue

    def __len__(self):
        """Returns the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Returns True if queue is empty"""
        return self._size == 0

    def first(self):
        """Returns but do not remove the element at the front of the queue
        
        Raises Empty if the queue is empty
        """

        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Returns and remove the element at the front of the queue
        
        Raise Empty if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None # to deprecate
        self._front = (self._front + 1)% len(self._data)
        self._size -=1

        if 0 < self._size < len(self._data)//4: # if the number of elements in queue is 1/4th of list
            self._resize(len(self._data)//2)
        return answer
    
    def __str__(self):
        """Returns the string representation of the current queue in memory"""
        start = self._front
        stop = self._front + self._size
        return f"Queue: {self._data[start: stop]}"

    def enqueue(self, e):
        """Add element e to the back of the queue"""
        if self._size == len(self._data): # if the queue is full
            self._resize(2 * len(self._data)) # double the size of list
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, capacity):
        """Nonpublic utility to resize to a new list of capacity >=len(self)"""
        old = self._data
        self._data [None] * capacity
        walk = self._front 
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


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