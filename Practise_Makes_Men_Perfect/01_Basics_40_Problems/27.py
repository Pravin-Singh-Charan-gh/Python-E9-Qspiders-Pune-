#Take two lists and find the elements that appear in both. Use Sets to perform the operation.

def dup(l1,l2):
    st1 = set()
    ans=[]

    for i in l1:st1.add(i)
    for i in l2: 
        if i in st1: ans.append(i)

    return ans

l1 = eval(input('Enter the first list : '))
l2 = eval(input('Enter the second list : '))

print(dup(l1,l2))