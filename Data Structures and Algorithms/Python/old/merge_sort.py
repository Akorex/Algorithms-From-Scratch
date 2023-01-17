def merge(S1, S2, S):
    """Merge two sorted python list S1 and S2 into proprerly sized list S"""
    i = j = 0

    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i] # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i + j] = S2[j] # copy jth element of S2 as next item of S
            j += 1


def merge_sort(S):
    """Sort the elements of python list S using the merge sort algorithm"""
    n = len(S)

    if n < 2:
        return # list is trivially sorted
    
    # divide
    mid = n//2
    S1 = S[0:mid] # copy the first half
    S2 = S[mid:n] # copy the second half

    # conquer with recursion
    merge_sort(S1) # sort copy first half
    merge_sort(S2) # sort copy second half

    # merge
    merge(S1, S2, S)


if __name__ == '__main__':
    l = [1, 5, 6, 2, 4, 5, 6, 7, 8]
    merge_sort(l)
    print(l)