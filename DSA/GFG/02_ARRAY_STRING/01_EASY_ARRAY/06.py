class Solution:
    def getSubArrays(self, arr: list[int]) -> list[list[int]]:
        # code here
        n = len(arr)
        res = []
        for i in range(n):
            for j in range(i,n):
                res.append(arr[i:j+1])
            # res.append(curr)
        return res