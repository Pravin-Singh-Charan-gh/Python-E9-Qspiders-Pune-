# Exercise 2. Perform List Manipulation
# Practice Problem: Take a given list and modify it through five specific actions:

# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 o the end of a list and print the new list.
# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.

l = eval(input('Enter the list : '))

l[1]=200
print(l)

l.append(600)
print(l)

l.insert(2,300)
print(l)

l.remove(600)
print(l)

l.pop(0)
print(l)