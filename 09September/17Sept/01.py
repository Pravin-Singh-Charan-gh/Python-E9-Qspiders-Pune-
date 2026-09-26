#WAP to print the following pattern
# 1, 12, 123, 1234, 12345, 
n = int(input('Enter the number : '))
'''
ans = ''
num = 0
for i in range(1,n+1):
    num=num*10+i
    ans = ans + str(num)+', '

print(ans)
'''

##using 2 loops

for i in range(1,n+1):
    for j in range(i):
        print(j+1,end='')
    print(', ',end = '')
