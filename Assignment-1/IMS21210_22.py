def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input('Enter number of elements in Fibonacci sequence'))
fib_seq = [fibonacci(i) for i in range(n)]
print(fib_seq)
