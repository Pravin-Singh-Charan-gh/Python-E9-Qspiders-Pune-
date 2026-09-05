# WAP to check whether the middle character of string is upper case or not

str = input("Enter string : ")

if len(str)%2==1 and 'A'<=str[len(str)//2]<='Z':
    print("YES")
else:
    print("NO")

    # First needs to check wether the string has middle character