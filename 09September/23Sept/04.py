#WAP to check whether a number is a strong number or not 

n = int(input('Enter the number : '))

t = n
res = 0
while t:
    fact = 1
    rem = t%10
    while rem:
        fact*=rem
        rem-=1
    res+=fact
    t//=10

if n==res:
    print('Strong Number')
else:
    print('Not Strong Number')