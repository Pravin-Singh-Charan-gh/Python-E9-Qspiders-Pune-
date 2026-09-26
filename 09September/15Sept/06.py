n = int(input('Enter the number : '))

req_numbers = 0
for i in range(1,n+1):
    req_numbers+=i

nums = [1]
curr = 2
while len(nums)<req_numbers:

    is_prime = True
    for j in range(2,curr):
        if curr%j==0:
            is_prime=False
            break
    if not is_prime:
        nums.append(curr)
    curr+=1

# PRINT The pattern
curr_index = 0
right_to_left = True
for i in range(0,n):
    
    if right_to_left:
        for j in range(curr_index+i,curr_index-1,-1):
            print(nums[j],end=' ')
            curr_index+=1

    else:
        for j in range(curr_index,curr_index+i+1):
            print(nums[curr_index],end=' ')
            curr_index+=1
            
    print()
    right_to_left=not right_to_left

# 1
# 2 3
# 4 5 6
# 10 9 8 7
# 11 12 13 14 15