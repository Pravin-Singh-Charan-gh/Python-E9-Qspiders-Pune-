#Write a program to perform matrix addition

def matrix_add(m1,m2):
    r = len(m1)
    c = len(m1[0])
    ans = []

    for i in range(r):
        curr=[]
        for j in range(c):
            curr.append(m1[i][j]+m2[i][j])
        ans.append(curr)
    return ans

m1 = eval(input('Enter first Matrix : '))
m2 = eval(input('Enter second Matrix : '))
print(matrix_add(m1,m2))

#using zip
res = []
i = 0
for v1,v2 in zip(m1,m2):
    res.append([])
    for j1,j2 in zip(v1,v2):
        res[i].append(j1+j2)
    i+=1
