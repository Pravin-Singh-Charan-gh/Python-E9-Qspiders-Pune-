#WAP to flaten a list

l = eval(input('Enter the list : '))

ans = []

for i in l:
    if type(i)==list:
        for j in i:
            ans.append(j)
    else:
        ans.append(i)
        
print(ans)
