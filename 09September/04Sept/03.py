#WAP to find the sum of first n even numbers

n = int(input('Enter a number : '))

s = 0
i = 1

while i<=n:
    s += i*2
    i+=1
print(s)
