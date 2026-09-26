# Exercise 27. List Cumulative Sum: Each element is the sum of all previous
# Practice Problem: Given a list of numbers, create a new list where each element is the sum of all elements from the original list up to that position.

l = [1, 2, 3, 4]
ans = [l[0]]

for i in range(1,len(l)):
    ans.append(ans[len(ans)-1]+l[i])

print(ans)

# 2.0