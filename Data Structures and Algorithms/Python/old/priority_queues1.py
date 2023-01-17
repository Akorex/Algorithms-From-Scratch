"""This is an implementation of the Priority Queue ADT using a python list as underlying storage"""
from stack import Empty

class PriorityQueueBase:
    """An abstract base class providing support for the priority queue"""
    #----------------nested class--------------------------
    class _Item:
        """Lighweight abstraction for storing (key, value) pairs"""
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key # provides support for self < other

        def __gt__(self, other):
            return self._key > other._key # provides support for self > other


    #-----------class methods--------------------------------------
    def is_empty(self):
        return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue base using python list as underlying storage"""
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the queue"""
        newest = self._Item(key, value)
        self._data.append(newest)

    def _find_min(self):
        """Non-public utility to find index of (k, v) pair with the minimum key"""
        min_index = 0
        for i in range(len(self._data)):
            if self._data[i]._key < self._data[min_index]._key:
                min_index = i
        return min_index

    def min(self):
        """Return but do not remove a (k, v) tuple with minimum key"""
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        p = self._find_min()
        key, value = self._data[p]._key, self._data[p]._value
        return (key, value)

    def remove_min(self):
        """Remove and return a (k, v) tuple with minimum key"""
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        item = self._data.pop(self._find_min())

        key, value = item._key, item._value
        return (key, value)

class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented sorted priority queue using python list as underlying storage"""
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def min(self):
        """Return but do not remove the (k, v) pair with the minimum key"""
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        key, value = self._data[0]._key, self._data[0]._value

        return (key, value)

    def remove_min(self):
        """Remove and return the (k, v) pair with the minimum key"""
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        item = self._data.pop(0)
        key, value = item._key, item._value

        return (key, value)

    def add(self, key, value):
        """Add a (k, v) pair to the Priority Queue"""
        newest = self._Item(key, value)
        key = newest._key

        min_index = 0
        for i in range(len(self._data) -1, 0, -1):
            if self._data[i]._key < key:
                min_index = i
        self._data.insert(min_index , newest)

if __name__ == '__main__':
    print("For Unsorted Priority Queue:")
    q = UnsortedPriorityQueue()
    q.add(-1, 'nothing')
    q.add(0, 'blow')
    q.add(1, 'stay')
    q.add(5, 'A')
    q.add(2, 'B')
    q.add(3, 'C')
    q.add(1, 'D')
    print(q.min())
    print(len(q))

    print("\nFor Sorted Priority Queue:")
    q = SortedPriorityQueue()
    q.add(-1, 'nothing')
    q.add(0, 'blow')
    q.add(1, 'stay')
    q.add(5, 'A')
    q.add(2, 'B')
    q.add(3, 'C')
    q.add(1, 'D')
    print(q.min())
    print(len(q))