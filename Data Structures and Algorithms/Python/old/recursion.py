def factorial(n):
    """
    Conmputes by recursion the factorial of a given number
    
    n        the number to calculate the factorial
    
    """

    if n < 0:
        raise ValueError('number cannot be less than zero')
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def binary_search(data, target, low, high):
    """
    data     sorted python list to conduct search on
    target   item to look for
    low      the lower index to begin the search
    high     the upper index to end the search
    """

    if low > high: # invalid case
        return False 
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]: # recur on the left
            return binary_search(data, target, low, mid - 1)
        else: # recur on the right
            return binary_search(data, target, mid + 1, high)

def bad_fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n <=1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)

def good_fibonacci(n):
    """Returns the pair of Fibonacci numbers, F(n) and F(n-1)"""
    if n <=1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)

def linear_sum(S, n):
    """Returns the sum of the first n numbers in the list S"""

    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n-1]

def reverse(S, start, stop):
    """Reverse elements in slice S[start:stop]"""
    if start < stop -1:
        S[start], S[stop - 1] = S[stop -1], S[start]
        reverse(S, start + 1, stop - 1)
    
    return S

def power(x, n):
    """Returns the exponential of an integer x, to power n"""
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError('this simple code only works for n >= 0')
    else:
        return x * power(x, n - 1)

def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start:stop]"""
    if start >= stop:
        return 0
    elif start == stop - 1: # one element in slice
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

def binary_search_iterative(data, target):
    """Return True if target us found in a python list"""
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1 # only consider values from left of mid
        else:
            low = mid + 1 # only consider values from right of mid
    return False

def reverse_iterative(S):
    """Reverse elements in Sequence S"""
    start, stop = 0, len(S)

    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        start, stop = start + 1, stop -1


def harmonic_number(n):
    """Returns the nth harmonic number"""
    if n == 0:
        raise ValueError('cannot be computed')
    elif n == 1:
        return 1
    else:
        return 1/n + harmonic_number(n - 1)

# a function that determines if a string has more vowels than consonants

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(3))
    #print(factorial(-3))
    print(factorial(24))

    print(bad_fibonacci(7))
    print(good_fibonacci(7))

    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(linear_sum( L, 8))
    print(reverse(L, 0, 10))
    print(power(2, 5))

    print(harmonic_number(3))