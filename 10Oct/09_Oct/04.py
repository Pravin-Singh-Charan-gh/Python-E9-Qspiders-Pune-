#Strong number using recursion

def isStrong(n):
    t = n
    s = 0
    while t:
        last = t%10
        s += fact(last)
        t //= 10

    return n==s

def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
# 40585
n = int(input('Enter the number : '))
if isStrong(n):
    print('Strong Number')
else:
    print('Not a strong number')