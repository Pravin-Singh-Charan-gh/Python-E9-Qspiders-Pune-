#GCD
n1 = int(input('Enter the first number : '))
n2 = int(input('Enter the second number : '))

mini = n1 if n1<n2 else n2

ans = 1

for i in range(1,mini+1):
    if n1%i==0 and n2%i==0:
        ans=i
print(ans)

## DevSep1

## Second method
r = abs(n1-n2)
for i in range(1,r+1):
    if n1%i==0 and n2%i==0:
        gcd = i
## no need to declare gcd
print(gcd)