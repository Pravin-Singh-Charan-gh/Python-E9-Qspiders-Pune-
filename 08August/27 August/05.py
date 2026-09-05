#WAP to check if the input password has length greater than 10 or not

password = input("Enter a password : ")

if len(password)>10:
    print("Yes, greater than 10")

if len(password)<=10:
    print("No, length is not greater than 10")