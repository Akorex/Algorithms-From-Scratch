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


def merge_sort(S):
    """Sort the elements of Python list S using the merge sort algorithm"""

    n = len(S)
    if n < 2:
        return
    
    mid = len(S)//2
    S1 = S[:mid]
    S2 = S[mid:n]

    merge_sort(S1)
    merge_sort(S2)

    merge(S1, S2, S)

    return S



def merge(S1, S2, S):
    """merge two sorted python lists S1 and S2 into properly sized list S"""
    i = j = 0

    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1

        else:
            S[i + j] = S2[j]
            j += 1


# another approach to merge sort
def merge_sort2(S):
    if len(S) > 1:
        mid = len(S)//2
        left = S[:mid]
        right = S[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            S[k] = left[i]
            i += 1
        else:
            S[k] = right[j]
            j += 1

        k += 1


    # copy the remaining element to S

    while i < len(left):
        S[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        S[k] = right[j]
        j += 1
        k += 1

    return S


def quick_sort(S):
    if len(S) < 2:
        return S
    
    pivot = S[len(S)//2]
    smaller = [x for x in S if x < pivot]
    middle = [x for x in S if x == pivot]
    larger = [x for x in S if x > pivot]

    return quick_sort(smaller) + middle + quick_sort(larger)


def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick sort algorithm"""
    if a > b:
        return
    
    pivot = S[b]
    left = a
    right = b-1

    while left <= right:
        while left <= right and  S[left] < pivot:
            left += 1

        while left <= right and pivot < S[right]:
            right -= 1
        
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1

    S[left], S[b] = S[b], S[left]
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)

    return S

if __name__ == '__main__':
    l = [2, 3, 4, 1, 0]

    print(insertion_sort(l))
    print(selection_sort(l))

    l = [2, 3, 4, 1, 0]
    print(merge_sort(l))
    print(merge_sort2(l))

    l = [2, 3, 4, 1, 0]
    print(quick_sort(l))

    l = [2, 3, 4, 1, 0]
    print(inplace_quick_sort(l, 0, len(l) - 1))