# 17. Rotate list by K positions.
import time


nums = eval(input('Enter the list : '))
k = int(input('Enter how many times to rotate : ')) 

start_time = time.perf_counter()
nums = nums[-k:]+nums[:-k]

print(nums)

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f" Execution time: {execution_time:.6f} seconds")