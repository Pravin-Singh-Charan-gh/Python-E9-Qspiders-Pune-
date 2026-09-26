# Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

pre = 0
for i in range(1,10):
    print(f'Previous : {pre}, Current : {i}, Sum = {pre+i}')
    pre = i
