def knapsack(weights,prices,W, i= 0):
    if W <= 0 or i == len(weights):
        return 0
    # exclude
    exclude = knapsack(weights, prices, W,i+1)

    # include
    if W-prices[i]>=0:
        include = knapsack(weights,prices,W-prices[i],i+1)+prices[i]
        return max(include,exclude)

    return exclude


val = [1, 2, 3]
wt = [4, 5, 1]
W = 4
print("Maximum value:", knapsack(val, wt,W))  # Output: 3