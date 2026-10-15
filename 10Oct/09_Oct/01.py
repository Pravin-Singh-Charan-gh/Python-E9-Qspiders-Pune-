# WAP to flatten a list

l = [1,2,[3,4,[2,3],[2,[4,[6,45,100,23223]]],1,3,10,32,34]]

def flat(l):
    res = []
    for i in l:
        if type(i)==list:
            res += flat(i)
        else:
            res.append(i)   
    return res              

def flat_single_line(l):
    return list(eval(str(l).replace('[','').replace(']','')))
print(flat(l))
print(flat_single_line(l))