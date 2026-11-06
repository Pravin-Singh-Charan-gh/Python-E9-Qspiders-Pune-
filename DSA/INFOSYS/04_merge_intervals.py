# Merge Overlapping Intervals

def mergeOverlap(arr):
    arr.sort()
    res = []

    for itvl in arr:
        if not res:
            res.append(itvl)
            continue
        last = res[-1]
        if itvl[0]<=last[1]:
            res[-1][1] = max(last[1],itvl[1])
        else:
            res.append(itvl)

    return res

arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
res = mergeOverlap(arr)
print(res)