#Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.

def merge_two(nums1,nums2):
    ans = []
    
    for i in nums1:
        if i%2:
            ans.append(i)
    for i in nums2:
        if not i%2:
            ans.append(i)
            
    return ans

nums1 = eval(input('Enter the first list : '))
nums2 = eval(input('Enter the second list : '))

print(merge_two(nums1,nums2))
