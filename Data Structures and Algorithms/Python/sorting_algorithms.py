"""
Implementation of different sorting algorithms in python.

"""

def insertion_sort(A):
    """Sort list of comparable elements into non-decreasing order"""

    for i in range(1, len(A)):
        curr = A[i]
        j = i

        while j > 0 and A[j-1] > curr:
            A[j] = A[j - 1]
            j -= 1
        A[j] = curr