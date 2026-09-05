# WAP to check greatest number among 3

n1 = input("Enter first number : ")
n2 = input("Enter second number : ")
n3 = input("Enter third number : ")

if n1>n2 and n1>n3:
    print(n1)

elif n2>n3:  # no need to check n2>n1 as it is already checked in first if
    print(n2)

else :
    print(n3)