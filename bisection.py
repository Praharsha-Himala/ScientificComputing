import math
import sys


def is_close(a, b):
    return abs(b - a) < sys.float_info.epsilon


def function(x):
    fn = x ** 0.5 - math.cos(x)
    return fn


def bisection_method(function, a, b, tol=0.0001, max_iter=100):
    for i in range(max_iter):
        p = (a + b) / 2
        fp = function(p)
        if is_close(fp, 0.0) or abs(b - a) / 2 < tol:
            break
        else:
            if function(a) * fp < 0:
                b = p
            else:
                a = p

    return print(p)


a = 0
b = 1
bisection_method(function, a, b, max_iter=3)
