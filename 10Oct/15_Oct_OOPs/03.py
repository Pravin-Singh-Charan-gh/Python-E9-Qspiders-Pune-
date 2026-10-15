class A:
    a = 10
    b = 20

a1 = A()
a1.c = 30
a1.d = 40
a1.e = 500

a2 = A()
a2.e = 50
a2.f = 60

print(a1.a,a1.b,a1.c,a1.d,a1.e)
print(a2.e,a2.f)


def add(a,b):
    return a.a +b
A.__add__ = add
