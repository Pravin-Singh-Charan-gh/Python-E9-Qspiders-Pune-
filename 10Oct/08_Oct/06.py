def flatten_list(l,i=0,ans=None):
    if i==0:
        ans=[]
        
    if i>=len(l):
        return ans
    
    if type(l[i])==list:
        ans=ans+flatten_list(l[i])
    else:
        ans.append(l[i])

    return flatten_list(l,i+1,ans)

l = [1,2,[3,4,[2,3],[2,[4,[6,45,100,23223]]],1,3,10,32,34]]
print(flatten_list(l))