#Print the following pattern where each row contains a number repeated a specific number of times based on its value.
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

def print_pattern(n):
    for i in range(1,n+1):
        print((str(i)+' ')*i)

n = int(input('Enter the number : '))

print_pattern(n)
