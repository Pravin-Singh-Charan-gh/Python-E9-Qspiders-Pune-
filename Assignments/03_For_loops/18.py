# 18. Find missing number in 1–N list.

nums = eval(input('Enter the list : '))
n = int(input('Enter n : '))

one_to_n={x for x in range(1,n+1)}

for i in nums:
    one_to_n.remove(i)

print('Missing Numbers : ')
print(one_to_n)