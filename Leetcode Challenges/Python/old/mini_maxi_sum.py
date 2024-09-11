"""Solution to HackerRank problem - Mini - Maxi Sum"""
def miniMaxSum(arr):
    # Write your code here
    arr_sum = sum(arr)
    mini = arr_sum - max(arr)
    maxi = arr_sum - min(arr)
    print(mini, maxi)
