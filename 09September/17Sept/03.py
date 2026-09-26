#WAP to reverse the previous pattern
#* * * * *
#* * * *
#* * *
#* *
##*

n = int(input('Enter the number : '))
'''
for i in range(n,0,-1):
    for j in range(i):
        print('* ',end='')
    print()

'''

# different method
for i in range(n):
    for j in range(n-i):
        print('* ',end='')
    print()
