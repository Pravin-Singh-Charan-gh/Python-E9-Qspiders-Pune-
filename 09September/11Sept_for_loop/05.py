#WAP TO check whether the number is power of 2 or not using loop

n = int(input('Enter the number : '))

power = 0
res = 2**power

while res<n:
    power +=1
    res = 2**power

if res == n:
    print('YES')
else:
    print('NO')
