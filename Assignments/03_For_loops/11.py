# 11. Find second largest number in a list .

nums = eval(input('Enter the list : '))

largest = second_largest = nums[0]

for i in nums:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest:
        second_largest=i

print(second_largest)