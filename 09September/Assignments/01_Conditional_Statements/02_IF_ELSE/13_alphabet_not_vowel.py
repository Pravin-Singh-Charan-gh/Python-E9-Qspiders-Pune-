##13. Check if a character is alphabet but NOT a vowel.

ch = input('Enter a character : ')

if len(ch)==1 and ('A'<=ch<='Z' or 'a'<=ch<='z') and ch not in ('A','E','I','O','U','a','e','i','o','u'):
    print('Yes')
else:
    print('No')