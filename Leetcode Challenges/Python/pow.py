def my_pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1. / my_pow(x, -(n))
    else:
        partial = my_pow(x, n//2)
        result = partial * partial
        if n % 2 != 0:
            result *= x
        return result
