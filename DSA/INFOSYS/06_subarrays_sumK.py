# # Count Subarrays having Sum K
# naive : n^2

# for 1 subarray
def sub_sum_k_1(arr,k):
    hm = {}
    pre_sum = 0
    for i in range(len(arr)):
        pre_sum += arr[i]
        if pre_sum == k:
            return arr[0:i+1]
        complement = k - pre_sum
        if complement in hm: 
            return arr[hm[complement]:i+1]
        hm[pre_sum] = i

# real
def sub_sum_k_n(arr,k):
    hm = {}
    pre_sum = 0
    ans = 0
    
    for i in arr:
         pre_sum += i
         if pre_sum == k:
             ans += 1
         complement = pre_sum - k
         if complement in hm:
             ans += hm[complement]
     
         if pre_sum in hm:
             hm[pre_sum] +=1
         else :
             hm[pre_sum] = 1
    
    return ans

arr =  [10, 2, -2, -20, 10]
print(sub_sum_k_1(arr,-10))
print(sub_sum_k_n(arr,-10))