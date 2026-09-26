##8.	Find GCD of two numbers.

a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))

mini = a if a<b else b
ans = 1

for i in range(1,mini+1):
    if a%i==0 and b%i==0:
        ans = i
print(ans)