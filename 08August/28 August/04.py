#WAP to check whether the list having middle value or not, if yes print it

lst = eval(input("Enter a list : "))

if len(lst)%2==1:
    print("Yes, middle value :",lst[len(lst)//2])
else:
    print("No")