#WAP to print the sum of number from 1 to n with the step of x

n = int(input('Enter Number : '))
x = int(input('Enter step : '))

ans = 0
i = 1

while i<=n:
    ans += i
    i+=x
print(ans)