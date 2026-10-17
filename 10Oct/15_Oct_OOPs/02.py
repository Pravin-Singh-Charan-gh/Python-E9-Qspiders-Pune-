class A:
    a = []

a1 = A()
a2 = A()

a1.a += [100]

print('A.a', A.a)
print('a1.a',a1.a)
print('a2.a',a2.a)

##################################################################
class B:
    b = []
b1 = B()
b2 = B()

b1.b = b1.b + [100]

print('B.b',B.b)
print('b1.b',b1.b)
print('b2.b',b2.b)