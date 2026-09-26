# Exercise 24. Hollow square pattern
# Practice Problem: Print a 5*5 square of stars where the middle is empty, leaving only the border.

# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

n = int(input('Enter the number : '))

for i in range(1,n+1):
    if i==1 or i==n:
        print('* '*n)
    else:
        print('* ',end='')
        print('  '*(n-2),end='')
        print('* ')
# 10.14