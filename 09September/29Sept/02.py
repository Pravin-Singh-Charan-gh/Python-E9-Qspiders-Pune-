"""
1
4 6
10 9 8
12 14 15 16
"""

def isprime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

n = int(input('Enter the number : '))

x = 1
for i in range(1,n+1):
    count = 0
    res = []
    while count<i:
        if not isprime(x):
            res.append(x)
            count+=1

        x+=1
    if i%2==0:
        print(*res)
    else:
        print(*res[::-1])  