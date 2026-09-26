# Exercise 20. Print right-angled triangle Number Pattern using a Loop
# Practice Problem: Write a program to print a right-angled triangle pattern where each row contains increasing numbers up to the row number.
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

n = int(input('Enter the number : '))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(end=f'{j} ')
    print()