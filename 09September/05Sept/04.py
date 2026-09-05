#WAP to find the sum of n odd numbers

n = int(input('Enter the number : '))

i=0
s=0
while i<n:
    s+=(i*2+1)
    i+=1
print(s)
