##Exercise 32. Dictionary of Squares (Mapping Logic)
##Practice Problem: Create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9).

ans = dict()

for i in range(1,11):
    ans[i]=i*i
print(ans)
