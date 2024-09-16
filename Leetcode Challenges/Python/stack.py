"""
Implement a simple stack data structure -> LIFO

"""

class Empty(Exception):
    pass

class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def top(self):
        """
        Returns the element at the top of the stack
        """

        if len(self._data) == 0:
            raise Empty("The stack is empty")
        
        return self._data[-1]
    
    def pop(self):
        """
        Returns and remove the element at the top of the stack
        """

        if len(self._data) == 0:
            raise Empty("Cannot pop an empty stack")
        
    def push(self, e):
        """
        Add an element to the top of the stack
        """

        self._data.append(e)


class LinkedStack:
    """LIFO stack implementation using a singly linked-list"""

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    
    def __init__(self):
        """Creates an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, e):
        """Add an element to the top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        
        return self._head._element
    
    def pop(self):
        """Return and remove the element at the top of the stack
        
        
        Raise Empty exception if the stack is empty
        """

        if self.is_empty():
            raise Empty("Stack is empty")
        
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        return e