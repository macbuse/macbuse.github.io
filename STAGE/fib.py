def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def number_base(n, base):
    if n == 0:
        return 0
    else:
        return n % base + 10 * number_base(n // base, base)




