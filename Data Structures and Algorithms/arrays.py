import sys
import ctypes
from time import time


# an empirical evidence python lists make use of dynamic arrays
data = []
for k in range(20):
    a = len(data)
    b = sys.getsizeof(data)

    print("Length: {0:3d}; size in bytes: {1:4d}".format(a, b))
    data.append(None)


# implementation of low-level dynamic arrays
class DynamicArrays:
    """A dynamic array class akin to a simplified python list"""

    def __init__(self):
        """Initializes an empty array"""
        self._n = 0 # number of elements in list
        self._capacity = 1 # number of elements that can actually be stored. (defaults to 1)
        self._A = self._make_array(self._capacity) # make the array

    def __len__(self):
        """Returns the number of elements in the array"""
        return self._n

    def __getitem__(self, index):
        """Returns the element at index"""
        if not 0 <= index < self._n:
            raise IndexError('index out of range')
        return self._A[index]

    def append(self, obj):
        """Add object to the end of the array"""
        if self._n == self._capacity: # not enough room
            self._resize(2 * self._capacity) # double capacity
        self._A[self._n] = obj
        self._n += 1

    def insert(self, obj, index):
        """Adds an element at a particular position in the array"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        for i in range(self._n, index, -1): # start shifting from the rightmost
            self._A[i] = self._A[i - 1]
        self._A[index] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c"""
        B = self._make_array(c) # make a bigger array
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = c 

    def count(self, obj):
        """Returns the number of occurences of obj in the array"""
        count = 0
        for i in range(self._n):
            if obj == self._A[i]:
                count += 1
        return count

    def __contains__(self, obj):
        """Loops through an array to find occurence of an obj"""
        for i in range(self._n):
            if self._A[i] == obj:
                return True
        return False # if the loop gets here

    def __setitem__(self, index, obj):
        """
        Replaces an entry at an index in the array with a new value obj
        """
        if not 0 <= index < self._n:
            raise IndexError('Index out of bounds')
        old_val = self._A[index]
        self._A[index] = obj

    def remove(self, obj):
        """Removes the first occurence of obj (or raise ValueError)"""
        for i in range(self._n):
            if self._A[i] == obj: # match found
                for j in range(i, self._n -1): # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError('value not found') # only reached if match is not found

    def pop(self, index=None):
        """
        Removes and returns an element from an array. 
        In the default state(user didn't enter an index ie pop()), it removes and returns the last element
        """
        if index is None:
            old_val = self._A[self._n -1]
            self._A[self._n -1] = None # sets the last element to none
            self._n -= 1 # reduce the counter by 1
            return old_val
        else:
            if not 0 <= index < self._n:
                raise IndexError('index out of range')
            old_val = self._A[index]
            for i in range(index, self._n -1):
                self._A[i] = self._A[i + 1]
            self._A[self._n -1] = None 
            self._n -= 1
            return old_val

    def _make_array(self, c):
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()

def compute_average(n):
    """Perform n number of appends to a python list so we can experimentally
    compute the average time elapsed for the operation"""
    data = []
    start = time()

    for i in range(n):
        data.append(None) # we don't care about the content

    end = time()

    return (end-start)/n



a = DynamicArrays()
print(len(a))
a.append(2)
a.append(3)
print(len(a))
a.append(4)
a.insert(2, 2)
a.__setitem__(0, 17)
a.append(5)
print(a[2])
print(a[0])
print(a.count(2))
print(a.pop())