def knapsack(wt,val,W,i=0):
    if W<=0 or i == len(wt):
        return 0

    select = val[i]+knapsack(wt,val, W-wt[i],i+1)
    not_select = knapsack(wt,val,W,i+1)

    return max(select,not_select)

wt = [5,4,2,3]
val = [10,40,30,50]                                                                                                                                                 
W = 5

print(knapsack(wt,val,W))