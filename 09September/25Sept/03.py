n = 5

for i in range(1,n+1):
    if i==n:
        print('* '*(i-1),end='')
    else:
        print('* '*i,end='')
    print('  '*((n-i)*2-1),end='')
    
    print('* '*i)
    
for i in range(n-1,0,-1):
    print('* '*i,end='')
    print('  '*((n-i)*2-1),end='')
    print('* '*i)
