# Minimum Platforms Required

def minimumPlateforms(arr,dep):
    ans = 0
    n = len(arr)

    for i in range(n):
        curr = 0
        for j in range(i,n):
            if arr[i]<=dep[j]<=dep[i] or arr[j]<=dep[i]<=dep[j]:
                curr += 1
        ans = max(ans,curr)

    return ans

arr = [1000,935,1100]
dep = [1200,1240,1130]
print(minimumPlateforms(arr,dep))