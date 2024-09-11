"""
From cracking the coding interview

Stack Min: How would you design a stack which, in addition to push and pop, has a function min 
which returns the minimum element?

"""

class MinStack:
    def __init__(self):
        self._data = []
        self.min = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def top(self):
        return self._data[-1]
    
    def getMin(self):
        return self.min[-1]
    
    def pop(self):
        if self._data[-1] == self.min[-1]:
            self.min.pop()
        return self._data.pop()
    
    def push(self, e):
        self._data.append(e)

        if self.min:
            if e <= self.min[-1]:
                self.min.append(e)
        else:
            self.min.append(e)