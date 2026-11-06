# Given an array arr[], check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.

class Solution:
    def isSorted(self, arr):
        # code here
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                return False
        return True