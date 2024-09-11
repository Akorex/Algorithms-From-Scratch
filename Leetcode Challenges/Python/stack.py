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