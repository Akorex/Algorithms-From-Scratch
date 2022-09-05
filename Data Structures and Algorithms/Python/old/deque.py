class Empty(Exception):
    pass

class ArrayDeque:
    """Implementation of a doubly-ended queue using a python list for underlying storage"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create a new Deque"""
        self._data = [None]*ArrayDeque.DEFAULT_CAPACITY # python list for storing elements
        self._size = 0 # counter for number of elements in deque
        self._front = 0 # index of the first element in the deque

    
    def __len__(self):
        """Returns the number of elements in the deque"""
        return self._size

    def is_empty(self):
        """Returns True if the deque is empty"""
        return self._size == 0

    def add_first(self, e):
        """Adds an element e at the front of the deque"""
        if self._size == len(self._data): # if number of elements in deque = size of underlying list
            self._resize(2 * len(self._data)) # double the capacity
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def first(self):
        """Returns but do not remove the element at the front of the deque
        
        Raise Empty if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def add_last(self, e):
        """Adds an element e to the back of the deque"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        back = (self._front + self._size ) % len(self._data)
        self._data[back] = e
        self._size += 1

    def last(self):
        """Returns but do not remove the element at the back of the deque
        Raise Empty if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def delete_first(self):
        """Return and remove the element at the front of the deque
        Raise Empty if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        """Return and remove the element at the back of the deque
        Raise Empty of the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        return answer

    def _resize(self, capacity):
        """Nonpublic utility to resize to a new list of capacity > len(self._data)"""
        old = self._data # copy the old list
        self._data = [None] * capacity
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def __str__(self):
        """Returns the string representation of the deque in memory""" # Note working
        start = self._front
        end = (self._front + self._size) % len(self._data)
        return f"Deque: {self._data[start:]}"

if __name__ == '__main__':
    d = ArrayDeque()
    print(d.is_empty())
    print(len(d))
    d.add_first(2)
    d.add_last(3)
    print(str(d))