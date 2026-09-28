# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        ans = 0
        curr = 0
        for i in nums:
            if i==1:
                curr+=1
            else:
                curr = 0
            ans = max(curr,ans)
        return ans