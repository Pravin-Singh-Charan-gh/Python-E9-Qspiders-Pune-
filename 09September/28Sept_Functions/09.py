#WAP which gives you the length of a collection without using len function

def length(coll):
    ans = 0
    for i in coll:
        ans+=1
    return ans

coll = eval(input('Enter the collection : '))
print('Size :',length(coll))