#revesrse an interger
a=int(input('Enter a number : '))
n=a

#for negative values    
n = abs(n)

ans = 0

while n:
    rem = n%10
    ans = ans*10+rem
    n//=10
    
if a<0:
    ans*=-1
print(ans)
