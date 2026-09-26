# Exercise 23. Iterate Both Lists Simultaneously
# Practice Problem: Use the zip() function to loop through two lists at once and print their values as pairs.

l1= eval(input('Enter the first list : '))
l2= eval(input('Enter the second list : '))

for i,j in zip(l1,l2):
    print(i,j)