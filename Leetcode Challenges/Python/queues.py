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