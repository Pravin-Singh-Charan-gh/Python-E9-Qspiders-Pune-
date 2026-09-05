#WAP to check whether the char is uppercase, lowercase, digit or special character

ch = input("Enter a character : ")

if 'A'<=ch<='Z':
    print("Uppercase")
elif 'a'<=ch<='z':
    print("Lower case")
elif '0'<=ch<='9':
    print("Digit")
else:
    print("Special Character")