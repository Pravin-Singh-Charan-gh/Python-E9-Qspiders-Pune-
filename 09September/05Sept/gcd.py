#GCD of 2 numbers
a= int(input('Enter first number : '))
b = int(input('Enter second number : '))

if a<b:
    mini=a
else:
    mini=b

ans = 1
i = 1

while i<=mini:
    if a%i==0 and b%i==0:
        ans = i
    i+=1

print(ans)
