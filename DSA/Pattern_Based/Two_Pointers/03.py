# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        D\o not return anything, modify nums in-place instead.
        """
        p =curr= 0
        while p<len(nums):
            if nums[p] != 0:
                nums[curr]=nums[p]
                curr+=1
            p+=1
        while curr<len(nums):
            nums[curr]=0
            curr+=1