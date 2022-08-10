class ArrayDeque:
    """Array based implementation of double-ended queues using list as underlying storage"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0 # the counter
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Returns (but do not remove) the element at front of the deque
        Raises error if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]


    def last(self):
        """Returns (but do not remove) the element at the back of the deque
        Raises error if the deque is empty"""
        if self.is_empty():
            raise Empty('Deque is empty')
        last = (self._front + self._size - 1) % len(self._data)
        return self._data[last]

    def add_last(self, e):
        """Adds the element e to the back of the deque"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    
    def delete_last(self):
        """Remove and return the element at the back of the deque
        Raises error if the deque is empty"""

        if self.is_empty():
            raise Empty('Deque is empty')
        last = (self._front + self._size - 1) % len(self._data)
        answer = self._data[last]
        self._data[last] = None
        self._size -= 1
        return answer

    def add_first(self, e):
        """Adds the element e to the front of the deque"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def delete_first(self):
        """Remove and return the element at the front of the deque
        Raises error if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._front]
        walk = self._data[self._front + 1]
        self._front = None
        for k in range(self._size):
            self._data = self._data[walk]
            walk = (walk + 1) % len(self._data)
            
        return answer


    def _resize(self, capacity):
        """Resizes the deque to the given capacity"""
        old = self._data # copy the old deque
        self._data = [None] * capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
        

if __name__ == '__main__':
    d = ArrayDeque()
    d.add_first(5)
    d.add_last(6)
    d.delete_last()
    print(d.last())
    print(d.first())
    print(d.__len__())