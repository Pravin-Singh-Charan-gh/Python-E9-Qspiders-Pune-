#WAP to print triangle star pattern using nested loop
## For input 6(n)
##*
##* *
##* * *
##* * * *
##* * * * *
##* * * * * *

n = int(input('Enter the number : '))

for i in range(n):
    for j in range(i+1):
        print('* ',end='')

    print()
