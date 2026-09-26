m1 = eval(input('Enter first Matrix : '))
m2 = eval(input('Enter second Matrix : '))

r1 = len(m1)
c1 = len(m1[0])

r2 = len(m2)
c2 = len(m2[0])

if c1!=r2:
    print('This matrix cannot be multiplied')
else:
    ans = []
    for i in range(c1):
        sum = 0
        curr=[]
        for j in range(r2):
            sum += (m1[i][j]+m2[j][i])
        curr.append(sum)
    ans.append(curr)
print(ans)























# 1 2 3 4
# 5 6 7 8

# 1 2
# 3 4 
# 5 6
# 7 8