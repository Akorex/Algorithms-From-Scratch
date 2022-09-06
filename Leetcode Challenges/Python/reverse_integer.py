def reverse(x):
    if x >= 2**31 - 1 or x <= -2**31:
        return 0
    str_x = str(x)

    if x > 0:
        reversed = str_x[::-1]
    elif x < 0:
        temp = str_x[1:]
        reversed = temp[::-1]
        reversed = "-" + reversed
    else:
        return 0

    # reversed meet the constraint
    if int(reversed) >= 2**31 -1 or int(reversed) <= -2**31:
        return 0
    else:
        return int(reversed)


if __name__ == '__main__':
    print(reverse(-123))
    print(reverse(210))
    print(reverse(0))
    print(reverse(10000))