def max_subarray(arr):
    res = 0
    n = len(arr)
    for i in range(0,n):
        curr = 0
        for j in range(i,n):
            curr += arr[j]
        res = max(res,curr)

    return res 

def kedans(arr):    #this function will not work properly if the array contains only negative values
    ans = arr[0]
    curr = 0
    for i in arr:
        if curr+i<0:
            curr = 0
        else :
            curr+=i
        ans = max(ans,curr)

    return ans

def kedane(arr):     #this works properly
    ans = arr[0]
    curr = 0
    for i in arr:
        curr += i
        ans = max(ans,curr)

        if curr<0:
            curr = 0
    return ans 

arr = [2, 3, -8, 7, -1, 2, 3]
print(max_subarray(arr))
print(kedans(arr))