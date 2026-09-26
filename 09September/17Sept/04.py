'''WAP to print

* * * * *
  * * * *
    * * *
      * *
        *
        '''

n = int(input('Enter the number : '))

'''
for i in range(n):
    for j in range(n):
        if j<i:
            print('  ',end='')
        else:
            print('* ',end='')
    print()
'''

for i in range(n):
    for j in range(i):
        print(end='  ')
    for j in range(n-i):
        print(end='* ')
    print()
