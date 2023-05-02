"""An implementation of merge sort algorithm in python"""

# the merge sort algorithm
def merge_sort(S):
    """Returns a sorted array S using the merge - sort algorithm"""
    
    # divide the arrays
    if len(S) < 2:
        return
    
    mid = len(S)//2
    left = S[:mid]
    right = S[mid:]

    # recursively divide the arrays
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

    # copy the remaining elements to S
    while i < len(left):
        S[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        S[k] = right[j]
        j += 1
        k += 1

    return S


