"""
This function contains code implementations to demonstrate the concept of object-oriented programming.
"""

class Range:
    """A class that mimics python's built-in range class"""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range object"""
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start  # computes the case of Range(0, n)
        
        self._start = start
        self._stop = stop
        self._step = step

    def __len__(self):
        """Returns the number of entries in range"""
        return max(0, (self._stop - self._start + self._step - 1)//self._step)
    
    def __iter__(self):
        return self

    def __getitem__(self, index):
        """Returns the entry at the given index"""
        if index < 0:
            index += len(self)
        
        if not 0 <= index < len(self):
            raise IndexError('index out of range')
        
        return self._start + index * self._step

class SequenceIterator:
    """An iterator for any of Python's sequence types"""
    def __init__(self, sequence):
        self._seq = sequence
        self._index = -1 # would increment to 0 on first call to next
    
    def __next__(self):
        """Returns the next element in Sequence or else raise StopIteration error"""
        self._index += 1
        if self._index < len(self._seq):
            return self._seq[self._index]
        else:
            raise StopIteration()

    def __iter__(self):
        return self

class Progression:
    """A generic class for producing a progression"""
    
    def __init__(self, start=0):
        """Initialize a Progression with the given start value"""
        self._current = start
    
    def _advance(self):
        """Update self._current to a new value, must be defined in subclass"""
        raise NotImplementedError('_advance() must be implemented by subclass')
    
    def __next__(self):
        """Return the next element or else raise StopIteration error"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        """By convention, an iterator for a sequence should return itself as an iterator"""
        return self

    def print_progression(self, n):
        """Prints the first n values of the progression"""
        return ' '.join(str(next(self)) for j in range(n))

class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression"""

    def __init__(self, start=0, increment=1):
        """Initializes an Arithmetic Progression
        
        increment   the fixed constant to add to each term (defaults to 1)
        start       the first term of the arithmetic progression (defauls to 0)
        """
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the fixed increment"""
        self._current += self._increment

class GeometricProgression(Progression):
    """Iterator producing a geometric progression"""

    def __init__(self, start=1, base=2):
        """Initializes a geometric progression
        
        start       the first term of the geometric progression (defaults to 1)
        base        the fixed constant multiplied to each term (defaults to 2)
        """
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        """Update current value by multipling it by the constant base"""
        self._current *= self._base

class FibonacciProgression(Progression):
    """Iterator producing a Fibonacci progression"""

    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression
        
        first   the first term of the progression
        second  the second term of the progression
        """

        super().__init__(first)
        self._prev = second - first
    
    def _advance(self):
        """Update current value by taking sum of previous two"""
        self._prev, self._current = self._current, self._prev + self._current

if __name__ == '__main__':
   r = Range(2, 150, 5)

   ap = ArithmeticProgression(3, 4)
   print(ap.print_progression(10))

   gp = GeometricProgression(5, 2)
   print(gp.print_progression(5))

   fb = FibonacciProgression()
   print(fb.print_progression(10))