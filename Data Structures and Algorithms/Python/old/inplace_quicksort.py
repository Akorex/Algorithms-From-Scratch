def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b:
        return # list is trivially sorted
    pivot = S[b]
    left = a
    right = b - 1
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1       
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot <S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1
        
    # put pivot into its final place
    S[left], S[b] = S[b], S[left]

    # make recursive calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)