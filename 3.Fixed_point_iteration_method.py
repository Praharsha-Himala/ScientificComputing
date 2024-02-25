def fixed_point_iterative(func, p_n, max_iter=1000, tol=1.0e-5):
    for iteration in range(max_iter):
        p = func(p_n)
        if abs(p - p_n) < tol:
            return p
        else:
            p_n = p


def function(x):
    return (x ** 2 - 1) / 2


soln = fixed_point_iterative(function, 1.5)
print(soln)
