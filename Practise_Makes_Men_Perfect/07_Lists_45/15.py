# Exercise 15. Find the Longest String in a List
# Practice Problem: In a list of strings, identify which string has the most characters.

words = eval(input('Enter the list of strings: '))

# curr = l[0]
# for s in l:
#     if len(s)>len(curr):
#         curr = s
# print(curr)

# using inbuilt max
ans = max(words,key=len)
print(ans)