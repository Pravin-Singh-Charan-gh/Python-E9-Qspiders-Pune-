# 15. Find common elements between two lists (without intersection method).

nums1 = eval(input('Enter the list 1 : '))
nums2 = eval(input('Enter the list 2 : '))

nums1_elements = set()
for i in nums1:
    nums1_elements.add(i)

ans = []
for i in nums2:
    if i in nums1_elements:
        ans.append(i)

print(ans)