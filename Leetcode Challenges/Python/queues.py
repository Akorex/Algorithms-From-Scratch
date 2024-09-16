"""
Implement a queue data structure -> FIFO
"""
class Empty(Exception):
    pass

class MyQueue:
    def __init__(self):
        self._data = []

    def __len__(self):
        """Return the number of elements in the queue"""
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def enqueue(self, e):
        """Add an element to the back of a queue"""
        self._data.append(e)

    def dequeue(self):
        """Return and Remove an element at the front of a queue"""
        if len(self._data) == 0:
            raise Empty("Cannot dequeue and empty queue")
        
        e = self._data.pop(0)

        return e
    
    def first(self):
        """Returns but do not remove an element at the front of a queue"""

        if len(self._data) == 0:
            raise Empty("The queue is empty")
        
        return self._data[0]
    
    def __str__(self):
        """Returns a string representation of the queue"""

        return f"Queue: {self._data}"
    



class LinkedQueue:
    """FIFO ADT implementation using a linked-list as underlying storage"""

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Creates and empty queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        """Return the element at the front of the queue"""
        if self.is_empty():
            raise Empty("The Queue is empty")
        
        return self._head._element
    
    def dequeue(self):
        """Return and remove the element at the front of a queue"""
        if self.is_empty():
            raise Empty("The queue is empty")
        
        e = self._head._element
        self._head = self._head._next
        self.size -=1 

        if self.is_empty():
            self._tail = None
        return e
    
    def enqueue(self, e):
        """Add an element to the back of the queue"""
        newest = self._Node(e, None)

        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

class CircularQueue:
    """Queue implementation using a circularly linked list for storage"""
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty("The Queue is empty")
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty("The Queue is empty")
        head = self._tail._next
        e = head._element

        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = head._next
        self._size -= 1
        return e
    
    def enqueue(self, e):
        newest = self._Node(e, None)

        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1








if __name__ == '__main__':
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(len(q))
    q.dequeue()
    print(q.is_empty())
    print(len(q))
    print(str(q))