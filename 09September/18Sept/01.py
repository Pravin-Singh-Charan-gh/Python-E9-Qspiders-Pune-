#WAP to find 2 elements from the list whose sum is equal to the target

l = eval(input('Enter the list : '))
target = int(input('Enter the target : '))

n = len(l)
ans = []

for i in range(n):
    for j in range(i,n):
        if l[i]+l[j]==target:
            ans.append((l[i],l[j]))
print(ans)


## doing with set

ans = []
s = set()
for i in l:
    if target-i in s:
        ans.append((target-i,i))
    s.add(i)
print(ans)
    
# using enumerate in place of range
ans = []
for n_index,value1 in enumerate(l,start=1):
    for value2 in l[n_index::]:
        if value1+value2==target:
            ans.append((value1,value2))
print(ans)
