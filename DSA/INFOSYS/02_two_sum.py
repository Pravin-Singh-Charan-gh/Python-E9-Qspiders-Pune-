def twoSum(arr,target):
    hm = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in hm:
            return [hm[complement],i]
        hm[arr[i]] = i

    return []

arr =  [2,7,11,15]
target = 9

print(twoSum(arr,target))