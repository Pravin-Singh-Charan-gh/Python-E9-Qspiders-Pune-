class A:
    a = 10
    b = 20
    lst = []

a1 = A()
a1.a = 100

a2 = A()

A.a = 200

print(A.a)  #200
print(a1.a) #100
print(a2.a) #200
