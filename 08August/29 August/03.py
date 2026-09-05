#WAP to toggle the character
# small letter into upper case letter and vice versa, character remains same for other chracters
ch = input("Enter a charcater : ")

if 'A'<=ch<='Z':
    ascii = ord(ch)
    ascii+=32
    print(chr(ascii))

elif 'a'<=ch<='z':
    ascii = ord(ch)
    ascii-=32
    print(chr(ascii))

else :
    print(ch)