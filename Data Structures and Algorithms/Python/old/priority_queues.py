from queue import Empty
from positional_lists import PositionalList

class PriorityQueueBase:
    """An abstract base class for a priority queue"""
    #----------------nested class--------------------------------
    class _Item:
        """Lightweight composite to store priority queue items"""
        __slots__ = '_key', '_value'
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key # provides < functionality for Items

        def __gt__(self, other):
            return self._key > other._key # provides > functionality for Items

    def is_empty(self):
        return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):
    """A concrete class for the priority queues, values and keys are unsorted
    The minimum key is higher priority convention is used for this class
    """

    def __init__(self):
        """Creates a new empty Priority Queue"""
        self._data = PositionalList()
    
    def _find_min(self):
        """Return the Position of item with minimum key"""
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the"""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k, v) tuple with the minimum key"""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with the minimum key"""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list"""

    def __int__(self):
        """Create a new empty queue"""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the queue"""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair"""
        newest = self._Item(key, value)
        walk = self._data.last()
        # walking backward looking for smallest key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (k, v) tuple with minimum key"""
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k, v) tuple with minimum key"""
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        p = self._data.first()
        item = self._data.delete(p)
        return (item._key, item._value)