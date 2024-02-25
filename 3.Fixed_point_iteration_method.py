def fixed_point(func, p0, max_iter, tol):
    for iteration in range(max_iter):
        p = func(p0)
        if abs(p - p0) < tol:
            return p
        else:
            p0 = p
    # print(p)
    return p
def function(x):
    return x**2 - 2

sol = fixed_point(function, 1.5, 10000, 0.0001)
print(sol)