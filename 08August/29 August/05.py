# WAP to check 2nd greatest number among 3 distinct numbers

n1 = input("Enter first number : ")
n2 = input("Enter second number : ")
n3 = input("Enter third number : ")

if n1>n2>n3 or n1<n2<n3:
    print(n2)
elif n2>n1>n3 or n2<n1<n3:
    print(n1)
else: 
    print(n3)


