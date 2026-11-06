class Solution:
    def maxProfit(self, prices):
        # code here
        max_profit = 0
        mini = prices[0]
        
        for i in prices:
            if i-mini>max_profit:
                max_profit = i-mini
            if i <mini:
                mini = i
        return max_profit