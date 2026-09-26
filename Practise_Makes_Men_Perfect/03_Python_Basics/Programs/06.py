import random
import time

current_time_seconds = int(time.time()*1000)
random.seed(current_time_seconds)
print(random.random())
print(random.random())

print(random.randint(10,100))