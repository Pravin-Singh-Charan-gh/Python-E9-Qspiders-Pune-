# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        max1 = max2 = max3 = -float('inf')

        for i in nums:
            if i>max1:
                max1, max2, max3 = (i,max1,max2)
            elif i>max2 and i!=max1:
                max2, max3 = (i,max2)
            elif i>max3 and i not in (max1,max2):
                max3 = i
        
        if max3==-float('inf'):
            return max1
        return max3