#WAP TO CHECK WHETHER THE SIDES CAN FORM TRIANGLE OR NOT

a = int(input("Enter first side of triangle : "))
b = int(input("Enter second side of triangle : "))
c = int(input("Enter third side of triangle : "))

if a+b>c and b+c>a and a+c>b:
    print("YES")
else:
    print("NO")
