n = int(input('Enter a number : '))

a = 0
b = 1

n-=2
while n:
    a,b=b,a+b
    n-=1

print(b)

# 0 1 1 2 3
