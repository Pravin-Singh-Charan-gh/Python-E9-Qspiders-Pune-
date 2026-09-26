##7.	Count number of digits in a number.

import input_number 

n = input_number.inpn()

t = n 
ans = 0
while t:
    t//=10
    ans += 1
print(ans)

