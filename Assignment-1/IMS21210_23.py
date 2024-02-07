n = int(input('Enter number of elements in Fibonacci sequence: '))

# initializing list with fibonacci numbers

fib_seq = [0, 1]
[fib_seq.append(fib_seq[-2]+fib_seq[-1]) for i in range(n-2)]

print(fib_seq)
