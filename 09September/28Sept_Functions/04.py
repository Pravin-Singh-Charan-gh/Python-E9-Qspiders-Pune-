#WAP to print n number of perfect numbers

def is_perfect(n):
    res = 0
    for i in range(1,n):
        if n%i==0:
            res+=i
    return res==n

n = int(input('Enter the number : '))

i = 1
num = 1
while i<=n:
    if is_perfect(num):
        print(num)
        i+=1
    num+=1
