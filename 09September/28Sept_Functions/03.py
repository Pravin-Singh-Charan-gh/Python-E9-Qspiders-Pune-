#WAP to calculate whether the number is a perfect number or not

def is_perfect(n):
    res = 0
    for i in range(1,n):
        if n%i==0:
            res+=i
    return res==n

n = int(input('Enter the number : '))
print(is_perfect(n))
