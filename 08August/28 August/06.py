#WAP to check whether the last value of list is palindrome string or not

data = eval(input("Enter data : "))

if type(data[-1]) == str and data[-1]==data[-1][::-1]:
    print("Yes")
else :
    print("No")