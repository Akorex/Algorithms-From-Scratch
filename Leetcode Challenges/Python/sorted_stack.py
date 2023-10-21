"""
Solution to problem from Cracking the Coding Interview chapter 3 -#5

Write a program to sort a stack such that the smallest items are on the top. You can use 
an additional temporary stack. but you may not copy the elements into any other data structure 
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty. 
"""

class Empty(Exception):
    pass
# implement the stack
class ArrayStack:
    """A LIFO ADT implementatation using python list as underlying storage"""

    def __init__(self):
        """Create an empty stack"""
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        """Returns True if no element in the stack"""
        return len(self._data) == 0

    def push(self, e):
        """Adds an element e to the top of the stack"""
        self._data.append(e)

    def pop(self):
        """Returns and remove the element at the top of the stack
        
        Returns Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self._data.pop()

    def top(self):
        """Returns but does not remove the element at the top of the stack.
        
        Returns Empty Exception is the stack is empty
        """
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self._data[-1]

    def __str__(self):
        """Returns a string representation of the current stack in memory"""
        return f"Stack: {self._data}"
    
# implement the SortedClass

class SortedStack(ArrayStack):
    def __init__(self):
        super().__init__()
        self.temp_stack = ArrayStack()

    def push(self, item):
        if self.is_empty() or item < self.top():
            super().push(item)
        else:
            while self.top() is not None and item > self.top():
                self.temp_stack.push(self.pop())
                super().push(item)

                while not self.temp_stack.is_empty():
                    super().push(self.temp_stack.pop())