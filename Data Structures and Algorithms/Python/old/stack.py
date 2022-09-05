# define the Empty excexption class
class Empty(Exception):
    pass

# implementation of Stack in python
class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """Returns the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if stack is empty"""
        return len(self._data) == 0
    
    def push(self, e):
        """Add an element e to the top of the stack"""
        self._data.append(e)

    def pop(self):
        """Removes and returns the element at the top of the stack
        
        Raise Empty Error if stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def top(self):
        """Returns but do not remove the element at the top of the stack
        
        Raises Empty Error if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def __str__(self):
        """Returns the string representation of the current stack in memory"""
        return f"Stack: {self._data}"


# an algorithm for matching delimiters
def is_matched(expr):
    """Returns True if all delimiters are properly matched. False otherwise"""
    left = '([{'
    right = ')]}'

    s = ArrayStack() # initialize a stack
    for c in expr:
        if c in left:
            s.push(c)
        elif c in right:
            if s.is_empty():
                return False
            if right.index(c) != left.index(s.pop()):
                return False # mismatched
    return s.is_empty() # were all symbols matched

def is_matched_html(raw):
    """Return True if all HTML tags are properly matched. False otherwise"""
    s = ArrayStack()
    j = raw.find('<') # find < if any

    while j != -1:
        k = raw.find('>', j + 1) # find next >
        if k == -1:
            return False
        tag = raw[j+1: k]
        if not tag.startswith('/'): # this is the opening tag
            s.push(tag)
        else:
            if s.is_empty():
                return False
            if tag[1:] != s.pop():
                return False
        j = raw.find('<', k + 1) # find the next < character

    return s.is_empty() # were all opening tags matched?

if __name__ == '__main__':
    s = ArrayStack()
    print(s.is_empty())
    s.push(2)
    s.push(3)
    print(s.top())
    print(s.is_empty())
    print(len(s))
    print(str(s))

    sentence = 'I am love with (a) girl'
    print(is_matched(sentence))