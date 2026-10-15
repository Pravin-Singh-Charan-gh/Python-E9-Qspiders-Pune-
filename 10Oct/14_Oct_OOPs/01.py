class A:
    a = 1
    b = 10
    c = 20

a1 = A()
a2 = A()

print(a1.a,a1.b,a1.c)
print(a2.a,a2.b,a2.c)

a1.a = 5
print(a1.a)
print(a2.a)

A.a = 6
print(a1.a)
print(a2.a)

A.d = 40
print(a1.d)
print(a2.d)
