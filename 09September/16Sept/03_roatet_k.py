# rotate k
import time

l = eval(input('Enter the list : '))
k = int(input('Enter the k : '))

start_time = time.perf_counter()

for i in range(k):
    l.insert(0,l.pop())
print(l)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")