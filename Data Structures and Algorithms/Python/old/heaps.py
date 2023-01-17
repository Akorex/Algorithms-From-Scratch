from priority_queues1 import PriorityQueueBase
from stack import Empty

class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap"""
    #------------------nonpublic behaviors-------------------
    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """Swap the elements at indices i and j"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j) 
                if self._data[right] < self._data[left]:
                    small_child = right
                    
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    #--------------------public behaviors-------------------------------

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    
    def add(self, key, value):
        """Add a key-value pair to the priority queue"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        """Return the (k, v)  tuple with the minimum key in the Priority Queue
        Raise Empty exception if the prioriry queue is empty
        """

        if self.is_empty():
            raise Empty('Priority Queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k, v) tuple with the minimum key in the Priority Queue
        
        Raise Empty exception if the priority queue is empty
        """
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

if __name__ == '__main__':
    h = HeapPriorityQueue()
    h.add(-1, 'nothing')
    h.add(0, 'blow')
    h.add(1, 'stay')
    h.add(5, 'A')
    h.add(2, 'B')
    h.add(3, 'C')
    h.add(1, 'D')
    print(h.min())
    print(len(h))

    print('\n')
    h = HeapPriorityQueue()
    print(h.is_empty())
    h.add(5, 'A')
    h.add(9, 'C')
    h.add(3, 'B')
    h.add(7, 'D')
    print(h.min())
    h.remove_min()
    print(h.min())
    print(len(h))
    print(h.is_empty())

   