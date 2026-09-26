#WAP to print whether the number is perfect number or nor
# a number is perfect if sum of all its factor is equal to actual numbers
# factors from 1 to n-1 eg 28 -> . 1,2,4,7,14 = 28


n = int(input('Enter the number : '))

res = 0
for i in range(1,n):
    if n%i==0:
        res+=i
if res == n:
    print('Perfect Number')
else:
    print('Not perfect')
