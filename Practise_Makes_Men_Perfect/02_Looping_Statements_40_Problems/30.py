# Exercise 30. Remove duplicates without set
# Practice Problem: Write a program to remove all duplicate values from a list using a loop, maintaining the original order of elements.

l = [1, 2, 2, 3, 4, 4, 4, 5]
ans = []
for i in range(len(l)):
    if l[i] not in ans:
        ans.append(l[i])
print(ans)

# 2.0