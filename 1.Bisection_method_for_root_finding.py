import sys


def isclose(a, b):
    return abs(b - a) < sys.float_info.epsilon


def bisection(func, a, b, max_iter=100, tol=1.0e-6):
    global mid
    for iteration in range(max_iter):
        mid = (a + b) / 2
        if isclose(func(mid), 0) or (b - a) / 2 < tol:
            return mid
        else:
            if func(mid) * func(a) < 0:
                b = mid
            else:
                a = mid
    return mid


def func(x):
    return x ** 3 + 4 * x ** 2 - 10


sol = bisection(func, 1, 2)
print(sol)
