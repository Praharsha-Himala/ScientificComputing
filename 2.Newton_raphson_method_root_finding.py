def newton_raphson(fn, dfn, x, tol: float = 0.0001, max_iter: int = 100):
    for iteration in range(max_iter):
        xnew = x - fn(x) / dfn(x)
        if abs(xnew - x) < tol:
            break
        x = xnew
    return xnew, iteration


y = lambda x: 2 * x ** 3 - 9.5 * x + 7.5
dy = lambda x: 6 * x ** 2 - 9.5

root, iteration_root = newton_raphson(y, dy, 10, 0.00001, 100)
print(f"The root for given function is {root:.2f} at iteration {iteration_root}")