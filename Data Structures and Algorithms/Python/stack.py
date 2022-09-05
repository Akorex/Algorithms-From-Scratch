# define the empty exception class
class Empty(Exception):
    pass

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

if __name__ == '__main__':
    s = ArrayStack()
    print(s.is_empty())
    s.push(2)
    s.push(3)
    print(s.top())
    print(s.is_empty())
    print(len(s))
    print(str(s))