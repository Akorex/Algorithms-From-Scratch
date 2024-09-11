def getElements(arr, queries):
    # Write your code here
    rows = arr[0] # know how many rows
    cols = (len(arr) - 1)//rows # how many columns
    arr = arr[1:]

    ans = []
    for query in queries:
        row_index = rows * (query[0] - 1)
        col_index = query[1] - 1
        index = row_index + col_index
        ans.append(arr[index])
    return ans
    

if __name__ == '__main__':
    arr = [5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    queries = [[2, 1], [2,2]]
    print(getElements(arr, queries))