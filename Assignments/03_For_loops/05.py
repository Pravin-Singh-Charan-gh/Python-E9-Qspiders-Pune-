# 5. Count digits in a number (using string loop).

num = int(input('Enter the number : '))

num_str = str(num)

length = 0
for i in num_str:
    length+=1

print(length)