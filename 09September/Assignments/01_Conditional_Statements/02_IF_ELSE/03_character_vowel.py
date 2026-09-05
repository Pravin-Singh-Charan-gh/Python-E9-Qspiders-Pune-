##3.	Check if a character is vowel or consonant.

ch = input('Enter the character : ')

if len(ch)==1 and ch in ('A','E','I','O','U','a','e','i','o','u'):
    print('Yes')
else:
    print('No')