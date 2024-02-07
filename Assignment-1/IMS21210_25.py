# Function given in Question
def func(x):
    return 2 * x ** 3 + 4 * x ** 2 + 1


# integrate function using given approximation function
def integrate(f, a, b):
    mid = (a + b) / 2
    return (mid / 3) * (func(a) + 4 * func(mid) + func(b))


# Exact integral taken by hand
def exact_integration(x):
    return (1 / 2) * x ** 4 + (4 / 3) * x ** 3 + x


# Taking interval limits as 0 and 1

a = 0
b = 1
print(
    f"Exact integration of given function in interval [{a}, {b}]: {round(exact_integration(b) - exact_integration(a), 4)}")
print(f"Integration of given function in interval [{a}, {b}]: {round(integrate(func, a, b), 4)}")
