# WAP to check whether the last character of string is vowel or not

str = input("Enter string : ")

if str[-1] in "AEIOUaeiou" :
    print("Yes")
else:
    print("No")