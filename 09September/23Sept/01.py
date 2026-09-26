n = int(input())
for i in range(2,n):
    if n%i==0:
        print('Not Prime')
        break
else:
    print('Prime')

# If break statement is not executed in the for loop, the loop else block will be executed.
