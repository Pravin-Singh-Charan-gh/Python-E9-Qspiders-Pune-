# 9. Find largest number in a list.

nums = eval(input('Enter the list : '))

ans = nums[0]
for i in nums:
    if i > ans:
        ans = i

print(ans)