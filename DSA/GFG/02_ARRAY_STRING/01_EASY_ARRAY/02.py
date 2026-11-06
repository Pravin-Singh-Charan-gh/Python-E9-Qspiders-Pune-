# Replace with Adjacent Multiplication
# https://www.geeksforgeeks.org/problems/replace-with-adjacent-multiplication/1

class Solution:
    def updateArray(self, arr):
        # code here
        prev = 1
        for i in range(len(arr)):
            temp = arr[i]
            next = 1 if i==len(arr)-1 else arr[i+1]
            arr[i] = prev * arr[i] * next
            prev = temp