def nextLargerElement(arr):
    n = len(arr)
    res = [-1]*n
    stk = []
    
    for i in range(n-1,-1,-1):
        while stk and stk[-1]<=arr[i]:
            stk.pop()
        if stk:
            res[i] = stk[-1]
            
        stk.append(arr[i])
        
    return res

arr = [6, 8, 0, 1, 3]
res = nextLargerElement(arr)
print(" ".join(map(str, res)))