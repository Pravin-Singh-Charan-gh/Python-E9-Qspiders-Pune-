#WAP to check if the numebr is divisible by both 3 and 7

a = int (input("Enter a number : "))

if a%3==0 & a%7==0:
    print("Yes")

if not a%3==0 & a%7==0:
    print("NO")
