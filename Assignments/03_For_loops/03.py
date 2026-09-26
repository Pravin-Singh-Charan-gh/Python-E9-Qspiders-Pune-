# 3. Find sum of first N numbers.

n = int(input('Enter the number : '))

s = 0
for i in range(1,n):
    s+=i
print(s)