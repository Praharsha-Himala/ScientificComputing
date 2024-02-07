n = int(input('Enter a number to check for even/odd: '))

if n < 0:
    raise ValueError('Enter positive values only')
else:
    if n % 2 == 0:
        print(f'{n} is an even number')
    else:
        print(f'{n} is an odd number')