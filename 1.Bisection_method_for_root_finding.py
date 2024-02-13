import numpy as np
import sys
import math


def is_close(a, b):
    return abs(b - a) < sys.float_info.epsilon


def function(x):
    fn = x ** 3 + 4 * x ** 2 - 10
    return fn


def bisection_method(function, a, b, tol=0.0001, max_iter=100):
    iter = 0
    while iter < max_iter:
        c = (a + b) / 2

        if is_close(function(c), 0.0) or abs(b - a) / 2 < tol:
            break
        else:
            if function(a) * function(c) < 0:
                b = c
            else:
                a = c
            iter = iter + 1

    return print(c)


a = 1
b = 2
bisection_method(function, a, b)
