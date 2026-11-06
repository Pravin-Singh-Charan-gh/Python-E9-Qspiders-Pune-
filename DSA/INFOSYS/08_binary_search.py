def binary_search(arr,k):
    l = 0
    r = len(arr)-1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] == k:
            return mid
        elif k<arr[mid]:
            r = mid-1 
        else:
            l = mid + 1

    return -1

arr = [1, 2, 3, 4, 6]
k = 6
print(binary_search(arr,k))