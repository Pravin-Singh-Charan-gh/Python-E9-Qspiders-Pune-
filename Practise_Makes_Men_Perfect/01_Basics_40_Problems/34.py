##Exercise 34. Print Reverse Number Pattern
##Practice Problem: Print a downward number pattern where each row starts with a decreasing value.

def downward_pattern(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(end=f'{j} ')
        print()

n = int(input('Enter the number : '))

downward_pattern(n)
