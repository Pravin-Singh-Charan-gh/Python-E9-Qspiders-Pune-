# 20. Check Armstrong numbers between 1–500.

def is_armstrong(n):
    dig_count = 0
    t = n
    while t:
        dig_count+=1
        t//=10

    ans = 0
    t = n
    while t:
        rem = t%10
        ans += rem**dig_count
        t//=10

    return ans == n

for i in range(1,501):
    if is_armstrong(i):
        print(i)