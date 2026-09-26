##Exercise 37. Simple Countdown Timer
##Practice Problem: Create a countdown timer that starts from a given number and counts down to zero using a while loop.

import time

n = int(input('Enter the number : '))
t = n
while t:
    print(t)
    time.sleep(1)
    t-=1
print('⌛⌛⌛⌛⌛⌛⌛')
