from sympy import isprime

n = int(input('Enter the number : '))

curr = 1
for i in range(1,n+1):
    arr = []
    while len(arr) <i:
        if not isprime(curr):
            arr.append(str(curr))
        curr+=1
    if i%2:
        print(' '.join(reversed(arr)))
    else:
        print(' '.join(arr))