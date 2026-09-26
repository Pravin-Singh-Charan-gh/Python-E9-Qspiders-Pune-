#WAP to check whether the number is strong or not ( sum of factorial of its digits should be equl to the actual number )

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

if res == n:
    print('Strong Number')
else:
    print('Not strong number')
