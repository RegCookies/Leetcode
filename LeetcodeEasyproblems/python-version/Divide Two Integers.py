def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    a = int(dividend / divisor)
    if a < -1 * (2 ** 31):
        return -2 ** 31
    elif a >= 2 ** 31:
        return 2 ** 31 - 1
    else:
        return a


a = -2147483648
b = 1

c = divide(a,b)
print(c)