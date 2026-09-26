# Exercise 22. Concatenate Two Lists Index-wise
# Practice Problem: Given two lists of strings, combine them index-by-index to form a single list of concatenated strings.

l_s1= eval(input('Enter the first list of strings : '))
l_s2= eval(input('Enter the second list of strings : '))

# ans = []
# for s1,s2 in zip(l_s1,l_s2):
#     ans.append(s1+s2)
# print(ans)

# using list comprehension
ans = [i+j for i,j in zip(l_s1,l_s2)]
print(ans)