import time

l = [1,2,3,4,5]
k = 2

start_time = time.perf_counter()
for i in range(k):
    l.insert(0,l.pop())
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Insert : Execution time: {execution_time:.6f} seconds")

###########################################

nums = [1,2,3,4,5]
k = 2

start_time = time.perf_counter()
nums = nums[-k:]+nums[:-k]


end_time = time.perf_counter()
print(f"Slicing Execution time: {execution_time:.6f} seconds")