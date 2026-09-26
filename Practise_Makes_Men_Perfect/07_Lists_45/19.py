# Exercise 19. Remove Empty Strings from a List of Strings
# Practice Problem: Take a list of strings that contains empty entries ("") and remove them to keep only the valid text.

l_str = eval(input('Enter the list of strings : '))

# ans = [s for s in l_str if s!='']
# print(ans)

# Using filter
ans = list(filter(None,l_str))
print(ans)