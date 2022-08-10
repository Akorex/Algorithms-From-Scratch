def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a python list
    
    data     sorted python list to conduct search on
    target   item to look for
    low      the lower index to begin the search
    high     the upper index to end the search"""

    data = sorted(data)
    if low > high:
        return False # this is an empty interval

    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]: # recur on the left portion of the python list
            return binary_search(data, target, low, mid - 1)
        elif target > data[mid]:
            return binary_search(data, target, mid + 1, high)


if __name__ == '__main__':
    data = [0, 1, 2, 3, 5, 6, 6, 8]
    print(binary_search(data, 12, 0, 5))

    data = [5, 7, 8, 0, -3, 6, 2, 3, 99]
    print(binary_search(data, 99, 0, 8))