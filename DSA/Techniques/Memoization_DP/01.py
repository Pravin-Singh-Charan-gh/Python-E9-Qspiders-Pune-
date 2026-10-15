# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/description/

class Solution:
    def fib(self, n: int,dp=None) -> int:
        if n<=1:
            return n
        if not dp:
            dp = [None]*(n+1)

        if dp[n]!=None:
            return dp[n]
        
        dp[n-1]=self.fib(n-1,dp)
        dp[n-2]=self.fib(n-2,dp)
        return dp[n-1]+dp[n-2]