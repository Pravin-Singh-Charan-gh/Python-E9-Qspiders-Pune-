##12.	Check if a number is within range 10–50 but exclude 25.

n = int(input('Enter a number : '))

if 10<=n<=50 and n!=25:
    print('YES')
else:
    print('NO')