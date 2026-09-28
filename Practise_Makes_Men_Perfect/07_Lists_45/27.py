##Exercise 27. Find the Most Frequent Element
##Practice Problem: Create a script that identifies the “Mode” of a list—the element that appears most frequently. If there is a tie, returning one of the top elements is sufficient for this exercise.

l = eval(input('Enter the list : '))

d = dict()
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

ans = l[0]
for i in d:
    if d[i]>d[ans]:
        ans = i
print(ans)
    
