"""Tests the run time of the merge sort algorithm"""

from merge_sort import merge_sort
import random
from time import time


def test_merge_sort(n = 5):
    """
    Creates a list of random numbers n number of times, 
    sorts them using the merge sort algorithm and then returns the time 
    it took to return a sorted list for each run
    
    Args:
        n = number of times to run the algorithm (Optional)
    """
    
    for _ in range(n):
        random_nums = [None] * 1000
        for i in range(1000):
            random_nums[i] = random.randint(1, 1000)
        
        start_time = time()
        merge_sort(random_nums)
        end_time = time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"{round(elapsed_time, 3)} ms")

if __name__ == '__main__':
    test_merge_sort()