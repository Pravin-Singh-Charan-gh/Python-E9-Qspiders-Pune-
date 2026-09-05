#WAP to print the sum of first n even numbers

n = int(input('Enter the number : '))

i = 1
s = 0

while i <= n:
    s+=i*2
    i+=1
print(s)
