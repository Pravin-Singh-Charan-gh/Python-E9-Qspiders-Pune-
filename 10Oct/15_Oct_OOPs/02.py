class A:
    lst = []

a1 = A()
a2 = A()

a1.lst += [100]
##a1.lst = a1.lst + [100]

print(A.lst)  
print(a1.lst)
print(a2.lst)


##a1.lst = [1,2,3]
##print(A.lst)  
##print(a1.lst)
##print(a2.lst)
