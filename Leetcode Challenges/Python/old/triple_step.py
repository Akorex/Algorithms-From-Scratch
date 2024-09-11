"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 
steps at a time. Implement a method to count how many possible ways the child can run up the 
stairs. 

"""

def count_ways(n):
    """Returns how many ways a staircase can be climbed given n
    
    n == number of steps
    
    """
    if n < 0:
        return 0
    if n == 0:
        return 1        
    if n == 1:
        return 1
    else:
        return count_ways(n - 1) + count_ways( n - 2) + count_ways(n - 3)

if __name__ == '__main__':
    print(count_ways(1))
    print(count_ways(30))