def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)

# Throw ValueError if n is below 0 or above 12


def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    else:
        return factorial_rec(n)
