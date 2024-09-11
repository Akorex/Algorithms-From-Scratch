from stack import Empty

class ArrayDeque:
    """An implementation of doubly-ended queues using a python list for underlying storage"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        """Add element e to the front of the deque"""
        if self._size == len(self._data): # if storage is full
            self._resize(2 * len(self._data)) # expand storage
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Add element e to the back of the deque"""
        if self._size == len(self._data): # if storage is full
            self._resize(2* len(self._data)) # expand storage
        back = (self._front + self._size) % len(self._data)
        self._data[back] = e
        self._size += 1

    def first(self):
        """Return (but do not remove) the element at the front of the deque
        
        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the element at the back of the deque
        
        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size) % len(self._data)
        return self._data[back]

    def delete_first(self):
        """Return and remove the element at the front of the deque
        
        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        ans = self._data[self._front]
        self._data[self._front] = None # deprecate
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return ans

    def delete_last(self):
        """Return and remove the element at the back of the deque
        
        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        ans = self._data[back]
        self._data[back] = None
        self._size -= 1
        return ans

    def __str__(self):
        """String representation of the current deque in memory""" # Not working
        start = self._front
        end = (start + self._size) % len(self._data)
        return f"Deque: {self._data[start:end]}"

    def _resize(self, capacity):
        """Nonpublic utility to resize a deque"""
        old = self._data
        self._data = [None] * capacity # create a new array
        walk = self._front

        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

if __name__ == '__main__':
    d = ArrayDeque()
    print(d.is_empty())
    print(len(d))
    d.add_first(2)
    d.add_last(3)
    print(len(d))
    print(str(d))