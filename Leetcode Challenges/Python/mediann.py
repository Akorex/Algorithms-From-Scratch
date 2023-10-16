def find_median(lst):
    """returns the median of a given list"""
    length = len(lst)

    if length == 0:
        return float(lst[0])
    
    # when the len is odd
    if length % 2 != 0:
        idx = int(((length + 1)/2 ) - 1)
        
        return float(lst[idx])
    else:
        res = int(length/2)
        x, y = lst[res], lst[res - 1]

        return float((x + y)/2)

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    b = [1, 2, 3, 4]
    c = [1, 4, 5, 8, 9]

    print(find_median(a))
    print(find_median(b))
    print(find_median(c))