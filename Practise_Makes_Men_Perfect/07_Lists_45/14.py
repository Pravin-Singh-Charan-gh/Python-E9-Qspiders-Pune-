# Exercise 14. Check if List Contains a Specific Item
# Practice Problem: Write a check to see if a certain value exists within a list and print a message based on the result.

l = eval(input('Enter the list : '))
val = int(input('Enter the value : '))

if val in l:
    print('Exists')
else:
    print('Not exists')