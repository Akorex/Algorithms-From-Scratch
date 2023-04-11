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

    return A

def selection_sort(A):
    """Sort list of comparable elements into non-decreasing order"""
    for i in range(len(A)):
        min_index = i

        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                min_index = j

        # Swap the minimum element with the first element of the unsorted part
        A[i], A[min_index] = A[min_index], A[i]
    
    return A


if __name__ == '__main__':
    l = [2, 3, 4, 1, 0]

    print(insertion_sort(l))
    print(selection_sort(l))
