##14.	Find factorial using while loop.

n = int(input('Enter the number : '))

t = n 
ans = 1

while t:
    ans*=t
    t-=1
print(ans)