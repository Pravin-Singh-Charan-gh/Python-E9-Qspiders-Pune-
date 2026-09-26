# Exercise 5: Flatten a Nested List
# Practice Problem: Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements.

def flat_list(l,index):
    if index == len(l):
        return []
    
    ans = [] 
    if type(l[index])==list:
        for i in l[index]:
            ans.append(i)
    else:
        ans.append(l[index])
    return ans+ flat_list(l,index+1)

l = [5,[7,6],[10,20,30],60,70,[8]]
ans = flat_list(l,0)
print(ans)