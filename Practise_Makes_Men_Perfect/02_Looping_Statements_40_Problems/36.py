# Exercise 36. Binary to decimal conversion using loop
# Practice Problem: Manually convert a binary string (e.g., "1101") into its decimal integer equivalent using a loop. Do not use int(binary, 2).

binary = "1000"

ans = 0

i = len(binary)-1
power = 0
while i>=0:
    if binary[i]=='1':
        ans = ans + (2**power)
    power+=1
    i-=1
print(ans)