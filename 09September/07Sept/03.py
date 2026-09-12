#WAP to find the sum of odd number between 1 to n

n = int(input('Enter a number : '))

i = 1
ans=0
while i<n:
    ans+=i
    i+=2
print(ans)