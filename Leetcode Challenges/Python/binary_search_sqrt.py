"""
Implement the Square root function using binary search.

"""
precision = 10

def binary_search_sqrt(number):
    """ Returns the square root of number"""

    start, end = 0, number
    ans = 1 

    # for the integral part
    while start <= end:
        mid = (start + end)//2

        if mid * mid == number:
            ans = mid
            break
        
        if mid * mid < number:
            start = mid + 1
            ans = mid

        else:
            end = mid - 1

    # for the fractional part 
    increment = 0.1

    for i in range(0, precision):
        while (ans * ans <= number):
            ans += increment

        # loop terminates when ans*ans > number
        ans -= increment
        increment /= 10
    return ans

print(binary_search_sqrt(540))