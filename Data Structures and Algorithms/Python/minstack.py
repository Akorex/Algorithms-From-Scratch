"""
A stack implementation that supports push, pop, top and retrieving the minimum
element in constant time
"""
class MinStack:
    """LIFO implementation with the requirements described above"""
    def __init__(self):
        self._data = [] # stores the entries
        self._min = [] # stores the minimum entry

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def pop(self):
        if self._data[-1] == self._min[-1]:
            self._min.pop() # convention to remove 
        return self._data.pop()

    def push(self, e):
        self._data.append(e)
        if self._min:
            if e <= self._min[-1]:
                self._min.append(e)
        else:
            self._min.append(e)

    def getMin(self):
        return self._min[-1]

    def top(self):
        return self._data[-1]

if __name__ == '__main__':
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())
    s.pop()
    print(s.getMin())
    print(s.top())