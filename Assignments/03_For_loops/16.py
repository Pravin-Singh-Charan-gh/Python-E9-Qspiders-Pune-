# 16. Find pairs in list whose sum = target value.

def two_sum(nums,target):
    elements = set()
    ans = []
    for i in nums:
        if target-i in elements:
            ans.append([target-i,i])
        elements.add(i)
    return ans

nums = eval(input('Enter the list : '))
target = int(input('Enter the target value : '))

ans = two_sum(nums,target)

for i in ans:
    print(i)