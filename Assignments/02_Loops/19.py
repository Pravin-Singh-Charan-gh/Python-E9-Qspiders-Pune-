##19.	Calculate power without using ** operator.

n = int(input('Enter the number to calculate power of : '))
power = int(input('How many powers to calculate : '))

ans = 1
while power:
    ans = ans*n
    power-=1
print(ans)